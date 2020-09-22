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

import config as cf
from App import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalogDetails():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalogDetails()
    return catalog

def initCatalogCasting():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalogCasting()
    return catalog
# _____________________________________________________________________________
#  Funciones para la carga de datos y almacenamiento de datos en los modelos
# _____________________________________________________________________________

def loadData(catalogoCast, catalogoDet, castingfile, detailsfile, moviesfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadMovies(catalogoCast, catalogoDet, moviesfile)
    loadDetails(catalogoDet, detailsfile)
    loadCasting(catalogoCast, castingfile)

def loadMovies(catalogoCast, catalogDet, moviesfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    moviesfile = cf.data_dir + moviesfile
    input_file = csv.DictReader(open(moviesfile, encoding="utf-8"))
    for movie in input_file:
        model.addMovie(catalogoCast, catalogDet, movie)
        director = movie['director_name'].split(",")  # Se obtienen los autores
        for direc in director:
            model.addMovieDirector(catalogDet, director.strip(), direc)

def loadDetails(catalog, detailsfile):
    detailsfile = cf.data_dir + detailsfile
    input_file = csv.DictReader(open(detailsfile))
    for details in input_file:
        model.addDetails(catalog, details)

def loadCasting(catalog, castingfile):
    """
    Carga la información que asocia tags con libros.
    Primero se localiza el tag y se le agrega la información leida.
    Adicionalmente se le agrega una referencia al libro procesado.
    """
    castingfile = cf.data_dir + castingfile
    input_file = csv.DictReader(open(castingfile))
    for casting in input_file:
        model.addCasting(catalog, casting)

# ____________________________________
#  Funciones Requerimientos Reto 2
# ____________________________________

def getMoviesByProductionCompany(catalog, company_name):
    productioninfo = model.getmoviesByProductionCompany(catalog, company_name)
    return productioninfo

def getMoviesByDirector(catalog, director_name):
    directorinfo = model.getMoviesByDirector(catalog, director_name)
    return directorinfo

def getMoviesByActor(catalog, actor_name):
    actorinfo = model.getMoviesByActor(catalog, actor_name)
    return actorinfo

def getMoviesByGenre(catalog, genre):
    genreinfo = model.getMoviesByGenre(catalog, genre)
    return genreinfo
    
def getMoviesByCountry(catalog, country_name):
    countryinfo = model.getMoviesByCountry(catalog, country_name)
    return countryinfo