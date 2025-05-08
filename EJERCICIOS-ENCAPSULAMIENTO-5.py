class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_notas(self):
        return self.__notas

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida.")

    def agregar_notas(self):
        n = 0
        print("Ingrese las notas para agregarlas a la lista:")

        while n >= 0:
            n = int(input())

            if n >= 0 and n <= 10:
                self.__notas.append(n)

            else:
                print("Se eligio algo invalido!")

        return self.__notas

    def promedio(self):
        return sum(self.__notas) / len(self.__notas)

    def mostrar_informacion(self):
        return f"Estudiante: Nombre: {self.__nombre}, Edad: {self.__edad}, Notas: {self.__notas}, Promedio: {self.promedio()}"


if __name__ == "__main__":

    estudiante1 = Estudiante("Maria", 20, 7)

    estudiante1.agregar_notas()
    
    estudiante1.promedio()
    print(estudiante1.mostrar_informacion())

    
