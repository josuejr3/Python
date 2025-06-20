
#### <span style="color:rgb(4, 255, 0)">Diagramas - Entidade - Relacionamento (DER)</span>

![[Pasted image 20250620154927.png]]

Esse diagrama basicamente é uma abstração da parte do sistemas que nós vamos criar.

-  Entendidades - são os retângulos;
-  Linhas que interligam - são os relacionamentos.

Cada uma das entidades (ou retângulos) vai representar uma tabela na nossa base de dados, e como consequência, uma entidade. Cada uma das tabelas possui atributos, cada atributo nós dizemos que são colunas da nossa tabela.

Além disso, temos uma chave primaria que é um PK. Essa chave primaria serve basicamente para que possamos identificar um objeto específico na tabela

-  O valor da chave sempre vai ser único na tabela 
-  Não pode ser nulo;
-  Não posso ter outra PK na mesma tabela;
-  Não pode ser alterada.
-  PK podem ser compostas como ocorre em *"users_roles"*

Em resumo, o PK funciona como um contador, ou um ID.

Além da PK, exitem também as FK que são Foreign Keys, ou chaves estrangeiras e essa FK vai referenciar uma outra coluna em outra tabela, (normalmente é a PK da outra tabela).