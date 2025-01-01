# Funções Lambda

# - São anônimas, (não possuem nome)
# - São inline, (codificadas em uma única linha)

# lista = [4, 32, 1, 34, 5, 6, 6, 21]

# lista.sort(reverse=True)  # modifica a lista real
# O parâmetro reverse indica se vai ser invertida ou não
# sorted(lista) # cria uma nova lista ordenada

dicionarios = [
    {"nome": "Luiz", "sobrenome": "Miranda"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]

# Nesse caso o python não vai saber muito bem ordenar os dicionarios
# que estão presentes na lista

#print(dicionarios)

# Como o Python não sabe como o rdenar dicionário, dentro de sort eu posso passar uma função
def ordena(item):
	return item["nome"]

dicionarios.sort(key=ordena)


def exibir(lista):
    for item in lista:
        print(item)
    print()


lista1 = sorted(dicionarios, key=lambda item: item["nome"])
lista2 = sorted(dicionarios, key=lambda item: item["sobrenome"])

# Não haveria necessidade de criar uma função "padrão" pois ela possui somente uma unica linha
# sendo assim, poderia usar uma função lambda
# segue o exemplo abaixo criando uma função lambda para organizar por sobrenome

print("\n")

exibir(lista2)
exibir(lista1)

# Convertendo algumas funções normais em funções lambda

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m, 2
)

print(duplica(2))

# função lambda soma
print(
    executa(lambda x, y: x + y, 2, 3),
    executa(soma, 2, 3),

)

print(
	executa(
		lambda *args: sum(args), 1,2,3,4,5,6,7
	)
)

# =========================== KWARGS ===================================
# empacotamento e desempacotamento de dicionários


a, b = 1, 2
a, b = b, a

print(a, b)

# Ok, aqui o a = 2 e o b = 1

pessoa = {
    "nome": "Aline",
    "sobrenome": "Silva",
}

dados_pessoa = {
    "idade": 16,
    "altura": 1.6,
}


# Desempacotamento/empacotando de dicionários
a, b = pessoa.values()
print(a, b)

# desempacotamento/empacotamento interno
(a1, a2), (b1, b2) = pessoa.items()

print(a1, a2)
print(b1, b2)

pessoa_completa = {**pessoa, **dados_pessoa, "chave": 1}
print(pessoa_completa)

# Exemplo de uso de kwargs para argumentos nomeados

def mostro_argumentos_nomeados(*args, **kwargs):
    print(args)
    print(kwargs)

mostro_argumentos_nomeados(4, nome="Joana", qLq = 123)


mostro_argumentos_nomeados(**pessoa_completa)

# exemplo de um arquivo de configuracao com muitos parametros
configuracoes = {
	"arg1": 1,
	"arg2": 2,
	"arg3": 3,
}

mostro_argumentos_nomeados(**configuracoes)

#  LIST COMPREHENSION
# criando uma lista

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista = [1 for numero in range(10)]
print(lista)

# incluindo um proprio numero
lista = [numero for numero in range(5)]
print(lista)

# multiplicando por 2 (usando operações)
lista = [numero*2 for numero in range(5)]
print(lista)

# usando como entrada
# lista = [input() for numero in range(10)]
# print(lista)


# ================== MAPEAMENTO =========================

produtos = [
    {"nome": "p1", "preco": 20, },
    {"nome": "p2", "preco": 10, },
    {"nome": "p3", "preco": 30, },
]

novos_produtos = [
    #{"nome": produto["nome"], "preco": produto["preco"]}
    {**produto, "preco": produto["preco"] * 1.05}
    # inserindo uma condicional
    if produto["preco"] > 20 else {**produto}
    for produto in produtos

    # aplicando filtro de preco
    if produto["preco"] >= 20 and produto["preco"] * 1.05 > 10

]

print(novos_produtos)

# desempacotando (so foi usado um * porque é uma lista e não dicionario
print(*novos_produtos, sep="\n")

print(novos_produtos)

import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


print("==========================================")

# ======================================= FILTROS ==========================================
lista_t = [i for i in range(10) if i < 5]
print(lista_t)


# List comprehension com mais de um for

lista_c_for_aninhado = [
                        (x,y)
                        for x in range(3)
                        for y in range(3)
                        ]

print(lista_c_for_aninhado)

print("=======================================================")
# Com o for do lado esquerdo
lista_for_esquerdo = [
		 [letra for letra in "Luiz"]
		 for x in range(3)
]
print("=======================================================")


# Para cada elemento x no range de 3 crie uma nova lista de tamanho 3

# De outra forma: para cada x em range 3 faça um laço no nome luiz
# Sendo assim, vamos ter 3 vezes o nome luiz


print(lista_for_esquerdo)


# ==================== DICTIONARY COMPREHENSION E SET COMPREHENSION ============================================

produto_1 = {
    "nome" : "Caneta Azul",
    "preço" : 2.5,
    "categoria" : "Escritório",
}

#

# Gerando um novo dicionário a partir do produto_1

dc = {
	# O que eu quero obter
    chave : valor
    # A condicional
    if isinstance(valor, str) else valor
    # O for
	for chave, valor
    # O iterável
	in produto_1.items()
}

print(dc)

s1 = {i for i in range(10)}

print(s1)

# =================================== ISINSTANCE =====================================

# serve para verificar se um objeto é de um determinado tipo


lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {"nome": "Luiz"}]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print(item.upper(), isinstance(item, str))

    # dentro da tupla, significa, int ou float
    if isinstance(item, (float, int)):
        print(item, item * 2)







