from datetime import datetime, timedelta

class Producto:
    def __init__(self, nombre, precio, fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio:}, Vence: {self.fecha_vencimiento.date()}")

class ProductoAlimenticio(Producto):
    def aplicar_descuento(self):
        hoy = datetime.today()
        dias_para_vencer = (self.fecha_vencimiento - hoy).days

        if dias_para_vencer <= 3:
            descuento = self.precio * 0.30
        elif dias_para_vencer <= 7:
            descuento = self.precio * 0.15
        else:
            descuento = 0

        self.precio -= descuento
        print(f"Descuento aplicado al producto : ${descuento}")

class ProductoElectronico(Producto):
    def aplicar_descuento(self):
        hoy = datetime.today()
        dias_para_vencer = (self.fecha_vencimiento - hoy).days

        if dias_para_vencer <= 30:
            descuento = self.precio * 0.10
            self.precio -= descuento
            print(f"Descuento aplicado al producto: ${descuento}")
        else:
            print("El descuento no aplica para el producto")


if __name__ == "__main__":
    prod1 = ProductoAlimenticio("Jugo", 1000.0, "2025-06-06")
    prod2 = ProductoElectronico("Auriculares", 2500.00, "2025-07-01")

    print("Antes de los descuentos:")
    prod1.mostrar_info()
    prod2.mostrar_info()

    print("Aplicando los descuentos")
    prod1.aplicar_descuento()
    prod2.aplicar_descuento()

    print("Despues de los descuentos:")
    prod1.mostrar_info()
    prod2.mostrar_info()
