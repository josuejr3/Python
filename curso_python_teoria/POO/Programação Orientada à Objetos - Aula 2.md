##### @property 

Em Python o @property ou propriedade em Português é um getter no estilo Pythônico.

-  Getter é um método especial para obter o valor de um determinado atributo;
-  No Python, getter se comporta como um atributo, sendo assim, nós não teríamos "cor -> get_cor()"

```Python
class Pen:  
    def __init__(self, color):  
        self.color = color  
  
    # getter  
    def get_color(self):  
        return self.color
```

De maneira simples, um @property é uma propriedade do objetos. Ela é um método especial em Python que se comporta como um atributo.

A @property é normalmente utilizada nos seguintes caso:

-  Como getter;
-  Para evitar quebrar código cliente;
	-  Código cliente é o código que usa o seu código.
-  Para habilitar um setter;
-  Para executar ações ao obter um atributo.

Ao trabalhar com getters e setters de forma "limpa" estamos suscetíveis a erros, podemos alterar um simples nome de atributo e isso pode ocasionar um efeito bola de neve que demandará tempo para ser resolvido. 

Pensando nisso, podemos encapsular os atributos de forma que nós possamos acessá-los indiretamente. Para isso, em outras linguagens de programação nós usamos palavras chaves: public, protected e private, em Python é bem diferente. 

Sendo bem objetivo, se temos atributos *private* ou *protected*, eles são incessíveis de fora da classe. Chegamos no ponto em fornecer o acesso do atributo para o programador, fazemos isso com o getter.

-  Exemplo de um getter original.

```Python
class Caneta:
	def __init__(self, cor):
		self.cor_tinta = cor

	def get_cor(self):
		return self.cor_tinta
```

Dessa forma, não quebramos o código cliente, pois estamos fazendo o uso de um getter. 

##### @property + @setter e getter

Diferente do getter o setter serve como uma ferramenta para alteramos algum dos atributos que compõe a classe. Ele serve para que possamos adequar a entrada ao que o atributo comporta.

Para usarmos o setter precisamos de um lugar na memória para que fique salvo. Dessa forma, precisamos criar um novo atributo, porém, ===usando um underline ou dois antes do nome. Isso significa que o valor não deve ser alterado.===

```Python
class Caneta:
	def __init__(self, cor):
		self.cor_tinta = cor
		self._cor = self.cor_tinta

	@property
	def cor(self):
		print("Property")
		return self.cor_tinta

def mostrar(caneta):
	return caneta.cor
```

===OBS: Em Python a organização por encapsulamento se dá da seguinte maneira. 

-  ._ - Acesso privado, ou seja, só pode ser usado dentro da própria classe;
-  .__ Acesso
-  (sem nada) - Acesso público, pode ser acessado dentro e fora da classe.

===OBS: Não podemos ter métodos de mesmo nome.

Como o setter e o getter são interligados, para criação de um setter devemos usar o nome do getter. 

```Python
# GETTER
@property
def cor(self):
	return self._cor_tinta

@cor.setter
def cor(self, color):
	self._cor = color
```

Além disso, quando criamos um objeto e os argumentos são iniciados, podemos substituir isso pelo setter direto, ou seja. 

```Python
def __init__(self, cor):
	# chama o setter .cor
	self.cor = cor
```

Outro exemplo, dessa vez usando apenas o setter sem colocá-lo no construtor. 

```Python
class Pen:  
    def __init__(self, color):  
        self.color = color  
        self._color_tip = None  
  
    # getters em Python  
    @property  
    def color(self):  
        print('PROPERTY')  
        return self._cor  
  
    @color.setter  
    def color(self, color):  
        print("ESTOU NO SETTER")  
        self._cor = color  
  
    @property  
    def color_tip(self):  
        return self._color_tip  
  
    @color_tip.setter  
    def color_tip(self, color):  
        self._color_tip = color
```

##### Encapsulamento e tipos de acesso: private, protected e public.

O encapsulamento de maneira simplificada é como vimos em C/C++ ele serve para que possamos proteger métodos e atributos. Entretanto, o Python não possui modificadores de acesso como os que vimos em C/C++, *private*, *protected* e *public*.

No entanto, nós usamos convenções de nome para identificar o tipo de acesso do método/atributo.

-  (sem underline) - é *public* ou seja, pode ser acessado dentro e fora da classe;
-  (um underline) - é *protected* só pode ser usado dentro da classe que foi declarado ou de suas subclasses;
-  (dois underlines) - é *private* só pode ser usado na classe em que foi declarado.

```Python
class Foo:  
    def __init__(self):  
        self.public = "isso eh publico"  
        self._protected = "isso eh protegido"  

		self._metodo_protected()
  
    def metodo_public(self):  
        return "metodo publico"  
  
    def _metodo_protected(self):  
        return "_metodo_protected"
```

O método protected pode ser usado para fazer alguma coisa dentro da classe, no entanto, fora dela não é viável.

===OBS: Apesar de ser considerado privado e ocorrer um erro de atributo quando tento acessar métodos e atributos privados. Eu posso acessar utilizando a seguinte forma.===

```Python
print(f.Foo__metodo_private())
```

===OBS: name mangling é a "sintaxe" usada.

```
_NomeClasse_nome_attr_method
```

Assim como temos métodos separados por delimitadores de acesso, temos classes também, ou seja, podemos ter classes private, protected e public.

#### UML - Associação, Agregação e Composição.

Associação, Agregação e Composição são formas de objetos distintos se relacionarem. 

-  Associação

Como exemplo temos um escritor (objeto tipo 1) que precisa de uma caneta para escrever (objeto tipo 2). A relação entre eles é de associação, pois um existe independente do outro existir. 

Exemplo

```Python
class Escritor:  
    def __init__(self, nome) -> None:  
        self.nome = nome  
        self._ferramenta = None  
  
    @property  
    def ferramenta(self):  
        return self._ferramenta  
  
    @ferramenta.setter  
    def ferramenta(self, ferramenta):  
        self._ferramenta = ferramenta  
  
class FerramentaDeEscrever:  
    def __init__(self, nome):  
        self.nome = nome  
  
    def escrever(self):  
        return f'{self.nome} está escrevendo'  
# Relacionando escritor e caneta (ASSOCIAÇÃO)  
  
escritor = Escritor('Arthur Conan Doyle')  
caneta = FerramentaDeEscrever('Caneta')  
maquina = FerramentaDeEscrever('Máquina')  
  
# LINKANDO OS DOIS OBJETOS  
escritor.ferramenta = maquina  
  
print(caneta.escrever())  
print(maquina.escrever())  
print(escritor.ferramenta.escrever())
```

> *O escritor usa uma caneta*

-  Agregação

É uma relação mais forte comparada a associação, porém, ainda sim é fraca. Esse tipo de relacionamento entre objetos acontece quando os objetos existem independentemente, porém, para realizar algum tipo de atividade é necessário que ocorra a interação. Como exemplo temos um carro e uma roda. Ambos existem independente um do outro, no entanto, para que o carro consiga se locomover é necessário que possua rodas. 

> Normalmente a relação é de *um* para *um*, ou *um* para *outros*.

Em resumo, os objetos funcionam sem precisar um do outro. 

```Python
class CarrinhoDeCompras:  
    def __init__(self):  
        self._produtos = []  
  
    def total(self):  
        return sum([produto.preco for produto in self._produtos])  
  
    def listar_produtos(self):  
        print()  
        for produto in self._produtos:  
            print(produto.nome, produto.preco)  
        print()  
  
    # empacotando  
    def inserir_produto(self, *produtos):  
        # Três formas iguais de inserir o produto  
        # self._produtos.extend(produtos)        # self._produtos += produtos        for produto in produtos:  
            self._produtos.append(produto)  
  
  
class Produto:  
    def __init__(self, nome, preco):  
        self.nome = nome  
        self.preco = preco  
  
carrinho = CarrinhoDeCompras()  
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)  
  
carrinho.inserir_produto(p1, p2)  
  
carrinho.listar_produtos()
```

-  Composição

É a última forma de relacionamento que temos entre classes além da herança. Aqui as classes são fortemente ligadas. Sendo assim, quando um objeto do tipo "pai" para de existir todos os seus filhos também são deletados. Para enxergar esse tipo de relação, podemos tomar como exemplo um cliente com um endereço. 

```Python
class Cliente:  
    def __init__(self, nome):  
        self.nome = nome  
        self.enderecos = []  
  
    def inserirEndereco(self, rua, numero):  
        self.enderecos.append(Endereco(rua, numero))  
  
    def inserirEnderecoExterno(self, endereco):  
        self.enderecos.append(endereco)  
  
    def listarEnderecos(self):  
        for endereco in self.enderecos:  
            print(endereco.rua, endereco.numero)  
  
    def __del__(self):  
        print("Apagando: ", self.nome)  
  
  
class Endereco:  
    def __init__(self, rua, numero):  
        self.rua = rua  
        self.numero = numero  
  
    def __del__(self):  
        print("APAGANDO", self.rua, self.numero)  
  
  
cliente1 = Cliente("Maria")  
cliente1.inserirEndereco("Av Brasil", 54)  
cliente1.inserirEndereco("25 Março", 123)  
  
  
endereco = Endereco("Saudade", 11)  
cliente1.inserirEnderecoExterno(endereco)  
  
cliente1.listarEnderecos()  
  
del cliente1  
  
print("ENDDDDDDDDDDDD")
```

===OBS: O método __ del __ serve como se fosse um destrutor, ele é chamado pouco antes do objeto ser completamente destruído.===

-  Quando eu deleto o objeto usando del o Python imediatamente excluí o restante das partes que compõe o todo. 
-  Isso não aconteceria se o endereço fosse criado externamente. Após o cliente ser apagado eu ainda teria acesso ao endereço.

```
 Sobre UML

-  Classes com relação de associação: puramente um seta
-  Classes com relação de agregação: seta com um losângo sem preenchimento na outra extremidade.
-  Classes com relação de composição: seta com um losângo com preenchimento preto na outra extremidade
```

![[Pasted image 20250131164838.png]]







