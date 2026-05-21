import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df = pd.read_csv('../csv/winequality-red.csv', sep=';')
df["qualidade_alta"] = (df["quality"] >= 7).astype(int)  
x = df.drop(columns=["qualidade_alta","quality"])
y = df["qualidade_alta"]
X_train, X_test, Y_train, Y_test, = train_test_split(
    x, 
    y,
    test_size=0.25,
    stratify=y,
    random_state=42
)


# ==========================================
# 1. ESCALONAMENTO (Apenas para o KNN)
# ==========================================
scaler = StandardScaler()

# print("Primeiras linhas do X_train:")
# print(X_train.head())
# print("\nTamanho do Treino:", X_train.shape)
# print("Tamanho do Teste:", X_test.shape)