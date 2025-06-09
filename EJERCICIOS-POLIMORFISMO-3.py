class Vehiculo:
    def mover(self):
        raise NotImplementedError("Este metodo debe ser sobrescrito por las subclases.")

class Coche(Vehiculo):
    def __init__(self, color):
        self.color = color

    def mover(self):
        return "El coche se está moviendo a 60 km/h sobre sus cuatro ruedas."

class Bicicleta(Vehiculo):
    def __init__(self, color):
        self.color = color

    def mover(self):
        return "La bicicleta se está moviendo a 12 mph sobre sus dos ruedas."

def main():
    vehiculos = [
        Coche("Rojo"),
        Bicicleta("Azul"),
        Coche("Blanco"),
        Bicicleta("Negro")
        ]

    for vehiculo in vehiculos:
        print(f"Como se mueve el/la {vehiculo.__class__.__name__}: {vehiculo.mover()}")

if __name__ == "__main__":
    main()
