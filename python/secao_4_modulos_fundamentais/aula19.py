from pathlib import Path

caminho_projeto = Path()

# Esse camuinho vai retornar o caminho relativo
# Basicamente ele vai retornar o local atual, nesse caso um ponto

print(caminho_projeto)

# Caso seja necessário ver o caminho absoluto, basta chamar o método

print(caminho_projeto.absolute())

# Obtendo o caminho com o arquivo em si

caminho_projeto = Path(__file__)
print(caminho_projeto)

# Obtendo a pasta anterior, ou "mãe/pai" da pasta analisada
print(caminho_projeto.parent)
# Como path retorna um path, então podemos chamar parent e depois um novo parent
print(caminho_projeto.parent.parent)

# Criando um novo caminho para uma nova pasta e acessando a pasta home
teste = Path().absolute() / "aula19_teste"
print(teste / "ideias" / "file.txt")
print(Path.home())

# Criando de fato um novo arquivo
Path.mkdir(teste)
arquivo = teste / 'arquivoo_teste19.txt'
arquivo.touch()
print(arquivo)

# Apagando o arquivo
# Lembrando que o arquivo excluido nao vai pra lixeira
# nao é possível recuperar
arquivo.unlink()

# Escrevendo arquivo
arquivo = teste / 'arquivoo_teste19.txt'
arquivo.touch()
arquivo.write_text('OPA')

print(arquivo.read_text())










