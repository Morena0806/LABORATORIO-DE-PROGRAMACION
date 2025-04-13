class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_carrera(self):
        return self.carrera

    def establecer_carrera(self, carrera):
        self.carrera = carrera

    def nota_media(self):
        notas = []
        n = 0
        print(f"Ingrese las notas con las que quiere sacar el promedio:")
        
        while n >= 0:
            n = int(input())
            
            if n >= 0 and n <=10:
                notas.append(n)

            else:
                print("Se eligio algo invalido!")
            
        return sum(notas) / len(notas)
        
        
        
if __name__ == "__main__":
    
    estudiante1 = Estudiante("María", 20, "Medicina")

    print(f"Nombre: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")
    
    print(f"Nota media: {estudiante1.nota_media()}")

    estudiante1.establecer_nombre("Carlos")
    estudiante1.establecer_edad(24)
    estudiante1.establecer_carrera("Veterinaria")

    print("\nDespués de actualizar:")
    print(" ")
    print(f"Nombre: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")

    print(f"Nota media: {estudiante1.nota_media()}")
