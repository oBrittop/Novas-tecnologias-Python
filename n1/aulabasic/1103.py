# Criando uma lista
#frutas = ["maçã", "banana", "laranja", "uva"]
# # Acessando por índice (começa em 0)
# print(frutas[0]) # maçã
# print(frutas[-1]) # uva (último elemento)
# # Fatiamento (slicing)
# print(frutas[1:3]) # ['banana', 'laranja']
# for n in frutas:
#     print(n)

#Dicionario
aluno = {
    "nome": "Gustavo",
    "idade": 18,
    "curso": "Eng.Software"
}

aluno["semestre"] = 5

# print(aluno)

for chave in aluno:
    print(f"{chave}:{aluno[chave]}")


caros = {
    "fiat": ["uno","mobi"],
    "Vlw": ["Gol","Polo"]
}

print(caros["fiat"])