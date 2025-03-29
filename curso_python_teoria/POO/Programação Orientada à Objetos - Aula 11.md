## Metaclasses

Metaclasses são as classes das classes e estão acima da classe "object". 

> Em Python tudo é objeto, incluindo as próprias classes. 

Lembrando que em Python, toda as classes herdam por herança da classe object.

```Python
class Foo(object):
	...

f = Foo()
print(isinstance(f, Foo))

# True -> f é do tipo Foo
```

Já se fizermos 

```Python
print(type(Foo))

# o tipo de Foo é da classe "type"
```

type sempre está acima de classes e acima de objects.

---

O fluxo da criação de classes se dá da seguinte maneira. 

1 - __ new __ da metaclasse é chamado e cria uma nova classe; (retorna a classe)
2 - __ call __ da metaclasse é chamado com os argumentos e chama:
	a - __ new __ da classe com os argumentos (cria a instância);
	b - __ init __ da classe com os argumentos.
3 - __ call __ da metaclasse termina a execução.

Alguns métodos importantes das metaclasses são:

Assinaturas de metaclasses
-  __ new __ (mcs, name, bases, dct) -> cria a classe;
	-  Recebe a própria metaclasse;
	-  O nome da classe;
	-  As heranças da classe;
	-  E um dict que são os atributos
-  __ call __ (cls, * args, ** kwargs)     -> cria e inicializa a instância.
	-  Recebe a classe propriamente dita;
	-  args e kwargs que queira usar.


