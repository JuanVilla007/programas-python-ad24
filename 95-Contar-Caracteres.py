# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

import os; os.system("cls")

cad = input("Escribe una cadena de caracteres: ")

cont = {}

for caracter in cad:
    if caracter in cont:
            cont[caracter] += 1
    else:
            cont[caracter] = 1
            
print(cont)