import requests
from bs4 import BeautifulSoup

# URL da página do cardápio rodando no servidor local
URL = "http://localhost:8010/index.html"

def raspar_cardapio():
    print(f"Acessando {URL}...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        
        # Garante o suporte a acentos via UTF-8
        response.encoding = 'utf-8'
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Localiza cada seção do cardápio na página
    secoes = soup.find_all('section', class_='secao-cardapio')

    print(f"\n==========================================")
    print(f" CARDÁPIO ORGANIZADO POR CATEGORIAS")
    print(f"==========================================\n")

    # Percorre cada seção individualmente
    for secao in secoes:
        # Extrai o título da categoria da seção atual
        categoria_titulo = secao.find('h2', class_='categoria-titulo').get_text(strip=True)
        
        print(f"📂 CATEGORIA: {categoria_titulo.upper()}")
        print("-" * 45)

        # Localiza apenas os itens pertencentes a esta seção específica
        itens = secao.find_all('div', class_='item-cardapio')

        for item in itens:
            nome = item.find('h3', class_='nome-item').get_text(strip=True)
            preco = item.find('span', class_='preco-item').get_text(strip=True)
            descricao = item.find('p', class_='descricao-item').get_text(strip=True)

            print(f"  • {nome} — {preco}")
            print(f"    Descrição: {descricao}")
        
        print("\n" + "=" * 45 + "\n")

if __name__ == "__main__":
    raspar_cardapio()