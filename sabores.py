class sabores:
    __num=0
    __nombre=''
    __descripcion=''
    
    
    def __init__(self,num,nom,desc):
        self.__num=num
        self.__nombre=nom
        self.__descripcion=desc
    def getnom(self):
        return self.__nombre
    def getnum(self):
        return self.__num
        
