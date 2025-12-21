
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

