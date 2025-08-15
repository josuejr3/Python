import sqlite3

from a7_1 import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Consulta - seleciona todos os elementos da tabela
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name="QUALQUER" '
    'WHERE id = 2'
)


# cursor.execute(
#     f'DELETE FROM {TABLE_NAME} '
#     'WHERE id = "3"'
# )



# for row in cursor.fetchall():
#     # print(row)
#     _id, name, weight = row
#     print(_id, name, weight)

cursor.close()
connection.close()