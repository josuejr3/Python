
Podemos criar arquivos estáticos para cada um dos apps que possuímos. Para isso, vamos criar uma pasta chamada *"static"* em algum dos apps.

```django
{% load static %}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
  </head>  <body>
```

Basicamene toda vez que for usar coisas estáticas em um arquivo deve-se usar o comando de load static

```django
{% load static %}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Title</title>  
    <link rel="stylesheet" href="{% static 'blue.css' %}">
  </head>  <body>
```

Para evitar ter conflitos de nomes devemos fazer o que fizemos anteriormente, dentro da pasta static criar uma nova pasta com o nome da pasta mãe e dentro dela colocar uma pasta para css, js, imagens e entre outros.
##### STATIC_URLS

##### STATIC_FILES_DIRS

#### Usando o context para enviar dados para dentro de templates do Django

O context é um argumento do render que serve para escrever na página conseguimos pegar esse valor armazenado e jogar no html. O tipo é um dicionário com várias variáveis que podem ser usadas.

```python
def home(request):  
    return render(  
        request,  
        'home.html',  
        {  
            'text': 'Estamos na home'  
        }  
    )
```

-  Não é possível blocks com includes

---
##### Fazendo laço for no django

```python
from . import data

def blog(request):
	print("blog")
	
	context = {
		"text": "Olá blog",
		"posts": data.posts
	}
	
	return render (
		request,
		"blog/index.html",
		context
	)
```

O for vai dentro do arquivo HTML

```html
{% block posts %}
	{% for post in posts %}
		{% include "global/partials/postblock.html" %}
	{% endfor %}
{% endblock posts %}
```

##### If e elses com django

```html
{% if %}
	...
{% endif %}
```

```html
{% if %}

{% elif $}

{% elif $}

{% elif $}

{% elif $}

{% else %}

{% endif %}
```

#### URLs dinâmicas

Para deixar uma URL dinâmica temos que alterar um dos códigos presentes noa rquivo urls.py em urlpatterns. 

```python
urlpatterns = [
	path("", views.blog, name="home"),
	path("post/<id>", views.blog, name="post"), ## <<<<<<<< USO DO <id>
	path("exemplo/", views.exemplo, name="exemplo"),
]
```

Entretanto, para que isso funcione corretamente, a view deve receber o argumento, que nesse caso vai ser o id.

```python
def post(request, id):
	context = {"posts": posts}
	return render(request, "blog/index.html", context)


urlpatterns = [
	path("", views.blog, name="home"),
	path("post/<id>", views.post, name="post"), ## <<<<<<<< USO DO <id>
	path("exemplo/", views.exemplo, name="exemplo"),
]
```

É importante informar o tipo

```python
urlpatterns = [
	path("", views.blog, name="home"),
	path("post/<int:id>", views.blog, name="post"), ## <<<<<<<< USO DO <id>
	path("exemplo/", views.exemplo, name="exemplo"),
]
```