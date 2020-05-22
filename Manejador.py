from zope.interface import Interface
from zope.interface import implementer
from ClaseInterfaz import Iinterfaz
@implementer(Iinterfaz)

class manejador(object):
    __lista=[]
    def __init__(self):
        self.__lista=[' ']
    def InsertarElemento(self,obj,pos):
        try:
            if self.__lista[pos]==None or self.__lista[pos] ==" ":
                self.__lista.insert(pos,obj)
                print("\nElemento agregado")
            else: print("\nYa existe un elemento en dicha posicion")
            
        except IndexError:
            print("\nERROR la posicion ingresada supera el tamaño")


    def AgregarElemento(self,obj):
        for cont in range(len(self.__lista)):
            i=cont
        if self.__lista[i]==None or self.__lista[i]==" ":
            self.__lista.pop(i)
        self.__lista.append(obj)
        print("\nElemento Agregado")


    def MostrarElemento(self,pos):
        try:
            print(self.__lista[pos])
        except IndexError:
            print("\nError no existe un elemento en dicha posicion")