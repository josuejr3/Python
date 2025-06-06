# Variáveis de Ambiente
import os

from dotenv import load_dotenv # type: ignore

# Por padrão, o load_dotenv vai buscar na raiz do projeto
load_dotenv()

# printa todas as variaveis de ambiente
#print(os.environ)

# aqui eu vou pegar a variavel que eu quero e ele retorna o valor
print(os.getenv('PASSWORD_BD'))

# criar um arquivo .env-example
