import pandas as pd
print(pd.__version__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A", "-"]
    )
# Exercicio Parcial 

print(df.head())
print(df.info())
print(df.shape)
print("-"*150)
descito = df.describe
print(descito)

print("Quantidade distintintas de Classes:",df["Pclass"].nunique())

print("Frequencia passageiros por sexo", df["Sex"].value_counts())
print("-"*150)
print(df.loc[0:10, ["Name", "Age"]])
print(df.iloc[14:15, 0:11])
print("-"*150)
filtro_age = df["Age"] > 60
print(df[filtro_age])
print("-"*150)
filtro_minas_ricas = (df["Sex"] == "female") & (df["Pclass"] == 1)
print(df[filtro_minas_ricas])
print("-"*150)
print(df[df["Fare"].between(50, 100)])
print("-"*150)
print(df.query("Embarked == 'C' and Survived == 1"))
