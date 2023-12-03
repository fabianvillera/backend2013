#para modificar el valor de un atributo solo basta con colocar la propiedad que este posee y listo 
class carro:
    def __init__(self, color , modelo,recorrido):
        self.color = color
        self.modelo = modelo 
        self.recorrido = recorrido

carro1 = carro('rojo',"bmw",20000)

#para modificar un atributo solo realizamos 
carro1.color ="violeta"
print(carro1.color,carro1.modelo,carro1.recorrido)
