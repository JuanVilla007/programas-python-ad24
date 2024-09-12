# Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0, además deberá contar cuantos números se introdujeron. 
# El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system("cls")

    print("Imprime la suma, el promedio y la cantidad de una serie de numeros introducidos")

    stop = 0
    num_int = 0
    s = 0
    while True:
        num_ing = int(input("Introduce un numero o 0 para parar: "))
        num_int += 1
        s = s + num_ing

        if num_ing == stop:
            num_int -= 1
            print(f"La suma es {s}")
            print(f"El promedio es {s/num_int}")
            print(f"Se introdujeron un total de {num_int} numeros")
            break

    if input("Deseas continuar (S/N) ").upper().startswith("N"): break

print("Proceso terminado ...")