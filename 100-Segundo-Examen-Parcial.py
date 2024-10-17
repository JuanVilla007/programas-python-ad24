# Segundo examen parcial
# Computacion Aplicada
# Alumno: Juan Antonio Villa Guerrero

import os; os.system("cls")

print("Muebleria Muebles Dico")
print("Sistema de Procesamiento de Empleados")
print("\nCaptura de datos de los empleados, presiona Enter para avanzar y * para terminar: ")

emps = []

while True:
    name = input("Nombre: ")
    if name == "*": break
    edad = int(input("Edad: "))
    sex = input("Sexo (H/M): ").lower()
    sueldo = float(input("Sueldo: "))
    pt = input("Pasatiempos (separados por espacio): ").lower().split(" ")
  
    emp = {
        "Nombre": name,
        "Edad": edad,
        "Sexo": sex,
        "Sueldo": sueldo,
        "Pasatiempos": pt
    }
    emps.append(emp)

print("\nCaptura de datos terminada... ")

print("\nTabla de datos: ")

for k in emps[0].keys():
    print(f"{k:<15}", end="")
print()

for cl in emps:
    name = cl['Nombre']
    edad = cl['Edad']
    sex = cl['Sexo']
    sueldo = cl['Sueldo']
    pt = ', '.join(cl['Pasatiempos'])
    print(f"{name:<15} {edad:<15} {sex:<12} {sueldo:<15,.3f} {pt}")
print()

numm = sum(1 for e in emps if e['Sexo'] == 'm')
numh = sum(1 for e in emps if e['Sexo'] == 'h')

ptc = {}
for emp in emps:
    for pas in emp['Pasatiempos']:
        ptc[pas] = ptc.get(pas, 0) + 1

SumE = sum(e['Edad'] for e in emps)
promE = SumE / len(emps) if len(emps) > 0 else 0
SumS = sum(e['Sueldo'] for e in emps)
promS = SumS / len(emps) if len(emps) > 0 else 0

maxe = emps[0]
mine = emps[0]
for emp in emps:
    if emp['Edad'] > maxe['Edad']:
        maxe = emp
    if emp['Edad'] < mine['Edad']:
        mine = emp


print("Resumen:")
print("Empleados : ", len(emps))
print("Mujeres   : ", numm)
print("Hombres   : ", numh)
print("Pasatiempos: ", ', '.join(f"{k}/{v}" for k, v in ptc.items()))
print(f"Edad -> suma: {SumE}, Promedio: {promE:.2f}")
print(f"Sueldo -> suma: {SumS:,.3f}, promedio: {promS:,.3f}")
print(f"{maxe['Nombre']} de {maxe['Edad']} es el mayor, {mine['Nombre']} de {mine['Edad']} es el menor.")

print("Proceso Terminado.")