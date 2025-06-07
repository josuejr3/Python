import requests
from bs4 import BeautifulSoup

url = "https://op.gg"
# codigo de status
response = requests.get(url)

# pagina - texto html
raw_html = response.text

# agora vamos fazer o parsed - analisador do html
parsed_html = BeautifulSoup(raw_html, "html.parser", from_encoding="utf-8")

# printa o nome da página
print(parsed_html.title.text)

# selecionando alguma coisa (funciona em texto)
#champions = parsed_html.select_one("body > div.bg-main-500.border-b.border-b-main-600 > div > nav > div.flex.shrink-0.items-center.gap-6 > a:nth-child(2)")

# selecionando um bloco "pai"
# if parsed_html.select_one("link do seletor") is not None:
#     article = parsed_html.select_one("link do seletor").parent
#     if article is not None:
#         # o for seleciona todas as tags P
#         for p in article.select('p'):
#             print(p.text)


#### codigo aula

# import re
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'http://127.0.0.1:3333/'
# response = requests.get(url)
# bytes_html = response.content
# parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
#
# top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
#
# if top_jobs_heading is not None:
#     article = top_jobs_heading.parent
#
#     if article is not None:
#         for p in article.select('p'):
#             print(re.sub(r'\s{1,}', ' ', p.text).strip())