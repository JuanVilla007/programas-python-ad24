# Verificar si la suma de 2 numeros es igual a un tercero
import os; os.system('cls')

print('Varificar si la suma de dos numeros es igual a un tercero')

n1 = int(input('Dame el numero 1: '))
n2 = int(input('Dame el numero 2: '))
n3 = int(input('Dame el numero 3: '))

if n1+n2==n3:
    print('Si son iguales!')
else:
    print('Son distintos!')