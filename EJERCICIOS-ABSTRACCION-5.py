from abc import ABC, abstractmethod
import math

class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass


class EmpleadoPorHora(Empleado):
    def calcular_sueldo(self):
        sueldo_total = 500000
        horas_trabajadas = 150

        sueldo_por_hora = sueldo_total / horas_trabajadas

        return "El sueldo por hra es de ",sueldo_por_hora,"."

class EmpleadoFijo(Empleado):
    def calcular_sueldo(self):
        sueldo_fijo = 500000

        return "El sueldo fijo es de ",sueldo_fijo,"."
