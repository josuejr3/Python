
#### <span style="color:rgb(4, 255, 0)">Protocolo HTTP (HyperText Transfer Protocol)</span>

HTTP (HyperText Transfer Protocol) é um protocolo usado para enviar e receber dados na Internet. Ele funciona n modo cliente/servidor. Nesse protocolo, o cliente faz uma requisição ao servidor que responde com os dados adequados.

Esse protocolo é bastante usado para fazer raspagem de dados, isto é, web scrapping ou seja, obter dados de sites.

-  Cliente: podemos considerar como sendo o navegador.
-  Servidor: podemos considerar como sendo o site

A mensagem de requisição do cliente deve incluir dados como por exemplo:

- O método HTTP
	-  Leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (metodos suportados)
	-  Escrita - POST, PUT (substitui), PATCH (atualiza), DELETE (possuem corpo de texto).
- O endereço de recurso a ser acessado (/ user /)
- Os cabeçalhos HTTP (Content-Type Authorization)
- O corpo da mensagem (caso necessário, de acordo com o método )

A mensagem de resposta do servidor deve incluir dados como:

-  O código de status HTTP (200 success, 404 not found, 301 moved permanently)
-  Os cabeçalhos HTTP (content-type, accept)
-  O corpo da mensagem (pode estar em vazio em alguns casos).

Executando o módulo http.server

```cmd
python -m http.server -d aula190_site/
```

Devemos selecionar uma porta, por padrão a porta é a 8000, porém, pode ter algo já rodando nessa porta. 

```cmd
python -m http.server -d aula190_site/ 3333
```

<mark style="background: #BBFABBA6;">Portas</mark> comuns:

- 8000
- 3333
- 8080
- 3000
- 3001
- 3002

![[Pasted image 20250607145111.png]]

```Python
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
```






































