# Diseña un programa con dos funciones que convierta: pulgadas a centímetros y metros a pies. Deberá́ mostrar un
# menú con las opciones correspondientes.
# Considere las siguientes formulas:
# centímetros = pulgadas * 2.54
# pies = metros * 3.281

def pac(pulgadas):
    return pulgadas * 2.54

# Función para convertir metros a pies
def map(metros):
    return metros * 3.281

# Programa principal
import os; os.system("cls")
while True:
    print("\nConversor de Unidades")
    print("1.- Convertir pulgadas a centímetros")
    print("2.- Convertir metros a pies")
    print("3.- Salir")

    opcion = int(input("\nElige una opción [1-3]: "))

    if opcion == 1:
        pulgadas = float(input("Ingresa el número de pulgadas: "))
        cm = pac(pulgadas)
        print(f"\n{pulgadas} pulgadas son {cm:.2f} centímetros")
    elif opcion == 2:
        metros = float(input("Ingresa el número de metros: "))
        pies = map(metros)
        print(f"\n{metros} metros son {pies:.2f} pies")
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Error. Elige entre 1 y 3.")