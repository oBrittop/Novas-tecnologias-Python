import os

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.jogador = "x"

    def mostrar_tabuleiro(self):
        for n in self.tabuleiro:
            print(n)
            print("\n")


    def fazer_jogada(self, posicao_jogada, jogador):
        for n in range(3):
            for x in range(3) :
                if self.tabuleiro[n][x] == posicao_jogada:
                    self.tabuleiro[n][x] = jogador  
                    return True
        print("Digite um numero valido")
        return False     


    def verificar_vencendor(self):
        for linha in range(3):
            if self.tabuleiro[linha][0] == self.tabuleiro[linha][1] == self.tabuleiro[linha][2]:
                return True#Alguem ganhou na horizontal 
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna]:
                return True # Alguem ganhou na vertical
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2]:
            return True # Alguem ganha diagonal 00 ou 22
        elif self.tabuleiro[2][0] == self.tabuleiro[1][1] == self.tabuleiro[0][2]:
            return True # Alguem ganho na diagonal 20 ou 02
        else:
            return False

        print("")
        
jogar = JogoDaVelha()
print(".-----!Bem vindo ao jogo da velha em Piton!-----.\n")
vencedor = False
jogar.jogador
print("Voce vai conmecar jogando com o X\n")
print("Esse e nosso tabuleiro:\n")
jogar.mostrar_tabuleiro()
posicao_jogada = int(input("\nOnde deseja jogar ?"))
jogar.fazer_jogada(posicao_jogada, jogar.jogador)
turno = 1

os.system('cls')
while vencedor == False:

    vencedor = jogar.verificar_vencendor()
    if vencedor == True:
        print(f"jogo acabou vencendor e: {jogar.jogador}")
        break    


    jogar.jogador = "o"
    jogar.mostrar_tabuleiro()
    print("-------")

    print(f"\n Vez do jogador: {jogar.jogador}")
    jogada_valida = False

    while jogada_valida == False:
        posicao_jogada = int(input("\nOnde deseja jogar ?"))
        jogada_valida = jogar.fazer_jogada(posicao_jogada, jogar.jogador)

    vencedor = jogar.verificar_vencendor()
    turno += 1

    if vencedor == True:
        print(f"jogo acabou vencendor e: {jogar.jogador}")
        break

    os.system('cls')
    jogar.mostrar_tabuleiro()
    print("-------")
    jogar.jogador = "x"
    jogar.mostrar_tabuleiro()
    print("-------")
    print(f"\n Vez do jogador: {jogar.jogador}")
    jogada_valida = False
    while jogada_valida == False:
        posicao_jogada = int(input("\nOnde deseja jogar ?"))
        jogada_valida = jogar.fazer_jogada(posicao_jogada, jogar.jogador)
    turno += 1
    os.system('cls')
    jogar.mostrar_tabuleiro()
    print("-------")
    if turno > 9:
        os.system('cls')
        print("--Deu velha!!--")
        print('Nao ha vencedore!')
        break






    



