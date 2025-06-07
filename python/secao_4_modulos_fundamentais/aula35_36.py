# requests para requisições HTTP
from idlelib.rpc import response_queue

import requests


url = "http://localhost:3333"

# se a porta for 80 (http) ou 443 (https) não precisa informar na url

# o código agora é o cliente
# o servidor continua sendo o site

# Resposta do servidor - metodo de leitura get e a url é passada
response = requests.get(url)
# Mostra o status code
print(response.status_code)
# Mostra os cabeçalhos
print(response.headers)
# Mostra o conteúdo em bytes
# print(response.content)
# Mostra o conteúdo em formato de texto
print()
print(response.text)

# Além disso, podemos tentar converter o conteúdo da pasta para json
# print(response.json())

# Tutotial / Aula requests: https://www.youtube.com/watch?v=Qd8JT0bnJGs