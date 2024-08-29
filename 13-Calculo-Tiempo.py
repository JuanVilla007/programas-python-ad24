# Calcular el equivalente en dias, minutos y segundos de la cantidad dada en horas
import os; os.system('cls')

print("Calcula el tiempo en dias, minutos y segundos")

h = float(input("Dame el total de horas: "))

d = h / 24
m = h * 60
s = m * 60

print(f"Dias: {d:.3f}")
print(f"Minutos: {m:,.3f}")
print(f"Segundos: {s:,.3f}")