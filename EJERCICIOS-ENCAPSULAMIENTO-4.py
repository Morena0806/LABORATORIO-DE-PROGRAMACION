class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion

    def descripcion(self):
        if self.__titulo == "La Ilíada":
            return("La Ilíada es una epopeya griega, atribuida tradicionalmente a Homero."
                  "Compuesta en hexámetros dactílicos, consta de 15 693 versos y su trama radica en la cólera de Aquiles.​"
                  "Narra los acontecimientos ocurridos durante 51 días en el décimo y último año de la guerra de Troya.")

        elif self.__titulo == "El Psicoanalista":
            return("'El Psicoanalista' de John Katzenbach es una novela de suspenso que narra la historia del psicoanalista Frederick Starks, quien recibe una amenaza anónima que le da 15 días para descubrir quién es el remitente."
                  "Si no lo logra, tendrá que elegir entre suicidarse o presenciar la muerte de sus seres queridos."
                  "La novela explora la relación entre el terapeuta y el paciente de una manera inesperada y ofrece un juego de misterio y suspenso.")

        else:
            return("No hay descripcion para este libro")
            
    def clasico_o_no(self):
        if self.__año_publicacion < 1975:
           return("Si, el libro mencionado es un clásico.")

        else:
            return("No, el libro mencionado NO es un clásico.")

    def mostrar_informacion(self):
        return f"Libro: Titulo: {self.__titulo}, Autor: {self.__autor}, Año de publicacion: {self.__año_publicacion}"

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_año_publicacion(self):
        return self.__año_publicacion

    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def set_año(self, nuevo_año_publicacion):
        self.__año_publicacion = nuevo_año_publicacion

        
if __name__ == "__main__":
    libro1 = Libro("La Ilíada", "Homero", 520)
    
    print(libro1.mostrar_informacion())

    print(" ")

    print(libro1.descripcion())

    print(" ")

    print(f"¿El libro es un clásico?: {libro1.clasico_o_no()}")

    libro1.set_titulo("El Psicoanalista")
    libro1.set_autor("John Katzenbach")
    libro1.set_año(2002)

    print(" ")

    print("Despues de cambiar de libro:")

    print(libro1.mostrar_informacion())

    print(libro1.descripcion())

    print(" ")

    print(f"¿El libro es un clásico?: {libro1.clasico_o_no()}")
