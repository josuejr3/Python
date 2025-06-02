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
print(caminho_projeto.parent.parent)