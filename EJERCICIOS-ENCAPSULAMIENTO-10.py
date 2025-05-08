class Circulo:
    def __init__(self, radio):
        self.__radio = radio

    def get_radio(self):
        return self.__radio

    def set_radio(self, nuevo_radio):
        if nuevo-radio > 0:
            self.__radio = nuevo_radio
        else:
            print("El radio ingresado debe ser mayor a 0")

    def area_cir(self):
        pi = 3.14

        area = pi * self.__radio * self.__radio

        return area

    def circun_cir(self):
        pi = 3.14

        circunferencia = 2 * pi * self.__radio

        return circunferencia

if __name__ == "__main__":
    circulo1 = Circulo(100)

    print(f"Área del círculo: {circulo1.area_cir()}")
    print(f"Circunferencia del círculo: {circulo1.circun_cir()}")
