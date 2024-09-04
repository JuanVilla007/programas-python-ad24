# Aceptar Estudiante en base a su edad y sus calificaciones
import os; os.system('cls')

print('Universad Autonoma De Zacatecas')
print('Aceptar un estudiante en base a su edad y 2 calificaciones')

nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

if edad >= 18:
    print('Dame 2 calificaciones separadas por enter:')
    c1, c2 = int(input()), int(input())
    if c1 >= 8 and c2 >= 8:
        print(f'{nombre}, bienvenid@ a la UAZ. Tu edad {edad} y calificaciones {c1} y {c2} lo permiten.')
    else:
        print('Solo aceptamos alumnos con calificaciones mayores a 8.')
else:
    print('Solo aceptamos mayores de 18.')

print('Gracias por usar este programa')