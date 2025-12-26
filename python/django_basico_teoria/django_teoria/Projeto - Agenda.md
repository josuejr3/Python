
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

-  Basicamente as migrations servem para fazer ou desfazer alguma coisa do banco de dados.

13.  Fazemos a primeira migration usando

```python
python manage.py migrate
```

Agora podemos acessar o "/admin" e logar como super user, porém, precisamos criar esse super user

-  O super usuário vai ter acesso quase que completo dentro da base de dados do django (incluindo acesso à area administrativa)

-  Existem validadores de senha que ficam no settings.py e estão em "*AUTH_PASSOWORD_VALIDATORS*"

```python
python manage.py createsuperuser
```

-  Se a senha for esquecida você pode alterar  senha executando

```python
python manage.py changepassword josuejunior
```

-  No settings.py vamos ter as configurações do banco de dados em *"DATABASES"*

		https://docs.djangoproject.com/pt-br/4.2/topics/db/models/

		https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-choices

---
##### Criando primeiro Model

Criamos o primeiro model conforme o código abaixo.

```python
from django.db import models  
from django.utils import timezone  
  
# Create your models here.  
  
# Model de Contato  
  
class Contact(models.Model):  
  
    # Dados do Contato, o blank deixa como opcional  
  
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50, blank=True)  
    phone_number = models.CharField(max_length=15)  
    email = models.EmailField(max_length=254, blank=True)  
  
    created_date = models.DateTimeField(default=timezone.now)  
    description = models.TextField(blank=True)
```

Em seguida, executamos o comando

```python
python manage.py makemigrations
```

Para aplicar essa modificações na base de dados, usamos o comando

```python
python manage.py migrate
```

-  Agora precisamos registrar o model criado no arquivo "admin.py" da pasta contacts

```python
from django.contrib import admin  
  
from contact.models import Contact  
  
# Register your models here.  
  
# Essa classe vai funcionar como uma configuração do model na Admin do Django  
@admin.register(Contact)  
class ContactAdmin(admin.ModelAdmin):  
    ...
```

E na classe do model adicionamos o método mágico de string

```python
def __str__(self) -> str:  
    return f"{self.first_name} {self.last_name}"
```

> Podemos usar o shell interativo do Django para fazer consultas de Models 

	Obs: o blank só valida no formulário, no shell não

> O que é um collectstatic?



---
##### Local Settings

Quando for para um servidor, os parâmetros e configurações vão ter que ser alteradas. Para rodar em qualquer lugar, como num servidor, é importante ter um arquivo com as configurações locais que chamamos de "*localsettings*".

##### Simulando Arquivos

Como vão ser necessárias muitas views, vamos simular o arquivo views.py a partir de um pacote python.

##### Injetando todos os contatos dentro do contexto do template index

1.  Aplicamos o CSS no template para que pudessemos ver na página
2.  No HTML base e dentro do body criamos o bloco *"content"* que é basicamente onde vai ficar o "miolo" do site
3.  Dentro desse bloco criamos um "*main*"

##### Querys

-  Para fazer querys basta usar o método filter ao invés do all que tinhamos usado anteriormente.

```python
def index(request):  
  
    # normalmente não usamos o all  
    contacts = Contact.objects.all().order_by('-id').filter(show=True)[0:10]  
    # filter faz o filtro do que vai ser selecionado  
    # Vendo a consulta que está sendo feita no terminal    
    # print(contacts.query)  
    context = {  
        'contacts': contacts,  
    }  
    return render(  
        request,  
        'contact/index.html',  
        context  
    )
```

##### Busca com contains

```python
def search(request):  
  
    search_value = request.GET.get('query', '').strip()  
  
    # Se for uma consulta inválida ele volta pra index  
    if search_value == '':  
        return redirect('contact:index')  
  
    contacts = Contact.objects.filter(show=True).filter(first_name__icontains=search_value).order_by('-id')[10:20]  
  
    context = {  
        'contacts': contacts,  
        'site_tile': "Search - "  
    }  
  
    return render(  
        request,  
        'contact/index.html',  
        context  
    )
```

Nesse caso a sintaxe é usada dentro da função filter com o nome do campo que eu quero procurar, seguido de dois underlines e com icontains por exemplo, porém pode ser outra forma de busca e igualar ao valor que se deseja, que nesse caso é o search value

Se colocarmos mais argumentos na função filter basicamente o django faz um and de tudo, para usarmos o or precisamos de uma função especial

```python
from django.db.models import Q
```

A consulta fica assim

```python
contacts = Contact.objects.filter(show=True).filter(  
    Q(first_name__icontains=search_value) |  
    Q(last_name__icontains=search_value)  
).order_by('-id')
```

Ambos os filtros envolvidos pela função Q e separados por um | que substitui a vírgula

