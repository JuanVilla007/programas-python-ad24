# Calcular el numero de la suerte sumando los digitos individuales del año de nacimiento
import os; os.system('cls')

print("Calcula el numero de la suerte")

a = int(input("Dame tu año de nacimiento: "))

m = a // 1000
c = (a - ( m *1000 ) ) // 100
d = ( a - ( m * 1000 + c *100) ) // 10
u = ( a -( m * 1000  + c * 100 + d * 10 ))

nums = m + c + d + u

print("El numero desglosado es:")
print("Unidades de millar: ", m)
print("Centenas: ", c)
print("Decenas: ", d)
print(f"Unidades: {u}")

print(f"Tu numero de la suerte es: {nums}")
