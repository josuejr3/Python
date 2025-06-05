import random
import time

r_range = random.randrange(10, 20)
r_int = random.randint(10, 20)
r_float = random.uniform(10, 20)

lista_de_items = ["A", "B", "C", "D", "E", "F"]
random.shuffle(lista_de_items)

# random.seed(time.time())
# print(time.time())

# aleatoriedade baseada em um numero 0
random.seed(0)

print(r_range, r_float, r_int)
print(lista_de_items)

novos_nomes = random.sample(lista_de_items, k=3)
print(novos_nomes)

novos_nomes = random.choices(lista_de_items, k=3)
print(novos_nomes)

selecionado = random.choice(novos_nomes)
print(selecionado)