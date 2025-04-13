class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_salario(self):
        return self.salario

    def establecer_salario(self, salario):
        self.salario = salario

    def obtener_cargo(self):
        return self.cargo

    def establecer_cargo(self, cargo):
        self.cargo = cargo

    def salario_anual(self):
        salan = 0

        self.salario

        salan = self.salario * 12

        return salan


if __name__ == "__main__":

    empleado1 = Empleado("Maria", 28, 1500000000, "Doctora")

    print(f"Nombre: {empleado1.obtener_nombre()}")
    print(f"Edad: {empleado1.obtener_edad()}")
    print(f"Salario: {empleado1.obtener_salario()}")
    print(f"Cargo: {empleado1.obtener_cargo()}")

    print(f"Salario anual: {empleado1.salario_anual()}")

    empleado1.establecer_nombre("Carlos")
    empleado1.establecer_edad(32)
    empleado1.establecer_salario(1000000000)
    empleado1.establecer_cargo("Veterinario")

    print("\nDespués de actualizar:")
    print(" ")
    print(f"Nombre: {empleado1.obtener_nombre()}")
    print(f"Edad: {empleado1.obtener_edad()}")
    print(f"Salario: {empleado1.obtener_salario()}")
    print(f"Cargo: {empleado1.obtener_cargo()}")

    print(f"Salario anual: {empleado1.salario_anual()}")
