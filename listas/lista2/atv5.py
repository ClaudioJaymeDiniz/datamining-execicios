import numpy as np

cpu = [42, 45, 47, 44, 46, 43, 48, 92]

# 1. Calculo da media e do desvio-padrao amostral (ddof=1)
media = np.mean(cpu)
desvio = np.std(cpu, ddof=1)

print("--- ESTATÍSTICAS DA CPU ---")
print(f"Média: {media:.2f}%")
print(f"Desvio-padrãa: {desvio:.2f}%\n")

print("--- CLASSIFICAÇÃO DAS LEITURAS DE CPU ---")

for valor in cpu:
    # Calculo do Z-Score
    z_score = (valor - media) / desvio

    if abs(z_score) > 3:
        classificacao = "Investigar"
    else:
        classificacao = "Comum"

    print(f"{valor:2d}% -> Z-Score: {z_score:+6.2f} -> {classificacao}")