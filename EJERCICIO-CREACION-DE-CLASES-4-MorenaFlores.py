class Rectángulo:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def area_rec(self):

        self.longitud
        self.anchura

        area = self.longitud * self.anchura

        return area

    def perimetro_rec(self):

        self.longitud
        self.anchura
        
        perimetro = 2 *(self.longitud + self.anchura)

        return perimetro


if __name__ == "__main__":

    rectangulo1 = Rectángulo(100, 200)

    print(f"Área del rectángulo: {rectangulo1.area_rec()}")

    print(f"Perímetro del rectángulo : {rectangulo1.perimetro_rec()}")
