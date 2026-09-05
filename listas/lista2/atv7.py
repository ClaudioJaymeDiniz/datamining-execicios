def interpretar_z(z):
    if abs(z) > 3:
        return "Investigar"
    elif z < 0:
        return "Abaixo da média"
    elif z > 0:
        return "Acima da média"
    else:
        return "Na média"


valores_z = [-3.5, -1.2, 0, 0.8, 3.7]

print("--- TESTE DA FUNÇÃO DE INTERPRETAÇÃO ---")
for z in valores_z:
    classificacao = interpretar_z(z)
    print(f"Z-Score: {z:+4.1f} | |Z|: {abs(z):3.1f} -> {classificacao}")