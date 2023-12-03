class Persona:
    def __init__(self , nombre, apellido ,edad ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1= Persona('juan', 'perez' , 28) # se le asignaron los nuevos valores a las variables que antes iniciamos
print(persona1.nombre)
print(persona1.edad)