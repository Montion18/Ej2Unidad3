from ManejadorEmpleados import Manejadorempleados
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, m):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(m)
    def salir(self):
        print('Salir')
    
    def opcion1(self,m):
        dni=str(input("\nIngrese el DNI de un empleado: "))
        h=int(input("\nIngrese las horas trabajadas hoy: "))
        m.buscaempleado(dni,h)

    def opcion2(self,m):
        tarea=str(input("Ingrese una tarea: "))
        m.buscatarea(tarea)
    def opcion3(self,m):
        m.ayuda()
    def opcion4(self,m):
        m.mostrarsueldos()


if __name__=='__main__':
    cant=int(input("\nIngrese la cantidad de empleados: "))
    m=Manejadorempleados(cant)
    m.Cargarempleados()
    
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n")
        print("\n1.Registrar horas")
        print("\n2.Total de tarea")
        print('\n3.Ayuda')
        print("\n4.Calcular Sueldo")
        print("\n0.Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op,m)
        salir = op == 0
    print(salir)