#### Referências Bibliográficas

-  PHP Programando com Orientação a Objetos;
-  Python Fluente;
-  Padrões de Projeto Soluções Reutilizáveis;
-  Patters of Enterprise Application Architechture.

##### Classes

Classes são moldes para criar novos objetos. Essas classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos. Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações. Por convenção, usamos *PascalCase* para nomes de classes. Para ter uma classe bem definida, ela deve possuir métodos e atributos.

-  Atributos: são propriedades ou características de uma classe, como por exemplo, na classe pessoa temos: nome, idade, altura e o peso;
-  Métodos são funções que representam ações de uma classe, como por exemplo, informar nome, alterar o peso e entre outros.

===Obs: é importante saber que como os atributos não são funções, não há necessidade de executar com ( ).===

```Python
class Pessoa:  
    ...  
  
p1 = Pessoa()  
p1.nome = "Luiz"  
p1.sobrenome = "Otávio"  

p2 = Pessoa()
p2.nome = "Maria"
p2.sobrenome = "Joana"
  
print(p1.nome)  
print(p1.sobrenome)
print(p2.nome)  
print(p2.sobrenome)
```

Há uma maneira mais fácil de inicializar os atributos dos objetos criados, para isso usamos *_ _ init  _ _* e o *self*

-  O método init é uma das primeiras coisas a serem executadas quando instanciamos objetos e também é responsável por inicializar todos os atributos do nosso objeto;

-  O self referencia ao objeto que está sendo criado, é semelhante ao ponteiro this que estudamos em C++;

-  Todo método que for tratar da instância, o primeiro parâmetro do init deve ser o self. Porém ao instanciar não há necessidade de passar o parâmetro, pois o Python faz isso automaticamente.

```Python
class Pessoa:  
    def __init__(self, nome, sobrenome):  
		self.nome = nome
		self.sobrenome = sobrenome

p1 = Pessoa("Luiz", "Otavio")
```

##### Métodos em instâncias de classes Python

Um método é um comportamento e é sempre uma função que está contida dentro da classe e sempre que a função for para instâncias nós usamos a palavra chave self. 

-  Sempre que o objeto tiver que ter o seu próprio atributo vou precisar colocar o atributo no init como vimos anteriormente. 

===Obs: método init sempre retorna None===

```Python
class Car:  
    def __init__(self, name_car="Sem modelo"):  
        self.name = name_car  
  
    def acelerar(self):  
        print(f"{self.name} está acelerando...")  

fusca = Car("Fusca")  
print(fusca.name)  
  
celta = Car("Celta")  
print(celta.name)  
  
fusca.acelerar()  
celta.acelerar()
```

Até o momento a classe não conhece dados, ela apenas fornece uma instância. Uma forma de chamar um método é passando a instância para ele.

```Python
Car.acelerar(fusca)
# dentro do () temos o self, que no caso é  instância, o fusca.
```

Você está informando que um carro irá acelerar e ao mesmo tempo indicado qual dos carros é que será acelerado, se é o celta ou o fusca.

##### Escopo de classes e métodos da classe

Assim como vimos anteriormente, as classes possuem um escopo próprio. Segue abaixo um exemplo. 

```Python
class Animal:
	nome = "Leão"

print(nome)
```

Ocorreria um erro, pois estão em escopos diferentes. O que eu poderia fazer para corrigir isso é pegar o nome de dentro da própria classe

```Python
print(Animal.nome)
```

Podemos fazer com que códigos sejam executados assim que o objeto e criado, basta que eles estejam dentro do escopo do método init. 

```Python
class Animal:  
    # name = "Leão"  
    def __init__(self, name):  
        self.nome = name  
        variavel = "valor"  
  
        print(variavel)
```

No exemplo acima, quando o objeto é criado, o print de "variavel" é visto na tela. Além disso, as variáveis definidas dentro do método init são exclusivas dele, ou seja, não podem ser acessadas por outros métodos.

-  Atributos de classe: são definidos no escopo geral da classe;
-  Atributos de instância normalmente são inicializados no método init;
	Dessa forma, se um atributo possui o "self" ele poderá ser chamado em qualquer local da classe.

##### Mantendo estados dentro da classe

A questão de manter ou não um estado de um objeto pode ser encarada como getters e setters que estudaremos mais para frente. Mas em resumo, podemos modificar um atributo ou mantê-lo através de métodos específicos. Segue abaixo um exemplo de aplicação de mudanças de atributos em um câmera fotográfica.

```Python
class Camera:  
    def __init__(self, name, filming=False):  
        self.name = name  
        self.filming = filming  
  
    def film(self):  
        if self.filming:  
            print(f"{self.name} JÁ está filmando...")  
            return  
  
        print(f"{self.name} está filmando...")  
        self.filming = True  
  
    def stop_film(self):  
        if not self.filming:  
            print(f"{self.name} NÃO está filmando...")  
            return  
        print(f"{self.name} está parando de filmar...")  
        self.filming = False  
  
    def click(self):  
        if self.filming:  
            print(f"{self.name} não pode fotografar filmando")  
            return  
        print(f"{self.name} está fotografando...")  

c1 = Camera("Canon")  
c2 = Camera("Sony")  
  
c1.film()  
c1.film()  
c1.click()  
c1.stop_film()  
c1.click()
```

E o mais importante é que as modificações que fizemos são exclusivas do objeto câmera "Canon", já que os atributos que são alterados são os dessa câmera em específico. 

---

Como vimos anteriormente, quando criamos uma variável dentro do escopo da classe sem estar definido em nenhuma função ou método especial o atributo é chamado de "atributo de classe". 

Segue abaixo um exemplo de como usar atributos de classe e como eles podem ser chamados. 

```Python
class Pessoa:  
  
    ANO_ATUAL = 2022  
    def __init__(self, nome, idade):  
        self.nome = nome  
        self.idade = idade  
  
    def get_ano_nascimento(self):  
        return Pessoa.ANO_ATUAL - self.idade  

p1 = Pessoa("João", 35)  
p2 = Pessoa("Maria", 12)  
print(Pessoa.ANO_ATUAL)  
  
# Isso modifica todas as instancias, já que elas dependem dos atributos da classe base  
# Pessoa.ANO_ATUAL = 1  
print(p1.get_ano_nascimento())  
print(p2.get_ano_nascimento())
```

É importante saber que quando temos um atributo de classe e modificamos ele todos os objetos que dependem daquele atributo vão ser alterados. Além disso, podemos chamar os atributos de classe de duas formas. 

-  Usando o self, porém, se tivermos um atributo de objeto com o mesmo nome pode gerar um conflito. 
-  Usando o nome da classe
```Python
Pessoa.ANO_ATUAL
```

#### Métodos especiais __ dict __ e __ vars __ para atributos de instâncias.

Ambos os métodos vars e dict funcionam como se fossem dicionários nas instâncias da minha classe.

-  Os atributos """" funcionam """' como se fossem chaves de um dicionário. 

Segue abaixo o exemplo. 

```Python
p1 = Pessoa("João", 35)
print(p1.__dict__)
print(vars(p1))
```

Como a classe Pessoa possui dois atributos, nome e idade a saída do print será

```Python
{"nome": "João, "idade" : 35}
```

===Obs: o dict não é somente leitura. Sendo assim, podemos criar novos atributos a partir dele.

```Python
p1.__dict__["outra"] = "coisa"
```

Dessa maneira, o objeto pessoa terá o atributo outra com o valor coisa. Além disso, da mesma maneira que podemos adicionar outras chaves/atributos, podemos também remover usando a palavra chave del que estudamos em dicionários. 

```Python
del p1.__dict__["outra"]
```

Sabendo disso, podemos usar o formato em "dicionário" para que seja salvo em um arquivo JSON para que em seguida possamos criar os objetos com as mesmas características. 

-  Exemplo criando um objeto a partir de um dicionário

```Python
dados = {"idade": 35, "outra": "coisa"}  
p1 = Pessoa(**dados)  # crio a chave = o valor
```

É feito o desempacotamento do meu dicionário dentro do objeto.

===Obs: a diferença entre o vars e o dict é que o vars é considerado mais seguro por ser de mais alto nível em relação ao dict. 

- Tipos de convenção:
	-  PascalCase - Palavras iniciadas sempre com letra maiúscula e não há nenhum separador. Normalmente usada para classes em Python.

	-  camelCase - A diferença dessa para a PascalCase é que nesse caso a primeira letra é sempre minúscula e o restante do começo de palavras é maiúsculo. (Não é utilizada em Python).

	-  snake_case - Esse tipo é o mais utilizado em Python e se caracteriza por ter um separador, que é o underline "\_" e todas os caracteres são minúsculos. 

##### Métodos de Classe (@classmethod) + factories methods (métodos de fábrica)

Os métodos de classe são métodos associados diretamente a classe, ou seja, não há necessidade de instanciar um objeto para usar o método. 

Para criar métodos de classe nós precisamos utilizar decoradores. Na realidade o decorador especial "@classmethod"

```Python
class Pessoa:
    ano = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    # Método normal
    def metodo_de_classe(self):
        print("Hey")

    # Método de classe
    @classmethod
    def metodo_de_classe(cls):
        print("Hey")
```

O método deve receber a classe em si *cls.*

-  Além de métodos de classe posso fazer também os métodos de fabrica, segue a sintaxe abaixo. 

```Python
# MÉTODOS DE FABRICA
    # Métodos de Fábrica

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
```

Dessa maneira, o código fica mais genérico, porém, eu continuo podendo criar uma pessoa a partir da classe, sem ter que chamar o construtor diretamente. 

```Python
pessoa2 = Pessoa.criar_com_50_anos("Jose")
```

```Python
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50_anos("Ze")
print(p2.nome)
```

===Obs IMPORTANTE: como os métodos se referem a classe em si (o molde dos objetos) ela não possui acesso aos atributos específicos de cada objeto, ou seja, o self===.

===Em resumo, métodos de classe nós usamos o decorador especial. Já os métodos fábrica são relacionados com a própria classe e normalmente retornam um objeto da classe.===

##### @staticmethod (métodos estáticos) em Python

Os métodos estáticos não possuem acesso nem a classe e nem as instâncias. 

```Python
class Classe:
	@staticmethod
	def funcao_que_esta_na_classe(*args, **kwargs):
		print("OI", args, kwargs)
```

É igual a uma função normal. A diferença é que o método está protegido com o namespace da classe.



















