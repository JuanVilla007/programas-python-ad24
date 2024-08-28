# Calcular la paga de un trabajador considerando las horas extras
import os; os.system('cls')

print('Calculando la paga de las horas extra de un trabajador (se pagan al doble)...')

nom=input('Dame tu nombre: ')
horas=int(input('Horas trabajdas: '))
paga=float(input('Paga x hora: '))
tasa=0.03
paganormal = 0
pagaextra = 0
pagabruta = 0
hextra = 0

if horas > 40:
    hextra = horas -48
    paganormal = 40 * paga
    pagaextra = hextra * paga * 2
    pagabruta = paganormal + pagaextra
else:
    pagabruta=horas * paga
    paganormal=pagabruta

imp = pagabruta * tasa
paganeta= pagabruta-imp

print(f'El trabajador {nom}, trabajo {horas} horas a una paga de {paga:.2f}')
print(f'Horas extra: {hextra}, Paga normal: {paganormal}, Paga extra: {pagaextra}')
print(f'Paga bruta: {pagabruta:.2f}')
print(f'Impuesto: {imp:.2f}')
print(f'Paga Neta: {paganeta:.2f}')