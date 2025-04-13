class Banco:
    def __init__(self, nombre, tasa_interes):
        self.nombre = nombre
        self.tasa_interes = tasa_interes

    def calcular_interes (self, cantidad, tiempo):

        interes = cantidad * (self.tasa_interes/100) * tiempo
        self.total_mas_interes = cantidad + interes

        return self.total_mas_interes
    

    def tiempo_duplicar (self):

        tiempo = 72/self.tasa_interes
        return tiempo


if __name__ == "__main__":

    cantidad = 0
    tiempo = 0

    banco1 = Banco("Banco" , 5)

    print("Ingrese la cantidad de dinero: ")

    cantidad = float(int(input()))

    print("Ingrese el tiempo en años: ")

    tiempo = float(int(input()))

    print(f"El total con interes despues de {tiempo} años es de {banco1.calcular_interes(cantidad, tiempo)}")

    print(f"Y se tardaria aproximadamente {banco1.tiempo_duplicar()} años para duplicar la cantidad original")
    
          
