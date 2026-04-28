class Carros:
    def __init__(self, id_carro, nome, preco_diaria, sts):
        self.id_carro = id_carro
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.sts =  sts

    def alugar(self):
        self.sts = "Alugado"
    def devolver(self):
        self.sts = "Disponivel"      

        
class Locadora:
    def __init__(self):
        self.inventario = []
        self.faturamento_por_cliente = {}
        

    def cadastrar_carros(self):
        id_novo = int(input("Diginte o Id do carro: "))
        nome_novo = str(input("Diginte o nome do carro: "))
        preco_novo = float(input("Digite o preco por dia do carro: ").replace(",", "."))
        novo_carro = Carros(id_novo, nome_novo, preco_novo, "Disponivel")
        self.inventario.append(novo_carro)
    
    def realizar_locacao(self, nome_cliente, id_carro, dias):
        print("----Parabens----")
        print(f"Carro alugado para {nome_cliente}")
        for n in self.inventario:
            if n.id_carro == id_carro:
                n.alugar()
                valor = n.preco_diaria * dias 
                self.faturamento_por_cliente[nome_cliente] = valor 
        
    def equipamentos_disponiveis(self):
        for n in self.inventario:
            if n.sts == "Disponivel":
                print("-"*25)
                print(f"{n.nome}   ID: {n.id_carro}\nDiaria : {n.preco_diaria}\n")



# ==========================================
# CÓDIGO TESTE (GAME LOOP / MENU DO SISTEMA)
# ==========================================

# 1. Abre a locadora
minha_locadora = Locadora()

# 2. Inicia o sistema
while True:
    print("\n" + "="*30)
    print("🚗 SISTEMA DA LOCADORA 🚗")
    print("1. Cadastrar Carro")
    print("2. Ver Carros Disponíveis")
    print("3. Alugar Carro")
    print("4. Ver Faturamento da Empresa")
    print("5. Devolver carro")
    print("6. Sair")
    print("="*30)
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        minha_locadora.cadastrar_carros()
        
    elif opcao == "2":
        minha_locadora.equipamentos_disponiveis()
        
    elif opcao == "3":
        cliente = input("\nNome do cliente: ")
        id_desejado = int(input("ID do carro que deseja alugar: "))
        dias_aluguel = int(input("Quantidade de dias: "))
        minha_locadora.realizar_locacao(cliente, id_desejado, dias_aluguel)
        
    elif opcao == "4":
        print("\n--- Faturamento por Cliente ---")
        if not minha_locadora.faturamento_por_cliente:
            print("Nenhum faturamento registrado ainda.")
        else:
            for cliente, valor in minha_locadora.faturamento_por_cliente.items():
                print(f"👤 {cliente}: R${valor:.2f}")
                
    elif opcao == "5":
        #minha_locadora.devolver()
        print("ainda estamos trabalhando na devolucao")

    elif opcao == "6":
        print("\nSaindo do sistema... Até logo e boas vendas!")
        break # Quebra o laço e encerra o programa
        
    else:
        print("\n❌ Opção inválida! Digite um número de 1 a 5.")