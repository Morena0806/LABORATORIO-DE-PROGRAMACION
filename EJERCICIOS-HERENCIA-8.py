class Transporte:
    def __init__(self, capacidad, velocidad_maxima):
        self.capacidad = capacidad
        self.velocidad_maxima = velocidad_maxima

    def mostrar_detalles(self):
        print(f"Capacidad: {self.capacidad}")
        print(f"Velocidad máxima: {self.velocidad_maxima}")


class Avion(Transporte):
    def tiempo_de_viaje(self):
        distancia = 2000
        velocidad = 200

        self.tiempo_avion = distancia / velocidad

        print("El tiempo de viaje es de", self.tiempo_avion)


class Barco(Transporte):
    def tiempo_de_viaje(self):
        distancia = 850
        velocidad = 40

        self.tiempo_barco = distancia / velocidad

        print("El tiempo de viaje es de", self.tiempo_barco)


if __name__ == "__main__":
    av = Avion(400, 800)
    av.mostrar_detalles()
    av.tiempo_de_viaje()

    print()

    b = Barco(300, 500)
    b.mostrar_detalles()
    b.tiempo_de_viaje()
