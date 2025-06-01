# Usando um método especial chamado __ call __



# class CallMe:
#     def __init__(self, phone):
#         self.phone = phone
#
#     def __call__(self, nome):
#         print('Chamando', nome)
#
#
# call1 = CallMe('123-456-7890')
# # Imagine que você queira chamar a instância da classe, ou seja
# # call1()
#
# call1('Luiz')
# print(call1.phone)









# Classes decoradoras

class Multiplicar:
    # a funcao usada, no caso a soma
    def __init__(self, func):
        self.func = func
        #print('INIT', func)
        self._multiplicador = 10

    # args e kwargs sao os argumentos da funcao soma
    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        resultado = self.func(*args, **kwargs) * self._multiplicador
        return resultado


@Multiplicar
def soma(x, y):
    return x + y



dois_mais_dois = soma(2, 4)
print(dois_mais_dois)
























