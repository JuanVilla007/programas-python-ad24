# Imprime la tabla de multiplicar que el usuario pida hasta donde la pida
import os

while(True):
    os.system("cls")

    n = int(input("Tablas de 1 hasta: ? "))
    m = int(input("Hasta donde? "))
    t = 1

    while t <=n:
        print(f"Tabla del {t}")
        c = 1
        while c <= m:
            print(f"{t} x {c} = {t*c}")
            c += 1
        t += 1

    if input("Deseas continuar (S/N) ").upper().startswith("N"): break

print("Proceso terminado")