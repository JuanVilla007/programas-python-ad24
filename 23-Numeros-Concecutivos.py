# Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, si no lo son (1,4,6) mandar mensaje de error.

import os; os.system("cls")

print("Verificar si tres numeros son consecutivos")

print("Dame tres numeros enteros: ")
n1,n2,n3 = int(input()), int(input()), int(input())

if n2 == n1 + 1 and n3 == n2 + 1:
    print(f"Los numeros {n1}, {n2}, {n3} son consecutivos")
elif n2 == n1 - 1 and n3 == n2 - 1:
    print(f"Los numeros {n1}, {n2}, {n3} son consecutivos")
else:
    print(f"Los numeros {n1}, {n2}, {n3} no son consecutivos")

print("Proceso terminado ... ")