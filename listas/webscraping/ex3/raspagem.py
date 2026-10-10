import requests
from bs4 import BeautifulSoup

# URL da página de notícias rodando no servidor local
URL = "http://localhost:8010/index.html"

def raspar_noticias():
    print(f"Acessando {URL}...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        
        # Força a codificação para UTF-8 garantindo a leitura correta de acentos
        response.encoding = 'utf-8'
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Localiza todos os blocos de notícias na página
    artigos = soup.find_all('article', class_='noticia')

    lista_noticias = []

    # Extrai os dados de cada notícia
    for artigo in artigos:
        categoria = artigo.find('span', class_='categoria').get_text(strip=True)
        titulo = artigo.find('h2', class_='titulo-noticia').get_text(strip=True)
        data = artigo.find('span', class_='data').get_text(strip=True)
        autor = artigo.find('span', class_='autor').get_text(strip=True)
        resumo = artigo.find('p', class_='resumo').get_text(strip=True)

        noticia_dict = {
            "categoria": categoria,
            "titulo": titulo,
            "data": data,
            "autor": autor,
            "resumo": resumo
        }
        lista_noticias.append(noticia_dict)

    # Exibição de todas as notícias de forma organizada
    print(f"\n==========================================")
    print(f" TODAS AS NOTÍCIAS ({len(lista_noticias)} encontradas)")
    print(f"==========================================")

    for i, n in enumerate(lista_noticias, 1):
        print(f"Notícia {i}:")
        print(f"  • Categoria: {n['categoria']}")
        print(f"  • Título: {n['titulo']}")
        print(f"  • Data: {n['data']} | Autor: {n['autor']}")
        print(f"  • Resumo: {n['resumo']}")
        print("-" * 50)

    # Filtragem por categoria escolhida (ex: 'Tecnologia')
    categoria_alvo = "Tecnologia"
    print(f"\n==========================================")
    print(f" FILTRAGEM: Notícias da categoria '{categoria_alvo}'")
    print(f"==========================================")

    filtradas = [n for n in lista_noticias if n['categoria'].lower() == categoria_alvo.lower()]

    if filtradas:
        for i, n in enumerate(filtradas, 1):
            print(f"{i}. {n['titulo']}")
            print(f"   (Data: {n['data']} — Por: {n['autor']})")
    else:
        print(f"Nenhuma notícia encontrada na categoria '{categoria_alvo}'.")
    print("==========================================\n")

if __name__ == "__main__":
    raspar_noticias()