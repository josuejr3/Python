# Uso de calendários e datas
# https://docs.python.org/3/library/calendar.html

# O calendar possibilita as seguintes coisas:
# - qual o último dia do mês (e: monthrange)
# - qual o nome e número do dia de uma determinada data (ex: weekday)
# - criar um calendario em si (ex: mothcalendar)
# - trabalhar com coisas especificas de calendarios (ex: calendar, moth)
# Por padrão dia da semana começa em 0 e vai até 6

import calendar

print(calendar.calendar(2022))
print(calendar.month(2025, 2))

print(calendar.monthrange(2025, 6))
print(calendar.day_name[calendar.weekday(1500, 4, 22)])
# print(calendar.THURSDAY)

# o primeiro item da tupla informa se o primeiro dia foi em um seg, ter, qua, qui, sex, sab, dom