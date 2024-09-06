#  Dados tres números enteros, verificar cual es el mayor, ej: 10, 9 8, el mayor es 10, 11, 30, -1 el mayor es 30 

import os; os.system("cls")

print("Verifica el numero mayor")

print("Dame tres numeros enteros: ")
n1,n2,n3 = int(input()), int(input()), int(input())

if n1 > n2 and n1 > n3:
    print(f"De los numeros {n1}, {n2}, {n3}) el mayor es: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"De los numeros {n1}, {n2}, {n3} el mayor es: {n2}")
elif n3 > n1 and n3 > n1:
    print(f"De los numeros {n1}, {n2}, {n3} el mayor es: {n3}")
elif n1 == n2 and n2 ==n3:
    print(f"Tus numeros son iguales :c")

print("Proceso terminado ... ")