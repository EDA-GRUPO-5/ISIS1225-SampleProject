import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

#API del TAD Catalogo de Peliculas

def newCatalog():
    catalog = { 'id': None,
                'genres': None,
                'original_title': None,
                'production_companies': None,
                'production_countries': None,
                'title': None,
                'vote_average': None,
                'vote_count': None,
                'actor1_name': None,
                'actor2_name': None,
                'actor3_name': None,
                'actor4_name': None,
                'actor5_name': None,
                'director_name': None} 

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareNumber)
    catalog['id'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareNumber)
    catalog['genres'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['original_title'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['production_companies'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['production_countries'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['title'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['vote_average'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareNumber)
    catalog['vote_count'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareNumber)
    catalog['actor1_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['actor2_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['actor3_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['actor4_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['actor5_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)
    catalog['director_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareString)

    return catalog

def newAuthor(name):
    author = {'name': "", 
              "peliculas": None,
              "promedio": 0,  
              "vote_average": 0}
    author['name'] = name
    author['movies'] = lt.newList('ARRAY_LIST', compareString)
    return author


def newTagBook(name, id):
    tag = {'name': '',
           'etiqueta': '',
           'total': 0,
           'peliculas': None,
           'count': 0.0}
    tag['name'] = name
    tag['etiqueta'] = id
    tag['peliculas'] = lt.newList()
    return tag

# Funciones para agregar informacion al catalogo

def addMovies(catalog, movie):
    pass

#Funciones de consulta

def getMoviesByProductionCompany(catalog, productionName):
    productor = mp.get(catalog['production_companies'], productionName)
    if productor:
        return me.getValue(productor)['movies']
    return None

def getMoviesByDirector(catalog, directorName):
    director = mp.get(catalog['director_name'], directorName)
    if director:
        return me.getValue(director)['movies']
    return None

def getMoviesByActor(catalog, actorName):
    pass

def getMoviesByGenre(catalog, genreName):
    genero = mp.get(catalog['genres'], genreName)
    if genero:
        return me.getValue(genero)['movies']
    return None

def getMoviesByCountry(catalog, countryName):
    pais = mp.get(catalog['production_countries'], countryName)
    if pais:
        return me.getValue(pais)['movies']
    return None

def productionCompanySize(catalog):
    return mp.size(catalog['production_companies'])

def directorSize(catalog):
    return mp.size(catalog['director_name'])

def actorSize(catalog):
    pass

def generosSize(catalog):
    return mp.size(catalog['genres'])

def countrySize(catalog):
    return mp.size(catalog['production_countries'])

#Funciones de comparacion

def compareNumber(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareString(keyname, entry):
    authentry = me.getKey(entry)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

