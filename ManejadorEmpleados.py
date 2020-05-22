from ClaseEmpleado import empleado
from EmpPlanta import empleadodeplanta
from EmpContratado import empleadocontratado
from Empexterno import empleadoexterno
import numpy as np
import datetime
import csv
class Manejadorempleados:
    __cantidad=0
    __dimension=0
    __arreglo=None
    def __init__(self,dimension):
        self.__arreglo=np.empty(dimension,dtype=empleado)
        self.__cantidad=0
        self.__dimension=dimension
    def guardar(self,empleado):
        self.__arreglo[self.__cantidad]=empleado
        self.__cantidad+=1

    def Cargarempleados(self):
        archivo=open('planta.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            empP=empleadodeplanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.guardar(empP)
        archivo.close()

        archivo=open('contratados.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            empC=empleadocontratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            self.guardar(empC)
        archivo.close()

        archivo=open('externos.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            empE=empleadoexterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])
            self.guardar(empE)
        archivo.close

    def buscaempleado(self,dni,hs):
        i=0
        while i<len(self.__arreglo):
            if type(self.__arreglo[i])==empleadocontratado:
                if dni== self.__arreglo[i].retornadni():
                    self.__arreglo[i].incrementarhora(hs)
                    i=len(self.__arreglo)+1
                else: i+=1
            else: i+=1
        if i==len(self.__arreglo):
            print("\nEl empleado que ingreso no se encontro o no es empleado contratado")

    def buscatarea(self,tarea):
        i=0
        while i<len(self.__arreglo):
            if type(self.__arreglo[i])==empleadoexterno:
                if tarea==self.__arreglo[i].gettarea():
                    if self.__arreglo[i].getfechaf()!= None:
                        print("Costo:",self.__arreglo[i].getcosto())
                        i=len(self.__arreglo)+1
                    else: 
                        print("Tarea no finalizada")
                        i=len(self.__arreglo)+1
                else: i+=1
            else: i+=1
        if i==len(self.__arreglo):
            print("\nError nombre de la tarea incorrecto")

    def ayuda(self):
        for i in range(len(self.__arreglo)):
            if type(self.__arreglo[i])==empleadocontratado:
                sueldo=self.__arreglo[i].getsueldo()
                if sueldo<25000:
                    self.__arreglo[i].mostrar()
            else:
                sueldo=self.__arreglo[i].getsueldo()
                if sueldo<25000:
                    self.__arreglo[i].mostrar()

    def mostrarsueldos(self):
        for i in range(len(self.__arreglo)):
            if type(self.__arreglo[i])==empleadocontratado:
                sueldo=self.__arreglo[i].getsueldo()
                print("\n")
                self.__arreglo[i].datos()
                print("Sueldo:",sueldo)
            else:
                sueldo=self.__arreglo[i].getsueldo()
                print("\n")
                self.__arreglo[i].datos()
                print("Sueldo:",sueldo)


                    
    
                





        


    