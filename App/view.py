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


#Imprimir información de respuesta

def printProductionCompany(production): #Imprime las peliculas de una productora de cine determinado
    t1_start = process_time()
    if production:
        print('Productora de cine:' + production)
        print('Promedio: ' + str(production['vote_average']))
        print('Total de peliculas: ' + str(lt.size(production['movies'])))
        iterator = it.newIterator(production['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'])
    else:
        print('No se encontro la productora de cine en el catalogo')
    t1_stop = process_time()
    print ("Tiempo de ejecucion:", t1_stop-t1_start,"segundos")

def printDirectorData(director): #Imprime las peliculas de un director determinado
    t1_start = process_time()
    if director:
        print('Director:' + director)
        print('Promedio:' + str(director['vote_average']))
        print('Total de peliculas: ' + str(lt.size(director['movies'])))
        iterator = it.newIterator(director['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'])
    else:
        print('No se encontro el director en el catalogo')
    t1_stop = process_time()
    print ("Tiempo de ejecucion:", t1_stop-t1_start,"segundos")

def printActorData(actor): #Imprime las peliculas de un actor determinado
    t1_start = process_time()
    if actor:
        print('Actor encontrado: ' + actor)
        print('Promedio: ' + str(actor['vote_average']))
        print('Total de peliculas: ' + str(lt.size(actor['movies'])))
        iterator = it.newIterator(actor['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'])
    else:
        print('No se encontro el actor en el catalogo')
    t1_stop = process_time()
    print ("Tiempo de ejecucion:", t1_stop-t1_start,"segundos")

def printGenreData(genero): #Imprime las peliculas de un genero cinematografico determinado
    t1_start = process_time()
    if genero:
        print('Genero cinematografico: ' + genero)
        print('Promedio: ' + str(genero['vote_count']))
        print('Total de peliculas: ' + str(lt.size(genero['movies'])))
        iterator = it.newIterator(genero['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'])
    else:
        print('No se encontro el genero cinematografico en el catalogo')
    t1_stop = process_time()
    print ("Tiempo de ejecucion:", t1_stop-t1_start,"segundos")

def printMoviesbyCountry(country): #Imprime las peliculas que han sido producidas en un pais
    t1_start = process_time()
    print('Se encontraron: ' + str(lt.size(country)) + ' peliculas')
    iterator = it.newIterator(country)
    while it.hasNext(iterator):
        movie = it.next(iterator)
        print(movie['original_title'])
    t1_stop = process_time()
    print ("Tiempo de ejecucion:", t1_stop-t1_start,"segundos")

#Menu principal

def printMenu():
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Descubrir productoras de cine")
    print("4- Enteder un género")
    print("0- Salir")

#Ejecutar menu principal

while True:
    printMenu()
    
    inputs =input('Seleccione una opción para continuar\n')
    
    if int(inputs[0])==1: #opcion 1
        catalogo = controller.initCatalogo()
        data = True
        controller.loadData(files, catalogo)
    
    elif int(inputs[0]) == 2:  #opcion 2
        productora = input("\nIngrese el nombre de la productora: ")
        controller.iniciarDescubrirProductoras(catalogo, productora)
    
    elif int(inputs[0]) == 4: #opcion 4
        genero = input("\nIngrese el género: ")
        controller.iniciarEntenderGenero(catalogo, genero)

    else:
        sys.exit(0)
sys.exit(0)

