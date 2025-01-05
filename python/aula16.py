# import, from, as e *

# Importando módulo inteiro

# import sys
# print(sys.platform)

# Importando partes

# from sys import exit, platform
# # se já existir uma variável chamada platform ou exit ela é sobrescrita
# # platform = "A MINHA"
# print(platform)

# Importando e alterando o nome do módulo

# import sys as s
# sys = "alguma coisa"
# print(s.platform)

# Importando e alternando o nome de elementos específicos do módulo
# from sys import platform as pf, exit as ex
# print(pf)
# ex()

# Má prática - Importa tudo 
# from sys import *



# MEUS MÓDULOS PYTHON E SYS.PATH

# O primeiro módulo que o python executa é o main que é obtido pelo nome
#print("Este modulo se chama", __name__)

# caso eu queria importar algum arquivo da mesma pasta que o main está o python reconhece

# try:
#     import sys
#     sys.path.append("/home")
# except ModuleNotFoundError:
#     ...
#
#
# import teste_modulo
# print("Este modulo se chama ", __name__)
# print(*sys.path, sep="\n")                        # usamos * pois sys.path é uma lista

# O python conhece a pasta onde o __main__ esta e as pastas abaixo dele

# from teste_modulo import variavel_modulo, soma
# print(teste_modulo.variavel_modulo)
# print(variavel_modulo)

# print(teste_modulo.soma(1, 1))
# print(soma(1, 1))

# Em resumo, o sys.path retorna uma lista de diretorios
# Eu posso adicionar um diretorio personalizado que contenha algum modulo (append)
# E a partir disso eu posso usar o módulo


# RECARREGANDO MÓDULOS
# import importlib
# import teste_modulo
#
# print(teste_modulo.variavel_modulo)
#
# for i in range(10):
# #    não adianta - o python só carrega uma única ve\
# #    import teste_modulo
# #    para recarregar um módulo, usar importlib e importlib.reload
#     importlib.reload(teste_modulo)
#     print(i)
# print("fim")



# # INTRODUÇÃO AOS PACKAGES EM PYTHON
# print(__name__)                         # se o name for main ele é o primeiro
#                                         # módulo de entrada
#
# from sys import path
# import teste_modulo
# print(*path, sep="\n")  # desempacotando a lista
#
# # O import package não faz nada
# # from teste_modulo_package.modulo import soma_do_modulo
#
#
# from teste_modulo_package.modulo import *
# print(variavel)
# # funcao nao disponivel
# # print(printa_msg)
#
# # importando de um módulo que importa de outro módulo
# # inicialmente nao vai funcionar
# fala_oi()


# TODAS AS IMPORTAÇÕES DEVEM ESTAR RELACIONADAS COM O ARQUIVO MAIN




# __init__ é um arquivo de inicialização de pacotes em Python

#
#
# import teste_modulo_package
#
# print(teste_modulo_package.dobra(2))
#

import teste_modulo_package

print(teste_modulo_package.soma_numeros(3, 5))

