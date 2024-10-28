# Diseña un programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos
# regrese la suma de números pares o impares en el rango de números especificados.
# El programa deberá mostrar un menú con las opciones correspondientes y llamara a la función según la opción
# seleccionada.

def sum(inicio, fin, tipo):
    suma = 0
    if tipo == 'P': 
        for num in range(inicio, fin+1):
            if num % 2 == 0:
                suma += num
    elif tipo == 'I': 
        for num in range(inicio, fin+1):
            if num % 2 != 0:
                suma += num
    return suma

# Programa principal
import os; os.system("cls")
while True:
    print("\nMenú de opciones")
    print("P.- Sumar números pares en un rango")
    print("I.- Sumar números impares en un rango")
    print("X.- Salir")

    opcion = (input("\nElige una opción: "))

    if opcion == 'p' or opcion == 'i':
        inicio = int(input("Desde? "))
        fin = int(input("Hasta? "))
        
        if opcion == 'p':
            res = sum(inicio, fin, 'P')
            print(f"\nLa suma de los números pares entre {inicio} y {fin} es: {res}")
        else:
            res = sum(inicio, fin, 'I')
            print(f"\nLa suma de los números impares entre {inicio} y {fin} es: {res}")
    
    elif opcion == 'x':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, elige entre 1 y 3.")