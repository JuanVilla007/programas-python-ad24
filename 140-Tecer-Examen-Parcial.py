# La Academia de futbol Santos Laguna, desea llevar el control de los jugadores en cada
# categoría, las categorías se conforman de acuerdo con la edad y pueden tener varios
# jugadores. Diseña una aplicación en Python, usando los conceptos aprendidos sobre
# programación orientada a objetos.

class Jugador:
    def __init__(self, nombre, AnoNac, sexo, becado):
        self.nombre=nombre
        self.AnoNac=AnoNac
        self.sexo=sexo
        self.becado=becado
        self.total=1
        self.ContHom=0
            
    def __str__(self):
        return f"Nombre: {self.nombre:<20} AñoNac: {self.AnoNac:<7} Sexo: {self.sexo:<8} Becado: {self.becado:<12} "
    
class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre=nombre
        self.rango=rango
        self.costo=costo
        self.jugadores=list()
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)
    def totalJugadores(self):
        total=0
        for jugador in self.jugadores:
            total += jugador.total
        return total
    def ContarGen(self):
        hom = sum(1 for jugador in self.jugadores if jugador.sexo == "Hombre")
        muj = sum(1 for jugador in self.jugadores if jugador.sexo == "Mujer")
        return hom, muj
    def subC(self):
        subtotal = sum(self.costo for jugador in self.jugadores if jugador.becado.lower() != "becado")
        return subtotal
    
    def __str__(self):
        return f"{self.nombre:<20} - {self.rango:<20} -   ({self.totalJugadores()})"
    
class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre=nombre
        self.propietario=propietario
        self.domicilio=domicilio
        self.categorias=list()
    def agregarCategoria(self, categoria):
        self.categorias.append(categoria)
    def contTot(self):
        totalH = 0
        totalM = 0
        for categoria in self.categorias:
            hom, muj = categoria.ContarGen()
            totalH += hom
            totalM += muj
        return totalH, totalM
    def TA(self):
        total = sum(categoria.subC() for categoria in self.categorias)
        return total
    
    def __str__(self):
        return f"Nombre: {self.nombre} \nPropietario: {self.propietario} \nDomicilio: {self.domicilio}"
        

def main():
    import os; os.system("cls")
    
    #Crear la academia, con 3 categoria iniciales y sus jugadores
    miacademia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidraulica")
    miacademia.agregarCategoria(Categoria("Junior A", "2006/2007/2008", 1250))
    miacademia.categorias[0].agregarJugador(Jugador("Alexander Lopez", 2006, "Hombre", "Sin beca"))
    miacademia.categorias[0].agregarJugador(Jugador("Uriel Puga", 2007, "Hombre", "Becado"))
    miacademia.categorias[0].agregarJugador(Jugador("Alejandra Escalona", 2008, "Mujer", "Sin beca"))

    miacademia.agregarCategoria(Categoria("Junior B", "2009/2010/2011", 850))
    miacademia.categorias[1].agregarJugador(Jugador("Armando Santana", 2009, "Hombre", "Sin beca"))
    miacademia.categorias[1].agregarJugador(Jugador("Daniel Mijares", 2010, "Hombre", "Sin beca"))
    miacademia.categorias[1].agregarJugador(Jugador("Antonia Hernandez", 2011, "Mujer", "Becado"))

    miacademia.agregarCategoria(Categoria("Pony A", "2012/2013/2014", 700))
    miacademia.categorias[2].agregarJugador(Jugador("Andrea Solis", 2006, "Mujer", "Becado"))
    miacademia.categorias[2].agregarJugador(Jugador("Marissa Hernandez", 2007, "Mujer", "Becado"))
    miacademia.categorias[2].agregarJugador(Jugador("Diana Soto", 2008, "Mujer", "Sin beca"))

    totalH, totalM = miacademia.contTot()


    # Se imprime un reporte con el total de categoerias y sus jugadores
    print("\nReporte del club deportivo:\n", miacademia)
    print("\nDatos generales de las Categorías:\n")
    print("Nombre: Junior A       Rango: 2006/2007/2008       Costo: $1,250.00")
    print("Nombre: Junior B       Rango: 2009/2010/2011       Costo: $850.00")
    print("Nombre: Pony A         Rango: 2012/2013/2014       Costo: $700.00")

    print("\nTotal de Categorias: ", len(miacademia.categorias))
    print("Total de Hombres: ", totalH)
    print("Total de Mujeres: ", totalM)

    print("\n-Jugadores por categoria:")
    for categoria in miacademia.categorias:
        print(categoria)
        for jugador in categoria.jugadores:
            print(jugador)
        print()
        print(f"Subtotal: ${categoria.subC():,.2f}")
        print()

    print(f"\nTotal: ${miacademia.TA():,.2f}")

if __name__ == "__main__":
    main()