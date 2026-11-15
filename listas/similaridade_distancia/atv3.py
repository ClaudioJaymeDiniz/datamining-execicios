# Dados dos alunos [nota média, frequência (%), horas de estudo por semana]
aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]

# Passo 14: Implementação manual da distância Euclidiana entre A e B (3 dimensões)
dif_nota_ab = aluno_a[0] - aluno_b[0]
dif_freq_ab = aluno_a[1] - aluno_b[1]
dif_horas_ab = aluno_a[2] - aluno_b[2]

soma_quadrados_ab = (dif_nota_ab ** 2) + (dif_freq_ab ** 2) + (dif_horas_ab ** 2)
dist_ab = soma_quadrados_ab ** 0.5

# Passo 15: Implementação manual da distância Euclidiana entre A e C (3 dimensões)
dif_nota_ac = aluno_a[0] - aluno_c[0]
dif_freq_ac = aluno_a[1] - aluno_c[1]
dif_horas_ac = aluno_a[2] - aluno_c[2]

soma_quadrados_ac = (dif_nota_ac ** 2) + (dif_freq_ac ** 2) + (dif_horas_ac ** 2)
dist_ac = soma_quadrados_ac ** 0.5

# Passo 16: Exibição dos resultados
print("=== Distâncias em relação ao Aluno A ===")
print(f"Distância entre A e B: {dist_ab:.2f}")
print(f"Distância entre A e C: {dist_ac:.2f}")
print("------------------------------------------")

# Passo 17: Informar qual aluno está mais próximo de A
if dist_ab < dist_ac:
    aluno_mais_proximo = "Aluno B"
else:
    aluno_mais_proximo = "Aluno C"

print(f"O aluno mais próximo (mais semelhante) ao Aluno A é o **{aluno_mais_proximo}**.")


# ==============================================================================
# OBSERVAÇÃO FINAL:
# A mesma lógica matemática utilizada para calcular a distância Euclidiana em 
# duas dimensões (x e y) aplica-se perfeitamente quando existem três ou mais 
# atributos. Cada atributo adicional representa apenas uma nova dimensão (eixo) 
# no cálculo da diferença quadrática e da raiz quadrada da soma.
# ==============================================================================