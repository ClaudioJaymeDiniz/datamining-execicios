import numpy as np

dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]

# 1. IQR
q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# 2. Media e Desvio-Padrao
media = np.mean(dados)
desvio = np.std(dados, ddof=1)  # Desvio-padrão amostral

# 3. Z-Score do valor 30
valor = 30
z_score = (valor - media) / desvio


print("--- MÉTODO DO IQR (ROBUSTO) ---")
print(f"Q1 (25%): {q1:.2f}")
print(f"Q3 (75%): {q3:.2f}")
print(f"IQR: {iqr:.2f}")
print(f"Limite Inferior: {limite_inferior:.2f}")
print(f"Limite Superior: {limite_superior:.2f}")

print("\n--- MÉTODO DO Z-SCORE (SENSÍVEL) ---")
print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print(f"Z-Score do valor 30: {z_score:+.2f}")