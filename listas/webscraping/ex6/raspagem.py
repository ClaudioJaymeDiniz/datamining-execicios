import requests
from bs4 import BeautifulSoup

# URL da agenda rodando no servidor local
URL = "http://localhost:8010/index.html"

def raspar_agenda():
    print(f"Acessando {URL}...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        
        # Garante suporte adequado a acentos em UTF-8
        response.encoding = 'utf-8'
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Localiza todos os blocos de eventos
    eventos = soup.find_all('article', class_='evento')

    lista_eventos = []

    # Extrai os dados de cada evento
    for ev in eventos:
        nome = ev.find('h2', class_='nome-evento').get_text(strip=True)
        data = ev.find('span', class_='data').get_text(strip=True)
        horario = ev.find('span', class_='horario').get_text(strip=True)
        local = ev.find('span', class_='local').get_text(strip=True)
        
        # Extrai múltiplos palestrantes
        elementos_palestrantes = ev.find_all('li', class_='palestrante')
        palestrantes = [p.get_text(strip=True) for p in elementos_palestrantes]

        # Extrai o link e o texto do botão de inscrição
        link_tag = ev.find('a', class_='link-inscricao')
        link_texto = link_tag.get_text(strip=True) if link_tag else "Sem link"
        link_href = link_tag['href'] if link_tag and link_tag.has_attr('href') else "#"

        evento_dict = {
            "nome": nome,
            "data": data,
            "horario": horario,
            "local": local,
            "palestrantes": palestrantes,
            "link_texto": link_texto,
            "link_href": link_href
        }
        lista_eventos.append(evento_dict)

    # Exibição organizada de todos os eventos
    print(f"\n==========================================")
    print(f" AGENDA COMPLETA DE EVENTOS ({len(lista_eventos)} encontrados)")
    print(f"==========================================")

    for i, e in enumerate(lista_eventos, 1):
        print(f"Evento {i}: {e['nome']}")
        print(f"  • Data/Hora: {e['data']} às {e['horario']}")
        print(f"  • Local: {e['local']}")
        
        # Identifica e exibe a informação de múltiplos palestrantes
        if len(e['palestrantes']) > 1:
            print(f"  • Palestrantes ({len(e['palestrantes'])} convidados): 👥 [Múltiplos Palestrantes]")
            for p in e['palestrantes']:
                print(f"    - {p}")
        else:
            print(f"  • Palestrante: {e['palestrantes'][0] if e['palestrantes'] else 'A definir'}")

        print(f"  • Inscrição: [{e['link_texto']}] -> Link: {e['link_href']}")
        print("-" * 50)

    print("\nFim da raspagem da agenda com sucesso!\n")

if __name__ == "__main__":
    raspar_agenda()