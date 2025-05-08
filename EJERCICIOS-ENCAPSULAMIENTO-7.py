class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.__nombre = nombre
        self.__salario = salario
        self.__departamento = departamento

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        if nuevo_salario >= 0:
            self.__salario = nuevo_salario
        else:
            print("El salario no puede ser negativo.")

    def get_departamento(self):
        return self.__departamento

    def set_departamento(self, nuevo_departamento):
        self.__departamento = nuevo_departamento


    def aumentar(self, porcentaje):
        if porcentaje > 0:
            aumento = self.__salario * (porcentaje/100)
            self.__salario += aumento

        else:
            print("Se eligio un porcentaje menor o igual a 0")


    def mostrar_informacion(self):
        return (f"Empleado: {self.__nombre}, Departamento: {self.__departamento}, Salario: ${self.__salario}")

if __name__ == "__main__":
    empleado1 = Empleado("Maria", 150000, "Marketing")
    print(empleado1.mostrar_informacion())

    empleado1.aumentar(10)

    print("Despues de aumentar el salario:")
    print(empleado1.mostrar_informacion())
