# Imprime numeros del 1 a n, en incrementos de p, usando while

import os; os.system("cls")

print("Imprime numeros del 1 a n, en incrementos de p")

c = 1

n = int(input("Hasa donde deseas llegar: "))
p= int(input("En incremento de: "))

while c <= n:
    print(c, end=" ")
    c = c + p

print("Ciclo terminado")