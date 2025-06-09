class Empleado:
    def calcularSalario(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

class EmpleadoPorHora(Empleado):
    def __init__(self, st, ht):
        self.st = st
        self.ht = ht
        
    def calcularSalario(self):
        self.st
        self.ht
        sueldo_por_hora = self.st / self.ht

        return "El sueldo por hora es de: ", sueldo_por_hora,"."

class EmpleadoFijo(Empleado):
    def __init__(self, st):
        self.st = st
        
    def calcularSalario(self):
        self.st
        return "El sueldo fijo es de: ",self.st,"."


def main():
    empleados = [
        EmpleadoPorHora(500000, 150),
        EmpleadoFijo(600000),
        EmpleadoPorHora(600000, 170),
        EmpleadoFijo(700000)
        ]

    for empleado in empleados:
        print(f"Salario de un {empleado.__class__.__name__}: {empleado.calcularSalario()}")

if __name__ == "__main__":
    main()
