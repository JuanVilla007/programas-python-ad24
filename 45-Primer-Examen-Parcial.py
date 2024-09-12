# Primer Examen Parcial
# Juan Antonio Villa Guerrero
# Computacion Aplicada

#Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo
#de usuario, paquete y cantidad.
#Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500
#Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900
#Se debe calcular un subtotal de la venta sumando el precio del tipo de usuario más el precio de tipo de paquete,
#y multiplicando por la cantidad solicitada.
#Se otrgará un descuento siempre y cuando el subtotal sea mayor a 5,000 y de acuerdo a lo siguiente
# Es Alumno 20%
# Es Trabajador y un 10%
# Es Docente y un 5%
#Al final mostrar un resumen con los datos calculados de la venta.
#Al terminar de procesar las ventas mostrar el total de ventas del día:

import os; os.system("cls")

tf = 0

while(True):
    print("Universidad Patito SA de CV")
    print("Sistema de Inscripción a la Presentacion de Proyectos: ")

    name = input("Dime tu nombre: ")
    print("Tipo de usuario: 1.-Alumno $100,   2.-Trabajador $200,   3.-Docente $500")
    tip = int(input("Que tipo de usuario eres? ( 1 / 2 / 3 ): "))
    des = 0
    tot = 0
    por = 0

    if tip > 3 or tip < 1:
        print("Opcion Incorrecta...")
        print("Proceso Terminado...")
    else:
        print("Tipo de paquete: 1.-Solo conferencias $600, 2.-Con eventos sociales $800, 3.-Con kit de acceso $900")
        paq = int(input("Que tipo de paquete necesitas? ( 1 / 2 / 3 ): "))
        if paq > 3 or paq < 1:
            print("Opcion Incorrecta...")
            print("Proceso Terminado...")
        else:
            can = int(input("Cuantos paquetes? "))

            if tip == 1:
                usu = "Alumno"
                if paq == 1:
                    tp = "Solo Conferencias"
                    sub = (100+600)*can
                elif paq == 2:
                    tp = "Con Eventos Sociales"
                    sub = (100+800)*can
                else:
                    tp = "Con Kit de Acceso"
                    sub = (100+900)*can
            elif tip == 2:
                usu = "Trabajador"
                if paq == 1:
                    tp = "Solo Conferencias"
                    sub = (200+600)*can
                elif paq == 2:
                    tp = "Con Eventos Sociales"
                    sub = (200+800)*can
                else:
                    tp = "Con Kit de Acceso"
                    sub = (200+900)*can
            else:
                usu = "Docente"
                if paq == 1:
                    tp = "Solo Conferencias"
                    sub = (500+600)*can
                elif paq == 2:
                    tp = "Con Eventos Sociales"
                    sub = (500+800)*can
                else:
                    tp = "Con Kit de Acceso"
                    sub = (500+900)*can
        
            if sub > 5000:
                if tip == 1:
                    des = sub * 0.2
                    tot = sub - (sub*0.2)
                    por = 20    
                elif tip == 2:
                    des = sub * 0.1
                    tot = sub - (sub*0.1)
                    por = 10
                else:
                    des = sub * 0.05
                    tot = sub - (sub*0.05)
                    por = 5
            else:
                tot = sub
        
            print(f"{name} tu pedido fueron {can} paquetes. Tipo de Usuario: {usu}. Tipo de paquete: {tp}")
            print(f"Subtotal: {sub:.2f} con un descuento de: {des:.2f} ({por}%) y un total de {tot:.2f}")
            tf = tf + tot

    if input("Deseas continuar (S/N) ").upper().startswith("N"): break

print(f"Importe Total de la venta: {tf:.2f}")

print("Proceso terminado ...")