import numpy as np
from sklearn.ensemble import IsolationForest

# 1. Dados de vendas
vendas = np.array([
    [80], [85], [90], [88],
    [92], [87], [95], [89],
    [91], [400]
])

# 2. Criar o modelo Isolation Forest
# Contaminação = 1 em 10 observações (0.1)
modelo = IsolationForest(contamination=0.1, random_state=42)

# 3. Ajustar o modelo e classificar as vendas
# fit_predict retorna 1 para valores normais e -1 para anomalias/outliers
previsoes = modelo.fit_predict(vendas)

# 4. Mostrar o valor sinalizado
print("--- Resultados da Classificação ---")
for valor, pred in zip(vendas, previsoes):
    status = "Normal" if pred == 1 else "Anomalia / Outlier 🚨"
    print(f"Venda: {valor[0]} -> {status}")