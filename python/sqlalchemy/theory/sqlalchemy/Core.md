
DBAPI - É uma PEP do Python que padroniza como os bancos de dados são usados com Python. O SQLAlchemy faz isso.

-  Connection Pooling - Serviço que abre várias conexões com objetivo de ter uma conversação mais rápida;
-  Dialect - Uma forma de reconhecer Postgres, MySQL, MariaDB e entre outros;
-  Engine - Gerencia a conexão do banco;
-  Schema/Types - Como os metadados da tabela são gerenciados - tipos de dados da tabela;
-  SQL Expression Language - forma de montar vários selects usando Python

---

<div align="center"><img src="Core.png"/></div>

Os plugins do SQLAlchemy servem para lidar com outros tipos de bancos de dados diferentes. 

> Pool

Piscina (reservátorio de água), num contexto de BD a pool é um _reservátorio de conexões_. (É como se fosse um cache)

	Como assim? 

	Basicamente a connection pool reaproveita conexões que já foram abertas para evitar ficar abrindo e fechando (MELHORA O DESEMPENHO).

> Engine

-  Fabrica a conexão com o banco de dados e aloca uma pool de conexões
-  Cada coisa ou transação que é feita no BD (requisição), selecionar, alterar e excluir passam pelo procedimento abaixo

	-  Inicia;
	-  Executa
	-  Termina -> Resultado

-  Se a transação deu certo ocorre um *commit* 
-  Se ocorrer um problema temos que fazer um *rollback* que é voltar ao estado anterior

As transações são "8 ou 80", ou dão 100% certo ou ela não dá certo. **Não tem como ter uma transação incompleta**

-  Exemplo

Transação de um valor de um usuário em um banco para outro, se o valor é transferido do user A para o user B, o valor sai de A, mas não chega em B então é feito o *rollback* e o valor é devolvido para A, a transaçã