## Métodos especiais, dunder methods ou métodos mágicos.

Dunder methods são importantes pois com eles podemos fazer determinadas tarefas com a nossa classe personalizada. Eles funcionam como se fossem a sobrecarga de operadores que estudamos em C++.

Alguns métodos mais importantes e utilizados quando estamos em um contexto de métodos especiais são os métodos "*repr*" e o "*str*". Esse dois métodos são usados quando queremos especificar como o objeto será representado. 

```Python
class Ponto:  
    def __init__(self, x: int, y: int):  
        self.x = x  
        self.y = y  
  
    def __repr__(self):  
        class_name = self.__class__.__name__  
        # class_name = type(self).__name__  
        return f"{class_name}(x={self.x}, y={self.y})"  
  
  
p1 = Ponto(1, 2)  
p2 = Ponto(3, 4)  
print(p1, p2)

# A saida será
# >>> Ponto(x=1, y=2) Ponto(x=3, y=4)
```

Acima vimos o método repr, no str a única diferença é como o objeto vai ser representado porém em formato de string. 

```Python
def __str__(self):  
    return f'({self.x}, {self.y})'

# A saída será
# >>> (1, 2) (3, 4)
```

===Em resumo, ambos os métodos vão ser usados para representação do objeto, entretanto, o método "repr" é mais voltado para desenvolvedores, enquanto que o str concentra-se em uma representação de formato string e "mais amigável".===

Ok, mas e se eu tiver definido os dois na minha classe, como vou ver o repr se sempre o objeto utiliza o str primeiro?

	Temos duas formas de solucionar isso, veja elas abaixo

1 - A primeira é usar a função repr(p2)

```Python
print(p1, repr(p2))

# Saída
# >>> (1, 2) Ponto(x=3, y=4)
```

2 - Utilizando uma exclamação dentro do print especificando o dunder method

```Python
print(f"{p2!r}")

# Saída
# >>> Ponto(x=3, y=4)
```

===Obs: é importante se atentar aos tipos quando estamos utilizando o repr pois eles são importantes. Dessa forma, sempre que formos definir o repr é necessário fazer o uso do "!r"===

```Python
class Ponto:  
    def __init__(self, x: int, y: int, z="String"):  
        self.x = x  
        self.y = y  
        self.z = z
	def __repr__(self):  
	    class_name = self.__class__.__name__  
	    # class_name = type(self).__name__  
	    return f"{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})"

print(p1, repr(p2))
# Saída
# >>> (1, 2) Ponto(x=3, y=4, z='String')
```

---
#### Métodos especiais new e init

Os dois métodos new e init juntos funcionam como se fosse um construtor que temos em outras linguagens de programação.

- Construtor é um método que cria um objeto (normalmente ele já cria e inicializa a instância).

- O new vai criar o objeto e o init inicializa ele.

"Por baixo dos panos" o Python faz o seguinte

```Python
class A:
	def __init__(self):
		print("Sou o init")
	def __repr__(self):
		return 'A()'

a = object.__new__(A)
a.__init__()
```

É como se o construtor mesmo (que vimos em C++) fosse o new e a definição de atributos fosse o init. 

Porém, em Python se quisermos fazer alguma coisa no meio do caminho do new ao init, temos essa liberdade, basta definir um método new  (ele cria e retorna o objeto, por esse motivo não retorna self, ele cria o self).

```Python
class A:
	def __new__(cls):
		# Lembrando que A herda automaticamente da classe object
		print("Antes de criar a instancia")
		return super().__new__(cls)
	def __init__(self):
		print("Sou o init")
	def __repr__(self):
		return 'A()'

a = object.__new__(A)
a.__init__()
```

===Obs: é importante as assinaturas do new e também do init serem iguais, caso não queira, posso passar args e kwargs===

---
 Lista com métodos especiais

```txt
__lt__(self, other) - self < other  
__le__(self, other) - self <= other  
__gt__(self, other) - self > other  
__ge__(self, other) - self >= other  
__eq__(self, other) - self == other  
__ne__(self, other) - self != other  
__add__(self, other) - self + other  
__sub__(self, other) - self - other  
__mul__(self, other) - self * other  
__truediv__(self, other) - self / other  
__neg__(self) - -self  
__str__(self) - str  
__repr__(self) - str - define uma forma de representação do objeto
```

































> Referências

-  https://docs.python.org/3/reference/datamodel.html#specialnames
- https://rszalski.github.io/magicmethods/




