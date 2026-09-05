import numpy as np

latencias = [98, 102, 101, 99, 100, 103, 97, 180]

# 1. Calculo da media e do desvio-padrao amostral (ddof=1) ou populacional (ddof=0)
# Utilizaremos ddof=1 (amostral), padrao para conjuntos de dados de medições
media = np.mean(latencias)
desvio = np.std(latencias, ddof=1)

# 2. Calculo do Z-Score para a latência de 180 ms
alvo = 180
z_score = (alvo - media) / desvio

print("--- ANÁLISE DE LATÊNCIA DA API ---")
print(f"Média das latências: {media:.2f} ms")
print(f"Desvio-padrão: {desvio:.2f} ms")
print(f"Z-Score para {alvo} ms: {z_score:+.2f}")
print(f"|Z|: {abs(z_score):.2f}")

print("\n--- AVALIAÇÃO DE REGRA PRÁTICA (|Z| > 3) ---")
if abs(z_score) > 3:
    print(
        f"O valor de {alvo} ms MERRECE INVESTIGAÇÃO, pois |Z| = {abs(z_score):.2f} > 3."
    )
else:
    print(
        f"O valor de {alvo} ms NÃO excede o limite crítico (|Z| = {abs(z_score):.2f} <= 3)."
    )

print("\n--- LEMBRETE IMPORTANTE DE CIÊNCIA DE DADOS ---")
print(
    "⚠️ AVISO: Identificar um valor como potencial outlier (|Z| > 3) apenas sinaliza que ele "
    "deve ser INVESTIGADO. Um outlier NÃO deve ser removido automaticamente! "
    "Ele pode representar um evento real importante (como uma queda de servidor, gargalo de banco de dados "
    "ou pico de requisições) que precisa ser diagnosticado pela equipe de engenharia."
)