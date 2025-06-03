# exemplo de um arquivo csv

# Nome, Idade, Endereço
# Luiz Otavio, 32, "Av Brasil, 21, Centro"
# João da Silva, 55, "Rua 22, 44, Nova Era"


# Guia para ler um CSV - Aula 21

# Importação de libs
from pathlib import Path
import csv

# Criação do caminho CSV
CAMINHO_CSV = Path(__file__).parent / "arquivo_aula_21.csv"

# Abertura do arquivo CSV
# with open(CAMINHO_CSV, 'r', encoding="utf-8") as file:
#     # Leitor do arquivo CSV
#     reader = csv.reader(file)
#
#     # Podemos usar next, pois ele retorna cada uma das linhas do arquivo
#     # E o resultado é em formato de lista
#     # print(next(reader))
#
#     # Outra forma
#     for linha in reader:
#         print(linha)
#
#
# # Outra forma de ler, dessa vez em formato de dicionário
# with open(CAMINHO_CSV, 'r', encoding="utf-8") as file:
#     # Leitor do arquivo CSV em formato de dicionário
#     reader = csv.DictReader(file)
#
#     for linha in reader:
#         print(linha)


################### Aula 22 - Escrita em arquivos CSV

clientes = [
            {"Nome": "Luiz Otavio", "Idade": 12, "Endereço":"Av Brasil, 21, Centro"},
            {"Nome": "João da Silva", "Idade": 55, "Endereço":"Rua 22, 44, Nova Era"}
            ]

# with open(CAMINHO_CSV, mode="w", encoding="utf-8") as arquivo:
#     colunas = clientes[0].keys()
#     escritor = csv.writer(arquivo)
#
#     escritor.writerow(colunas)
#
#     for cliente in clientes:
#         escritor.writerow(cliente.values())


with open(CAMINHO_CSV, mode="w", encoding="utf-8") as arquivo:
    colunas = clientes[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)

    # Escreve o topo do arquivo, o nome das colunas
    escritor.writeheader()

    for cliente in clientes:
        escritor.writerow(cliente)
