
#### <span style="color:rgb(4, 255, 0)">Módulo random para números pseudoaleátorios</span>

O módulo random é utilizado para criação de números pseudoaleatórios, o que significa que os números parecem ser aleatórios, mas na verdade não são. Portanto, este módulo <mark style="background: #BBFABBA6;">não deve ser usado para segurança ou uso criptrográfico.</mark>

O motivo disso é que quando temos uma mesma entrada e um mesmo algoritmo, então a saída pode ser previsível. Podemos conferir mais detalhes nesse link: https://docs.python.org.pt-br/3/library/random.html

Dentre as funções mais fundamentais nesse módulo temos as seguintes:

-  seed

Inicializa o gerador de random, funciona como se fosse uma semente para o número aleatório.

-  random.randrange(inicio, fim, passo)

Gera um número inteiro aleatório dentro de um intervalo específico e considerando um passo.

-  random.randint(inicio, fim)

Faz a mesma coisa que o randrange, porém nesse caso ele não tem nenhum passo e considera o final (inclusivo).

-  random.uniform(inicio, fim)

Gera um número em ponto flutuante que é aleatório dentro de um intervalo e não possui passo.

-  random.shuffle(SequênciaMutável)
-  random.choice(iterável)
-  random.choices(iterável, k=N)
-  random.sample(iterável, k=N)