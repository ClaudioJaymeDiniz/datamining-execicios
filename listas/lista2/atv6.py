media_a = 100
desvio_a = 2

media_b = 100
desvio_b = 20

valor = 110

# 1. Calculo do Z-Score no Grupo A
z_a = (valor - media_a) / desvio_a

# 2. Calculo do Z-Score no Grupo B
z_b = (valor - media_b) / desvio_b

print("--- COMPARAÇÃO DE CONTEXTOS ---")
print(f"Grupo A (Média: {media_a}, Desvio: {desvio_a}) | Valor: {valor} -> Z-Score: {z_a:+.2f}")
print(f"Grupo B (Média: {media_b}, Desvio: {desvio_b}) | Valor: {valor} -> Z-Score: {z_b:+.2f}")



'''
A distância em valor absoluto entre $110$ e a média $100$ é rigorosamente 
a mesma em ambos os grupos: $10$ unidades ($110 - 100 = 10$). 
Porém, o Z-Score mede a distância relativa em relação à dispersão/variabilidade dos dados:Grupo A 
(Baixa Variabilidade / Desvio = 2):Como o desvio-padrão é muito pequeno ($2$), os dados deste grupo estão 
extremamente concentrados ao redor da média de $100$ (a imensa maioria dos valores varia entre $94$ e $106$).
Estar $10$ unidades distante da média significa andar 5 desvios-padrão, tornando $110$ um evento 
extremamente raro / atípico ($\vert{}Z\vert{} = 5 > 3$).Grupo B (Alta Variabilidade / Desvio = 20):
Como o desvio-padrão é grande ($20$), os dados deste grupo variam amplamente ao redor da média de $100$ 
(valores entre $80$ e $120$ ocorrem com frequência normal).Estar $10$ unidades distante da média 
significa andar apenas meio desvio-padrão, tornando $110$ um valor perfeitamente comum e dentro do 
comportamento esperado do grupo.
'''