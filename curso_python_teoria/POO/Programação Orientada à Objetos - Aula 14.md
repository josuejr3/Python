##### O que são dataclasses?

Dataclasses são usadas para melhorar a legibilidade do código. Chamamos também de syntax sugar, açucar sintático.

> Exemplo

```Python
from dataclasses import dataclass  
  
@dataclass  
class Pessoa:  
    nome: str  
    idade: int
```

Nesse caso, basta importar dataclass do pacote dataclasses e após isso definir a classe junto com seus tipos.

Esse procedimento já faz todo o conjunto com init, getters e setters, metodos magicos como eq, repr e entre outros.

> Caso eu queira, posso adicionar os metodos desejados

```Python
from dataclasses import dataclass  
  
@dataclass  
class Pessoa:  
    nome: str  
    sobrenome: str  
  
    @property  
    def nome_completo(self):  
        return f'{self.nome} {self.sobrenome}'  
  
    @nome_completo.setter  
    def nome_completo(self, valor):  
        nome, sobrenome = valor.split()  
        self.nome = nome  
        self.sobrenome = sobrenome  
  
if __name__ == '__main__':  
  
    p1 = Pessoa('Josue', 'Ferreira')  
    p2 = Pessoa('Joseph', 'Joestar')  
    print(p1)  
    print(p1 == p2)
```

---
##### Init e Post Init na dataclass

- Post init é executado após o init da classe

```Python
from dataclasses import dataclass  
  
@dataclass  
class Pessoa:  
    nome: str  
    sobrenome: str  
  
    def __post_init__(self):  
        self.nome_completo = f'{self.nome} {self.sobrenome}'
```

É simplesmente um método que é chamado logo que termina o init da dataclasse.

- Se não há init, não é possível ter um post-init. Seria necessario definir o proprio init.

- Para isso, basta colocar o callable do decorator como False

![[Pasted image 20250329155323.png]]

Basicamente isso faz com que o init seja removido da minha dataclass, fazendo com que seja necessário eu mesmo definir.

==O POST INIT SO PODE SER USADO SE O INIT QUE EU ESTIVER USANDO FOR O DA DATACLASS, DO CONTRARIO ELE NAO PODERA SER USADO==


- O decorator da dataclass me posibilita desativar varias configuracoes que forem desejadas, como por exemplo o metodo EQ.

Alguns exemplos de método são listados abaixo

- init - o inicializador da classe;
- frozen - congela a classe e impossibilita o set de atributos
- eq - 






































