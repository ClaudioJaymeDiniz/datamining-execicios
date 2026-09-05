temperaturas = [21, 23, 25, 27, 29]
media = 25
desvio = 2

z_scores = []

print("--- CALCULO DOS Z-SCORES ---")
for temp in temperaturas:
    z = (temp - media) / desvio
    z_scores.append(z)
    print(f"Temperatura: {temp}°C | Z-Score: {z:+.1f} | |Z|: {abs(z):.1f}")

# Encontrando o maior valor absoluto de Z
maior_abs_z = max([abs(z) for z in z_scores])

# Identificando as temperaturas que possuem esse maior valor absoluto
mais_incomuns = [
    temp for temp, z in zip(temperaturas, z_scores) if abs(z) == maior_abs_z
]

print("\n--- RESULTADO DA ANALISE ---")
print(f"Maior valor absoluto de Z (|Z|): {maior_abs_z:.1f}")
print(f"Temperatura(s) com maior |Z|: {mais_incomuns}")