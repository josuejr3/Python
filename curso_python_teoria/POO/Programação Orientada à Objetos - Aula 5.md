#### Polimorfismo e assinatura de métodos

Polimorfismo é um princípio que permite que classes derivadas de uma superclasse em comum, tenham métodos com a mesma assinatura, porém, implementações/comportamentos diferentes.

-  Assinatura do método - mesmo nome e quantidade de parâmetros, o retorno não faz parte da assinatura. Segue abaixo um exemplo simples.

```Python
class Animal:
	@abstractmethod
	def mover(): ...

class Peixe(Animal):
	def mover():
		print("Nadando")

class Passaro(Animal):
	def mover():
		print("Voando")
```

> Assinatura de método: Nome, parâmetros e retornos iguais

**SO'L'ID** - *Objetos de uma superclasse devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação*

Obs importantes:

-  Python não suporta sobrecarga de métodos (overload);
-  Python suporta a sobreposição de métodos (override).

```Python
from abc import ABC, abstractmethod  
  
class Notificacao(ABC):  
  
    def __init__(self, msg) -> None:  
        self.msg = msg  
  
    @abstractmethod  
    def enviar(self) -> bool:  
        ...  
  
class NotificacaoSMS(Notificacao):  
  
    def enviar(self) -> bool:  
        print("SMS: enviando - ", self.msg)  
  
class NotificacaoEmail(Notificacao):  
  
    def enviar(self) -> bool:  
        print("Email: enviando - ", self.msg)  
  
n = NotificacaoSMS("testando notificacao")  
n.enviar()
```

Pelo princípio de Liskov, onde nós usamos uma superclasse, podemos substituir para usar também uma subclasse.

Sendo assim, no código acima, onde nós usamos uma notificação podemos trocar e usar uma notificação de sms, ou uma notificação de e-mail. Por esse motivo e pelo princípio de Liskov eu devo poder usar qualquer filho da classe mãe no lugar dela sem que o código quebre. 

Ok, mas onde realmente entra o polimorfismo? 

O polimorfismo pode ser enxergado quando definimos um tipo de "entrada", veja o exemplo abaixo.

```Python
def notificar(notificacao: Notificacao) -> None:  
    notificao_enviada = notificacao.enviar()  
    print("Notificacao enviada" if notificao_enviada else "Notificacao nao enviada")
```

No exemplo, definimos a classe notificar que serve para qualquer tipo de notificação, (ela recebe um objeto do tipo Notificação) e pelo princípio de Liskov, podemos substituir por uma classe filha. Sendo assim, podemos fazer o mostra o código a seguir.

```Python
nsms = NotificacaoSMS()
nemail = NotificacaoEmail()

notificar(nsms)
notificar(nemail)
```

Ou seja, a função notificar vai receber um tipo de notificação, seja ela e-mail ou sms e vai executar de acordo com a particularidade de cada um dos subtipos de notificação. 

Segue abaixo o código completo

```Python
from abc import ABC, abstractmethod  
  
class Notificacao(ABC):  
  
    def __init__(self, msg) -> None:  
        self.msg = msg  
  
    @abstractmethod  
    def enviar(self) -> bool:  
        ...  
  
class NotificacaoSMS(Notificacao):  
  
    def enviar(self) -> bool:  
        print("SMS: enviando - ", self.msg)  
        return True  
  
class NotificacaoEmail(Notificacao):  
  
    def enviar(self) -> bool:  
        print("Email: enviando - ", self.msg)  
        return False  
  
def notificar(notificacao: Notificacao) -> None:  
    notificao_enviada = notificacao.enviar()  
    print("Notificacao enviada" if notificao_enviada else "Notificacao NAO enviada")  
  
notificacao_email = NotificacaoEmail("testando email")  
notificar(notificacao_email)  
notificacao_sms = NotificacaoSMS("testando sms")  
notificar(notificacao_sms)
```