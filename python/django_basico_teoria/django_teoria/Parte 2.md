
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


