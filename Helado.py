class helado:
    __gramos=0
    __sabores=[]
    def __init__(self,g,sabor=None):
        self.__gramos=g
        self.__sabores=sabor
    def getsabor(self):
        return self.__sabores
    def getgramos(self):
        return self.__gramos