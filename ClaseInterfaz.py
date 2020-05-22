from zope.interface import Interface
from zope.interface import implementer


class Iinterfaz(Interface):
    def InsertarElemento(objeto,pos):
        pass
    def AgregarElemento(objeto):
        pass
    def MostrarElemento(pos):
        pass
