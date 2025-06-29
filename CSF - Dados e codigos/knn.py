import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# === Caminhos dos arquivos ===
caminho_treino = r'C:\Users\julio\OneDrive\Área de Trabalho\CSF - Dados e codigos\datasets\dadosRP_final.csv'
caminho_teste = r'C:\Users\julio\OneDrive\Área de Trabalho\CSF - Dados e codigos\datasets\dadosTP_final.csv'

# === Carregar os dados ===
df_train = pd.read_csv(caminho_treino)
df_test = pd.read_csv(caminho_teste)

# === Separar features e rótulos ===
X_train = df_train.drop(columns=['rp'])
y_train = df_train['rp']

X_test = df_test.drop(columns=['rp'])
y_test = df_test['rp']

# === Normalizar ===
scaler = MinMaxScaler()
X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.transform(X_test)

# === Treinar modelo KNN ===
k = 10
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_norm, y_train)

# === Previsão ===
y_pred = knn.predict(X_test_norm)

# === Relatório normal ===
print("📌 Avaliação tradicional:")
print("Acurácia:", accuracy_score(y_test, y_pred))
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, zero_division=0))

# === Matriz de confusão ===
plt.figure(figsize=(12, 6))
sns.heatmap(pd.crosstab(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.xlabel("Previsão do modelo (RP)")
plt.ylabel("Posição real (TP)")
plt.title("Matriz de Confusão - KNN com TPs vs RPs")
plt.tight_layout()
plt.show()
