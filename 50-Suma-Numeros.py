# Suma n numeros introducidos por el usuario

import os

os.system("cls")

suma = 0
n = int(input("Cuantas calificaciones: "))

for i in range (1, n+1):
    print(f"Calificacion {i}: ", end="")
    x = float(input())
    suma = suma + x

print ("La suma es: ", suma)
print (f"El promedio es: {suma / n}")