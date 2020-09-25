import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from time import process_time 

#Ruta archivos .csv

files = ("Data/SmallMoviesDetailsCleaned.csv", "Data/AllMoviesCastingRaw.csv")

#Menu principal

def printMenu():
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Descubrir productoras de cine")
    print("4- Entender un género")
    print("0- Salir")

#Ejecutar menu principal

while True:
    printMenu()
    
    inputs =input('Seleccione una opción para continuar\n')
    
    if int(inputs[0])==1: #opcion 1
        t1_start = process_time()
        catalogo = controller.initCatalogo()
        data = True
        controller.loadData(files, catalogo)
        t1_stop = process_time()
        print ("\nTiempo de ejecucion:", t1_stop-t1_start,"segundos")
    
    elif int(inputs[0]) == 2:  #opcion 2
        t1_start = process_time()
        productora = input("\nIngrese el nombre de la productora: ")
        controller.iniciarDescubrirProductoras(catalogo, productora)
        t1_stop = process_time()
        print ("\nTiempo de ejecucion:", t1_stop-t1_start,"segundos")
        
    elif int(inputs[0]) == 4: #opcion 4
        t1_start = process_time()
        genero = input("\nIngrese el género: ")
        controller.iniciarEntenderGenero(catalogo, genero)
        t1_stop = process_time()
        print ("\nTiempo de ejecucion:", t1_stop-t1_start,"segundos")

    else:
        sys.exit(0)

sys.exit(0)
