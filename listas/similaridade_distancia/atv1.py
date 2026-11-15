# Passo 1: Armazene os dados dos clientes em listas
cliente_a = [25, 2]
cliente_b = [28, 6]

# Passo 2: Calcule a diferença entre as idades (posição 0)
diferenca_idade = cliente_a[0] - cliente_b[0]

# Passo 3: Calcule a diferença entre as quantidades de compras (posição 1)
diferenca_compras = cliente_a[1] - cliente_b[1]

# Passo 4: Eleve cada diferença ao quadrado
quadrado_idade = diferenca_idade ** 2
quadrado_compras = diferenca_compras ** 2

# Passo 5: Some os resultados obtidos
soma_dos_quadrados = quadrado_idade + quadrado_compras

# Passo 6: Calcule a raiz quadrada da soma (utilizando ** 0.5 para evitar funções prontas de distância)
distancia_euclidiana = soma_dos_quadrados ** 0.5

# Passo 7: Exiba a distância Euclidiana entre os dois clientes
print(f"A distância Euclidiana entre o Cliente A e o Cliente B é: {distancia_euclidiana:.2f}")