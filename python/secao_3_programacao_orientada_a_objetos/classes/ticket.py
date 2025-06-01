class Ticket:
    def __init__(self, id: str, description: str, amount: int, price: float) -> None:
        self.id = id
        self.description = description
        self.amount = amount
        self.price = price

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self.__description

    @property
    def amount(self):
        return self.__amount

    @property
    def price(self):
        return self.__price

    @id.setter
    def id(self, id):
        self.__id = id

    @description.setter
    def description(self, description):
        self.__description = description

    @amount.setter
    def amount(self, amount):
        self.__amount = amount if amount > 0 else 0
        self.__amount = amount

    @price.setter
    def price(self, price):
        self.__price = price

    def calculate_price(self):
        return self.price * self.amount


mouses = Ticket(11, "mouse gamer", 4, 128.5)
print(mouses.calculate_price())

mouses.amount = 2
print(mouses.amount)
print(mouses.id)
print(mouses.description)
print(mouses.price)
print(mouses.calculate_price() )
























