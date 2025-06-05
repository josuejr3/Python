
#### <span style="color:rgb(4, 255, 0)">Módulo random para números pseudoaleátorios</span>

O módulo random é utilizado para criação de números pseudoaleatórios, o que significa que os números parecem ser aleatórios, mas na verdade não são. Portanto, este módulo <mark style="background: #BBFABBA6;">não deve ser usado para segurança ou uso criptrográfico.</mark>

O motivo disso é que quando temos uma mesma entrada e um mesmo algoritmo, então a saída pode ser previsível. Podemos conferir mais detalhes nesse link: https://docs.python.org.pt-br/3/library/random.html

Dentre as funções mais fundamentais nesse módulo temos as seguintes:

-  seed

Inicializa o gerador de random, funciona como se fosse uma semente para o número aleatório. O Python para dentro do seed uma data, ou seja, a data que consta no aparelho.

-  random.randrange(inicio, fim, passo)

Gera um número inteiro aleatório dentro de um intervalo específico e considerando um passo.

-  random.randint(inicio, fim)

Faz a mesma coisa que o randrange, porém nesse caso ele não tem nenhum passo e considera o final (inclusivo).

-  random.uniform(inicio, fim)

Gera um número em ponto flutuante que é aleatório dentro de um intervalo e não possui passo.

-  random.shuffle(SequênciaMutável)

Embaralha a lista original.

-  random.choice(iterável)

O choice escolhe um elemento aleatório do iterável, ou seja é praticamente o choices com k = 1.

-  random.choices(iterável, k=N)

Similar ao sample, a diferença é que nesse caso ele pode repetir elementos do array original

-  random.sample(iterável, k=N)

Escolhe elementos do iterável e retorna outro iterável (não repete).

```Python
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
```

