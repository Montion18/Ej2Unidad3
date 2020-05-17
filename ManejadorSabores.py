from sabores import sabores
import csv
class Manejadorsabores:
    __lista=[]

    def Crearsabor(self):
        archivo=open("sabores.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            s=sabores(fila[0],fila[1],fila[2])
            self.__lista.append(s)
                        
    def muestrasabores(self):
        for i in self.__lista:
            print("Sabor: ",i.getnom())

    def cantidaddegramos(self,num):
        i=0
        bandera=False
        while i<len(self.__lista):
            if num == int(self.__lista[i].getnum()):
                bandera=True
                i+=1
            else:
                i+=1
        if bandera==True:
            return self.__lista[num-1].getnom()
        else: return 0
           
           
        
          
        

        
       
