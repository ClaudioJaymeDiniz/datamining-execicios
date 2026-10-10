import requests
from bs4 import BeautifulSoup

# URL da página da biblioteca rodando no servidor local
URL = "http://localhost:8010/index.html"

def raspar_biblioteca():
    print(f"Acessando {URL}...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        
        # Garante a codificação correta para leitura de acentos
        response.encoding = 'utf-8'
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Localiza todos os blocos de livros na página
    artigos_livros = soup.find_all('article', class_='livro')

    lista_livros = []

    # Extrai os dados e palavras-chave de cada livro
    for artigo in artigos_livros:
        titulo = artigo.find('h2', class_='titulo-livro').get_text(strip=True)
        autor = artigo.find('span', class_='autor').get_text(strip=True)
        ano = artigo.find('span', class_='ano').get_text(strip=True)
        genero = artigo.find('span', class_='genero').get_text(strip=True)
        situacao = artigo.find('span', class_='situacao').get_text(strip=True)

        # Percorre a lista de palavras-chave (ul -> li)
        keywords_elements = artigo.find_all('li', class_='tag-keyword')
        palavras_chave = [kw.get_text(strip=True) for kw in keywords_elements]

        livro_dict = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "genero": genero,
            "situacao": situacao,
            "palavras_chave": palavras_chave
        }
        lista_livros.append(livro_dict)

    # Exibição de todos os livros de forma organizada
    print(f"\n==========================================")
    print(f" ACERVO COMPLETO DA BIBLIOTECA ({len(lista_livros)} obras)")
    print(f"==========================================")

    for i, l in enumerate(lista_livros, 1):
        print(f"Livro {i}: {l['titulo']}")
        print(f"  • Autor: {l['autor']} ({l['ano']})")
        print(f"  • Gênero: {l['genero']}")
        print(f"  • Situação: {l['situacao']}")
        print(f"  • Palavras-chave: {', '.join(l['palavras_chave'])}")
        print("-" * 50)

    # Filtragem e exibição apenas dos livros disponíveis
    print(f"\n==========================================")
    print(f" LIVROS COM SITUAÇÃO: 'Disponível'")
    print(f"==========================================")

    disponiveis = [l for l in lista_livros if l['situacao'].lower() == 'disponível']

    if disponiveis:
        for i, l in enumerate(disponiveis, 1):
            print(f"{i}. {l['titulo']} — Autor: {l['autor']}")
            print(f"   Palavras-chave: {', '.join(l['palavras_chave'])}")
    else:
        print("Nenhum livro disponível no momento.")
    print("==========================================\n")

if __name__ == "__main__":
    raspar_biblioteca()