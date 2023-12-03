class persona:
    def __init__(self,nombre,apellido,edad):
      self.nombre = nombre
      self.apellido = apellido
      self.edad = edad 

persona1 = persona ('juan','par',27)
print(persona1.nombre, persona1.apellido , persona1.edad)