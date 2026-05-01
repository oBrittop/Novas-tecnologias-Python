import pandas as pd

df = pd.read_csv(
    "n2/csv/funcionarios.csv",
    sep=",",
    encoding= "utf-8",
    na_values=["N/A","-"]
)
print(df.isnull().sum())
df["salario"].dropna(inplace=True)
print(df)