# Calcular el volumen de un cilindro dado su radio y su altura
import os; os.system('cls')
import math as mt

print("Calcular el volumen de un cilindro")

r =  float(input("Dame el radio del cilindro: "))
h = float(input("Dame la altura del cilindro: "))

v = mt.pi * ( r ** 2 ) * h

print(f"El volumen del cilindro es : {v:.3f}")
