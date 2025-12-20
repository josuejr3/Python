
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
	-  O view é o que vai decidir o que vai ser feito quando receber a request (função)

##### Exemplo de URLs com Requests e Response

No arquivo de urls.py eu vou ter uma lista com todas as minhas rotas e as minhas <span style="color:rgb(4, 255, 0)">views</span>

```python
from django.contrib import admin  
from django.urls import path  
from django.http import HttpResponse

urlpatterns = [  
    path("admin/", admin.site.urls),  
    path("blog/", my_view),  
]
```

As views são basicamente "o que vai retornar"

```python  
def my_view(request):  
    print("Oie")  
    return HttpResponse("Uma Mensagem")
```

No django não trabalhamos diretamente no projeto, mas sim com apps. Para isso, quando criarmos no nosso app devemos colocar ele na lista de apps instalados no arquivos de settings.

> Exemplo 

*Criando um app para a página inicial e outra para uma página de blog*

<mark style="background: #FF5582A6;">!!! Lembrando que os apps são completamente distintos um do outro !!!!</mark>

Dica: se as coisas estiverem associadas, cria tudo no mesmo app, se forem coisas muito
