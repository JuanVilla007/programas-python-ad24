# Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la temperatura final en grados centígrados 
# y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor final. 
# El proceso debe poder repetirse hasta que el usuario lo decida.

import os, random

while(True):
    
    os.system("cls")
    print("Imprime la temperatura en farenheit de un rango de valores")
    ti = float(input("Introduce un la temperatura inicial en °Celcius "))
    tf = float(input("Introduce un la temperatura final en °Celcius "))
    c = 0   
    while True:
        print(f"{ti} °C = {ti * (9/5) + 32:.2f} °F")
        ti += 1

        if ti >= tf :
            break

    if input("Deseas continuar (S/N) ").upper().startswith("N"): break

print("Proceso terminado ...")