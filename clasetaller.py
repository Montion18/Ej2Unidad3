class taller:
    __id=0
    __nom=''
    __vacante=0
    __montoins=0

    def __init__(self,id,nom,vacante,monto):
        self.__id=id
        self.__nom=nom
        self.__vacante=vacante
        self.__montoins=monto

    def getv(self):
        return self.__vacante
    def getnombre(self):
        return self.__nom
    def modvac(self):
        self.__vacante=int(self.__vacante)-1
    def getmonto(self):
        return self.__montoins
    def getid(self):
        return self.__id


