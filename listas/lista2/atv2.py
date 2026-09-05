casos = [85, 100, 120]
media = 100
desvio = 10

print("--- ANÁLISE DOS CASOS ---")

for valor in casos:
    # Calculo do Z-Score: (X - Media) / Desvio Padrao
    z_score = (valor - media) / desvio
    
    # Classificacao em relacao a media
    if z_score > 0:
        posicao = "acima da media"
    elif z_score < 0:
        posicao = "abaixo da media"
    else:
        posicao = "exatamente na media"
        
    print(f"Valor: {valor:3d} | Z-Score: {z_score:+.1f} | Posicao: {posicao}")