import numpy as np
from sklearn.ensemble import IsolationForest

# 1. Criar pelo menos 12 medições de latência (ms)
# Maioria entre 20 e 70 ms, com dois valores acima de 200 ms
latencias = np.array([
    [25], [30], [45], [52], [38], 
    [60], [22], [41], [68], [33], 
    [49], [55], [215], [240]
])

# 2. Aplicar o Isolation Forest
# Definimos a contaminação considerando os picos anômalos
modelo = IsolationForest(contamination=0.15, random_state=42)
previsoes = modelo.fit_predict(latencias)

# 3. Imprimir a classificação de cada medição
print("--- Resultados da Classificação de Latência ---")
for latencia, pred in zip(latencias, previsoes):
    status = "Normal (Estável)" if pred == 1 else "Anomalia / Pico de Latência 🚨"
    print(f"Latência: {latencia[0]:3d} ms -> {status}")