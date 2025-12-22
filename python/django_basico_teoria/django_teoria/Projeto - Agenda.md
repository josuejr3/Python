
1.  Foi criado o projeto da agenda
2.  Criado e ativado o ambiente virtual
3.  Criação do app contact
4.  Foram feitas as pastas static para arquivos estáticos e templates (essa já existia)
5.  Dentro dessas pastas criadas, foi criada a global para os arquvios globais do projeto e inseridos na de templates o arquivo base html e na de static uma pasta css responsável por conter os arquivos css gerais.
6.  Foi criada depois dentro do app contact a pasta templates e depois para fazer o namespace uma pasta chamada contact em que colocamos o html base desse app

---

7.  No arquivo de settings.py em *"INSTALLED_APPS"*  inserir os apps que criamos, nesse caso o de contacts

```python
INSTALLED_APPS = [  
    "django.contrib.admin",  
    "django.contrib.auth",  
    "django.contrib.contenttypes",  
    "django.contrib.sessions",  
    "django.contrib.messages",  
    "django.contrib.staticfiles",  
  
    "contact.apps.ContactConfig",  # <<<<<<<<<<<<<<<<< AQUI 
]
```

8.  Em *"TEMPLATES"* colocar em "*DIRS*" o diretório referente aos templates gerais.
9.  E embaixo colocar uma variável indicando a pasta com arquivos estáticos

```python
STATICFILES_DIRS = (  
    BASE_DIR / "static",  
)
```

10.  Foi criada uma view para o app contact chamada index que funciona como se fosse a resposta a uma determinada request

```python
def index(request):  
  
    return render(  
        request,  
        'contact/index.html',  
    )
```

11.  Em seguida, adicionamos isso nas urls do app contact que diz basicamente o seguinte, "quando você acessar a página raiz você receberá o retorno da view index".

```python
urlpatterns = [  
    # Na página raiz do site ele vai chamar a view index "resposta"  
    path("", views.index, name="index"),  
]
```

12.  Agora adicionamos também ao urls principal usando o include

```python
from django.contrib import admin  
from django.urls import path, include  
  
urlpatterns = [  
    path("", include('contact.urls')),  
    path("admin/", admin.site.urls),  
]
```

> Como é o fluxo?

-  Primeiro o Django abre o urls.py principal
-  Ele vai encontrar

```python
path("", include("contact.urls"))
```

-  Vê que o prefixo bate ("")
-  Entra em contact/urls.py
-  Encontra

```python
path("", views.index)
```

-  Chama views.index

---
#### Criando e editando a senha de um super usuário Django

O Django trabalha com migrations e basicamente toda vez que uma alteração é feita nas models significa que você está trabalhando na base de dados.