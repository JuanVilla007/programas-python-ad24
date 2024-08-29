# Calcular la hipotenusa de un triangulo rectangulo
import os; os.system('cls')
import math as mt

print('Calculando la hipotenusa de un triangulo ractangulo')

l1 = float(input("Dame la medida del cateto opuesto: "))
l2 = float(input("Dame la medida del cateto adyacente: "))

hip = mt.sqrt( ( l1 ** 2 ) + ( l2 ** 2) )

print(f"La medida de la hipotenusa del triangulo es: {hip:.3f}")