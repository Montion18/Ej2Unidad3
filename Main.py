from ManejaHelados import ManejaHelados
from ManejadorSabores import Manejadorsabores
class menu:
    __switcher=None
    def __init__(self):
        self.__switcher={0:self.salir,
                         1:self.registrarventa,
                         2:self.muestramasvendido,
                         3:self.muestragramos,
                         4:self.muestrasabor
            }
    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Saliendo')

    def muestramasvendido(self):
        m.cont_sabores()
        

    def registrarventa(self):
        p=int(input("Ingrese el Peso del helado "))
        print("--Lista Sabores disponibles--")
        sab.muestrasabores()
        s=str(input("\nIngrese el nombre de los sabores separados por comas: "))
        m.registrarventa(p,s)
        print("venta registrada")

    def muestragramos(self):
        num=int(input("\nIngrese el numero de un sabor "))
        sabor=sab.cantidaddegramos(num)
        if sabor == 0:
            print("ERROR Ingrese un numero correcto")
        else:
            m.estimagramos(sabor)

    def muestrasabor(self):
        gr=int(input("\nIngrese el tamaño: "))
        m.masvendidostamaño(gr)

if __name__ == '__main__':
    menu=menu()
    m=ManejaHelados()
    sab=Manejadorsabores()
    sab.Crearsabor()
    salir = False
    while not salir:
        print("---Menu---")
        print("\n0.para salir")
        print("\n1.Registrar Venta")
        print("\n2.Muestra mas vendidos")
        print("\n3.Estimar gramos vendidos")
        print("\n4.Muestra segun tipo de helado")
        op = int(input('\nIngrese una opcion: '))
        menu.opcion(op)
        salir = op == 0
    