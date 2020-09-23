"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

from time import process_time 

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


castingfile = 'MoviesCastingRaw-smaller.csv'
detailsfile = 'SmallerMoviesDetailsCleaned.csv'
#castingfile = 'AllMoviesCastingRaw.csv'
#detailsfile = 'AllMoviesDetailsCleaned.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Descubrir productoras de cine")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un género cinematográfico")
    print("6- Encontrar películas por país")
    print("0- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar:\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo...")
        # cont es el controlador que se usará de acá en adelante
        t1_start = process_time()
        contCast = controller.initCatalogCasting()
        contDet = controller.initCatalogDetails()
        t1_stop = process_time()
        print ("Tiempo de ejecución:", t1_stop-t1_start,"segundos\n")

    elif int(inputs[0]) == 2:
        print("Cargando archivos en Catalogos...")
        controller.loadData(contCast, contDet, castingfile, detailsfile)
        print('Detalles cargados: ' + str(controller.detSize(contDet)))
        print('Casting cargados: ' + str(controller.castSize(contCast)))

    elif int(inputs[0]) == 3:
        company_name = input("Ingrese la productora de cine a buscar:")
        t1_start = process_time()
        production = controller.getMoviesByProductionCompany(contDet, company_name)
        if production != None:
            print(production)
        else:
            print ("No existe esta productora de cine en el catalogo.")
        t1_stop = process_time()
        print ("Tiempo de ejecución:", t1_stop-t1_start,"segundos\n")

    elif int(inputs[0]) == 4:
        director_name = input("Ingrese el nombre del director a buscar:")
        t1_start = process_time()
        director = controller.getMoviesByDirector(contCast, director_name)
        if director != None:
            print(director)
        else:
            print ("No existe este director en el catalogo.")
        t1_stop = process_time()
        print ("Tiempo de ejecución:", t1_stop-t1_start,"segundos\n")

    elif int(inputs[0]) == 5:
        actor_name = input("Ingrese el nombre del actor a buscar:")
        t1_start = process_time()
        actor = controller.getMoviesByActor(contCast, actor_name)
        if actor != None:
            print(actor)
        else:
            print ("No existe este actor en el catalogo.")
        t1_stop = process_time()
        print ("Tiempo de ejecución:", t1_stop-t1_start,"segundos\n")

    elif int(inputs[0]) == 6:
        genre = input("Ingrese el nombre del genero a buscar:")
        t1_start = process_time()
        genero = controller.getMoviesByGenre(contDet, genre)
        if genero != None:
            print(genero)
        else:
            print ("No existe este genero en el catalogo.")
        t1_stop = process_time()
        print ("Tiempo de ejecución:", t1_stop-t1_start,"segundos\n")

    elif int(inputs[0]) == 7:
        conuntry_name = input("Ingrese el nombre del pais a buscar:")
        t1_start = process_time()
        pais = controller.getMoviesByCountry(contDet, conuntry_name)
        if pais != None:
            print(director)
        else:
            print ("No existe este pais en el catalogo.")
        t1_stop = process_time()
        print ("Tiempo de ejecución:", t1_stop-t1_start,"segundos\n")

    else:
        sys.exit(0)
sys.exit(0)

