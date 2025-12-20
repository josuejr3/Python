
Trabalhamos ants usando HttpReponse e passando valores. Esses valores renderizam HTML.

-  Para isso usamos o render

```python
from django.shortcuts import render
```

Basicamente isso serve para renderizarmos HTML e CSS.

Essa função vai receber obrigatoriamente uma request e um template. Os templates podem ser criados em um arquivo a parte em cada pasta de app.

```PYTHON
def my_view(request):  
    print("Oie")  
    return render(  
        request,  
        'blog.html',  
    )
```

O 'blog.html' é um arquivo html que fica dentro da pasta templates de cada um dos apps.

Após feito isso, para que funcione adequadamente é necessário informar nas configurações do django, em apps instalados.

```python
INSTALLED_APPS = [  
    "django.contrib.admin",  
    "django.contrib.auth",  
    "django.contrib.contenttypes",  
    "django.contrib.sessions",  
    "django.contrib.messages",  
    "django.contrib.staticfiles",  
  
    "blog",  
]
```

Só que te um problema aqui...

Se tivermos dois templates html com o mesmo nome o django pode pegar qualquer um dos dois. Para resolver isso criamos namespaces para cada um dos apps que criamos. A estrutura de pastas fica estranha, mas funciona.

> Exemplo

```txt
blog/templates/blog/index_blog.html
```

```python
def my_view(request):  
    
    return render(  
        request,  
        'home/index.html',  
    )
```

Obs: nas configs do django em templates vai ter um campo especial chamado "dirs" e nele podemos colocar diretórios em que queremos procurar templates.

Conseguimos criar um "super template" e com ele "herdar" o restante

```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>TESTANDO A BASE</title>  
</head>  
<body>  
<H1>{% block texto %} BASE {% endblock texto %}</H1>  
</body>  
</html>
```

Observe o campo, em H1 ele é genérico

```django
{% extends 'global/index.html' %}  
{% block texto %} TESTANDO HOME {% endblock texto %}
```

Modificando o bloco.

Essa sintaxe "{ % block % }" significa que você está executando algum comando. Há outra sintaxe que é { { X } } para printar o valor que está dentro, no caso, o X.

##### <span style="color:rgb(4, 255, 0)">Partials</span> 

Partials são partes do meu html que eu posso selecionar e separar, por exemplo eu posso ter uma parte que contém somente o cabeçalho.

