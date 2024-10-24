# Calcula el promedio de una lista, luego me regresa los que son mayores al promedio

def promedio(nums):
    s = 0
    for n in nums:
        s += n
    return s / len(nums)

def maypresprom(nums, prom):
    mp = []
    for n in nums:
        if n > prom:
            mp.append(n)
    return mp

def leerdatos():
    datos=[]
    while True:
        d=int(input("Numero: "))
        if d==-1: break;
        datos.append(d)
    return datos

# Programa principal
nums = leerdatos()
import os; os.system("cls")
#nums = [9, 8, 7.5, 6, 9.5, 7, 10, 6, 7]
prom = promedio(nums)
mp = maypresprom(nums, prom)
print('\nResumen \n')
print(f'Lista de números: {nums} y son {len(nums)}')
print(f'El promedio : {prom}')
print(f'Mayores promedio : {mp} y son {len(mp)}')