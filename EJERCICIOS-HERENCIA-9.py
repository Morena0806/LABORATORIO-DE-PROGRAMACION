class Tienda:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.inventario = []
        self.ventas = 0

    def mostrar_informacion(self):
        print(f"Tienda: {self.nombre}, Ubicación: {self.ubicacion}")
        print(f"Productos en inventario: {len(self.inventario)}")
        print(f"Total de ventas: ${self.ventas}")

    def agregar_producto(self, nombre, precio, cantidad):
        self.inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"Producto agregado: {nombre},  ${precio}, hay {cantidad} unidades")

    def eliminar_producto(self, nombre):
        self.inventario = [prod for prod in self.inventario if prod["nombre"] != nombre]
        print(f"Producto eliminado: {nombre}")

class TiendaRopa(Tienda):
    def calcular_ventas(self):
        total = 0
        for producto in self.inventario:
            if "vendido" in producto:
                vendido = producto["precio"] * producto["vendido"]
            else:
                vendido = 0
            total += vendido
        self.ventas = total
        print(f"Ventas totales en la tienda de ropa: ${self.ventas}")

    def registrar_venta(self, nombre_producto, cantidad_vendida):
        for producto in self.inventario:
            if producto["nombre"] == nombre_producto and producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                if "vendido" not in producto:
                    producto["vendido"] = 0
                producto["vendido"] += cantidad_vendida
                print(f"Venta registrada: {cantidad_vendida} unidades de {nombre_producto}")
                return
        print(f"No se registró la venta")

class TiendaElectronica(Tienda):
    def calcular_ventas(self):
        total = 0
        for producto in self.inventario:
            if "vendido" in producto:
                vendido = producto["precio"] * producto["vendido"]
            else:
                vendido = 0
            total += vendido
        self.ventas = total
        print(f"Ventas totales en la tienda electrónica: ${self.ventas}")

    def registrar_venta(self, nombre_producto, cantidad_vendida):
        for producto in self.inventario:
            if producto["nombre"] == nombre_producto and producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                if "vendido" not in producto:
                    producto["vendido"] = 0
                producto["vendido"] += cantidad_vendida
                print(f"Venta registrada: {cantidad_vendida} unidades de {nombre_producto}")
                return
        print(f"No se registró la venta")


if __name__ == "__main__":
    ropa = TiendaRopa("Cheeky", "Caballito")
    electronica = TiendaElectronica("ElectroMundo", "Av. Boedo 123")

    ropa.agregar_producto("Remera", 25.0, 50)
    ropa.agregar_producto("Jean", 40.0, 30)
    electronica.agregar_producto("Telefono", 300.0, 20)
    electronica.agregar_producto("Auriculares", 50.0, 40)
    print()
    ropa.registrar_venta("Remera", 5)
    electronica.registrar_venta("Telefono", 2)
    print()
    ropa.calcular_ventas()
    electronica.calcular_ventas()
    print()
    print("Información de las tiendas:")
    ropa.mostrar_informacion()
    electronica.mostrar_informacion()
