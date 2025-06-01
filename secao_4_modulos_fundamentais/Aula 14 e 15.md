
#### <span style="color:rgb(4, 255, 0)">Gerenciamento de arquivos</span>

Utilizando a biblioteca do sistema operacional (os) nós podemos gerenciar nossos arquivos de forma a fazer as seguintes tarefas

-  Mover/Renomear - shutil.move
-  Mover/Renomear - os.rename
-  Copiar - shutil.copy
-  Apagar - os.unlink
-  Apagar diretório recursivamente - shutil.rmtree

Lembrando que ao realizar procedimentos de exclusão, os arquivos que forem removidos eles não vão para a lixeira. Dessa forma, não é possível recuperá-los.

```Python
# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copyAdd commentMore actions
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminnho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminnho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)
```

#### <span style="color:rgb(4, 255, 0)">Movendo, copiando, renomeado e apagando arquivos com shutil e os</span>

Diferente do que vimos acima, poderíamos ter copiado uma pasta passando a raiz para uma função, como por exemplo.

```Python
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
```

Todas as pastas são copiadas para a nova. Esse função de tree é usada também para quando queremos apagar pastas que contém subpastas que devem ser apagadas também.

```Python
shutil.rmtree(NOVA_PASTA)
```

