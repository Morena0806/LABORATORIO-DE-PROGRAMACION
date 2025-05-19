from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def calcular_area(self):
        pi = math.pi
        radio = 5

        area = pi * radio * radio

        return area_circ

class Rectangulo(Figura):
    def calcular_area(self):
        longitud = 10

        anchura = 5

        area = longitud * anchura

        return area_rec
