from datetime import datetime
class inscripcion:
    __fecha=None
    __pago= False
    __persona=None
    __taller=None
    def __init__(self,fecha,pago,persona,taller):
        self.__fecha=fecha
        self.__pago=pago
        self.__persona=persona
        self.__taller=taller
    def buscadni(self):
        return self.__persona.getdni()
    def buscataller(self):
        return self.__taller.getnombre()
    def buscat(self):
        return self.__taller.getmonto()
    def buscaid(self):
        return self.__taller.getid()
    def listap(self):
        self.__persona.listarp()
    def modifica(self):
        self.__pago=True
    def pago(self):
        return self.__pago
    def fecha(self):
        return self.__fecha


