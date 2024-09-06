# Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V, VI, VII, VIII, IX, X). 
# Si el número no esta en el rango solicitado que mande un mensaje de error.

import os; os.system("cls")

print("Muestra el equivalente en numero romano de un numero")

n = int(input("Introduce un numero entero del 1 al 10: "))

if n == 1:
    print("El numero romano es I")
elif n == 2:
    print("El numero romano es II")
elif n == 3:
    print("El numero romano es III")
elif n == 4:
    print("El numero romano es IV")
elif n == 5:
    print("El numero romano es V")
elif n == 6:
    print("El numero romano es VI")
elif n == 7:
    print("El numero romano es VII")
elif n == 8:
    print("El numero romano es VIII")
elif n == 9:
    print("El numero romano es IX")
elif n == 10:
    print("El numero romano es X")
else:
    print("Numero fuera de rango")

print("Proceso terminado ... ")