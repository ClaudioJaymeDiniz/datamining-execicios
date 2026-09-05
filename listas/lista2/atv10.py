import pandas as pd
import numpy as np

dados = {
    "Evento": ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40]
}

df = pd.DataFrame(dados)

# 1. Media e do desvio-padao amostral
media = df["Tentativas_Login"].mean()
desvio = df["Tentativas_Login"].std()

# 2. Z-Score
df["Z_Score"] = (df["Tentativas_Login"] - media) / desvio

# 3. Z| > 3
df["Status"] = np.where(df["Z_Score"].abs() > 3, "Investigar (|Z| > 3)", "Comum")

print("--- RELATÓRIO DE EVENTOS DE SEGURANÇA ---")
print(df.to_string(index=False))

print(f"\nMédia do conjunto: {media:.2f} tentativas")
print(f"Desvio-padrão: {desvio:.2f}")

print("\n--- EVENTOS COM |Z| > 3 ---")
df_suspeitos = df[df["Status"] == "Investigar (|Z| > 3)"]
if df_suspeitos.empty:
    print("Nenhum evento atingiu o limiar estrito de |Z| > 3.")
else:
    print(df_suspeitos.to_string(index=False))