# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# Github: https://github.com/PyMySQL/PyMySQL

import pymysql


connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados',
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor, # Escolhe o cursor que retorna dicionario
)

TABLE_NAME = "customers"

# connection e cursor sao context manager no pymysql
with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO !!! ISSO LIMPA A TABELA
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")
    connection.commit()

    ##################### CREATE

    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            f'(nome, idade) '
            f'VALUES (%s, %s)', ("Joseph", 23)
        )
    connection.commit()

    with connection.cursor() as cursor:
        # SQL - Adicionando em forma de DICIONARIO
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            f'(nome, idade) '
            f'VALUES (%(name)s, %(age)s) ',
            {
                'name': 'Jacoby',
                'age': 22,
            }
        )
    connection.commit()

    with connection.cursor() as cursor:
        # SQL - Adicionando em forma de DICIONARIO
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            f'(nome, idade) '
            f'VALUES (%(name)s, %(age)s) ',
            {
                'name': 'John',
                'age': 21,
            }
        )
    connection.commit()

    with connection.cursor() as cursor:
        # SQL - Adicionando vários elementos
        cursor.executemany(
            f'INSERT INTO {TABLE_NAME} '
            f'(nome, idade) '
            f'VALUES (%(name)s, %(age)s) ',
            ({
                'name': 'Jax',
                'age': 24,
            }, {'name': 'Justin', 'age': 25})
        )
    connection.commit()

    ##################### READ

    with connection.cursor() as cursor:
        # SQL - Leitura
        coluna = 'id'
        id_recebido = input('Digite um id: ')

        sql = (
            f"SELECT * FROM {TABLE_NAME} "
            f"WHERE {coluna} = %s"
        )
        cursor.execute(sql, (id_recebido))  # type: ignore

        print(cursor.mogrify(sql, (id_recebido,)))

        # Converte o iterator numa tupla
        data = cursor.fetchall()

        # Iterator
        for row in data:
            print(row)

        # for row in data:
        #     print(row)

    # Em SELECTs não há necessidade de commit

    # Utilizando o DELETE - PRECISA DE COMMIT POIS PODE FAZER UM ROLLBACK!!!
    with connection.cursor() as cursor:
        # sql = (
        #     f"DELETE FROM {TABLE_NAME} "
        # )

        sql = (
            f"DELETE FROM {TABLE_NAME} WHERE id = 4 "
        )
        cursor.execute(sql)
        connection.commit()

    # Usando o UPDATE
        # ERRADO!!! TODOS OS NOMES NA TABELA VAO SER LUIZ
        sql = (
            f"UPDATE {TABLE_NAME} SET nome = 'LUIZ' "
        )

        sql2 = (
            f"UPDATE {TABLE_NAME} SET nome = %s WHERE id = %s "
        )

        cursor.execute(sql2, ('Jax', 1))
        # Sem o commit no delete, ele não apaga
        # Sempre que fizer uma mudança na tabela é importante commitar
        # É importante usar o WHERE no DELETE e no UPDATE
        connection.commit()

        cursor.execute(f"SELECT * FROM {TABLE_NAME} ")
        # data_1 = cursor.fetchall()

        # metodo scroll para rolar
        cursor.scroll(-1) # volta uma linha
        # SSCursor é um cursor que nao salva dados na memoria
        # Podemos usar o SSDictCursor - (retorna um generator)

        # Usando o cursor como dicionário
        for row in cursor.fetchall():
            print(row['nome'])
