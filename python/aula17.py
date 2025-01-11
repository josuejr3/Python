# Variáveis livres + nonlocal

# def fora(x):
#     a = x
#     def dentro():
#         # printa variáveis livres e que tenho acesso dentro da função dentro
#         #print(locals())
#
#         # printa variaveis livres dentro da funcao dentro
#         print(dentro.__code__.co_freevars)
#         return a
#
#     return dentro
#
# dentro1 = fora(10)
# dentro2 = fora(20)
#
# print(dentro1(), dentro2())


# def concatenar(string_inicial):
#     valor_final = string_inicial
#     def interna(valor_a_concatenar=""):
#
#         # valor_final é uma variavel livre pois está definida somente fora da função interna
#         # valor_final += valor_a_concatenar # erro, pois a variavel é somente de leitura nesse escopo
#         # É necessário informar ao python que a variável não é do escopo
#         nonlocal valor_final
#         valor_final += valor_a_concatenar
#         return valor_final
#     return interna
#
# c = concatenar('a')
# print(c("b"))
# print(c("c"))
# print(c("d"))
# print(c())


# Funções decoradoras

# função decorada - closure
# def make_function(func):
#     def interna(*args, **kwargs):
#         print("vou te decorar")
#         for arg in args:
#             is_string(arg)
#
#         result = func(*args, **kwargs)
#         print("vc foi decorada")
#         return result
#     return interna
#
# @make_function
# def inverte_string(string):
#     # método name retora o nome da função
#     # o nome vai ser o nome da função interna, já que a função interna deixou de existir
#     print(f"{inverte_string.__name__}")
#     return string[::-1]
#
# def is_string(string):
#     if not isinstance(string, str):
#         raise TypeError("O parâmetro não é uma string")
#
# invertida = inverte_string("123")
# print(invertida)


# DECORADORES COM PARÂMETROS


# def fabrica_de_funcoes(func):
#     print("Decoradora 1")
#     def aninhada(*args, **kwargs):
#         print("Aninhanda")
#         res = func(*args, **kwargs)
#         return res
#     return aninhada
#
# # exemplo de uma fabrica de decoradores
# def fabrica_de_decoradores(a, b, c):
#     return fabrica_de_funcoes
#
# @fabrica_de_funcoes
# def soma(a, b):
#     return a +b
#
# dez_mais_cinco = soma(10, 5)
# print(dez_mais_cinco)


# ordem de aplicação de decoradores

def parametros_decorador(nome):
    def decorador(func):
        print("Decorador:", nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f"{res} {nome}"
            return final

        return sua_nova_funcao
    return decorador

@parametros_decorador(nome="3")
@parametros_decorador(nome="2")
@parametros_decorador(nome="1")
def soma(a, b):
    return a + b

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)






















