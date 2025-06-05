class Animal:
    def __init__(self, raza, color, edad):
        self.raza = raza
        self.color = color
        self.edad = edad

    def mostrar_detalles(self):
        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}")
        print(f"Edad: {self.edad}")


class Perro(Animal):
    def sonido(self):
        print("El perro hace: Woof!")

class Gato(Animal):
    def sonido(self):
        print("El gato hace: Meow!")


if __name__ == "__main__":
    p = Perro("Labrador", "Amarillo", 5)
    p.mostrar_detalles()
    p.sonido()
    print()

    g = Gato("Maine Coon", "Marron", 3)
    g.mostrar_detalles()
    g.sonido()
    print()
