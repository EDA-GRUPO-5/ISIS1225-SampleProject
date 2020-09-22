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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

Se define la estructura de un catálogo de libros.
El catálogo tendrá  una lista para los libros.

Los autores, los tags y los años se guardaran en
tablas de simbolos.
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalogDetails():

    catalog = { 'id': None,
                'genres': None,
                'original_title': None,
                'production_companies': None,
                'production_countries': None,
                'title': None,
                'vote_average': None,
                'vote_count': None} 
                
    catalog['id'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['genres'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['original_title'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['production_companies'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['production_countries'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['title'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['vote_average'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['vote_count'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)

    return catalog

def newCatalogCasting():

    catalog = { 'id': None,
                'actor1_name': None,
                'actor1_gender': None,
                'actor2_name': None,
                'actor2_gender': None,
                'actor3_name': None,
                'actor3_gender': None,
                'actor4_name': None,
                'actor4_gender': None,
                'actor5_name': None,
                'actor5_gender': None,
                'actor_number': None,
                'director_name': None}

    catalog['id'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['actor1_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor1_gender'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor2_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor2_gender'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor3_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor3_gender'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor4_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor4_gender'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor5_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor5_gender'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor_number'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog['director_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addMovie(catalogCast, catalogoDet, movie):
    """
    Esta funcion adiciona una pelicula a la lista de peliculas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Crea una entrada en el Map de Años, para indicar que esta pelicula
    fue publicada en ese año
    """
    lt.addLast(catalogCast['id'], movie)
    lt.addLast(catalogoDet['id'], movie)
    mp.put(catalogoDet['title'], movie['id'], movie)
    mp.put(catalogCast['title'], movie['id'], movie)

def addProductionCompany(catalog, company_name):
    pass

def addMovieDirector(catalog, director_name):
    pass

def addActor(catalog, actor_name):
    pass

def addGenre(catalog, genre):
    pass

def addCountry(catalog, country_name):
    pass

# =================================
# Funciones Requerimientos Reto 2
# =================================

def getmoviesByProductionCompany(catalog, company_name):
    company_name = mp.get(catalog['production_companies'], company_name)
    if company_name:
        return me.getValue(company_name)
    return None

def getMoviesByDirector(catalog, director_name):
    director_name = mp.get(catalog['director_name'], director_name)
    if director_name:
        return me.getValue(director_name)
    return None

def getMoviesByActor(catalog, actor_name): #PENDIENTE
    pass

def getMoviesByGenre(catalog, genre):
    genre = mp.get(catalog['genres'], genre)
    if genre:
        return me.getValue(genre)
    return None

def getMoviesByCountry(catalog, country_name):
    country_name = mp.get(catalog['production_countries'], country_name)
    if country_name:
        return me.getValue(country_name)
    return None

# ==============================
# Funciones de Comparacion
# ==============================


def compareMoviesIds(id1, id2):
    """
    Compara dos ids de las peliculas
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareActorByName(keyname, actor):
    """
    Compara dos nombres de un actor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(actor)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
