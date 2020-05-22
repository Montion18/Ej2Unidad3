from Manejador import manejador
if __name__=='__main__':
    m=manejador()
    m.InsertarElemento("uno",0)
    m.InsertarElemento("dos",1)
    m.InsertarElemento("tres",2)
    m.AgregarElemento("cuatro")
    m.AgregarElemento("cinco")
    m.MostrarElemento(0)
    m.MostrarElemento(1)
    m.MostrarElemento(2)
    m.MostrarElemento(3)
    m.MostrarElemento(4)
    #elementos Incorrectos
    print("----------------------")
    m.InsertarElemento("mal",5)
    m.MostrarElemento(5)