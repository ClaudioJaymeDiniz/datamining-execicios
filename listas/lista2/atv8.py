import pandas as pd
import numpy as np

dados = {
    "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400]
}

df = pd.DataFrame(dados)

# 1. Calculo da media e do desvio-padrao da coluna Requisicoes
media = df["Requisicoes"].mean()
desvio = df["Requisicoes"].std()

# 2. Coluna Z_Score
df["Z_Score"] = (df["Requisicoes"] - media) / desvio

# 3. Coluna Status (|Z| > 3 para "Investigar", caso contrario "Comum")
df["Status"] = np.where(df["Z_Score"].abs() > 3, "Investigar", "Comum")

# 4. |Z| > 3
df_investigar = df[df["Status"] == "Investigar"]

print("--- DATAFRAME COMPLETO ---")
print(df.to_string(index=False))

print(f"\nMédia: {media:.2f}")
print(f"Desvio-Padrão: {desvio:.2f}")

print("\n--- LINHAS MARCADAS PARA INVESTIGAÇÃO (|Z| > 3) ---")
if df_investigar.empty:
    print("Nenhuma linha atingiu o critério estrito de |Z| > 3.")
else:
    print(df_investigar.to_string(index=False))