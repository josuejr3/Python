from datetime import datetime, tzinfo
from pytz import timezone

data = datetime(2022, 4, 20, 7, 6, 8, tzinfo=timezone('Asia/Tokyo'))
print(data)

# Outra forma usando strptime

data_str = "2022/04/20 07:06:08"
formato_data = "%Y/%m/%d %H:%M:%S"

data_s = datetime.strptime(data_str, formato_date)

print(data_s)

#https://docs.python.org/3/library/datetime.html