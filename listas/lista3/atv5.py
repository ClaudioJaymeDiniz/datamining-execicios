import numpy as np
from sklearn.ensemble import IsolationForest

# 1. Dados de consumo de água (litros/m³)
consumo_agua = np.array([
    [48], [52], [50], [55],
    [49], [53], [51], [54],
    [56], [12], [180]
])

print("--- 1. ABORDAGEM: Regra Fixa (Limiar Manual) ---")
# Definindo uma regra fixa: Normal entre 30 e 100
limite_inferior = 30
limite_superior = 100

for valor in consumo_agua:
    v = valor[0]
    if v < limite_inferior or v > limite_superior:
        print(f"Consumo: {v} -> Anomalia pela Regra 🚨")
    else:
        print(f"Consumo: {v} -> Normal")


print("\n--- 2. ABORDAGEM: Isolation Forest ---")
# Como temos 11 elementos e 2 extremos claros, definimos contamination ~ 0.2 (2 em 11)
modelo = IsolationForest(contamination=0.2, random_state=42)
previsoes = modelo.fit_predict(consumo_agua)

for valor, pred in zip(consumo_agua, previsoes):
    v = valor[0]
    status = "Normal" if pred == 1 else "Anomalia / Outlier 🚨"
    print(f"Consumo: {v} -> {status}")