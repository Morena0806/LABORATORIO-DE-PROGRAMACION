from abc import ABC, abstractmethod
import math

class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass

class Email(Notificacion):
    def enviar(self):
        return "El e-mail se ha enviado correctamente."

class SMS(Notificacion):
    def enviar(self):
        return "El mensaje SMS se ha enviado correctamente."
