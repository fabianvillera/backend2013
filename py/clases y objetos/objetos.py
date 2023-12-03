class Persona:
    def __init__(self):
        self.nombre = 'juan'
        self.apellido = 'perez' # vaslores dados en seco , se recomienda no darselos , se coloca un nuevo parametro con el metodo init
        self.edad = 9 

persona1 = Persona() # manda a llamar a la referenia  de la clase
print (persona1.nombre ) # se manda a llamar por  valores independientes y se agrega con el objeto mas la propiedad de la misma
