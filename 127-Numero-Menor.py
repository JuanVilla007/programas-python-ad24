# Diseña un programa con una función que pida 3 números enteros y devuelva el menor de ellos, usando una función

def menor():
    n1 = int(input("Ingresa el primer número: "))
    n2 = int(input("Ingresa el segundo número: "))
    n3 = int(input("Ingresa el tercer número: "))
        
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3


# Programa principal
import os; os.system("cls")
men = menor()

print("El número menor es: ", men)