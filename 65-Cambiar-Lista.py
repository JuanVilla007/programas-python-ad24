# Cambiar los elemntos de una lista de numeros

import os; os.system("cls")

nums = [10, 9, 8.5, 6.5, 7.5, 6.2, 9.5]

print("Cambiar o modificar los elementos de una lista")

print(type(nums))
print("La lista: ", nums, len(nums))

print("Modificar los elementos en las posiciones 0 y 1")
nums[0] = 7
nums[1] = 8
print("Resulta en: ",nums)

print("Modificar los elementos en las posiciones de 2 a 5")
nums[2:5] = [9.0, 9.0, 9]
print("Resulta en: ",nums)