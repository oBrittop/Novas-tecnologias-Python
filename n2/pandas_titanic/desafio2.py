import pandas as pd

df = pd.read_csv(
    "n2/csv/funcionarios.csv",
    sep=",",
    encoding= "utf-8",
    na_values=["N/A","-"]
)
print(df.isnull().sum())
print(df)
print("-"*150)
df.dropna(subset=["salario"], inplace=True)
print(df)
print("-"*150)
media_idade = df["idade"].mean()
df.fillna({"idade":media_idade}, inplace=True)
print(df)
print("-"*150)
df.info()
df["data_admissao"] = pd.to_datetime(df["data_admissao"])
dias_trabalhados = (pd.to_datetime("today") - df["data_admissao"]).dt.days
df["anos_empresa"] = (dias_trabalhados/365.25).astype(float)
print(df)
print("-"*150)
media_departamento = df.groupby("departamento")["salario"].transform("mean")
filtro_anos_empresa = df["anos_empresa"] > 5
filtro_salario_baixo = df["salario"] < media_departamento
print(df[filtro_salario_baixo & filtro_anos_empresa])