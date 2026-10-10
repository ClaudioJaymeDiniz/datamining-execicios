# 🕸️ Práticas de Web Scraping com Python e BeautifulSoup

Este repositório contém uma série de exercícios práticos de Web Scraping desenvolvidos com **Python**, utilizando as bibliotecas **`requests`** e **`BeautifulSoup`**, juntamente com páginas HTML estruturadas semanticamente para simular cenários reais de extração de dados.

---

## 📂 Estrutura de Pastas

Os exercícios estão divididos em diretórios independentes:

* `ex1/` — Catálogo de cursos
* `ex2/` — Loja de informática
* `ex3/` — Portal de notícias
* `ex4/` — Biblioteca
* `ex5/` — Cardápio por categorias
* `ex6/` — Agenda de eventos

---

## 🛠️ Pré-requisitos

Certifique-se de ter o **Python 3** instalado em sua máquina. Além disso, você precisará instalar as dependências necessárias para a raspagem:

```bash
pip install requests beautifulsoup4

🚀 Como Executar

Para testar os scripts de raspagem localmente, utilizamos um servidor HTTP embutido do Python servindo as páginas HTML.
1. Iniciar o Servidor Local

Abra o terminal na raiz do projeto (onde estão as pastas ex1, ex2, etc.) e inicie o servidor na porta 8010:
Bash

python -m http.server --bind 127.0.0.1 8010

    Nota: Mantenha este terminal aberto enquanto estiver testando os scripts, pois ele é responsável por hospedar as páginas HTML localmente (http://127.0.0.1:8010/...).

2. Executar um Exercício Específico

Abra um segundo terminal, navegue até a pasta do exercício que deseja testar (por exemplo, ex1) e execute o script de raspagem:
Bash

cd ex1
python raspagem.py

Basta repetir o processo para os demais exercícios (ex2, ex3, ex4, ex5 e ex6), sempre acessando a pasta correspondente e executando python raspagem.py.
📝 Resumo dos Exercícios

    Exercício 1 (Catálogo de Cursos): Extração de dados tabulares e listagem aninhada (<ul>/<li>) de assuntos estudados.

    Exercício 2 (Loja de Informática): Raspagem de produtos e filtragem condicional por situação de estoque (Disponível).

    Exercício 3 (Portal de Notícias): Extração de metadados textuais (autor, data, resumo) e filtragem por categoria específica.

    Exercício 4 (Biblioteca): Coleta de metadados literários e palavras-chave estruturadas, isolando obras disponíveis.

    Exercício 5 (Cardápio por Categorias): Navegação e extração hierárquica por seções do cardápio (Pratos, Bebidas, Sobremesas).

    Exercício 6 (Agenda de Eventos): Tratamento de elementos múltiplos (múltiplos palestrantes) e extração de atributos de links (href).