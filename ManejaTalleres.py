from clasetaller import taller
import numpy as np
import csv
class manejadortalleres:
    __cant=0
    __dim=0
    __arreglo=None
    
    def __init__(self):
        archivo=open("Talleres.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            if self.__dim==0:
                self.__dim=int(fila[0])
                self.__arreglo=np.empty(self.__dim, dtype=taller)
            else:
                if self.__cant<self.__dim:
                    ta=taller(fila[0],fila[1],fila[2],fila[3])
                    self.__arreglo[self.__cant]=ta
                    self.__cant+=1
    def getnom(self,nom):
        i=0
        while i<self.__cant and self.__arreglo[i].getnombre() != nom:
            i+=1
        if i<self.__cant:
            return self.__arreglo[i]
        else:
            return 0
    def getcant(self):
        total=0
        for i in range(len(self.__arreglo)):
            total+=int(self.__arreglo[i].getv())
        return total


    


