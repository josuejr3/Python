
#### <span style="color:rgb(4, 255, 0)">Compactando e Descompactando arquivos</span>

Para realizar procedimentos de compactação de descompactação de arquivos, nós utilizamos a biblioteca zipfile que já vem com o Python. Abaixo temos um exemplo da criação de diretórios e arquivos para que eles possam ser compactados e também descompactados.

```Python
# Compactando e Descompactando arquivos zip  
import shutil  
from pathlib import Path  
from zipfile import ZipFile  
import os  
  
CAMINHO_RAIZ = Path(__file__).parent  
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'arquivos_zip'  
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'arquivos_compactado.zip'  
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'arquivos_decompactado.zip'  
  
# Apenas para Excluir PASTAS  
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)  
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)  
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)  
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)  
  
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)  
  
def criar_arquivos(qtd: int, zip_dir: Path):  
    for i in range(qtd):  
        texto = 'arquivo_%s' % i  
        with open(zip_dir / f'{texto}.txt', 'w') as file:  
            file.write(texto)  
  
criar_arquivos(3, CAMINHO_ZIP_DIR)
```

-  Uma observação é que para que não vá todos os diretórios "pais" até a pasta que estamos tentando compactar dentro do arquivo zip, devemos passar o argumento de nome na função de zip utilizada.

```Python
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:  
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):  
        for file in files:  
            zip.write(os.path.join(root, file), file)
```

```Python
# Criando zip e adicionando arquivos (compactando)  
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:  
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):  
        for file in files:  
            zip.write(os.path.join(root, file), file)  
  
# Lendo arquivos de um zip  
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:  
    for arquivo in zip.namelist():  
        print(arquivo)  
  
# Extraindo e desempacotando arquivos zip  
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:  
    zip.extractall(CAMINHO_DESCOMPACTADO)
```










