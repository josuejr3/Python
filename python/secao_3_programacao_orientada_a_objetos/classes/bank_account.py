class BankAccount:
    def __init__(self, balance: float) -> None:
        # setter para saldo da conta
        self.balance = balance

    @property
    def balance(self) -> float:
        # getter
        return self.__balance

    @balance.setter
    def balance(self, value):
        # setter
        self.__balance = value if value > 0.0 else 0.0

    def credit(self, amount: float) -> None:
        self.balance += amount

    def debit(self, amount: float) -> (None | str):
        if amount > self.balance:
            return f"Amount to be withdrawn is greater than the total balance"
        self.balance -= amount



conta1 = BankAccount(-10)
print(conta1.balance)

print(conta1.debit(100))
conta1.balance = 100 # credit
print(conta1.balance)
conta1.credit(100)
conta1.debit(10)
print(conta1.balance)
