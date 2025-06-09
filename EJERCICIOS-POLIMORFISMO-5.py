class Pago:
    def procesarPago(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

class TarjetaCredito(Pago):
    def __init__(self, monto, nt, titular):
        self.monto = monto
        self.nt = nt
        self.titular = titular

    def procesarPago(self):
        print("Procesando pago con tarjeta")
        print(f"Tarjeta: {self.nt}, Monto a pagar: {self.monto}")
        print("Pago aprobado.")


class PayPal(Pago):
    def __init__(self, monto, correo_paypal):
        self.monto = monto
        self.correo_paypal = correo_paypal

    def procesarPago(self):
        print("Procesando pago con PayPal")
        print(f"Cuenta: {self.correo_paypal}, Monto a pagar: {self.monto}")
        print("Pago aprobado.")


def main():
    pagos = [
        TarjetaCredito(120.50, "1234567890123456", "Maria"),
        PayPal(75.00, "maria@gmail.com"),
        TarjetaCredito(100.75, "0987654321098765", "Pablo"),
        PayPal(90.00, "pablo@gmail.com")
        ]

    for pago in pagos:
        print(f"Realizando pago con {pago.__class__.__name__}: {pago.procesarPago()}")

if __name__ == "__main__":
    main()
