# Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n), además deberá imprimirse la suma de esos números impares. 
# El proceso debe poder repetirse hasta que el usuario lo decida.

import os

while(True):
    os.system("cls")

    print("Imprime numeros impares del 1 a n y la suma de estos")

    n = int(input("Dijite el numero hasta el cual imprimir los numeros: "))
    ni = 1
    c = 0
    s = 0
    print("Numeros impares")
    while ni <= n:
        print(ni, end="  ")
        c += 1
        s = s + ni
        ni = 2*c+1

    if input(f"La suma de los numeros impares es: {s}\nDeseas continuar (S/N) ").upper().startswith("N"): break

print("Proceso terminado")