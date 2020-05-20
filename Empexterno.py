from ClaseEmpleado import empleado
class empleadoexterno(empleado):
    __tarea=''
    __fechai=None
    __fechaf=None
    __montoviatico=0.0
    __costoobra=0.0
    __segurodevida=0.0
    def __init__(self,dni,nom,direc,tel,tarea,fechai,montov,costoo,segurov,fechaf=None):
        super().__init__(dni,nom,direc,tel)
        self.__tarea=tarea
        if fechaf=='':
            self.__fechaf=None
        else: self.__fechaf=fechaf
        self.__fechai=fechai
        self.__montoviatico=montov
        self.__costoobra=costoo
        self.__segurodevida=segurov
    def getsueldo(self):
        return int(self.__costoobra)-int(self.__montoviatico)-int(self.__segurodevida)
    def gettarea(self):
        return self.__tarea
    def getcosto(self):
        return self.__costoobra
    def getfechaf(self):
        return self.__fechaf
    def mostrar(self):
        print("Nombre:",super().getnom().ljust(10,' '),"DNI:",super().retornadni().center(10,' '),"DIRECCION:",super().getdirec().rjust(5,' '),"\n")

    def datos(self):
        print("Nombre:",super().getnom().ljust(10,' '),"TELEFONO:",super().gettel().center(5,' '))
