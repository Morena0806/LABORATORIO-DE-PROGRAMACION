class Producto:
    def __init__(self, nombre, precio, stock_dis):
        self.nombre = nombre
        self.precio = precio
        self.stock_dis = stock_dis

    def obtener_stock(self):
        return self.stock_dis

    def aumentar_s(self):
        stock_ag = 0
        
        print(f"Ingrese la cantidad de stock que quiere aumentar:")
        stock_ag = int(input())

        self.stock_dis = self.stock_dis + stock_ag

        return self.stock_dis

    def disminuir_s(self):
        stock_dis = 0
        
        print(f"Ingrese la cantidad de stock que quiere disminuir:")
        stock_dis = int(input())

        self.stock_dis =  self.stock_dis - stock_dis

        return self.stock_dis

        



if __name__ == "__main__":

    producto1 = Producto("Jugo de naranja", 1400, 20)

    opcion = ""
    
    print(f"Stock aumentado: {producto1.aumentar_s()}")

    print("¿Quiere disminuir el stock? (SI/NO):")

    opcion = input()

    if opcion == "SI":
        print(f"Stock disminuido: {producto1.disminuir_s()}")

    elif opcion == "NO":
        print("Adios")

    else:
        print("Se ingreso algo invalido!")
