import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sobrevivência")
CLOCK = pygame.time.Clock()

# Fontes para o HUD e Game Over
fonte_grande = pygame.font.SysFont("Arial", 48, bold=True)
fonte_normal = pygame.font.SysFont("Arial", 28)

class EntidadeBase:
    def __init__(self, x, y, largura, altura, cor):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

    def colidiu_com(self, outra):
        return self.rect.colliderect(outra.rect)

class Jogador(EntidadeBase):
    def __init__(self, x, y, direcao_atual):
        super().__init__(x, y, 50, 50, (22, 242, 50))
        self.velocidade = 9
        self.direcao_atual = "direita"

    def mover(self, teclas):
        # Limita o movimento às bordas da tela
        if teclas[pygame.K_LEFT] and self.rect.x > 0: 
            self.rect.x -= self.velocidade
            self.direcao_atual = "esquerda"
        if teclas[pygame.K_RIGHT] and self.rect.x < 750: 
            self.rect.x += self.velocidade
            self.direcao_atual = "direita"
        if teclas[pygame.K_UP] and self.rect.y > 0: 
            self.rect.y -= self.velocidade
            self.direcao_atual = "cima"
        if teclas[pygame.K_DOWN] and self.rect.y < 550: 
            self.rect.y += self.velocidade
            self.direcao_atual = "baixo"
        
    def atirar(self, lista_balas):
        nova_bala = Bala(self.rect.centerx, self.rect.centery, self.direcao_atual)
        lista_balas.append(nova_bala)

class Bala:
    def __init__(self, x_inicial, y_inicial, direcao):
        self.rect = pygame.Rect(x_inicial, y_inicial, 10, 10)
        self.direcao = direcao
        self.velocidade = 18
        self.rect = pygame.Rect(x_inicial, y_inicial, 10, 10)

    def atualizar(self):
   # A bala continua se movendo para a direção em que nasceu
        if self.direcao == "esquerda": self.rect.x -= self.velocidade
        if self.direcao == "direita":  self.rect.x += self.velocidade
        if self.direcao == "cima":     self.rect.y -= self.velocidade
        if self.direcao == "baixo":    self.rect.y += self.velocidade
      
    def desenhar(self, tela):
    # Desenha a bala na tela (amarela)
        pygame.draw.rect(tela, (255, 255, 0), self.rect)

class Inimigo(EntidadeBase):
    def __init__(self, x, y, velocidade=3, vida_inimigo = 3, largura=40,altura=40,cor=(225,227,14)):
        super().__init__(x, y, largura, altura, cor)
        self.velocidade = velocidade
        self.vida_inimigo = vida_inimigo

    def perseguir(self, alvo):
        """Move o inimigo em direção ao alvo (jogador)."""
        if self.rect.x < alvo.rect.x: self.rect.x += self.velocidade
        if self.rect.x > alvo.rect.x: self.rect.x -= self.velocidade
        if self.rect.y < alvo.rect.y: self.rect.y += self.velocidade
        if self.rect.y > alvo.rect.y: self.rect.y -= self.velocidade

def desenhar_hud(tela, estado):
    """Desenha o HUD (Heads-Up Display) do jogo."""

    texto_pont = fonte_normal.render(f"Pontuação: {estado['pontuacao']}", True, (255, 255, 255))
    tela.blit(texto_pont, (10, 10))
    

    for i in range(estado["vidas"]):
        pygame.draw.circle(tela, (255, 80, 80), (730 - i*35, 25), 12)
        # 2. Escreve a quantidade do lado dela
    texto_qtd_vidas = fonte_normal.render(f"Vidas: x {estado['vidas']}", True, (255, 255, 255))
    tela.blit(texto_qtd_vidas, (630, 50))

def desenhar_game_over(tela):
    """Exibe a tela de Game Over centralizada."""
    overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    tela.blit(overlay, (0, 0))
    texto = fonte_grande.render("GAME OVER", True, (255, 60, 60))
    tela.blit(texto, texto.get_rect(center=(400, 300)))
    
class InimigoRapido(Inimigo):
    def __init__(self, x, y, velocidade):
        #super().__init__(x, y, 40, 40, (205, 207, 104))
        super().__init__(x, y, velocidade=velocidade, vida_inimigo=1, largura=35, altura=35, cor=(225, 225, 100))
        
class InimigoBig(Inimigo):
    def __init__(self, x, y, velocidade):
        #super().__init__(x, y, 40, 40, (205, 207, 104))
        super().__init__(x, y, velocidade=velocidade, vida_inimigo=6, largura=55, altura=55, cor=(10, 225, 100))

    

# ==========================================
# Configuração inicial do Mini-Game
# ==========================================

conf_level = {
    1: {
        "vel_min" : 2,
        "vel_max" :3,
        "quantidade_inimigos": 1
               
    },
    2: {
        "vel_min" : 4,
        "vel_max" :6,
        "quantidade_inimigos": 5     
    },
    3: {
        "vel_min" : 6,
        "vel_max" :8,
        "quantidade_inimigos": 8     
    }
    
}
mensagem_nivel = ""
tempo_mensagem = 0
mostrar_mensagem = False

jogador = Jogador(375, 275, "direita")
inimigos = [#x, y, velocidade, 
    Inimigo(random.randint(0, 750), random.randint(0, 100), random.randint(2, 4)) 
    for _ in range(2)
]

# lista inimigos_rapidos por isso (adiciona os rápidos na lista principal)
for _ in range(2):
    inimigos.append(InimigoRapido(random.randint(0, 750), random.randint(0, 100), random.randint(6, 9)))
    
for _ in range(1):
    inimigos.append(InimigoBig(random.randint(0, 750), random.randint(0, 100), random.randint(1, 3)))


estado = {"pontuacao": 0, "vidas": 80, "rodando": True}
timer_spawn = 0
balas_no_jogo =[]
while estado["rodando"]:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE: # Se for a barra de espaço
                jogador.atirar(balas_no_jogo)

    # Atualizar jogador
    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)
    
    if estado["pontuacao"] == 0:
        mensagem_nivel = "Inicio do Nivel 1"
        tempo_mensagem = pygame.time.get_ticks()
        mostrar_mensagem = True
        
    
        
    
# Atualiza inimigos    
    for ini in inimigos: 
        ini.perseguir(jogador)
        if jogador.colidiu_com(ini):
            estado["vidas"] -= 1
            ini.rect.topleft = (random.randint(0, 750), 0)
            if estado["vidas"] <= 0:
                estado["rodando"] = False

    # Spawn de novos inimigos a cada 300 frames
    if estado["pontuacao"] < 500:#Nivel 1
        timer_spawn += 1
        for n in range(conf_level[1]["quantidade_inimigos"]):
            if timer_spawn % 470 == 0:
                inimigos.append(Inimigo(random.randint(0, 750), 0, random.randint(conf_level[1]["vel_min"], conf_level[1]["vel_max"])))
                #inimigos.append(InimigoRapido(random.randint(0, 750), 0, random.randint(6, 7)))

        
    if estado["pontuacao"] == 500:
        mensagem_nivel = "NÍVEL 2: PREPARE-SE!"
        tempo_mensagem = pygame.time.get_ticks()
        mostrar_mensagem = True      
    if estado["pontuacao"] >= 500 and estado["pontuacao"] < 1000:#Nivel 2
        timer_spawn += 1
        for n in range(conf_level[2]["quantidade_inimigos"]):
            if timer_spawn % 250 == 0:
                inimigos.append(Inimigo(random.randint(0, 750), 0, random.randint(conf_level[1]["vel_min"], conf_level[1]["vel_max"])))
                inimigos.append(InimigoBig(random.randint(0, 750), 0, random.randint(1, 3)))

  
    if estado["pontuacao"] == 1000:
        mensagem_nivel = "NÍVEL 3:\nNao sera facil!!!"
        tempo_mensagem = pygame.time.get_ticks()
        mostrar_mensagem = True
               
    if estado["pontuacao"] >= 1000:#Nivel 3
        timer_spawn += 1
        for n in range(conf_level[3]["quantidade_inimigos"]): 
            if timer_spawn % 200 == 0:
                inimigos.append(Inimigo(random.randint(0, 750), 0, random.randint(conf_level[1]["vel_min"], conf_level[1]["vel_max"])))
            if timer_spawn % 60 == 0:
                estado["pontuacao"] += 9 # pontos por segundo

    # Renderizar 
    TELA.fill((20, 20, 40))
    jogador.desenhar(TELA)
    
    for ini in inimigos[:]:
        ini.desenhar(TELA)
        
    for bala in balas_no_jogo[:]: 
        bala.atualizar()
        bala.desenhar(TELA)
        bala_bateu = False
        for ini in inimigos[:]:   
            if bala.rect.colliderect(ini.rect):
                print("POW! Acertou!")
                ini.vida_inimigo -= 1
                bala_bateu = True # Tira vida do inimigo
                if ini.vida_inimigo <= 0:
                    estado["pontuacao"] += 50
                    inimigos.remove(ini)
                    
                break
        if bala_bateu: balas_no_jogo.remove(bala)
        elif bala.rect.x < 0 or bala.rect.x > 800 or bala.rect.y < 0 or bala.rect.y > 600:
            balas_no_jogo.remove(bala)
            
        # --- SISTEMA DE MENSAGEM TEMPORÁRIA ---
    if mostrar_mensagem == True:
        tempo_atual = pygame.time.get_ticks()
        
        # Checa se a diferença entre agora e o início é menor que 2 segundos
        if tempo_atual - tempo_mensagem < 2000:
            # Pinta a mensagem na tela
            texto = fonte_grande.render(mensagem_nivel, True, (255, 255, 0)) # Amarelo
            TELA.blit(texto, (200, 300)) # Centraliza mais ou menos na tela
        else:
            # Se já passou de 2000 ms, desliga a mensagem!
            mostrar_mensagem = False

        
                
            
        # --- LIMPEZA DE TELA ---
        
    desenhar_hud(TELA, estado) # função definida anteriormente
    
    pygame.display.flip()
    CLOCK.tick(60)

# Fim de jogo
desenhar_game_over(TELA)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
sys.exit()
