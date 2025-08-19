# Criação de metadados
from traceback import print_tb

import sqlalchemy as sa
from sqlalchemy import insert, update

# Construtor dos metadados da tabela
metadata = sa.MetaData()

engine = sa.create_engine('sqlite:///database.db')
# Inspeciona o banco de dados
inspect = sa.inspect(engine)
# Retorna o nome das tabela
print(inspect.get_table_names())
print(inspect.get_columns("comments"))

## Reflection
t = sa.Table("comments", metadata, autoload_with=engine)
print(t)

# Construindo a tabela e passando os metadados dela
# t = sa.Table(
#     "comments", metadata,
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("name", sa.String(), nullable=False),
#     sa.Column("comment", sa.String(), nullable=False),
#     sa.Column("live", sa.String(), nullable=False),
#     sa.Column("created_at", sa.DateTime(), nullable=True),
#     sa.PrimaryKeyConstraint("id")
# )
#
# engine = sa.create_engine("sqlite:///database.db")
# # Metadata cria para mim esse banco de dados
# # Ou melhor, a partir da engine que eu construi crie uma tabela com os metadados
# # que eu possuo
# metadata.create_all(engine)


############################################################################

## Retorna um select
sql = (sa.select(t.c.id, t.c.comment, t.c.name)
       .where(t.c.name == "dunossauro")
       .limit(10)
       .offset(10)
       .order_by(sa.desc(t.c.id))
       #.join(t)
)

sql2 = (
    insert(t).values(name="Jacoby", comment="What?", live="Twitch")
)

## >>> SELECT comments.id, comments.name, comments.comment, comments.live, comments.created_at FROM comments
print(sql)

with engine.connect() as con:
    result = con.execute(sql2)
    print(result)


