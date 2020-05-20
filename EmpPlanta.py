from ClaseEmpleado import empleado
class empleadodeplanta(empleado):
    __sueldobasico=0.0
    __antiguedad=0
    def __init__(self,dni,nom,direc,tel,sb,ant):
        super().__init__(dni,nom,direc,tel)
        self.__sueldobasico=sb
        self.__antiguedad=ant
    
    def getsueldo(self):
        s=int(self.__sueldobasico)
        a=int(self.__antiguedad)
        return (s+(s*1/100))*(a)
    def mostrar(self):
        print("Nombre:",super().getnom().ljust(10,' '),"DNI:",super().retornadni().center(10,' '),"DIRECCION:",super().getdirec().rjust(5,' '),"\n")

    def datos(self):
        print("Nombre:",super().getnom().ljust(10,' '),"TELEFONO:",super().gettel().center(5,' '))