import requests
from bs4 import BeautifulSoup

# URL da página rodando no servidor local
URL = "http://localhost:8010/index.html"

def raspar_cursos():
    print(f"Acessando {URL}...")
    try:
        response = requests.get(URL)
        response.raise_for_status() # Lança exceção caso ocorra erro HTTP
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return

    # Analisa o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Localiza todos os elementos de curso na página
    cursos = soup.find_all('div', class_='curso')

    print(f"\n--- Catálogo de Cursos Raspados ({len(cursos)} encontrados) ---\n")

    # Percorre cada curso encontrado
    for i, curso in enumerate(cursos, 1):
        # Extrai nome, área e carga horária utilizando as classes do HTML
        nome = curso.find('h2', class_='nome-curso').get_text(strip=True)
        area = curso.find('span', class_='area-curso').get_text(strip=True)
        carga_horaria = curso.find('span', class_='carga-horaria').get_text(strip=True)

        print(f"Curso {i}: {nome}")
        print(f"  • Área: {area}")
        print(f"  • Carga Horária: {carga_horaria}")
        print(f"  • Principais Assuntos:")

        # Localiza a lista de assuntos (ul -> li) dentro do curso atual
        assuntos = curso.find_all('li', class_='assunto')
        for assunto in assuntos:
            print(f"    - {assunto.get_text(strip=True)}")
        
        print("-" * 50)

if __name__ == "__main__":
    raspar_cursos()