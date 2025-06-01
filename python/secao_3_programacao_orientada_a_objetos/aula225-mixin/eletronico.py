from log import LogPrintMixin, LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()
        msg = f"{self._nome} está ligado"
        if self._ligado:
            self.log_sucess(msg)


    def desligar(self):
        super().desligar()
        msg = f"{self._nome} está desligado"
        if not self._ligado:
            self.log_error(msg)





