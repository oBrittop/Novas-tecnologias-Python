import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
import os
st.set_page_config(page_title="QA Dashboard", layout="wide")

@st.cache_data  
def carregar_dados():
    arquivo = "../csv/commits_dataset.csv"
    
    # Se o arquivo não existir, criamos dados falsos (Mocking)
    if not os.path.exists(arquivo):
        devs = ['Gustavo', 'Ana', 'Carlos', 'Beatriz']
        dados = []
        data_atual = datetime(2026, 1, 1)
        
        for _ in range(100): # Gera 100 commits aleatórios
            data_atual += timedelta(days=random.randint(1, 3)) # Avança alguns dias
            dados.append([
                data_atual.strftime('%Y-%m-%d'),
                random.choice(devs),
                random.randint(10, 500),   # Linhas Adicionadas
                random.randint(0, 200),    # Linhas Removidas
                random.randint(0, 5)       # Bugs Gerados
            ])
            
        df_mock = pd.DataFrame(dados, columns=['Data', 'Desenvolvedor', 'Linhas_Adicionadas', 'Linhas_Removidas', 'Bugs_Gerados'])
        df_mock.to_csv(arquivo, index=False)
    
    df = pd.read_csv(arquivo)
    df['Data'] = pd.to_datetime(df['Data'])
    return df

df = carregar_dados()


st.title("🛡️ Dashboard do Engenheiro de Qualidade")
st.write("Análise de commits, linhas de código e bugs gerados pela equipe.")

st.sidebar.header("Filtros de Pesquisa")
lista_devs = df['Desenvolvedor'].unique()

dev_selecionado = st.sidebar.radio("Selecione o Desenvolvedor:", lista_devs)

st.sidebar.divider()
st.sidebar.info("Utilize este painel para monitorar a saúde do código.")
df_filtrado = df[df['Desenvolvedor'] == dev_selecionado]


total_linhas = df_filtrado['Linhas_Adicionadas'].sum()

st.subheader(f"Métricas de {dev_selecionado}")
st.metric(label="Total de Linhas Adicionadas", value=f"{total_linhas:,} linhas")

st.divider()


st.subheader(f"📈 Evolução de Bugs Gerados no Tempo ({dev_selecionado})")

df_grafico = df_filtrado[['Data', 'Bugs_Gerados']].set_index('Data')
st.line_chart(df_grafico, color="#ff4b4b")

st.divider()
st.subheader("⚠️ Análise de Risco da Equipe")

if st.button("Descobrir Maior Gerador de Bugs (Média)"):
    medias_bugs = df.groupby('Desenvolvedor')['Bugs_Gerados'].mean()

    dev_mais_bugs = medias_bugs.idxmax()
    maior_media = medias_bugs.max()

    st.error(f"🚨 **Atenção:** O desenvolvedor com a maior média de bugs por commit é **{dev_mais_bugs}** (Média: {maior_media:.2f} bugs/commit).")
    st.write("Ranking completo:")
    st.dataframe(medias_bugs.sort_values(ascending=False))