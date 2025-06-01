# class MinhaString(str):
#     def upper(self):
#         print("CHAMOU UPPER")
#         retorno = super().upper()
#         print("DEPOIS DO UPPER")
#         return retorno
#
# string = MinhaString('Luiz')
# print(string.upper())


class A:
    atributo_a = 'a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = "valor b"

    # sobreposicao do metodo init do A
    def __init__(self, atributo, outra_coisa="oxi"):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa


class C(B):
    atributo_c = 'c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("burlei o sistema")

    def metodo(self):
        # chame o classe mae de B e use o metodo dela
        super(B, self).metodo()
        super(C, self).metodo()
        print('C')

c = C("Atributo", "aiaiai")
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
#
# c.metodo()

# verificar o method resolution order
# print(C.mro())


