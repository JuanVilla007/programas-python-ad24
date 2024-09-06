# Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo, 2 es lunes y así hasta 7 es viernes. Si el número no está en el rango especificado, mostrar un mensaje de error. 

import os; os.system("cls")

print("Muestra el dia de la semana correspondiente al numero")

n = int(input("Introduce un numero entero del 1 al 7: "))

if n == 1:
    print("El dia es Domingo")
elif n == 2:
    print("El dia de es Lunes")
elif n == 3:
    print("El dia es Martes")
elif n == 4:
    print("El dia es Miercoles")
elif n == 5:
    print("El dia es Jueves")
elif n == 6:
    print("El dia es Viernes")
elif n == 7:
    print("El dia es Sabado")
else:
    print("Numero fuera de rango!")

print("Proceso terminado ... ")