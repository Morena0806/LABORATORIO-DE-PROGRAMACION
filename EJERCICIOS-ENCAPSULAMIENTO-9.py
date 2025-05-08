class Juego:
    def __init__(self, nombre, genero, precio):
        self.__nombre = nombre
        self.__genero = genero
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_genero(self):
        return self.__genero

    def get_precio(self):
        return self.__precio

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_genero(self, nuevo_genero):
        self.__genero = nuevo_genero

    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Precio invalido.")

    def mostrar_informacion(self):
        return(f"Juego: {self.__nombre}, Género: {self.__genero}, Precio: ${self.__precio}")

    def oferta(self, valor_dado):
        if self.__precio < valor_dado:
            print("Este juego esta en oferta!")
        else:
            print("Este juego no esta en oferta")

if __name__ == "__main__":
    juego1 = Juego("Minecraft", "Sandbox", 18000)

    valor = 20000

    print(juego1.mostrar_informacion())
    juego1.oferta(valor)
