#asignar un nuevvo parametro a un objeto 
class carro:
    def __init__(self, color,tamano, recorrido) :
        self.color = color 
        self.tamano= tamano
        self.recorrido = recorrido
    def mostrarDetalle (self):
        print(f'carro: {self.color} {self.tamano} {self.recorrido} ')

carro1 = carro('rojo','mediano',10000)
carro1.mostrarDetalle()
#agregar una nueva propiedad a el objeto:
carro.marca = 'renault'
#solo se agregara de manera local por lo que sera complicado realizar una llamada  global 

