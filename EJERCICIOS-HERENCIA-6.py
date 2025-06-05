class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info_personal(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera=None):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def asignar_carrera(self, carrera):
        self.carrera = carrera
        print(f"Carrera asignada al estudiante: {self.carrera}")

    def mostrar_info_estudiante(self):
        self.mostrar_info_personal()
        print(f"Rol: Estudiante, Carrera: {self.carrera}")

class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura=None):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def asignar_asignatura(self, asignatura):
        self.asignatura = asignatura
        print(f"Asignatura asignada al profesor: {self.asignatura}")

    def mostrar_info_profesor(self):
        self.mostrar_info_personal()
        print(f"Rol: Profesor, Asignatura: {self.asignatura}")


if __name__ == "__main__":
    estudiante = Estudiante("Maria", 20)
    profesor = Profesor("Pablo", 45)

    print("Asignando roles:")
    estudiante.asignar_carrera("Ingenieria en Informatica")
    profesor.asignar_asignatura("Matematica")
    print()
    print("Mostrando información:")
    estudiante.mostrar_info_estudiante()
    print()
    profesor.mostrar_info_profesor()
