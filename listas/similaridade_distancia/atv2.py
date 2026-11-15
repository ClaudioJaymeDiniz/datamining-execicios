# Dados dos clientes [idade, compras por mês]
cliente_a = [25, 2]
cliente_b = [27, 3]
cliente_c = [45, 10]
cliente_d = [52, 12]

# Passo 8: Distância entre A e B
dif_idade_ab = cliente_a[0] - cliente_b[0]
dif_compras_ab = cliente_a[1] - cliente_b[1]
dist_ab = ((dif_idade_ab ** 2) + (dif_compras_ab ** 2)) ** 0.5

# Passo 9: Distância entre A e C
dif_idade_ac = cliente_a[0] - cliente_c[0]
dif_compras_ac = cliente_a[1] - cliente_c[1]
dist_ac = ((dif_idade_ac ** 2) + (dif_compras_ac ** 2)) ** 0.5

# Passo 10: Distância entre A e D
dif_idade_ad = cliente_a[0] - cliente_d[0]
dif_compras_ad = cliente_a[1] - cliente_d[1]
dist_ad = ((dif_idade_ad ** 2) + (dif_compras_ad ** 2)) ** 0.5

# Armazenando os resultados em um dicionário para facilitar a comparação
distancias = {
    "Cliente B": dist_ab,
    "Cliente C": dist_ac,
    "Cliente D": dist_ad
}

# Passos 11 e 12: Comparação e determinação da menor distância
cliente_mais_proximo = min(distancias, key=distancias.get)
menor_distancia = distancias[cliente_mais_proximo]

# Passo 13: Exibir todas as distâncias e o cliente mais próximo
print("=== Distâncias em relação ao Cliente A ===")
print(f"Distância entre A e B: {dist_ab:.2f}")
print(f"Distância entre A e C: {dist_ac:.2f}")
print(f"Distância entre A e D: {dist_ad:.2f}")
print("------------------------------------------")
print(f"O cliente mais semelhante ao Cliente A é o **{cliente_mais_proximo}**, com a menor distância de {menor_distancia:.2f}.")


# ==============================================================================
# Na distância Euclidiana, cada atributo (idade e compras por mês) funciona como 
# uma coordenada em um plano cartesiano. Quanto menor for o valor da distância 
# entre dois pontos, mais próximos eles estão geograficamente/matematicamente.
# No contexto dos dados, isso significa que perfis com menor distância possuem 
# valores de idade e frequência de compras muito parecidos com os do Cliente A, 
# representando comportamentos e características demográficas altamente semelhantes.
# ==============================================================================