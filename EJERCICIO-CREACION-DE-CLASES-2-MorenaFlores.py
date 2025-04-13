import datetime


class Coche:
    def __init__(self, marca, modelo, añofab):
        self.marca = marca
        self.modelo = modelo
        self.añofab = añofab


    def obtener_años(self):
        self.añofab
        
        añopres = datetime.date.today().year

        añospas = añopres - self.añofab

        return añospas


if __name__ == "__main__":

    coche1 = Coche("Ford", "Mondeo", 1980)

    print(f"Años que pasaron desde la fabricación del coche: {coche1.obtener_años()}")
