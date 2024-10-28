#Diseña un programa con una función que pida un número entero entre 1 y 7 y devuelva el día de la semana con letra.

def dia_semana():
    num = int(input("Ingresa un número entre 1 y 7: "))

    if num < 1 or num > 7:
        return "Error. Ingresa un número entre 1 y 7!!."
       
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    
    return dias_semana[num]

# Programa principal
import os; os.system("cls")
dia = dia_semana()
print("El día de la semana es:", dia)