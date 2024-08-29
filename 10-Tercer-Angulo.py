# Calcular el tercer angulo conociendo los pasados 2
import os; os.system('cls')

print("Calcula el tercer angulo de un triangulo")

a1 = float(input("Dame el primer angulo: "))
a2 = float(input("Dame el segundo angulo: "))

a3 = 180 - (a1 + a2)

print("El valor del tercer angulo es : ", a3)