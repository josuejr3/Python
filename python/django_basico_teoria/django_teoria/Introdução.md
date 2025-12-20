
Inicialmente vamos criar um projeto django com o seguinte comando

```cmd
django-admin startproject <nome_do_projeto>
```

Se usarmos um "project ." no lugar do nome ele joga na raiz.

Agora podemos subir o servidor com  o comando a seguir

```cmd
python manage.py runserver
```
#### Ok, mas o que é Django?

Django é um framework web python de código aberto.

---

O comando django-admin é basicamente onde os comandos do django são executados. No caso que usamos ele cria o projeto.

-  No arquivo manage.py vai ter uma função principal que recebe uma variável de ambiente chamada *DJANGO_SETTING_MODULE* que é basicamente onde está o arquivo de configuração do django.

-  Podemos no arquivo *"urls.py"* definir novas urls para o site. (NUNCA COMEÇAM COM /)

-  O Django trabalha com MVT (Model View Template)
	-  O model trabalha com base de dados
	-  O view é o que vai decidir o que vai ser feito quando receber a request