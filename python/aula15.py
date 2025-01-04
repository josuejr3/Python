# Try, except, else e finally

# a = 18
#b = 0

# levanta exceção de divisão por zero
# c = a / b
try:
    a = 18
    b = 0
    print("Linha1")
    print(b[0])
    c = a / b
    print("Linha2")
except ZeroDivisionError:
    print("Dividiu por 0")
except NameError:
    print("Uma das variáveis não foi definida")
# Descobrindo o nome do erro através do alias "as error"
# Nesse caso, o error só vem a mensagem e não o nome do erro
except (TypeError, IndexError) as error:
    print("O tipo não é float ou inteiro / Indíce inválido")
    print("MSG:", error)
    print("Nome do erro/Nome da classe: ", error.__class__.__name__)
except Exception:
    print("Erro desconhecido")

# Caso eu não queira erro nenhum, eu posso tratar a classe base das classes de exceções

print("CONTINUAR")

# Para o finally, vamos exemplificar no ato de ocorrer um erro ao abrir um arquivo

try:
    print("ABRIR O ARQUIVO")
    8/0
    # open
except ZeroDivisionError:
	print("Dividiu por zero")
else:
    print("Codigo executado com sucesso")
finally:
    # sempre é executado
    print(2)
    print("FECHAR ARQUIVO")

# O finally executa mesmo se tiver erros

# Link para todas as exceções que herdam de Exception
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


# RAISES

# print(123)
# raise ValueError("Deu erro")
# print(456)


# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         print("-----")
#         raise

# Porém o except com raise ao invés do return é redundante
# Não teria necessidade de um except
# print(divide(8, 0))


# O caso acima, só será viável caso seja
# necessário fazer algum código dentro do bloco do except que está o raise


# Criando o meu próprio erro "ZeroDivisionError"
def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero")
    return True

def deve_ser_int_ou_float(n):

    tipo_n = type(n)

    if not isinstance(n, (float, int)):
        raise TypeError(
            f"{n} deve ser int ou float. "
            f"{tipo_n.__name__} enviado"
        )
    return True


def divide(n, d):

    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceita_zero(d)
    return n / d


print(divide(8, "0"))