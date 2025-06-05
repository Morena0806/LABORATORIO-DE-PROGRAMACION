class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_detalles(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")


class Automovil(Vehiculo):
    def eficiencia_combus(self):
        distancia_reco = 500
        combustible_consum = 40

        self.eficiencia_auto = distancia_reco / combustible_consum

        print("La eficiencia del combustible es de",self.eficiencia_auto)

    def cantidad_necesaria(self):
        distancia_viaje = 750
        self.eficiencia_auto

        self.cantidad_necesaria_auto = distancia_viaje / self.eficiencia_auto

        print("La cantidad necesaria para el viaje es de", self.cantidad_necesaria_auto)

class Motocicleta(Vehiculo):
    def eficiencia_combus(self):
        distancia_reco = 250
        combustible_consum = 30

        self.eficiencia_moto = distancia_reco / combustible_consum

        print("La eficiencia del combustible es de",self.eficiencia_moto)

    def cantidad_necesaria(self):
        distancia_viaje = 550
        self.eficiencia_moto

        self.cantidad_necesaria_moto = distancia_viaje / self.eficiencia_moto

        print("La cantidad necesaria para el viaje es de", self.cantidad_necesaria_moto)


if __name__ == "__main__":
    a = Automovil("Ford", "Mondeo", 1980)
    a.mostrar_detalles()
    a.eficiencia_combus()
    a.cantidad_necesaria()
    print()

    m = Motocicleta("Honda", "Transalp", 1987)
    m.mostrar_detalles()
    m.eficiencia_combus()
    m.cantidad_necesaria()
