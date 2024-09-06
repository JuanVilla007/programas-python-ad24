# Imprime los numeros de n a 1 en decrementos de p

import os; os.system("cls")

print("Imprime los numeros de 100 a 1")

n= int(input("Desde donde: "))
p = int(input("Decrementos de: "))

c = n

while c >= 1:
    print(c, end=" ")
    c = c - p
    
print("Ciclo terminado")