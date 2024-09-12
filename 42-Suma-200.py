# Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, luego mostrar cuantos números fueron introducidos y la suma de estos. 
# El proceso debe poder repetirse hasta que el usuario lo decida.
import os, random

while(True):
    
    os.system("cls")
    print("Imprime la suma y la cantidad de numeros introducidos cuando la suma de >= 200")
    num_int = 0
    s = 0
    while True:
        num = int(input("Ingresa un numero: "))
        num_int += 1
        s = s + num

        if s >= 200:
            print(f"La suma es {s}")
            print(f"Se introdujeron un total de {num_int} numeros")
            break

    if input("Deseas continuar (S/N) ").upper().startswith("N"): break

print("Proceso terminado ...")