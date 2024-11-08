# Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
# Crear una función para cada una de las siguientes estadísticas (poblacional):
# Mayor
# Menor
# Media
# Varianza
# Desviación estánda
# Se muestran los resultados de cada operación.

import math

def leer_arreglo():
    nums = input("Dame numeros (separados por espacio): ").split()
    lista = []
    for num in nums:
        lista.append(int(num))  
    return lista

def mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

def menor(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

def media(lista):
    suma = 0
    for num in lista:
        suma += num  
    return suma / len(lista) 

def varianza(lista):
    m = media(lista)
    suma2 = 0
    for x in lista:
        suma2 += (x - m) ** 2  
    return suma2 / len(lista)  

def desviacion(lista):
    return math.sqrt(varianza(lista)) 

# Programa principal
import os; os.system("cls")

nums = leer_arreglo()  
med = media(nums)
may = mayor(nums)
men = menor(nums)
var = varianza(nums)
desv = desviacion(nums)

print(f"\nLista de números: {nums}")
print(f"La media: {med:.3f}")
print(f"Mayor de los datos: {may}")
print(f"Menor de los datos: {men}")
print(f"Varianza: {var:.3f}")
print(f"Desviación estándar: {desv:.3f}")