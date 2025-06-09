
#### <span style="color:rgb(4, 255, 0)">Deque</span>

Deque, também conhecido como "double-ended queue" é uma estrutura de dados que trabalha nas "duas pontas". 

-  LIFO  (Last In First Out)

Estrutura do tipo LIFO também é conhecida como pilha, ou stack e ela funciona basicamente da seguinte forma: o último elemeto inserido é sempre o primeiro a ser removido. Funciona como se fosse uma pilha de pratos.

	Complexidade

	Para tirar do final da Pilha: O(1) - Tempo constante
	Para tirar do ínicio da Pilha: O(n) - Tempo linear

-  FIFO (First In First Out)

Estrutura do tipo FIFO também é conhecida como fila, ou queue e ela funciona basicamnte da seguinte forma: o primeiro elemento a entrar é sempre o primeiro a ser removido. Funciona como se fosse uma fila de almoço em um restaurante, por exemplo.

	Complexidade

	Para tirar do final da Fila: O(1) - Tempo constante
	Para tirar do ínicio da Fila: O(1) - Tempo constante

---

Ok, podemos usar as listas do Python para trabalhar tanto com filas, como também com pilhas.

<mark style="background: #FF5582A6;">PORÉM,</mark> em Python é melhor trabalhar com listas quando queremos alterar apenas o final. Pois não fazemos nenhum tipo de alteração na estrutura, apenas acrescentamos ou removemos mais um elemento. 

Já na Fila, como as operações são sempre no ínicio, significa que por exemplo: toda vez que um elemento é removido eu tenho que diminuir a posição dos elementos restantes em uma posição. Isso gera um custo de processamento.

-  Para Pilhas

```Python
lista.append() # acrescenta no final
lista.pop()    # remove do final
```

Para resolver o problema das filas, nós usamos o módulo collections com a estrutura deque que possibilita a remoção em ambas as extremidades da estrutura.

```Python
from collections import deque

fila_correta: deque[int] = deque()  
fila_correta.append(3)  
fila_correta.append(4)  
fila_correta.append(5)  
fila_correta.appendleft(0)  
fila_correta.appendleft(1)  
fila_correta.appendleft(2)  
print(fila_correta)  
fila_correta.pop()  
fila_correta.popleft()  
print(fila_correta)
```

-  Links para saber mais

	https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/
	https://youtu.be/svWVHEihyNI




















