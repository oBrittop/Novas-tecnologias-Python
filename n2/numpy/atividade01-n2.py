import numpy as np

notas = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 4.5, 6.0, 5.5],
    [9.0, 9.5, 8.5, 10.0],
    [3.0, 4.0, 5.0, 4.5],
    [8.0, 7.5, 9.0, 8.5]
])

medias = []

medias = np.mean(notas, axis=1)

print("A medias das notas sao:",medias)
print("\nA maior nota e ",np.max(medias))
indece_maior_nota = np.argmax(medias)
print(" e pertence ao aluno de id:", indece_maior_nota)

media_provas = np.mean(notas, axis=0)
desvio_provas = np.std(notas, axis=0)
notas_normalizadas = (notas - media_provas) / desvio_provas

print("\nNotas Normalizadas (Média ~0, Desvio ~1):")
print(notas_normalizadas)

aprovados_mask = medias >= 6.0

notas_aprovados = notas[aprovados_mask]

print("\nStatus dos alunos (True = Aprovado):")
print(aprovados_mask)

print("\nNotas originais apenas dos alunos aprovados:")
print(notas_aprovados)