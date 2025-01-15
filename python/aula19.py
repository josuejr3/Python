# CRIANDO ARQUIVOS COM PYTHON + CONTEXT MANAGER


# caminho = "aula116.txt"
# caminho_arquivo = "D:\\Josue\\Cursos\\python\\python\\aula116.txt"

# caminho_com_acento = "C:\\Users\\geenu\\OneDrive\\Desktop\\nova pasta atenção\\"
# obs: poderia ter inserido um r antes r"C:\\Users\\geenu\\OneDrive\\Desktop\\nova pasta atenção\\"

# caminho_arquivo = caminho_com_acento + caminho
# print(caminho_arquivo)

# Porém o arquivo não existe na pasta

# arquivo = open(caminho_arquivo, "w")
# #
# arquivo.close()


# with open(caminho_arquivo, "w") as arquivo:
#     ...

# lista = ["a", "b", "c"]
# with open("arquivo_teste.txt", "w+") as arquivo1:
#     print(type(arquivo1))
#     arquivo1.write("Linha 1\n")
#     arquivo1.write("Linha 2\n")
#     arquivo1.writelines(
#         # só recebe iteraveis
#         ("Linha 3\n", "Linha 4\n")
#         #lista
#     )
#     # Aqui ele não vai printar nada, pois o cursor de texto está em uma "linha" vazia
#     arquivo1.seek(0, 0)
#     print(arquivo1.read())
#     print("Lendo")
#     arquivo1.seek(0,0)
#     # readline lê linha por linha, o end="" e o strip() removem os espaços
#     print(arquivo1.readline(), end="")
#     print(arquivo1.readline(), end="")
#     print(arquivo1.readline(), end="")
#     print(arquivo1.readline().strip())
#     print(arquivo1.readline().strip())
#     print("READLINES")
#     arquivo1.seek(0,0)
#     for linha in arquivo1.readlines():
#         print(linha.strip())

# with open("arquivo_teste.txt", "r") as arquivo1:
#     print(arquivo1.read())

# obs: o modo w apaga tudo que estiver no arquivo e



# ENCODING

import os

# with open("encoding.txt", "w", encoding="utf-8") as arquivo2:
#     arquivo2.write("Atenção\n")
#
# with open("aa.txt", "w", encoding="utf8") as arq:
#     ...

# excluindo com unlink
# os.unlink("aa.txt")

# excluindo com remove
# os.remove("oie.txt")

# renomeando com rename
# os.rename("oie.txt", "aa.txt")

# Para entender um pouco mais sobre encoding
# https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

# =========================================================================================================

# JSON

import json

# pessoa = {
#     "nome": "Luiz Otavio",
#     "sobrenome": "Miranda",
#     "endereços": [
#         {"rua": "R1", "numero": 32},
#         {"rua": "R2", "numero": 33},
#     ],
#     "altura": 1.8,
#     "numeros_preferidos": (2, 4, 6, 8, 10),
#     "dev": True,
#     "nada": None,
# }
#
# with open("aula117.json", "w", encoding="utf8") as file:
#     json.dump(pessoa, file, ensure_ascii=False, indent=2)


# importando a pessoa de um arquivo json

# with open("aula117.json", "r", encoding="utf8") as file:
#     pessoa = json.load(file)
#     print(pessoa["nome"])
#     print(type(pessoa))



# Problema dos parâmetros mutáveis em funções Python

# def add_customer(name, lista=None):
#     if lista is None:
#         lista = []
#     lista.append(name)
#     return lista
#
#
# cliente1 = add_customer("Luiz")
# add_customer("Joana", cliente1)
# print(cliente1)
#
#


# POSITIONAL ONLY PARAMETERS E KEYWORD ONLY PARAMETERS

# def soma(a, b, /, x, y):
#     print(a + b + x + y)
#
# soma(1, 2)
#


def soma(a, b, /, *, c, d, **kwargs):
	print(kwargs)
	print(a + b + c + d)

soma(1, 2, c=3, d=4, nome="teste", sobrenome="2")




















































