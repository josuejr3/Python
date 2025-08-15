import sqlite3
from pathlib import Path

ROOT_DIR_FILR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR_FILR / DB_NAME

TABLE_NAME = 'customers'

# Abrindo conexão com banco de dados pelo local do arquivo
connection = sqlite3.connect(DB_FILE)
# Definindo o cursor que vai ser responsável por manipular o db
cursor = connection.cursor()

# Limpar a tabela - DELETE SEM O WHERE - CUIDADO!!!!
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()


# Reseta os ids
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Codigos SQL

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name TEXT,'
    'weight REAL'
    ')'
)

# Atualiza o bd
connection.commit()

# Registra valores nas colunas da tabela

# cursor.executemany(
#     f'INSERT INTO {TABLE_NAME} (name, weight)'
#     f' VALUES (?, ?)',
#     [['Luck', 17], ['Dax', 34]]
# )

# Usando dicionários

# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (name, weight) '
#     f'VALUES (:nome, :peso)', {"nome": "John", "peso": 100}
# )

# Dicionarios com com lista

cursor.executemany(
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    f'VALUES (:nome, :peso)',
    (
    {'nome': 'nome1', 'peso': 100},
    {'nome': 'nome2', 'peso': 200},
    {'nome': 'nome3', 'peso': 300},
    {'nome': 'nome4', 'peso': 400},)
)


connection.commit()

# Fechando o cursor
cursor.close()
# Fechando a conexão
connection.close()