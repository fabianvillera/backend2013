#dada una lista iterela y saque el mayor numero de esta 
# Pedir al usuario que ingrese los puntajes separados por espacio y luego dividirlos en una lista
studenScore = input("Ingrese los puntajes separados por espacio: ").split()

# Convertir cada elemento de la lista a entero
for n in range(len(studenScore)):
    studenScore[n] = int(studenScore[n])

# Inicializar la variable puntajeAlto con 0
puntajeAlto = 0

# Iterar sobre los puntajes en la lista
for score in studenScore:
    # Verificar si el puntaje actual es mayor que el puntaje más alto actual
    if score > puntajeAlto:
        # Actualizar el puntaje más alto si el puntaje actual es mayor
        puntajeAlto = score

# Imprimir el puntaje más alto
print("El puntaje más alto es:", puntajeAlto)
# Pedir al usuario que ingrese los puntajes separados por espacio y luego dividirlos en una lista
studenScore = input("Ingrese los puntajes separados por espacio: ").split()

# Convertir cada elemento de la lista a entero
for n in range(len(studenScore)):
    studenScore[n] = int(studenScore[n])

# Inicializar la variable puntajeAlto con 0
puntajeAlto = 0

# Iterar sobre los puntajes en la lista
for score in studenScore:
    # Verificar si el puntaje actual es mayor que el puntaje más alto actual
    if score > puntajeAlto:
        # Actualizar el puntaje más alto si el puntaje actual es mayor
        puntajeAlto = score

# Imprimir el puntaje más alto
print("El puntaje más alto es:", puntajeAlto)
