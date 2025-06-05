from datetime import datetime

class Pago:
    def __init__(self, monto, fecha=None):
        self.monto = monto
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mostrar_detalles(self):
        print(f"Monto: ${self.monto}, Fecha: {self.fecha}")

class PagoTarjeta(Pago):
    def __init__(self, monto, numero_tarjeta, titular, fecha=None):
        super().__init__(monto, fecha)
        self.numero_tarjeta = numero_tarjeta
        self.titular = titular

    def procesar_pago(self):
        print("Procesando pago con tarjeta")
        print(f"Tarjeta: {self.numero_tarjeta}")
        print("Pago aprobado.")

    def generar_recibo(self):
        print("---RECIBO DE PAGO CON TARJETA---")
        self.mostrar_detalles()
        print(f"Titular: {self.titular}")
        print(f"Tarjeta: {self.numero_tarjeta}")
        print("--------------------------------")

class PagoPayPal(Pago):
    def __init__(self, monto, correo_paypal, fecha=None):
        super().__init__(monto, fecha)
        self.correo_paypal = correo_paypal

    def procesar_pago(self):
        print("Procesando pago con PayPal")
        print(f"Cuenta: {self.correo_paypal}")
        print("Pago aprobado.")

    def generar_recibo(self):
        print("---RECIBO DE PAGO CON PAYPAL---")
        self.mostrar_detalles()
        print(f"Cuenta PayPal: {self.correo_paypal}")
        print("-------------------------------")

if __name__ == "__main__":
    pago1 = PagoTarjeta(120.50, "1234567890123456", "Maria")
    pago2 = PagoPayPal(75.00, "maria@gmail.com")
    print()
    pago1.procesar_pago()
    pago1.generar_recibo()
    print()
    pago2.procesar_pago()
    pago2.generar_recibo()
