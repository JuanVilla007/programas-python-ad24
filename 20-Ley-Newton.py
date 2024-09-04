# Calcular la segunda ley de Newton
import os; os.system('cls')

print('Calculando los valores de la segunda ley de Newton')
print('[F] Calcular la fuerza   f = m * a')
print('[M] Calcular la masa   m = f / a')
print('[A] Calcular la aceleración   a = f / m')

op = input('Elige una opción: ').upper()

if op == 'F':
    print('\nCalculando la fuerza...')
    m = float(input('Dame la masa: '))
    a = float(input('Dame la aceleración: '))
    f = m * a
    print(f'La fuerza es {f}')
elif op == 'M':
    print('\nCalculando la masa...')
    f = float(input('Dame la fuerza: '))
    a = float(input('Dame la aceleración: '))
    m = f / a
    print(f'La masa es {m}')
elif op == 'A':
    print('\nCalculando la aceleración...')
    f = float(input('Dame la fuerza: '))
    m = float(input('Dame la masa: '))
    a = f / m
    print(f'La aceleración es {a}')
else:
    print('Opcion Invalida')

print('Proceso Terminado')