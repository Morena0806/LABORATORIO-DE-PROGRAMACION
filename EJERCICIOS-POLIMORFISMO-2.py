class Animal:
    def hacerSonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

class Perro(Animal):
    def __init__(self, raza):
        self.raza = raza
        
    def hacerSonido(self):
        return "Guau!"

class Gato(Animal):
    def __init__(self, raza):
        self.raza = raza
        
    def hacerSonido(self):
        return "Miau!"

def main():
    animales = [
        Perro("Labrador"),
        Gato("Maine Coon"),
        Perro("Boxer"),
        Gato("Devon Rex")
        ]

    for animal in animales:
        print(f"Sonido del {animal.__class__.__name__}: {animal.hacerSonido()}")

if __name__ == "__main__":
    main()
