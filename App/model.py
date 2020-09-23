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
                'actor_number': None,
                'director_name': None} 

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['id'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['genres'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['original_title'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['production_companies'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['production_countries'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['title'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['vote_average'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['vote_count'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor1_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor2_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor3_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor4_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['actor5_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)
    catalog['director_name'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMoviesIds)

    return catalog

def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    author = {'name': "", 
              "books": None,
              "average": 0,  
              "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('SINGLE_LINKED', compareAuthorsByName)
    return author


def newTagBook(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_books': 0,
           'books': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['books'] = lt.newList()
    return tag

# Funciones para agregar informacion al catalogo

def addBook(catalog, book):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['books'], book)
    mp.put(catalog['bookIds'], book['goodreads_book_id'], book)
    addBookYear(catalog, book)

def addCasting(catalog, movie)
def addDetails(catalog, movie)

def addBookYear(catalog, book):

    try:
        years = catalog['years']
        if (book['original_publication_year'] != ''):
            pubyear = book['original_publication_year']
            pubyear = int(float(pubyear))
        else:
            pubyear = 2020
        existyear = mp.contains(years, pubyear)
        if existyear:
            entry = mp.get(years, pubyear)
            year = me.getValue(entry)
        else:
            year = newYear(pubyear)
            mp.put(years, pubyear, year)
        lt.addLast(year['books'], book)
    except Exception:
        return None


def newYear(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'year': "", "books": None}
    entry['year'] = pubyear
    entry['books'] = lt.newList('SINGLE_LINKED', compareYears)
    return entry


def addBookAuthor(catalog, authorname, book):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    authors = catalog['authors']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newAuthor(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['books'], book)
    author['average'] += float(book['average_rating'])
    totbooks = lt.size(author['books'])
    if (totbooks > 0):
        author['average_rating'] = author['average'] / totbooks


def addTag(catalog, tag):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo
    """
    newtag = newTagBook(tag['tag_name'], tag['tag_id'])
    mp.put(catalog['tags'], tag['tag_name'], newtag)
    mp.put(catalog['tagIds'], tag['tag_id'], newtag)


def addBookTag(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    entry = mp.get(catalog['tagIds'], tagid)

    if entry:
        tagbook = mp.get(catalog['tags'], me.getValue(entry)['name'])
        tagbook['value']['total_books'] += 1
        tagbook['value']['count'] += int(tag['count'])
        book = mp.get(catalog['bookIds'], bookid)
        if book:
            lt.addLast(tagbook['value']['books'], book['value'])
            
#Funciones de consulta

def getMoviesByProductionCompany(catalog, productionName):
    productor = mp.get(catalog['production_companies'], productionName)
    if productor:
        return me.getValue(productor)['movies']
    return None

def getMoviesByDirector(catalog, directorName):
    director = mp.get(catalog['director_name'], directorName)
    if director:
        return me.getValue(director)
    return None

def getMoviesByActor(catalog, actorName):
    pass

def getMoviesByGenre(catalog, genreName):
    genero = mp.get(catalog['genre'], genreName)
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
    return mp.size(catalog['genre'])

def countrySize(catalog):
    return mp.size(catalog['production_countries'])

#Funciones de comparacion

def compareMoviesIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapMoviesIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareAuthorsByName(keyname, directorName):
    authentry = me.getKey(directorName)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareTagNames(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1

def compareTagIds(id, tag):
    tagentry = me.getKey(tag)
    if (int(id) == int(tagentry)):
        return 0
    elif (int(id) > int(tagentry)):
        return 1
    else:
        return 0

def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0
