# Manipulação de PDF

from pathlib import Path
from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PDFS_ORIGINAIS = PASTA_RAIZ / "aula51_pdfs"
PASTA_NOVA = PDFS_ORIGINAIS / "arquivos_novos"

RELATORIO_BACEN = PDFS_ORIGINAIS / "pdf1.pdf"

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# Printa o número de paginas
print(len(reader.pages))

# for page in reader.pages:
#     print(page)

page0 = reader.pages[0]  # Página 1
print(page0.extract_text())  # extrai um texto
# print(type(page0.images))
# "printa as imagens" em uma página

imagem0 = page0.images[0]

# wb é writebytes
with open(PASTA_NOVA / imagem0.name, 'wb') as i:
    i.write(imagem0.data)

