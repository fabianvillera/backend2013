#tenemos una serie de numeros los cuales debemos iteerar y pasar la suma de estos el numero lo debe presentar el usuario
total =0 
n = int(input('ingrese el numero deseado para realizar la suma '))
for number in range (1 , n):
    total += number 
    print(total)