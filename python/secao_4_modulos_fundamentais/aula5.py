# Formatação de data com o datetime
from datetime import datetime

# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

fmt = "%d/%m/%Y"
data = datetime(2022, 12, 13, 7, 59, 23)

# primeiro - criar uma data
nova_data = datetime.strptime('2022-12-13 07:59:23', "%Y-%m-%d %H:%M:%S")

# passando para o formato padrão usando strftime()
print(data.strftime(fmt))


print(data.strftime("%Y"), nova_data.year)
print(data.strftime("%m"), nova_data.month)