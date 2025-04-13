class Tienda:
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def añadir_p(self):
        p = ""

        while p != "FIN":
            print("Ingrese los productos que quiere agregar a la lista:")

            p = input()

            if p != "FIN":
                self.productos.append(p)

        return self.productos

    def eliminar_p(self):
        p = ""

        while p != "FIN":
            print("Ingrese los productos que quiere eliminar de la lista:")

            p = input()

            if p!= "FIN":
                if p in self.productos:
                    self.productos.remove(p)

        return self.productos

if __name__ == "__main__":
    lista = Tienda("Día", ["FIDEOS","JUGO","QUESO"])

    opcion = ""

    print(f"Lista luego de agregar productos: {lista.añadir_p()}")

    print("¿Quiere eliminar productos de la lista? (SI/NO):")

    opcion = input()

    if opcion == "SI":
        print(f"Lista luego de eliminar productos: {lista.eliminar_p()}")

    elif opcion == "NO":
        print("Adios")
