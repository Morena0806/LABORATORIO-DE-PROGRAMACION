class Instrumento:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material

    def tipo_sonido(self):
        print(f"El {self.nombre} hace un sonido de un instrumento de {self.material}.")

class Guitarra(Instrumento):
    def tocar_nota(self, nota):
        print(f"La guitarra toca la nota {nota}.")

class Piano(Instrumento):
    def tocar_nota(self, nota):
        print(f"El piano toca la nota {nota}.")

if __name__ == "__main__":
    guitarra = Guitarra("Guitarra Acústica", "madera")
    piano = Piano("Piano de cola", "madera y metal")

    print("Información del instrumento:")
    guitarra.tipo_sonido()
    piano.tipo_sonido()

    print("Tocando las notas musicales:")
    guitarra.tocar_nota("Mi")
    piano.tocar_nota("Do")
