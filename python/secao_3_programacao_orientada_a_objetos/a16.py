from contextlib import contextmanager

@contextmanager

def my_open(caminho_arquivo, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding="utf8")
        yield arquivo
    # except Exception as e:
    #     print('Ocorreu uma exceção', e)
    finally:
        print("Fechando arquivo")
        arquivo.close()
    # generator


with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n', 3)
    arquivo.write('Linha3\n')
    print('WITH', arquivo)