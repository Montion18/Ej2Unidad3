import numpy as np
from ClaseInscripcion import inscripcion
from ClassPersona import persona
class manejadorinscripcion:
    __arregloins=None
    __cant=0
    def creararreglo(self,mt):
        cantt=mt.getcant()
        self.__arregloins=np.empty(cantt, dtype=inscripcion)

    def registrarinscripcion(self,fecha,p,t,pago=None):
        if int(t.getv())>0:
            ins=inscripcion(fecha,pago,p,t)
            self.__arregloins[self.__cant]=ins
            t.modvac()
            self.__cant+=1
            print("\n----Inscripcion registrada----")
        else:
            print("\nERROR,No hay mas vacantes en este taller")

    def consulta(self,dni):
        i=0
        while i<int(self.__cant) and str(self.__arregloins[i].buscadni())!= dni:
            i+=1
        if i<self.__cant:
            print("\n----Persona Inscripta----")
            print("\nTaller: ",self.__arregloins[i].buscataller())
            if bool(self.__arregloins[i].pago())==False:
                print("\nMonto: ",self.__arregloins[i].buscat())
            else:
                    print("\nMonto: 0")
        else:
            print("Persona NO inscripta")
               
    def listar(self,id):
        for i in range(self.__cant):
            if int(self.__arregloins[i].buscaid())==id:
                self.__arregloins[i].listap()
            else: print("No se encontraron personas inscriptas en ese taller")
    
    def registrarp(self,dni):
        i=0
        while i<self.__cant and str(self.__arregloins[i].buscadni())!=dni:
            i+=1
        if i<self.__cant:
            self.__arregloins[i].modifica()
            print("--Pago Registrado--")
        else:
            print("Persona NO inscripta")
        
    def getcant(self):
        return self.__cant
    def getdni(self,i):
        return self.__arregloins[i].buscadni()
    def getid(self,i):
        return self.__arregloins[i].buscaid()
    def getfecha(self,i):
        return self.__arregloins[i].fecha()
    def getpago(self,i):
        return self.__arregloins[i].pago()
        

                

