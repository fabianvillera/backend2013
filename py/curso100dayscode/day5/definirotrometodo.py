class carro:
    def __init__(self, color , modelo,recorrido):
        self.color = color
        self.modelo = modelo 
        self.recorrido = recorrido
    #definimos otro metodo para hacer el codigo mas legible
    def mostrarDetalle(self):
        print(f'persona: {self.color} {self.modelo} {self.recorrido}')

carro1 = carro('rojo',"bmw",20000)

#para modificar un atributo solo realizamos 
carro1.color ="violeta"
carro1.mostrarDetalle()
