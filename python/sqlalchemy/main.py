from sqlalchemy import create_engine

# Cria um banco de dados SQLite em memória

engine = create_engine( # Factory - Fábrica de conexões/motores
    "sqlite://", # uri
    echo=True,   # mostra a comunicação com o banco de dados
)

print(engine)
print(engine.dialect)

con = engine.connect()                  # conexão com banco de dados
print(engine.pool.status())

print(con.connection.dbapi_connection)  # vê o conector

# - A: atomico / atomicidade


con.close()