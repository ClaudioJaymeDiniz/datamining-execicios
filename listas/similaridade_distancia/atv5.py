import math
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Passo 22: Criar um DataFrame utilizando pandas
dados_clientes = {
    "Cliente": ["A", "B", "C", "D", "E"],
    "Idade": [20, 25, 40, 55, 70],
    "Renda": [2000, 3000, 6000, 9000, 12000]
}
df_clientes = pd.DataFrame(dados_clientes).set_index("Cliente")

print("=== DataFrame Original ===")
print(df_clientes)
print("-" * 40)

# Passo 23: Calcular com math.dist() a distância Euclidiana entre A e B (valores originais)
valores_a_orig = df_clientes.loc["A"].tolist()
valores_b_orig = df_clientes.loc["B"].tolist()
dist_orig_ab = math.dist(valores_a_orig, valores_b_orig)

print(f"Passo 23 - Distância original entre A e B: {dist_orig_ab:.2f}")

# Passo 24: Normalize as colunas Idade e Renda utilizando MinMaxScaler, do scikit-learn
scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(
    scaler.fit_transform(df_clientes),
    columns=df_clientes.columns,
    index=df_clientes.index
)

# Passo 25: Exibir o DataFrame com os valores normalizados
print("\n=== Passo 25: DataFrame com Valores Normalizados (0 a 1) ===")
print(df_normalizado)
print("-" * 40)

# Passo 26: Calcular novamente a distância Euclidiana entre A e B usando os valores normalizados
valores_a_norm = df_normalizado.loc["A"].tolist()
valores_b_norm = df_normalizado.loc["B"].tolist()
dist_norm_ab = math.dist(valores_a_norm, valores_b_norm)

print(f"Passo 26 - Distância normalizada entre A e B: {dist_norm_ab:.4f}")

# Passo 27: Comparar os dois resultados
print(f"\nPasso 27 - Comparação:")
print(f"  • Distância usando valores originais: {dist_orig_ab:.2f}")
print(f"  • Distância usando valores normalizados: {dist_norm_ab:.4f}")


# ==============================================================================
# A distância Euclidiana é calculada somando os quadrados das diferenças de 
# cada atributo. Como a Idade varia em uma faixa pequena (de 20 a 70, amplitude 
# de 50) e a Renda varia em uma faixa muito ampla (de 2.000 a 12.000, amplitude 
# de 10.000), as diferenças numéricas brutas da Renda são centenas de vezes 
# maiores que as da Idade. 
# 
# Quando elevamos essas diferenças ao quadrado, o peso da Renda domina 
# completamente o resultado matemático, fazendo com que a Idade praticamente 
# não afete o cálculo da distância. A normalização com MinMaxScaler resolve 
# esse desequilíbrio ao colocar todas as colunas na mesma escala (de 0 a 1), 
# garantindo que todos os atributos tenham o mesmo peso na análise de similaridade.
# ==============================================================================