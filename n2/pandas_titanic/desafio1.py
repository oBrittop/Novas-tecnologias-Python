import pandas as pd

df = pd.read_csv(
    "n2/csv/vendas.csv",
    sep=',',
    encoding="utf-8",
    na_values=["N/A","-"]
)
print(df.head(10))
df.info()
total_venda = pd.Series(df["quantidade"] * df["preco_unitario"])
df["total_venda"] = total_venda
filtro_eletronicos = df["categoria"] == "Eletrônicos"
filtro_eletronicos_caros = df["total_venda"] >  1000
filtro_full = filtro_eletronicos & filtro_eletronicos_caros
print("-"*150)
print(df[filtro_full])
print("-"*150)
print(df)
print("-"*150)
media_por_cidade =  df.groupby("cidade")["total_venda"].mean()
print(media_por_cidade.sort_values(ascending=False))