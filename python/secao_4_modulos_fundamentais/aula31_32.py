# Compactando e Descompactando arquivos zip
import shutil
from pathlib import Path
from zipfile import ZipFile
import os

CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'arquivos_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'arquivos_compactados.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'arquivos_decompactados.zip'

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


with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_RAIZ):