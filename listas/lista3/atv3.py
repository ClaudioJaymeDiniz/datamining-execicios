import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 1. Dados de consumo: [distância_km, litros_consumidos]
consumo = np.array([
    [10, 1.0], [20, 1.8], [30, 2.6],
    [40, 3.5], [50, 4.3], [60, 5.1],
    [70, 6.0], [80, 7.0], [90, 8.0],
    [100, 20.0]
])

# 2. Aplicar o Isolation Forest às duas características
modelo = IsolationForest(contamination=0.1, random_state=42)
previsoes = modeloo = modelo.fit_predict(consumo)

# 3. Imprimir a classificação
print("--- Resultados da Classificação ---")
for dados, pred in zip(consumo, previsoes):
    status = "Normal" if pred == 1 else "Anomalia / Incomum 🚨"
    print(f"Distância: {dados[0]:3.0f} km | Litros: {dados[1]:4.1f} L -> {status}")

# 4. Criar o gráfico de dispersão
plt.figure(figsize=(8, 5))
normais = consumo[previsoes == 1]
anomalias = consumo[previsoes == -1]

plt.scatter(normais[:, 0], normais[:, 1], color='blue', label='Normal', s=80, alpha=0.8)
plt.scatter(anomalias[:, 0], anomalias[:, 1], color='red', label='Anomalia', s=120, marker='X')

plt.title('Isolation Forest - Consumo de Combustível vs Distância')
plt.xlabel('Distância Percorrida (km)')
plt.ylabel('Litros Consumidos (L)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()