from Helado import helado
import operator
class ManejaHelados:
    __lista=[]
    
    def registrarventa(self,gramos,sabores):
        h=helado(gramos,sabores)
        self.__lista.append(h)
        
    def cont_sabores(self):
        max=[]
        for i in range(len(self.__lista)):
            aux=self.__lista[i].getsabor().split(',',4)
            for j in range(len(aux)):
                cont=0
                
                for x in range(len(self.__lista)):
                   cont+=self.__lista[x].getsabor().count(aux[j])
                
                if max.count(aux[j])==0:   #No cargar dos veces el mismo sabor
                    max.extend((aux[j],cont))
            
        #Ordena la lista
        for i in range(0, len(max)):  
            for j in range(0, len(max)-2,2): 
                if (max[j+1] < max[j+3]): 
                    sab = max[j]
                    cant= max[j+1]
                    max[j]=max[j+2]
                    max[j+1]=max[j+3]
                    max[j+2]= sab  
                    max[j + 3]= cant  
               
        print("\n---------------------")
        q=0
        print("\nHelados mas pedidos: \n ")
        for t in range(0,len(max),2):
            if q<=5:
                print("{}: {}".format(q+1,max[t]))
                q+=1
    def estimagramos(self,sabor):
        gtotal=0
        for i in range(len(self.__lista)):
            aux=self.__lista[i].getsabor().split(',',4)
            for j in range(len(aux)):
                if aux[j]==sabor:
                    gtotal+=self.__lista[i].getgramos()/(len(aux))
                    
        print("\nPara el sabor:",sabor,"se vendieron:",gtotal,"gr.")
                

    def masvendidostamaño(self,tam):
        sab=[]
        print("--Sabores--")
        for i in range(len(self.__lista)):
            if self.__lista[i].getgramos()==tam:
                aux=self.__lista[i].getsabor().split(',',4)
            for j in range(len(aux)):
                if sab.count(aux[j])==0:
                    sab.append(aux[j])
        for k in range(len(sab)):
            print("-",sab[k])