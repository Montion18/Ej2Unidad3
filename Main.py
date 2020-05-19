
from ManejadorInscr import manejadorinscripcion
from ManejaTalleres import manejadortalleres
from ManejadorPersona import manejadorpersona
from ClassPersona import persona
from datetime import datetime
import csv
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.inscribir,
                            2:self.consultainsc,
                            3:self.consultainscriptos,
                            4:self.registrarpago,
                            5:self.guardarins,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,mi,mt,mp):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mi,mt,mp)
    def salir(self):
        print('Salir')
    
    def inscribir(self,mi,mt,mp):
        n=str(input("Ingrese su nombre: "))
        d=str(input("Ingrese su direccion: "))
        dni=int(input("Ingrese su DNI: "))
        p=persona(n,d,dni)
        mp.crearlista(p)
        nom=str(input("Ingrese el nombre del taller: "))
        t=mt.getnom(nom)
        if t!= 0:
            cantvac=mt.getcant()
            fecha=datetime.today()
            mi.crearinscripcion(fecha,p,t,cantvac)
        else: print("\nNO se encontro ese taller")
    def consultainsc(self,mi,mt,mp):
        dni=str(input("Ingrese el DNI: "))
        mi.consulta(dni)
    def consultainscriptos(self,mi,mt,mp):
        id=int(input("Ingrese el id de un taller: "))
        mi.listar(id)
    def registrarpago(self,mi,mt,mp):
        dni=str(input("Ingrese un DNI para registrar el pago: "))
        mi.registrarp(dni)
    def guardarins(self,mi,mt,mp):
        datos=[]
        cant=mi.getcant()
        for j in range(cant):
            datos.append(mi.getdni(j))
            datos.append(',')
            datos.append(mi.getid(j))
            datos.append(',')
            datos.append(mi.getfecha(j))
            datos.append(',')
            datos.append(bool(mi.getpago(j)))
            datos.append("\n")
        archivo=open("copia.csv","w")
        for i in range(len(datos)):
            archivo.write(str(datos[i]))
        print("Datos Guardados")

if __name__=='__main__':
    mi=manejadorinscripcion()
    mt=manejadortalleres()
    mp=manejadorpersona()
    menu=Menu()
    salir = False
    while not salir:
        print("-----Menu-----")
        print("\n1.Inscribir una persona. ")
        print("\n2.Consultar Inscripcion. ") 
        print("\n3.Consultar inscriptos. ")
        print("\n4.Registrar pago. ")
        print("\n5.Guardar Inscripciones. ")
        op = int(input('\nIngrese una opcion: '))
        menu.opcion(op,mi,mt,mp)
        salir = op == 0