# def func_multiplica(*args):
#
#     total = 1
#     for i in range(len(args)):
#         total *= args[i]
#
#     return total
#
#
# def func_impar_par(num):
#
#     return f"{num} é par" if num % 2 == 0 else f"{num} é impar"
#
#
# print(func_impar_par(0))
# print(func_multiplica(1, 2, 3))
# print(func_multiplica(5, 10, 1))
# print(func_multiplica(10, 2, 3, 4, 5))


# def duplicar(numero):
#
#     def dup():
#         return numero*2
#     return dup
#
# def triplicar(numero):
#     def tri():
#         return numero*3
#
#     return tri
#
# # Tentativa de fazer um closure
# a = triplicar(3)
# print(a())
#
# def quadruplicar(numero):
#     def quad():
#         return numero*4
#     return quad
#
#
# b = quadruplicar(3)
# c = duplicar(5)
# d = triplicar(8)
# print(b())
# print(c())
# print(d())


# Solucao

# USANDO CLOSURE - PROF

def criar_multiplicador(multiplicador):
    def mult(numero):
        return numero * multiplicador

    return mult

# Cria uma funcao com o multiplicador 3
duplicar = criar_multiplicador(2)
print(duplicar(100))

# ================ INTRODUCAO A DICIONARIOS =============









