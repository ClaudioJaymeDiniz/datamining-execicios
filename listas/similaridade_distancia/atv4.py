import math

# Dicionário com os clientes e seus atributos [idade, compras por mês]
clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12]
}

# Definindo o cliente de referência
cliente_referencia = "A"
dados_a = clientes[cliente_referencia]

distancias = {}

# Passos 18, 19 e 20: Importar math, usar math.dist() e exibir cada distância calculada
print(f"=== Distâncias em relação ao Cliente {cliente_referencia} ===")

for nome, dados in clientes.items():
    if nome == cliente_referencia:
        continue  # Pula o cálculo de A para A
    
    # math.dist() calcula diretamente a distância Euclidiana entre dois pontos (listas ou tuplas)
    distancia = math.dist(dados_a, dados)
    distancias[nome] = distancia
    
    print(f"Distância entre {cliente_referencia} e {nome}: {distancia:.2f}")

print("-" * 50)

# Passo 21: Identificar automaticamente o cliente mais próximo de A
# Usamos a função min() passando como chave o dicionário.get para encontrar a menor distância
cliente_mais_proximo = min(distancias, key=distancias.get)
menor_distancia = distancias[cliente_mais_proximo]

# Exibição final solicitada
print(f"O cliente com o perfil mais próximo do Cliente {cliente_referencia} é o **Cliente {cliente_mais_proximo}**, "
      f"apresentando uma distância de {menor_distancia:.2f} considerando os atributos de idade e compras por mês.")