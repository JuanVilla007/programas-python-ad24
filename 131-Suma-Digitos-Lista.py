# Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
# Se crea una función que suma los dígitos individuales de un número (ya la hicimos en clase)
# Se crea una función que recibe las lista capturada, usa la función anterior (suma dígitos) y recorre la lista
# de números y suma sus dígitos, y regresa una lista con las sumas de tos dígitos de los números de la lista.
# Se imprime la lista original y la lista con las sumas de los dígitos de los números capturados.

 
def leer_arreglo():
    nums = list(map(int, input("Dame los números separados por espacios: ").split()))
    return nums

def suma_dig(num):
    suma = 0
    while num > 0:
        suma += num % 10  
        num //= 10        
    return suma

def lis_sum_dig(lista):
    sum_dig = []
    for num in lista:
        sum_dig.append(suma_dig(num))
    return sum_dig

# Programa principal
import os; os.system("cls")
n = leer_arreglo()
lista = lis_sum_dig(n) 

print("\nLa lista de números original:", n)
print("La lista con la suma de los dígitos de los números:", lista)