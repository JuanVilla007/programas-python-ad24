# Imprime el factorial de un número

import os; os.system("cls")

print('Imprime el factorial de un número ')
n = int(input('De que numero deseas el factorial? '))
f = 1

print(f"{n}! = ", end=" ")

for i in range(1, n+1):
    f = f * i 
    print(f"{i} {"x" if i!=n else ""}", end=" ")

print(f"= {f}")