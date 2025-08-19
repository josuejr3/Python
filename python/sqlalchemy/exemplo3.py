# Fazendo uma busca no banco de dados

from sqlalchemy import create_engine, text

engine = create_engine("sqlite://", echo=True)

with engine.connect() as con:
    # Garante que vai ser executada de forma atomica
    with con.begin():
        sql = text('SELECT id, name, comment FROM comments')
        con.execute(sql)
    # Outra transação atomica
    with con.begin():
        sql = text('SELECT id, name, comment FROM comments')
        con.execute(sql)

    # Outro exemplo garantindo a atomicidade e fazendo o rollback
    with con.begin():
        ### Operações que precisam acontecer juntas SEM DESCARTAR a conexão e ter que pegar outra
        sql = text("Pega 10 conto do almir")
        result = con.execute(sql)

        ### result - Result
        sql = text('coloca os 10 conto na minha conta')
        result = con.execute(sql)

# connection = engine.connect()
#
# sql = text('SELECT id, name, comment FROM comments')
# result = connection.execute(sql)
#
# connection.close()