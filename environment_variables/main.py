from os import environ, getenv

# getenv identifica se a variavel de ambiente existe
# se sim, ela retorna true

print(getenv('SPLASH'))
print(getenv('XPTO'), 'fritas')
getenv()

environ['SPLASH'] = 'AAAAAA'
print(getenv('SPLASH'))
