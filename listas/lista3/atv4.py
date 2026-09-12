import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# 1. Dados de viagens: [passageiros, atraso_minutos]
viagens = np.array([
    [32, 3], [45, 5], [50, 4],
    [60, 6], [55, 5], [70, 7],
    [65, 6], [80, 8], [75, 7],
    [10, 45]
])

# 2. Aplicar o Isolation Forest às duas características
modelo = IsolationForest(contamination=0.1, random_state=42)
previsoes = modelo.fit_predict(viagens)

# 3. Identificar e imprimir a classificação
print("--- Resultados da Classificação de Viagens ---")
for dados, pred in zip(viagens, previsoes):
    status = "Normal" if pred == 1 else "Anomalia / Incomum 🚨"
    print(f"Passageiros: {dados[0]:2d} | Atraso: {dados[1]:2d} min -> {status}")

# 4. Criar o gráfico de dispersão
plt.figure(figsize=(8, 5))
normais = viagens[previsoes == 1]
anomalias = viagens[previsoes == -1]

plt.scatter(normais[:, 0], normais[:, 1], color='blue', label='Normal', s=80, alpha=0.8)
plt.scatter(anomalias[:, 0], anomalias[:, 1], color='red', label='Anomalia', s=120, marker='X')

plt.title('Isolation Forest - Passageiros vs Atraso de Ônibus')
plt.xlabel('Número de Passageiros')
plt.ylabel('Atraso (minutos)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()