from ClaseEmpleado import empleado
import datetime
class empleadocontratado(empleado):
    __fechaini=None
    __fechafin=None
    __canthoras=0
    valorxhora=350
    def __init__(self,dni,nom,direc,tel,fechai,fechaf,canth):
        super().__init__(dni,nom,direc,tel)
        self.__fechaini=fechai
        self.__fechafin=fechaf
        self.__canthoras=int(canth)
    def getcanth(self):
        return self.__canthoras
    def getdni(self):
        return super().retornadni()
    def incrementarhora(self,hs):
        self.__canthoras+=int(hs)
        print("Horas incrementadas")
    def mostrar(self):
        print("Nombre:",super().getnom().ljust(10,' '),"DNI:",super().retornadni().center(10,' '),"DIRECCION:",super().getdirec().rjust(5,' '),"\n")
    def datos(self):
        print("Nombre:",super().getnom().ljust(10,' '),"TELEFONO:",super().gettel().center(5,' '))
    @classmethod
    def getvalorhora(cls):
        return cls.valorxhora

    
