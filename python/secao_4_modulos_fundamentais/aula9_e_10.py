import os

#os.system('echo "hello world"')
#os.system("cls")

# aula 10

caminho = os.path.join("Desktop", "curso", "arquivo.txt")
print(caminho)
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao = os.path.splitext(caminho)
print(caminho_arquivo)
print(extensao)

# Verifica se existe o diretorio
print(os.path.exists(caminho))

# caminho absoluto
print(os.path.abspath(caminho))

# printa o diretorio
print(os.path.dirname(caminho))

# https://docs.python.org/3/library/os.path.html#module-os.path