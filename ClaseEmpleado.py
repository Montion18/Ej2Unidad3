class empleado(object):
    __DNI=''
    __nombre=''
    __direccion=''
    __telefono=''
    def __init__(self,dni,nom,direc,tel):
        self.__DNI=dni
        self.__nombre=nom
        self.__direccion=direc
        self.__telefono=tel
    def retornadni(self):
        return self.__DNI
    def getnom(self):
        return self.__nombre
    def getdirec(self):
        return self.__direccion
    def gettel(self):
        return self.__telefono