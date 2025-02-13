#### Herança múltipla

Em Python Orientado à Objetos, a herança múltipla é quando uma classe herda métodos e atributos de mais de uma única classe.

-  Exemplo de uma herança simples

	Animal  -> Mamífero -> Humano -> Pessoa -> Cliente 

A herança múltipla funciona da mesma forma que vimos acima, porém pode complicar um pouco mais. 

-  Herança múltipla e mixins

Na herança múltipla, os mixins são uma classe que não faz parte da família de classes principal como a que temos acima (de animal até cliente). 

Ex: relacionar a classe cliente com a classe *"Log"*.

	Log -> FileLog

Nesse caso, a classe Log possui uma classe filha chamada FileLog e com ela nós fazemos mixins com a classe Pessoa (uma não tem nada a ver com a outra) para criar a classe Cliente.

```Python
class Cliente(Pessoa, FileLog)
```

> *Problema do Diamante*

Ocorre quando um classe herda de duas outras classes e essas outras classes herdam de uma única. Veja o exemplo abaixo com as classes A, B, C e D.

```txt
   A    = falar()
 /   \
B     C = falar()
 \   /
   D    = não possui
```

A partir disso surge a pergunta, se eu quiser utilizar um método que está em C ou em B e o método tem o mesmo nome tanto em B como em C, como que o D vai descobrir qual o "caminho" correto a seguir.

Para resolver isso, usamos o método de classe especial **Classe.mro()**, ou então **__mro__**

-  C3 superclass linearization é como vai ser definido quem vai ser chamado. Define a ordem que as coisas vão ficar.

===Obs: a ordem em que as classes são disponibilizadas dentro dos parenteses é IMPORTANTE pois muda o mro===

```Python
class A:  
    ...  
    def quem_sou(self):  
        print("A")  
  
class B(A):  
    ...  
    def quem_sou(self):  
        print("B")  
  
class C(A):  
    ...  
    def quem_sou(self):  
        print("C")  
  
class D(B, C):  
    ...  
    def quem_sou(self):  
        print("D")  
  
d = D()  
d.quem_sou()
```

Normalmente, quando temos o problema de diamante a classe que herda de duas outras classes tem mais chances de buscar primeiro na primeiro classe entre parenteses, no caso acima, o B.

-  Se o atributo não estiver em B, porém em C e A, pelo mro a classe filha busca o método na antecedente mais próximo, nesse caso o C.

Para ver o mro da classe D eu posso fazer o seguinte. 

```Python
print(D.__mro__)
# ou 
print(D.mro())
```

#### Classes abstratas - Abstract Base Class (abc)

Classes abstratas são classes que não devem ser instanciadas e elas servem apenas como base para outras classes que vão ser especializadas.

No exemplo que estudamos de eletrônico, smartphone, log e mixin, a classe log pode ser considerada de forma brusca uma classe abstrata. 

Classes abstratas podem:

-  Possuir métodos abstratos (não possuem corpo);
-  Método concretos.

As regras para classes abstratas com métodos abstratos é que **NÃO PODEM** ser instanciadas diretamente. 

-  Métodos abstratos devem ser implementados nas subclasses;
-  Uma classe abstrata em Python tem sua metaclasse sendo "**ABCMeta**".

Além disso, em classes abstratas podemos usar o que já estudamos antes. 

-  property;
-  setter;
-  classmethod;
-  staticmethod;
-  method (método normal).

Para isso, usamos o decorador mais interno *@abstractmethod* e herdamos de ABC. 

	A classe ABC é uma classe que tem uma metaclass "ABCMeta"

Segue abaixo duas formas de criar uma classe abstrata com ABC

```Python
from abc import ABC

class Log(ABC):
	...
```

Ou então, se preferir. 

```Python
from abc import ABCMeta

class Log(metaclass=ABCMeta):
	...
```

---

Segue abaixo outro exemplo mais detalhado usando classes ABC

```Python
class AbstractFoo(ABC):  
    def __init__(self, name):  
        self._name = None  
        self.name = name  
  
    @property  
    @abstractmethod    
    def name(self): ...  
  
    @name.setter  
    def name(self, name): ...  
  
class Foo(AbstractFoo):  
    def __init__(self, name):  
        super().__init__(name)  
        #print("Sou inútil")  
  
    @property  
    def name(self):  
        return self._name  
  
    @name.setter  
    def name(self, name):  
        self._name = name
```

Para evitar copiar os getters e setters na classe concreta, e sabendo que as property com getters e setters são métodos que se comportam como atributos, poderiamos fazer o seguinte.  (Só funciona para atributos de classe e não de instâncias)

===Obs: se definimos um getter concreto na classe abstrata e um setter abstrato, nas classes filhas, somente ajustando o setter não vai funcionar.===


```Python
class AbstractFoo(ABC):  
    def __init__(self, name):  
        self._name = None  
        self.name = name  
  
    @property      
    def name(self):
	    return self._name  
  
    @name.setter  
    @abstractmethod
    def name(self, name): ...  

clas Foo(AbstractFoo):
	def __init__(self, name):  
	        super().__init__(name)  
	        #print("Sou inútil")  
	  
	@name.setter               | 
	def name(self, name):      | 
		self._name = name      |
```

Ocorre um erro, pois a *property* é da classe em que ela está.

Para resolver isso, basta modificar o namespace do setter. 

```Python
clas Foo(AbstractFoo):
	def __init__(self, name):  
	        super().__init__(name)  
	        #print("Sou inútil")  
	  
	@AbstractFoo.name.setter                
	def name(self, name):      
		self._name = name      
```






















































