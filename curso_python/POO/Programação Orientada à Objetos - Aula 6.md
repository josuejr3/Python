#### Criando Exceptions em Python Orientado à Objetos (exceções)

Exceções são criadas para que possam informar ao programador se ocorreu algum erro. 

-  Um detalhe importante é que quando for definirmos nossa classe de erros, por convenção e padrão sempre colocamos o nome "Error" no final. 

-  O básico para criar exceções consiste em criar uma classe de erro e herdar de "Exception".

```Python
class MeuError(Exception):
	...
```

No link abaixo, você consegue ver todas as exceções que o Python disponibiliza para serem usadas e que já estão prontas. 

```txt
https://docs.python.org/3/library/exceptions.html
```

Formas de informar sobre uma exceção

-  raise - Em Python utilizamos essa como uma forma de levantar uma exceção;
-  throw - Em outras linguagens, usamos essa para lançar exceções.

> Exemplo de um erro

```Python
class MeuError(Exception):  
    ...  
def levantar():  
    raise  MeuError("A mensagem do meu erro")  
  
try:  
    levantar()  
except MeuError as e:  
    print(e)
```

No caso acima, estamos tratando o erro utilizado o bloco "Try-Except", porque o erro "MeuError" já possui uma mensagem, porém com o bloco de try-except podemos modificar a mensagem que aparece.

-  Para relançar uma exceção podemos usar apenas a palavra chave *raise* sem necessitar informar qual é a exceção.

Isso possibilita ainda fazer alguma coisa no except, como por exemplo printar algo ou salvar num log e também continua relançando a exceção.

-  Podemos relançar uma exceção dentro de uma outra exceção também da seguinte forma. 

```Python
class MeuError(Exception):  
    ...  
class OutroError(Exception):  
    ...    
def levantar():  
    exception_ = MeuError("a", 'b', 'c')  
    raise exception_  
  
try:  
    #1/0  
    levantar()  
except (MeuError, ZeroDivisionError) as e:  
    print(e.__class__.__name__)  
    print(e)  
    print()  
    exception_2 = OutroError('Vou lançar de novo')  
    raise exception_2 from e
```

Uma funcionalidade recente do Python 3.11 é a adição de notas em nossas exceções. Para isso, basta eu usar o método especial ".add_note(nota)". Além disso, eu posso obter a listas de notas que uma determinada exceção contém usando ". __ notes__"


























