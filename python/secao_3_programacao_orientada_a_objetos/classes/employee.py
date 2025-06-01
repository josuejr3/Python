class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            salary = 0
        self.__salary = salary


empregado1 = Employee('John', 'Smith', 1518)
empregado2 = Employee('Mary', 'Adams', 1410)

print(empregado1.name)
print(empregado2.name)

print(empregado1.surname)
print(empregado2.surname)

print(empregado1.salary)
print(empregado2.salary)

empregado1.name = "Joseph"
empregado2.name = "Anne"
empregado1.surname = "Porter"
empregado2.surname = "Wilson"

print("===================================================================")

empregado1.salary = empregado1.salary + (empregado1.salary*0.10)
empregado2.salary = empregado2.salary + (empregado2.salary*0.10)

print(empregado1.name)
print(empregado2.name)

print(empregado1.surname)
print(empregado2.surname)

print(empregado1.salary)
print(empregado2.salary)






















