import requests
from bs4 import BeautifulSoup

url = "https://op.gg"
# codigo de status
response = requests.get(url)

# pagina - texto html
raw_html = response.text

# agora vamos fazer o parsed - analisador do html
parsed_html = BeautifulSoup(raw_html, "html.parser")

# printa o nome da página
print(parsed_html.title.text)

# selecionando alguma coisa (funciona em texto)
champions = parsed_html.select_one("body > div.bg-main-500.border-b.border-b-main-600 > div > nav > div.flex.shrink-0.items-center.gap-6 > a:nth-child(2)")

# selecionando um bloco "pai"

