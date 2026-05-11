import pandas as pd

df_estoque = pd.read_csv(
    "n2/csv/estoque_atual.csv",
    sep=",",
    encoding= "utf-8",
    na_values=["N/A","-"]
)
df_produtos = pd.read_csv(
    "n2/csv/produtos.csv",
    sep=",",
    encoding= "utf-8",
    na_values=["N/A","-"]
)
df_vendas = pd.read_csv(
    "n2/csv/vendas_mensal.csv",
    sep=",",
    encoding= "utf-8",
    na_values=["N/A","-"]
)
df_aux_custo_total_estoque = pd.merge(df_estoque, df_produtos, on="produto_id", how='left')
# df = pd.merge(df_aux, df_vendas, on="produto_id", how="inner")
print(df_estoque.head())
print("-"*120)
print(df_produtos.head())
print("-"*120)
print(df_vendas.head())
print("-"*120)
print(df_aux_custo_total_estoque.head())
print("-"*120)
df_aux_custo_total_estoque["custo_total_estoque"] = df_aux_custo_total_estoque["quantidade"] * df_aux_custo_total_estoque["preco_custo"]
print(df_aux_custo_total_estoque.head())
print("-"*120)
df_aux_valor_venda_mes = pd.merge(df_vendas, df_produtos, on="produto_id", how="left")
markup = 1.5
df_aux_valor_venda_mes["valor_venda_mes"] = df_aux_valor_venda_mes["quantidade_vendida"] * df_aux_valor_venda_mes["preco_custo"] * markup
print(df_aux_valor_venda_mes)
print("-"*120)

print("Filtro df estoque baixo:")
df_baixo_estoque = pd.merge(df_vendas, df_estoque, on="produto_id", how="right")
print(df_baixo_estoque)
print("-"*120)
filtro_sem_estoque = df_baixo_estoque["quantidade_vendida"] > df_baixo_estoque["quantidade"]
df_baixo_estoque_filtraqdo =df_baixo_estoque[filtro_sem_estoque]
if df_baixo_estoque_filtraqdo.empty:
    print("Nao tem nenhum registro de estoque negativo!")
else:
    print(df_baixo_estoque_filtraqdo)