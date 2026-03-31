transacoes = [
    (1, "Infraestrutura", 1500.50),
    (2, "Licenças", 450.00),
    (3, "Infraestrutura", 3200.00),
    (4, "Marketing", 800.00),
    (5, "Licenças", 150.00)
]
def dic_f(transacoes, dicionario):
       for n in transacoes:
                categoria = n[1]
                valor_aux = n[2]
                if n[1] in dicionario:
                        dicionario[categoria] = dicionario[categoria] + valor_aux
                else:
                        dicionario[categoria] = valor_aux

       print("Gastos por categoria\n",dicionario)


mi_set = set()
for n in transacoes:
        mi_set.add(n[1])

dicionario = {}

print(mi_set)
dic_f(transacoes, dicionario)



                

print(mi_set)