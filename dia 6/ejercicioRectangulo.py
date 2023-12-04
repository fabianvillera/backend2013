#realizar un algoritmo usando poo que use clases para calcular el area de un rectangulo
class AreaRectangulo:
    def __init__(self, Largo , Ancho):
        self.Largo = Largo
        self.Ancho = Ancho
    def Area(self):
        return self.Largo * self.Ancho

AreaRectangulo1 = AreaRectangulo (2,5)
print(AreaRectangulo1.Area())