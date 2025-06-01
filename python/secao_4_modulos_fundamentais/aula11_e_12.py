# Aula 11 - utilizando os.listdir para navegar em caminhos

import os

from itertools import count

# Caminho teste
# Josue\Cursos\Python\python\secao_4_modulos_fundamentais

# caminho = r"Josue\\Cursos\\Python\\python\\secao_4_modulos_fundamentais"

# a barra é adicionada, pois estou vindo da raiz
caminho = os.path.join("\\Josue", "Cursos", "Python", "python", "secao_4_modulos_fundamentais")

# for item in os.listdir(caminho):
#     print(item)

# Aula 12

counter = count()
for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print("Pasta atual: ", root, counter)

    for dir_ in dirs:
        print("  ", the_counter, "Dir: ", dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print("  ", the_counter, "File: ", caminho_completo_arquivo)


