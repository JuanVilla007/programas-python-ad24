# Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.

import os; os.system("cls")

print("Universidad Kitty Kat SA")
print("Aceptar un estudiante base a su edad, sexo y tres calificaciones")

name = input("Dime tu nombre: ")
sex = input("Dime tu sexo ( M / F ) ").upper()

if sex == "M":
    print("Solo aceptamos mujeres :c")
elif sex == "F":
    edad = int(input("Dime tu edad: "))
    if edad < 21:
        print("Eres mujer, pero no tienes la edad suficiente, solo mayores de 21")
    else:
        print("Dame 3 calificaciones: ")
        c1, c2, c3 = float(input()), float(input()), float(input())
        pro = (c1 + c2 + c3) / 3
        if pro >= 8 and pro <= 9.5:
            print(f"{name} has sido aceptada, tu edad de {edad} y tu promedio de {pro}, lo permiten")
        else:
            print("Eres mujer, tienes la edad, pero tu promedio no da, solo aceptamos promedios de 8 a 9.5")
else:
    print("Sexo invalido")
print("Proceso terminado ... ")