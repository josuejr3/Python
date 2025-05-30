from datetime import datetime, timedelta

fmt = "%d/%m/%Y %H:%M:%S"
data_inicio = datetime.strptime("20/04/1900 00:00:00", fmt)
data_fim = datetime.strptime("30/05/2025 18:46:00", fmt)

print(data_fim - data_inicio)

# obtendo mais dados a partir do timedelta
delta = data_fim - data_inicio
print(delta.days, delta.seconds, delta.total_seconds(), delta.microseconds)

timed = timedelta(days=10)
print(data_fim + timed)

# usando relativdelta

from dateutil.relativedelta import relativedelta
print(data_fim + relativedelta(seconds=59))