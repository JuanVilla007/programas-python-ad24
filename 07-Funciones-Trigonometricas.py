# Calcula las funciones trigonometricas sobre un angulo

import math as mt

print('Calculo de las funciones trigonometricas sobre un angulo')
print('Dame un angulo: ')

angulod = float(input())
angulor = mt.radians(angulod)

print(f"Angulo original: {angulod} ,  Angulo en radianes : {angulor}")

seno = mt.sin(angulor)
coseno = mt.cos(angulor)
tangente = mt.tan(angulor)
grados = mt.degrees(angulor)

salida=('Resumen de funciones trigonometricas\n'
f'El seno es {seno:.3f}\n'
f'El coseno es {coseno:.3f}\n'
f'La tangente es {tangente:.3f}\n')

print(salida)