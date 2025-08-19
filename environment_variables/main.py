from os import environ, getenv

# getenv identifica se a variavel de ambiente existe
# se sim, ela retorna true

print(getenv('SPLASH'))
print(getenv('XPTO'), 'fritas')

environ['SPLASH'] = 'AAAAAA'
print(getenv('SPLASH'))

from dotenv import load_dotenv
load_dotenv(".env")

print(getenv('POKE_API'))