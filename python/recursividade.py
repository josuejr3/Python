# Funções recursivas e recursividade

def fatorial(n):
    # caso base
    if n <= 1:
        return 1
    # caso recursivo
    return n * fatorial(n-1)


print(fatorial(6))
print(fatorial(1))

# Função recursiva de fibonacci
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


# contando de um número até outro número
def recursiva(inicial=0, fim=10):
    # Caso recursivo
    # contar até chegar ao final

    if inicial >= fim:
        return fim

    inicial += 1
    return recursiva(inicial, fim)

print(recursiva())