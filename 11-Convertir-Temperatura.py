# Conversion de temperaturas de centigrados a farenheit
import os; os.system('cls')

print('Convirtiendo de Celsius a Farenheit:')

temp = float(input('Dame los grados Celsius: '))
res = (temp * 9/5)+32
print(f'{temp}° Celsius equivale a {res}° Farenheit')
