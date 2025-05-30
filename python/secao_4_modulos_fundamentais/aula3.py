# Obtendo a data e o horário atual

from datetime import datetime
from pytz import timezone

print(datetime.now(timezone("America/Fortaleza")))
print(datetime.now(timezone("Asia/Tokyo")))

# Segundos de 1/1/1970 até hoje
print(datetime.now().timestamp())


# Criando data a partir do timestamp
print(datetime.fromtimestamp(1748616998.970635))