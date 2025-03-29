#### Herança

A herança em Python funciona semelhante com a que conhecemos da biologia. Basicamente, uma classe "mãe" repassa métodos e atributos para classes "filhas" que foram derivadas delas. Ela é utilizada para reaproveitamento de código, a classe "filha" vai funcionar como uma especialização da classe "mãe".

Diferenças entre relações

-  Associação - um objeto _usa_ outro objeto;
-  Agregação - um objeto _tem_ um outro objeto;
-  Composição - é _dono de_ um outro objeto;
-  Herança - _é um_ 

> Generalização que também chamamos de "extend" é uma forma de estender a classe mãe para que contenha características adicionais. Falamos então que "(Classe filha) estende a (Classe mãe)".

> As relações entre classes composição e herança são muito semelhantes, entretanto, podemos diferenciar elas da seguintes forma. 

Em UML a relação entre duas classes é sinalizada por uma seta da classe filha para a mãe. A seta é vazia. 

-  Composição: uma classe é composta por outra, a classe "menor" é um membro da "maior" e quando o todo é deletado a parte também é. 

-  A herança por sua vez, funciona como uma especialização de uma classe superior, fornecendo métodos e atributos adicionais. 

Em Python, todas as classes já herdam de uma classe "built-in objects" da própria linguagem. 

Segue abaixo um exemplo da sintaxe de herança em Python

```Python
class Foo(object):  
    ...  
# informações a respeito da classe foo  
help(Foo)
```

Para herdar de uma classe mãe, basta colocar ela entre parênteses na declaração da classe filha. 

Outro exemplo usando herança com a classe "Pessoa" sendo uma classe generalista e "Cliente" a especializada.

```Python
class Pessoa:  
    def __init__(self, nome, sobrenome):  
        self.nome = nome  
        self.sobrenome = sobrenome  
  
    def falar_nome_classe(self):  
        # nome da classe  
        print(self.nome, self.sobrenome, self.__class__.__name__)  
  
class Cliente(Pessoa):  
    ...  
  
class Aluno(Pessoa):  
    ...  
  
c1 = Cliente('Josue', 'Junior')  
c1.falar_nome_classe()  
a1 = Aluno('Jose', 'Luiz')  
a1.falar_nome_classe()  
  
help(Cliente)
```

===OBS: METHOD RESOLUTION ORDER - (MRO)===

Execução da função help(class).

```txt
Help on class Cliente in module __main__:

class Cliente(Pessoa)
 |  Cliente(nome, sobrenome)
 |
 |  Method resolution order:
 |      Cliente
 |      Pessoa
 |      builtins.object
 |
 |  Methods inherited from Pessoa:
 |
 |  __init__(self, nome, sobrenome)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  falar_nome_classe(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Pessoa:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
```

O Method resolution order define a ordem em que métodos e atributos vão ser buscados no meu objeto. Sendo assim, se estivermos buscando o atributo "nome", primeiro ele procura na classe Cliente, se não encontrar ele busca na classe Pessoa e caso continue sem achar ele busca na "builtins.object".

#### Super e sobreposição de membros em Python Orientado à Objetos.

A sobreposição de membros em Python ocorre quando "um faz sombra no outro" e ele nem sequer é chamado. 

Para isso usamos a palavra chave "super" que retorna temporariamente a classe mãe e a partir disso podemos chamar métodos da super classe. Segue abaixo um exemplo do código. 

```Python
class MinhaString(str):  
    def upper(self):  
        print("CHAMOU UPPER")  
        return super().upper() 
  
string = MinhaString('Luiz')  
print(string.upper())
```

Nesse caso, fizemos uma sobreposição do método upper, porém,  combinamos com a funcionalidade principal dele que é de deixar em maiúsculo. Para isso, fizemos o código arbitrário que é representado pelo *"print("CHAMOU UPPER)"* e em seguida retornamos o método da classe mãe com a palavra chave **super**. A classe super recebe parâmetros, sendo o primeiro o nome da classe, que no caso é "MinhaString" e o segundo o "self".

Assim como classes podem ter atributos distintos e posso chamar eles em classes derivadas, posso fazer o mesmo com métodos, chamando eles em cadeia, do menos especializado até o mais especializado. Segue o exemplo. 

```Python
class A:  
    atributo_a = 'a'  
  
    def metodo(self):  
        print('A')  
  
class B(A):  
    atributo_b = 'b'  
  
    def metodo(self):  
        print('B')  
  
class C(B):  
    atributo_c = 'c'  
  
    def metodo(self):  
        super(C, self).metodo()  # Metodo de B
        print('C')  
  
c = C()  
print(c.atributo_a)  
print(c.atributo_b)  
print(c.atributo_c)  
  
c.metodo()
```

Nesse caso, a classe C é sub de B que é sub de A. 

No código acima podemos printar os atributos individuais apenas chamando C pois os atributos não estão sendo sobrepostos. 

===Como assim, Josué? ===

	Bem, C é especializado e tem o atributo "atributo_c", porém ele herda de B o "atributo_b" e o mesmo ocorre com B que herda "atributo_a". Sendo assim, temos três atributos individuais em C.

	Levendo em consideração a classe "super" que recebe a instância e a classe em que está eu consigo chamar um método da classe mãe. Sendo assim, quando eu chamo

```Python
super(C, self).metodo()
```

	Eu estou executado a função método da classe mãe "B" que por sua vez printa o B na tela, e após isso executo o print de "C", resultando em "B C", métodos encadeados através das classes mãe. 

	O mesmo ocorreria se eu chamasse o super com método em B, ele chamaria a função método de A para que só após isso o print de B fosse executado. 

Caso esteja com dúvida em relação a hierarquia podemos conferir além do help usando uma função de method resolution order. 

```Python
c.mro()
```

---

Os parâmetros entre uma classe e outra em Python são bem importantes e requerem atenção (método especial init). Para evitar perdas de informação é importante repassarmos os parâmetros necessários para a classe mãe. Segue o exemplo abaixo. 

```Python
class B(A):
	atributo_b = "valor b"
	def __init__(self, atributo, outra_coisa):
		super().__init__(atributo)
		self.outra_coisa = outra_coisa
```

Nesse caso o parâmetro da classe "mãe" (A) é o atributo, já o parâmetro da classe filha (B) é o "outra_coisa".

===Obs: caso não queira usar a sintaxe do super é possível fazer o seguinte. 

```Python
A.metodo(self) # Busca o metodo da classe A
``` 

Basicamente, usamos  super() como uma forma de repassar os parâmetros que são semelhantes.


