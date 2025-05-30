## Método especial call e classes decoradoras

O método __ call __ é algo que pode ser executado com parênteses. Em classes normais, call faz a instância de uma classe "callable".

De forma simples, transformamos a instância em uma instância que pode receber alguma coisa.

```Python
class CallMe:  
    def __init__(self, phone):  
        self.phone = phone  
  
    def __call__(self, nome):  
        print('Chamando', nome)  
  
  
call1 = CallMe('123-456-7890')  
# Imagine que você queira chamar a instância da classe, ou seja  
# call1() 

### AQUI A INSTÂNCIA É FUNCIONA COMO CALLABLE
call1('Luiz')  
print(call1.phone)
```
#### Classes decoradoras (decorator classes)

Classes decoradoras são classes que decoram objetos, por padrão as classes decoradoras também tem sua primeira letra maiúscula.

```Python
class Multiplicar:  
    # a funcao usada, no caso a soma  
    def __init__(self, func):  
        self.func = func  
        #print('INIT', func)  
        self._multiplicador = 10  
  
    # args e kwargs sao os argumentos da funcao soma  
    def __call__(self, *args, **kwargs):  
        print(args, kwargs)  
        resultado = self.func(*args, **kwargs) * self._multiplicador  
        return resultado  
  
@Multiplicar  
def soma(x, y):  
    return x + y  
  
dois_mais_dois = soma(2, 4)  
print(dois_mais_dois)
```

===Obs: é importante usar o decorador "@" sem o "()", pois caso coloquemos os parênteses será feita a execução da classe.===

