## Enumeracoes

Enumeracoes são usadas para enumerar coisas, como exemplo temos as cores de um semaforo. Ele e semelhante a chave e valor de dicionários.

Algumas caracteristicas importantes:

- Enums tem membros e seus valores sao constantes;
- São usados quando temos um determinado número de coisas;
- Sao um conjunto de nomes simbolicos ligados a valores unicos;
- Podem ser iterados para retornar seus membros canonicos na ordem de definicao.

<span style="color:rgb(300, 0, 0)">Obs: usaremos enum.Enum que é uma superclasse para enumeracoes. Porem, podemos usar ela diretamente, no entanto, ela nao se comporta como uma classe normal de Python.</span> 

Isso ocorre, pois a metaclasse da classe Enum e diferente. Alem disso, podemos usar o Enum como um tipo, ou seja, podemos aplicar type annotations e isinstance. 

> Ok, mas como fazemos para acessar inforamcoes do Enum?

	Basta que nos criemos um código da seguinte forma.

```Python
membro = Classe(valor) 
membro = Classe['chave']

# Somente o valor da chave
chave = Classe.chave.name

# ou então
valor = Classe.chave.value
```

Lembrando que quando o Enum e criado um novo tipo e criado e com esse novo tipo possui membros.

```Python
Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])  
  
def mover(direcao):  
    if not isinstance(direcao, Direcoes):  
        raise TypeError('direcao invalida')  
    print(f'Movendo para {direcao}')  
  
  
mover(Direcoes.ESQUERDA)  
mover(Direcoes.DIREITA)  
# mover('baixo')  
# mover('cima')  
  
# CHAMANDO PELO VALOR - O VALOR É A ENUMERAÃO EM SI  
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)  
  
  
# Pegando somente o nome e o valor da numeração (indice)  
print(Direcoes(1).name, Direcoes(1).value)  
print(Direcoes['DIREITA'].name, Direcoes.DIREITA.value)
```

Porem essa forma nao e muito legal para entender o que esta acontecendo, ja que os objetos Enum ficam sendo reconhecidos como "any" ou "qualquer".

```Python
class Direcoes(enum.Enum):  
    ESQUERDA = 1  
    DIREITA = 2  
  
  
#Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])  
  
def mover(direcao: Direcoes):  
    if not isinstance(direcao, Direcoes):  
        raise TypeError('direcao invalida')  
  
    direcao.DIREITA  
  
    print(f'Movendo para {direcao}')
```

No exemplo acima, agora a classe de "direcao" e de Direcao e podemos ainda usar atributos de classe, como tambem informacoes da classe Enum como o value e o name.


<mark style="background: #ABF7F7A6;">Obs: se a enumeracao nao esta sendo importante, ha uma funcao que faz isso automaticamente, chamada "enum.auto()".
</mark>




































