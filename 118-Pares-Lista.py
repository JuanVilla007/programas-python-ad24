# dad una lista de numeros, regresar los pares

def pares(lista):
    p = []
    for n in lista:
        if n % 2 == 0:
            p.append(n)
    return p

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)
res = pares(nums)
print('Los pares son ', res)