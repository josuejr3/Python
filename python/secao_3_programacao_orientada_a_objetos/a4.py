# Revisando os métodos classmethod, staticmethod e method

class Connection:
    # método de instância, inicializa atributos da instância
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    # ---- MÉTODOS DE INSTÂNCIAS (SELF)
    # configura o valor do usuário,
    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    # ---- MÉTODOS DE CLASSES (CLASS)
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


    # staticmethod - Função dentro da classe que não possui acesso a nada da classe e das instâncias
    @staticmethod
    def soma(x, y):
        return x + y


# c1 = Connection()
# c1.set_user("admin")
# c1.set_password("<PASSWORD>")
# print(c1.user)
# print(c1.password)


# classmethod
c1 = Connection.create_with_auth("luiz", "123")
print(c1.user)
print(c1.password)

print(c1.soma(1, 2))