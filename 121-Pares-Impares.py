# Dada una lista de nuemros devolver los pares y los impares

def pares_impares(nums):
    pares=[]
    impares=[]
    for n in nums:
        if n % 2 == 0 : pares.append(n)
        else: impares.append(n)
    return pares, impares

# Programa principal
import os; os.system('cls')

nums = [9, 8, 60, 6, 90, 7, 10, 6, 7]
pares, impares = pares_impares(nums)
print(f'La numeros : {nums} -> {len(nums)}')
print(f'Los pares : {pares} -> {len(pares)}')
print(f'Los impares: {impares} -> {len(impares)}')