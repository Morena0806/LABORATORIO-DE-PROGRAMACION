class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def set_base(self, nueva_base):
        if nueva_base > 0:
            self.__base = nueva_base
        else:
            print("La base debe ser mayor que cero.")

    def get_altura(self):
        return self.__altura

    def set_altura(self, nueva_altura):
        if nueva_altura > 0:
            self.__altura = nueva_altura
        else:
            print("La altura debe ser mayor que cero.")

    def area_rec(self):
        self.__base
        self.__altura

        area = self.__base * self.__altura

        return area

    def perimetro_rec(self):
        self.__base
        self.__altura

        perimetro = 2 *(self.__base + self.__altura)

        return perimetro


if __name__ == "__main__":
    rectangulo1 = Rectangulo(100, 200)

    print(f"Área del rectángulo: {rectangulo1.area_rec()}")

    print(f"Perímetro del rectángulo: {rectangulo1.perimetro_rec()}")

    rectangulo1.set_base(250)
    rectangulo1.set_altura(400)
    print("Después de cambiar las dimensiones:")
    print(f"Área del rectángulo: {rectangulo1.area_rec()}")
    print(f"Perímetro del rectángulo: {rectangulo1.perimetro_rec()}")
