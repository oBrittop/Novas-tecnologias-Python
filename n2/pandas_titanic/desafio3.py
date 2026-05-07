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
df_aux = pd.merge(df_estoque, df_produtos, on="produto_id", how='left')
# df = pd.merge(df_aux, df_vendas, on="produto_id", how="inner")
print(df_estoque.head())
print("-"*120)
print(df_produtos.head())
print("-"*120)
print(df_vendas.head())
print(df_aux.head())
custo_total_estoque = df_aux.groupby("quantidade")["preco_custo"].prod()
df_aux["custo_total_estoque"] = custo_total_estoque
print(custo_total_estoque)
print(df_aux.head())












# df["custo_total"] = (df["quantidade"] * df["preco_custo"])
# df["valor_venda_mes"] = (df["quantidade_vendida"] * df["preco_custo"] * 1.5)
# print(df)
# filtro_estoque_insuficiente = df["quantidade_vendida"] > df["quantidade"]
# print(df[filtro_estoque_insuficiente])