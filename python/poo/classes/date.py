class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        self.__day = day if 1 <= day <= 31 else 1

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        self.__month = month if 1 <= month <= 12 else 1

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year if year <= 2025 else 2025
        # metodo fill

    def show_date(self):
        return f"{self.__day}/{self.month}/{self.year}"


data1 = Date(40, 13, 2026)
data2 = Date(0, 0, 0)
print(data1.show_date())
print(data2.show_date())

data1.day = 16
data1.month = 13
data1.year = 2001

print(data1.day, data1.month, data1.year)
print(data1.show_date())














