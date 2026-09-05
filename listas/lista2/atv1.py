media = 100
desvio = 5
valor = 115

# 1. Distancia entre o valor e a media
distancia = valor - media

# Calculo do Z-Score
z_score = distancia / desvio

# Resultados
print(f"Distancia entre o valor e a media: {distancia}")
print(f"Quantidade de desvios-padrao: {z_score}")
print(f"Z-Score obtido: {z_score:.2f}")