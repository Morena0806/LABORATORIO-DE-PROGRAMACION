class Círculo:
    def __init__(self, radio, diametro):
        self.radio = radio
        self.diametro = diametro

    def area_cir(self):
        pi = 3.14
        self.radio

        area = pi * self.radio * self.radio

        return area

    def circun_cir(self):
        pi = 3.14
        self.radio

        circunferencia = 2 * pi * self.radio

        return circunferencia

if __name__ == "__main__":
    circulo1 = Círculo(100,200)

    print(" ")
    print(f"Área del círculo: {circulo1.area_cir()}")

    print(" ")
    print(f"Circunferencia del círculo : {circulo1.circun_cir()}")
