# Abstração

from pathlib import Path

from poo.a6 import endereco

# define o diretorio do arquivo log.txt
LOG_FILE = Path(__file__).parent / 'log.txt'

# A classe log funciona como uma classe abstrata

class Log:
    # assinatura do metodo
    def _log(self, msg):
        # quando esse erro aparece significa que voce esta usando uma classe
        # que nao deveria ser utilizada
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_sucess(self, msg):
        return self._log(f"Success: {msg}")

# adicionar coisas a classe
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        print("Salvando no log: ", msg_formatada)
        with open(LOG_FILE, 'a') as f:
            f.write(msg_formatada)
            f.write("\n")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")

# Estudar
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_sucess("s")
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_sucess("Que legal")


