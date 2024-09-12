# Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir 
# El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system("cls")

    print("Imprime el numero mayor de una serie de numeros introducidos")

    mayor = 0
    
    while True:
        num_ing = int(input("Introduce un numero o 0 para parar: "))
        
        if mayor == 0 or num_ing > mayor:
            mayor = num_ing

        if num_ing == 0:
            print(f"El numero mayor es: {mayor}")
            break

    if input("Deseas continuar (S/N) ").upper().startswith("N"): break

print("Proceso terminado ...")