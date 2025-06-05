import locale
from datetime import datetime

# doc: https://docs.python.org/3/library/string.html#template-strings

locale.setlocale(locale.LC_ALL, '')

def convert_para_brl(numero: float) -> str:
    brl = "R$ " + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome="Joao",
    valor=convert_para_brl(1_234_456),
    data=data.strftime("%d/%m/%Y"),
    empresa = 'O. M.',
    telefone="+55 (11) 7890-5432"
)

import json
import string
print(json.dumps(dados, indent=2, ensure_ascii=False))

# Criando um template

texto = """
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de $valor no dia $data. Caso
deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

Atenciosamente,

${empresa},
Abraços
"""
template = string.Template(texto)

print(template.substitute(dados))
print()
print()
print(template.safe_substitute(dados))