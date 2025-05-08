class Producto:
    def __init__(self, nombre, precio , stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido.")

    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Stock no puede ser negativo.")

    def aumentar_s(self):
        stock_ag = 0

        print("Ingrese la cantidad de stock que quiere aumentar:")
        stock_ag = int(input())

        self.__stock += stock_ag

        return self.__stock

    def disminuir_s(self):
        stock_dis = 0

        print("Ingrese la cantidad de stock que quiere disminuir:")
        stock_dis = int(input())

        self.__stock -= stock_dis

        return self.__stock

    def mostrar_informacion(self):
        return (f"Producto: {self.__nombre}, Precio: ${self.__precio}, Stock disponible: {self.__stock}")


if __name__ == "__main__":
    producto1 = Producto("Jugo de naranja", 1400, 20)

    opcion = ""

    print(producto1.mostrar_informacion())
    
    producto1.aumentar_s()
    print("Luego de aumentar el stock:")
    print(producto1.mostrar_informacion())

    print("¿Quiere disminuir el stock? (SI/NO):")

    opcion = input()

    if opcion == "SI":
        
        producto1.disminuir_s()
        print(f"Luego de disminuir el stock:")
        print(producto1.mostrar_informacion())

    elif opcion == "NO":
        print("Adios")

    else:
        print("Se eligio algo invalido!")
