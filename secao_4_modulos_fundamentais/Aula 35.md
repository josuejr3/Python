
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