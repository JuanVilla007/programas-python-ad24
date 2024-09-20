# Imprime numeros del 100 a 1 en decrementos de 1 usando for

import os; os.system("cls")

n = int(input("Desde donde deseas imprimir? "))

i = int(input("Decrementos de: "))

for x in range (n, 0, -i):
    print (x, end=" ")