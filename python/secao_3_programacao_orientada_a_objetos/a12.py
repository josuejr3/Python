# Polimorfismo e Assinatura de Métodos

from abc import ABC, abstractmethod

class Notificacao(ABC):

    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoSMS(Notificacao):

    def enviar(self) -> bool:
        print("SMS: enviando - ", self.msg)
        return True

class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print("Email: enviando - ", self.msg)
        return False

def notificar(notificacao: Notificacao) -> None:
    notificao_enviada = notificacao.enviar()
    print("Notificacao enviada" if notificao_enviada else "Notificacao NAO enviada")

notificacao_email = NotificacaoEmail("testando email")
notificar(notificacao_email)
notificacao_sms = NotificacaoSMS("testando sms")
notificar(notificacao_sms)

