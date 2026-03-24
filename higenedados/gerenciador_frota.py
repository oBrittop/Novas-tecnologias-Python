class Equipamento:
    def __init__(self, id_equipamento, nome, preco_diaria):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.status = "Disponível"

    def alugar(self):
        self.status = "Alugado"

    def devolver(self):
        self.status = "Disponível"

class Locadora:
    def __init__(self):
        self.inventario = []
        self.faturamento_por_cliente = {}

    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)

    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        for equipamento in self.inventario:
            if equipamento.id_equipamento == id_equipamento:
                if equipamento.status == "Disponível":
                    equipamento.alugar()
                    custo = equipamento.preco_diaria * dias
                    
                    # Atualiza o dicionário de faturamento
                    if nome_cliente in self.faturamento_por_cliente:
                        self.faturamento_por_cliente[nome_cliente] += custo
                    else:
                        self.faturamento_por_cliente[nome_cliente] = custo
                    
                    print(f"Aluguel de {equipamento.nome} feito para {nome_cliente}.")
                    return
                else:
                    print("Equipamento já está alugado.")
                    return
        print("Equipamento não encontrado.")

    def equipamentos_disponiveis(self):
        nomes_disponiveis = []
        for equipamento in self.inventario:
            if equipamento.status == "Disponível":
                nomes_disponiveis.append(equipamento.nome)
        return nomes_disponiveis
    


locadora = Locadora()

eq1 = Equipamento(1, "Furadeira", 50.0)
eq2 = Equipamento(2, "Makita", 80.0)
eq3 = Equipamento(3, "Betoneira", 150.0)

locadora.cadastrar_equipamento(eq1)
locadora.cadastrar_equipamento(eq2)
locadora.cadastrar_equipamento(eq3)

print(locadora.equipamentos_disponiveis())

locadora.realizar_locacao("Gustavo", 1, 2)
locadora.realizar_locacao("Anna", 3, 5)

print(locadora.equipamentos_disponiveis())

print(locadora.faturamento_por_cliente)