
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
