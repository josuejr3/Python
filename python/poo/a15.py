# with open('aula149.txt', 'w') as file:
#     ...


class MyOpen:

    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        # abrindo o arquivo
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf-8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)
        #
        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        #return True # tratei a exceção de alguma forma

        raise ConnectionError('Nao deu pra conectar')


with MyOpen('aula149.txt', 'w') as alguma_coisa:
    alguma_coisa.write('LINHA1', 123)
    print('WITH', alguma_coisa)

    from contextlib import contextmanager


