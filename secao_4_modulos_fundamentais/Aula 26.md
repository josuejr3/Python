
#### <span style="color:rgb(4, 255, 0)">string.Template</span>

A classe Template dentro do módulo string serve para substituir variáveis em textos. Os métodos mais usados são:

-  substitute: substitui, mas gera erros se faltar chaves
-  safe_substitute: substitui sem gerar erros

Além disso, é possível criar delimitadores e outras coisas criando uma subclasse a partir da classe Template.

Utilizaremos o locale nessa aula, pois ele é importante caso queiramos converter números e outras coisas que possam ser necessárias, outro exemplo é o "currency" que é basicamente a moeda de um local.


