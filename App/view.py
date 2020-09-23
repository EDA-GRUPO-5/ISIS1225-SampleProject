import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

from time import process_time 

#Ruta archivos .csv

castingfile = 'Movies/MoviesCastingRaw-small.csv'
detailsfile = 'Movies/SmallMoviesDetailsCleaned.csv'

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
    print ("Tiempo de ejecucion:", t1_start-t1_stop,"segundos")

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
    print ("Tiempo de ejecucion:", t1_start-t1_stop,"segundos")

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
    print ("Tiempo de ejecucion:", t1_start-t1_stop,"segundos")

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
    print ("Tiempo de ejecucion:", t1_start-t1_stop,"segundos")

def printMoviesbyCountry(country): #Imprime las peliculas que han sido producidas en un pais
    t1_start = process_time()
    print('Se encontraron: ' + str(lt.size(country)) + ' peliculas')
    iterator = it.newIterator(country)
    while it.hasNext(iterator):
        movie = it.next(iterator)
        print(movie['original_title'])
    t1_stop = process_time()
    print ("Tiempo de ejecucion:", t1_start-t1_stop,"segundos")

#Menu principal

def printMenu():
    print("***Bienvenido***")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Descubrir productora de cine")
    print("4- Conocer un director")
    print("5- Conocer un actor")
    print("6- Entender un genero cinematografico")
    print("7- Encontrar peliculas por pais")
    print("0- Salir")

#Ejecutar menu principal

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo...") #cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos...")
        controller.loadData(cont, detailsfile, castingfile)
        t1_start = process_time()
        print('Productoras de cine cargadas: ' + str(controller.productionCompanySize(cont)))
        print('Directores cargadas: ' + str(controller.directorSize(cont)))
        print('Actores cargados: ' + str(controller.actorSize(cont)))
        print('Géneros cinematograficos cargados: ' + str(controller.generosSize(cont)))
        print('Paises cargados: ' + str(controller.countrySize(cont)))
        t1_stop = process_time()
        print ("Tiempo de ejecucion:", t1_start-t1_stop,"segundos")

    elif int(inputs[0]) == 3: #Productora de cine
        productionName = input("Nombre de la productora de cine a buscar: ")
        productioninfo = controller.getMoviesByProductionCompany(cont, productionName)
        printProductionCompany(productioninfo)

    elif int(inputs[0]) == 4: #Director
        directorName = input("Nombre del director a buscar: ")
        directorinfo = controller.getMoviesByDirector(cont, directorName)
        PrintDirectorData(directorinfo)

    elif int(inputs[0]) == 5: #Actor
        actorName = input("Nombre del actor a buscar: ")
        actorinfo = controller.getMoviesByActor(cont, actorName)
        printActorData(actorinfo)

    elif int(inputs[0]) == 6: #Genero cinematografico
        genreName = input("Nombre del genero cinematografico a buscar: ")
        generoinfo = controller.getMoviesByGenre(cont, genreName)
        printGenreData(generoinfo)

    elif int(inputs[0]) == 7: #Pais
        coutryName = input("Nombre del pais a buscar: ")
        countryinfo = controller.getMoviesByCountry(cont, coutryName)
        printMoviesbyCountry(countryinfo)
    else:
        sys.exit(0)
sys.exit(0)
