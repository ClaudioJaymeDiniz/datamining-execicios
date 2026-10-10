import requests
from bs4 import BeautifulSoup

# URL da página de produtos rodando no servidor local
URL = "http://localhost:8010/index.html"

def raspar_produtos():
    print(f"Acessando {URL}...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        response.encoding = 'utf-8'
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    # Localiza todos os cards de produtos na página
    cards_produtos = soup.find_all('div', class_='produto')

    lista_produtos = []

    # Extrai os dados de cada produto
    for card in cards_produtos:
        nome = card.find('h2', class_='nome-produto').get_text(strip=True)
        fabricante = card.find('span', class_='fabricante').get_text(strip=True)
        categoria = card.find('span', class_='categoria').get_text(strip=True)
        preco = card.find('span', class_='preco-valor').get_text(strip=True)
        situacao = card.find('span', class_='situacao').get_text(strip=True)

        produto_dict = {
            "nome": nome,
            "fabricante": fabricante,
            "categoria": categoria,
            "preco": preco,
            "situacao": situacao
        }
        lista_produtos.append(produto_dict)

    # Parte 1: Exibir todos os produtos de forma organizada
    print(f"\n==========================================")
    print(f" CATÁLOGO COMPLETO DE PRODUTOS ({len(lista_produtos)})")
    print(f"==========================================")
    
    for i, p in enumerate(lista_produtos, 1):
        print(f"{i}. {p['nome']}")
        print(f"   • Fabricante: {p['fabricante']}")
        print(f"   • Categoria: {p['categoria']}")
        print(f"   • Preço: R$ {p['preco']}")
        print(f"   • Situação: {p['situacao']}")
        print("-" * 40)

    # Parte 2: Exibir separadamente apenas os produtos com situação 'Disponível'
    print(f"\n==========================================")
    print(f" PRODUTOS COM SITUAÇÃO: 'Disponível'")
    print(f"==========================================")

    disponiveis = [p for p in lista_produtos if p['situacao'].lower() == 'disponível']

    if disponiveis:
        for i, p in enumerate(disponiveis, 1):
            print(f"{i}. {p['nome']} (R$ {p['preco']}) — Fabricante: {p['fabricante']}")
    else:
        print("Nenhum produto disponível encontrado no momento.")
    print("==========================================\n")

if __name__ == "__main__":
    raspar_produtos()