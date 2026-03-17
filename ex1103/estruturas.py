mouse = {
    "nome": "Logitec 305",
    "preco": 168.33,
    "quantidade": 25
}

teclado = {
    "nome": "Logitec oringin",
    "preco": 192.90,
    "quantidade": 18
}

monitor = {
    "nome": "Lg Supreme olde 27' ",
    "preco": 1850.69,
    "quantidade": 14
}

notebook = {
    "nome": "Nitro acer",
    "preco": 5670.89,
    "quantidade": 9
}
rtx7090 = {
    "nome": "Nvidea GPU RTX7090",
    "preco": 85670.89,
    "quantidade": 0

}
estoque = [mouse, teclado, monitor, notebook, rtx7090]
valor_total = 0
intens_caros = []
for n in estoque:
    valor_total += (n["preco"] * n["quantidade"])
    if n["preco"] > 500:
        intens_caros.append(n)

produtos_none = [n["nome"] for n in estoque if n["quantidade"] == 0 ]



print(f"Itens caros :{intens_caros}\n")
print(f"Valor total do estoque:{valor_total}\n")
print(f"Sem estoque: {produtos_none}")



