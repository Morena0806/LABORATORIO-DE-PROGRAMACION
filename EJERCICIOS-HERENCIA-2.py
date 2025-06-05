class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Cargo: {self.cargo}, Salario: ${self.salario:.2f}")


class Gerente(Empleado):
    def calcular_aumento(self):
        aumento = self.salario * 0.10
        self.salario += aumento
        print(f"Aumento para el gerente: ${aumento}")

class EmpleadoTemporal(Empleado):
    def calcular_aumento(self):

        if self.salario < 800000:
            aumento = self.salario * 0.05
            self.salario += aumento
            print(f"Aumento para el empleado temporal: ${aumento}")
        else:
            print("El aumento no aplica para el empleado temporal con salario igual o mayor a $700000.")

if __name__ == "__main__":
    gerente = Gerente("Maria", 1000000, "Gerente de Proyecto")
    temp = EmpleadoTemporal("Pablo", 700000, "Asistente Temporal")


    print("Antes del aumento :")
    gerente.mostrar_info()
    temp.mostrar_info()

    print("Aplicando el aumento:")
    gerente.calcular_aumento()
    temp.calcular_aumento()

    print("Después del aumento:")
    gerente.mostrar_info()
    temp.mostrar_info()
