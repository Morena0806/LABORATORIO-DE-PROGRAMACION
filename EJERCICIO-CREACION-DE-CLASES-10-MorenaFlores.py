class Libro:
    def __init__(self, titulo, autor, genero, num_pag):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.num_pag = num_pag

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_autor(self):
        return self.autor

    def establecer_autor(self, autor):
        self.autor = autor

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def obtener_num_pag(self):
        return self.num_pag

    def establecer_num_pag(self, num_pag):
        self.num_pag = num_pag

    def ficcion_o_no(self):

        if self.genero == "ficcion":
            a = "El libro es de ficción" 

        elif self.genero == "no ficcion":
            a = "El libro no es de ficción"

        return a


if __name__ == "__main__":

    libro1 = Libro("Estudio en escarlata", "Arthur Conan Doyle", "ficcion", 192)

    print(f"Titulo: {libro1.obtener_titulo()}")
    print(f"Autor: {libro1.obtener_autor()}")
    print(f"Número de páginas: {libro1.obtener_num_pag()}")

    print(f"¿Es de ficción?: {libro1.ficcion_o_no()}")

    libro1.establecer_titulo("Emboscada")
    libro1.establecer_autor("Facundo Pastor")
    libro1.establecer_genero("no ficcion")
    libro1.establecer_num_pag(256)

    print("\nDespues de actualizar:")
    print(" ")
    print(f"Titulo: {libro1.obtener_titulo()}")
    print(f"Autor: {libro1.obtener_autor()}")
    print(f"Número de páginas: {libro1.obtener_num_pag()}")

    print(f"¿Es de ficción?: {libro1.ficcion_o_no()}")
