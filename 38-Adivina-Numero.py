# El usuario adivina un numero entero entre el 1 y 100

import os, random

while(True):
    os.system("cls")

    numero_sec = random.randint(1,100)
    intentos = 0
    while True:
        numero_ing = int(input("Adivina el numero secreto (del 1-100): "))
        intentos += 1
        if numero_ing == numero_sec:
            print(f"\nFelicidades adivinaste en {intentos} intentos")
            break
        elif numero_ing < numero_sec:
            print("El numero secreto es mayor")
        else:
            print("El numero secreto es menor")
    

    if input("Deseas continuar? (S/N) ").upper().startswith("N"): break

print("Proceso terminado ...")