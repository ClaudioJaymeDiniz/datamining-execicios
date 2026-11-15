import math
import numpy as np
import pandas as pd

# Dados fornecidos
registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4]
}

chaves = list(registros.keys())
matriz_dados = []

# Passos 28 e 29: Calcular a distância Euclidiana entre todos os pares e construir a matriz
for c1 in chaves:
    linha = []
    for c2 in chaves:
        # Passo 28: math.dist() calcula a distância Euclidiana entre os registros
        dist = math.dist(registros[c1], registros[c2])
        linha.append(dist)
    matriz_dados.append(linha)

# Passo 29: Construir uma matriz de distâncias utilizando pandas.DataFrame
df_matriz = pd.DataFrame(matriz_dados, index=chaves, columns=chaves)

print("=== Matriz de Distâncias entre os Registros ===")
print(df_matriz.round(2))
print("-" * 50)

# Passos 30 e 31: Identificar o menor valor diferente de zero e o par mais próximo
# Substituímos temporariamente os zeros da diagonal por infinito (inf) para o min() ignorá-los
matriz_sem_zero = df_matriz.replace(0, np.inf)
menor_valor = matriz_sem_zero.min().min()

# Localiza as coordenadas (par de registros) correspondentes à menor distância
resultado_min = np.where(matriz_sem_zero == menor_valor)
par_mais_proximo = (df_matriz.index[resultado_min[0][0]], df_matriz.columns[resultado_min[1][0]])

print(f"Passo 30 - Menor distância diferente de zero: {menor_valor:.2f}")
print(f"Passo 31 - Par de registros mais próximo: {par_mais_proximo[0]} e {par_mais_proximo[1]}")
print("-" * 50)

# Passo 32: Verificar que a diagonal principal possui apenas zeros
# A diagonal principal representa o elemento comparado com ele mesmo (ex: A com A)
diagonal_zero = all(df_matriz.loc[k, k] == 0 for k in chaves)
print(f"Passo 32 - A diagonal principal possui apenas zeros? {diagonal_zero}")

# Passo 33: Verificar que a matriz é simétrica (a matriz é igual à sua transposta)
matriz_simetrica = np.allclose(df_matriz, df_matriz.T)
print(f"Passo 33 - A matriz de distâncias é simétrica? {matriz_simetrica}")


# ============================================================================== 
# 1. Por que a diagonal principal é formada apenas por zeros?
#    A diagonal principal corresponde à distância de um registro em relação a 
#    ele mesmo (por exemplo, a distância de A para A, de B para B, etc.). Como a 
#    distância de um ponto para si mesmo é matematicamente zero, todos os valores 
#    dessa diagonal assumem o valor 0.
# 
# 2. Por que d(A, B) = d(B, A)?
#    A distância Euclidiana possui a propriedade matemática da simetria. O 
#    comprimento do segmento de reta que conecta o ponto A ao ponto B é exatamente 
#    o mesmo segmento que conecta o ponto B ao ponto A. Por esse motivo, a 
#    distância de A para B é idêntica à distância de B para A, tornando a 
#    matriz perfeitamente simétrica em relação à sua diagonal principal.
# ==============================================================================