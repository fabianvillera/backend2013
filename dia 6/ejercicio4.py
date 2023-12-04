#realizar un algoritmo usando poo que use clases para calcular el area de un cubo
class AreaCubo:
    def __init__(self, Largo , Ancho, Profundidad):
        self.Largo = Largo
        self.Ancho = Ancho
        self.Profundidad = Profundidad
    def Area(self):
        return self.Largo * self.Ancho * self.Profundidad
AreaCubo1 =AreaCubo (2,5 ,7)
print(AreaCubo1.Area())