class Persona:
    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad

    def set_sexo(self, nuevo_sexo):
        self.__sexo = nuevo_sexo

    def mostrar_informacion(self):
        return(f"Persona: {self.__nombre}, Edad: {self.__edad}, Sexo: {self.__sexo}")

if __name__ == "__main__":
    persona1 = Persona("Maria", 20, "Femenino")
    print(persona1.mostrar_informacion())

    persona1.set_edad(25)

    print("Después de cambiar la edad:")
    print(persona1.mostrar_informacion())
