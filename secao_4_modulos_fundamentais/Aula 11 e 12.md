
#### <span style="color:rgb(4, 255, 0)">Utilizando os.listdir</span> 

O módulo os.listdir é ideal para fazer a navegação ente diretórios e pastas.

```Python
# a barra é adicionada, pois estou vindo da raiz  
caminho = os.path.join("\\Josue", "Cursos", "Python", "python", "secao_4_modulos_fundamentais")  
  
for item in os.listdir(caminho):  
    print(item)
```

Essa função retorna tudo que está contido dentro do diretório

```cmd
aula1
aula11.py
aula2.py
aula3.py
aula4.py
aula5.py
aula6.py
aula7.py
aula8.py
aula9_e_10.py
pasta_teste_listdir
```

#### <span style="color:rgb(4, 255, 0)">os.walk</span>

O problema de usar listdir é que ele faz apenas um mapeamento de primeiro nível, ou seja, pastas e arquivos que estão contidos em outros diretórios não são encontrados. Nesse caso, podemos usar a função walk que faz uma recursividade de pastas e retorna tuplas e listas com pastas e arquivos mais internos.

```Python
# a barra é adicionada, pois estou vindo da raiz  
caminho = os.path.join("\\Josue", "Cursos", "Python", "python", "secao_4_modulos_fundamentais")  
  
for item in os.walk(caminho):  
    print(item[0])
```

Lembrando que o resultado de um os.walk é uma tupla sempre com três elementos.

-  O primeiro elemento da tupla é o diretório atual (root ou raiz);
-  O segundo elemento é uma lista de subdiretórios (dirs);
-  Já o terceiro é uma lista de arquivos do diretório atual.

Além disso, a biblioteca os.path me permite verificar se um diretório que eu estou tentando acessar é realmente um diretório valido com a função "os.path.isdir". Outra coisa importante é o uso da função "unlink()" ela apaga todos os arquivos dentro de uma pasta e eles <mark style="background: #FF5582A6;">NÃO PODEM SER RECUPERADOS.
</mark>

```Python
counter = count()  
for root, dirs, files in os.walk(caminho):  
    the_counter = next(counter)  
    print("Pasta atual: ", root, counter)  
  
    for dir_ in dirs:  
        print("  ", the_counter, "Dir: ", dir_)  
  
    for file_ in files:  
        caminho_completo_arquivo = os.path.join(root, file_)  
        print("  ", the_counter, "File: ", caminho_completo_arquivo)
```
