#Genera 2 lista de numeros aleatorios y las suma

def genera_aleatorios(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(1,100))
    return nums

def suma_listas(nums1, nums2, n):
    suma = []
    for i in range(n):
        suma.append( nums1[i] + nums2[i] )
    return suma

# programa principal
import os; os.system('cls')
import random
MAX = 10

nums1 = genera_aleatorios(MAX)
nums2 = genera_aleatorios(MAX)
suma = suma_listas(nums1, nums2, MAX)

print(f'Lista 1 : {nums1}')
print(f'Lista 2 : {nums2}')
print(f'Suma listas : {suma}')