import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../csv/simulacao_bugs_ti.csv")
print(df)
media_tempohoras_resolucao = df["Tempo_Resolucao_Horas"].mean()
df["Tempo_Resolucao_Horas"]= df["Tempo_Resolucao_Horas"].fillna(media_tempohoras_resolucao)
print("-"*120)
print(df)
tempo_medio_x_modulo = df.groupby('Módulo')["Tempo_Resolucao_Horas"].mean()
print("-"*120)
print(tempo_medio_x_modulo)
print("-"*120)

tempo_ordenado = tempo_medio_x_modulo.sort_values(ascending=False)

print("Médias Ordenadas Prontas para o Gráfico:")
print(tempo_ordenado)
print("-" * 50)

tempo_ordenado.plot(kind='bar', color='#4C72B0', edgecolor='black')
plt.title("Tempo Médio de Resolução de Bugs por Módulo", fontsize=14)
plt.xlabel("Módulo do Sistema", fontsize=12)
plt.ylabel("Tempo Médio (Horas)", fontsize=12)
plt.xticks(rotation=0)  # Deixa o nome (Backend, Frontend) retinho de ler
plt.show()