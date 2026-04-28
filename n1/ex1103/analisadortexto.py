frase = input("Digite uma frase: \n")
lista_frase = frase.split()
frequencia = {}

for n in lista_frase:
    if n in frequencia:
        frequencia[n] += frequencia[n]
    else:
        frequencia[n] = 1


print(frequencia)

