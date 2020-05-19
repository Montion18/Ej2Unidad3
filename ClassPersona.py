class persona:
    __nombre=''
    __direc=''
    __dni=''
    def __init__(self,nom,direc,dni):
        self.__nombre=nom
        self.__direc=direc
        self.__dni=dni
    def getdni(self):
        return self.__dni
    def listarp(self):
        print("\n---Alumno---")
        print("Nombre:   ",self.__nombre)
        print("Direccion:",self.__direc)
        print("DNI:      ",self.__dni)

