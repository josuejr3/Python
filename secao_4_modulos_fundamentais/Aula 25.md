
#### <span style="color:rgb(4, 255, 0)">Módulo Secrets</span>

O módulo secrets é semelhante ao módulo random, porém mais seguro. Entretanto, há também o system random que usa a aleatoriedade que já vem com o SO e é mais seguro que o random.

```Python
import secrets  
random = secrets.SystemRandom()  
  
# print(secrets.randbelow(100))  
# print(secrets.choice((1, 2, 3)))  
  
  
# Importamos o secrets e igualamos a variavel "random" a classe SystemRandom()  
  
# gerando senhas aleatórias com caracteres  
  
# 1 - importar modulo string  
import string as s  
from secrets import SystemRandom as Sr  
  
# caracteres que posso usar para gerar senhas  
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))  
  
  
r_range = random.randrange(10, 20)  
r_int = random.randint(10, 20)  
r_float = random.uniform(10, 20)  
  
lista_de_items = ["A", "B", "C", "D", "E", "F"]  
random.shuffle(lista_de_items)  
  
# random.seed(time.time())  
# print(time.time())  
  
# aleatoriedade baseada em um numero 0  
# ignorado  
random.seed(0)  
  
print(r_range, r_float, r_int)  
print(lista_de_items)  
  
novos_nomes = random.sample(lista_de_items, k=3)  
print(novos_nomes)  
  
novos_nomes = random.choices(lista_de_items, k=3)  
print(novos_nomes)  
  
selecionado = random.choice(novos_nomes)  
print(selecionado)
```






