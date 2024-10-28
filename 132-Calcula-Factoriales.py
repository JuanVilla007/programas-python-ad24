# Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
# Se crea una función que calcula el factorial de un número (ya la hicimos en clase)
# Se crea una función que recibe las lista capturada, usa la función anterior (calcular factorial) que recorre la
# lista de números y calcula el factorial de cada uno de ellos, y regresa como resultado una lista con los
# factoriales de los números de la lista.
# Se imprime la lista original y la lista con los factoriales de los números capturados.

def leer_lista():
    nums = input("Dame los números: ")
    lista = list(map(int, nums.split()))
    return lista

def calcular_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact

def calcular_factoriales(lista):
    lista_factoriales = []
    for num in lista:
        lista_factoriales.append(calcular_fact(num))
    return lista_factoriales

# Función principal
def main():
    lista = leer_lista()
    lista_fact = calcular_factoriales(lista)
    print("La lista de números originales:", lista)
    print("La lista con los factoriales:", lista_fact)

# Programa Principal
import os; os.system("cls")
main()