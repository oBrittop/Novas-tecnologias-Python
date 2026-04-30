import numpy as np

# Criando a "imagem" 4x6
imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

brilho_geral = np.mean(imagem)

brilho_linhas = np.mean(imagem, axis=1)

brilho_colunas = np.mean(imagem, axis=0)

linha_escura_idx = np.argmin(brilho_linhas)

print(f"Brilho médio geral: {brilho_geral:.2f}")
print("Médias por linha:", brilho_linhas)
print(f"A linha mais escura é a de índice: {linha_escura_idx}")

imagem_binaria = np.zeros_like(imagem)


imagem_binaria[imagem >= 128] = 255
print("\nImagem Binária (Preto e Branco):")
print(imagem_binaria)