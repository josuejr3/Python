
O ORM é o mapeamento de objetos (classes) Python com os dados do nosso banco de dados.

<mark style="background: #ABF7F7A6;">Obs</mark>

	O SQLAlchemy NÃO é um ORM ele TEM um ORM.

-  Object - um objeto python, como uma classe que construímos;
-  Relational - relacional é em relação aos bancos relacionais;
-  Mapper - quer dizer que é feito um mapeamento entre os metadados das tabelas em uma classe e cada row é relacionada a uma instância.

<div align="center"><img src="ORM.png"/></div>

##### Session

 A session entra como uma ferramenta que faz a junção do registry ou da classe base junto com a engine, possibilitando assim usarmos as ferramentas de SQL.

Além disso, a session cria um cache dos objetos em memória.

A session faz o papel da "connection" do core, mas retorna objetos do ORM na query
















