# Conversion de temperaturas de centigrados a farenheit o viceversa
import os; os.system('cls')

print('Conversion de temperaturas entre Celsius y Farenheit')
print('[1]   Convertir de Farenheit a Celsius')
print('[2]   Convertir de Celsius a Farenheit')
op = int(input('Elige una opcion: '))

if op == 1:
    print('Convirtiendo de Farenheit a Celsius:')
    temp = float(input('Dame los grados Farenheit: '))
    res = (temp - 32)*5/9
    print(f'{temp}° Farenheit equivale a {res}° Celsius')
else:
    print('Convirtiendo de Celsius a Farenheit:')
    temp = float(input('Dame los grados Celsius: '))
    res = (temp * 9/5)+32
    print(f'{temp}° Celsius equivale a {res}° Farenheit')
