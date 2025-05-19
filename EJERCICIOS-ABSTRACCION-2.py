from abc import ABC, abstractmethod
import math

class Pago(ABC):
    @abstractmethod
    def procesar_pago(self):
        pass

class TarjetaCredito(Pago):
    def procesar_pago(self):
        return "El pago con tarjeta de credito ha sido efectuado."


class PayPal(Pago):
    def procesar_pago(self):
        return "El pago con PayPal se ha realizado con éxito."

