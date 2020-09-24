import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

# -----------------------------------------------------
# API del TAD Catalogo de Películas
# -----------------------------------------------------

info = {
    "numelements" : 2000,
    "maptype" : 'CHAINING',
    "loadfactor": 1,
    "listtype" : 'ARRAY_LIST'
}

elements = info["numelements"]

def newCatalog():
    catalogo = {
        "movies" : None,
        "production_company" : None
    }

    catalogo["movies"] = mp.newMap(
                                    numelements = info["numelements"],
                                    maptype=info["maptype"],
                                    loadfactor=info["loadfactor"],
                                    comparefunction=compareMoviesIds
                                    )
    catalogo["production_company"] = mp.newMap (
                                    numelements = info["numelements"],
                                    maptype=info["maptype"],
                                    loadfactor=info["loadfactor"],
                                    comparefunction=compareProductionCompanies
                                    )
    catalogo["director_name"] = mp.newMap (
                                    numelements = info["numelements"],
                                    maptype=info["maptype"],
                                    loadfactor=info["loadfactor"],
                                    comparefunction=compareDirector
                                    )
    catalogo["genres"] = mp.newMap (
                                    numelements = info["numelements"],
                                    maptype=info["maptype"],
                                    loadfactor=info["loadfactor"],
                                    comparefunction=compareGenres
                                    )    
    return catalogo


def newMovie(data: dict):
        data["id"] = int(data["id"])
        data["budget"] = int(data["budget"])
        data["genres"] = data["genres"]
        data["imdb_id"] = data["imdb_id"] 
        data["original_language"] = data["original_language"] 
        data["original_title"] = data["original_title"] 
        data["overview"] = data["overview"]
        data["popularity"] = data["popularity"]
        data["production_companies"] = data["production_companies"] 
        data["production_countries"] = data["production_countries"] 
        data["release_date"] = data["release_date"]
        data["revenue"] = int(data["revenue"])
        data["runtime"] = int(data["runtime"]) 
        data["spoken_languages"] = data["spoken_languages"] 
        data["status"] = data["status"]
        data["tagline"] = data["tagline"]
        data["title"] = data["title"]
        data["vote_average"] = float(data["vote_average"]) 
        data["vote_count"] = int(data["vote_count"])
        data["production_companies_number"] = int(data["production_companies_number"]) 
        data["production_countries_number"] = int(data["production_countries_number"]) 
        data["spoken_languages_number"] = int(data["spoken_languages_number"])
        data["actor1_name"] = data["actor1_name"]
        data["actor1_gender"] = int(data["actor1_gender"]) 
        data["actor2_name"] = data["actor2_name"]
        data["actor2_gender"] = int(data["actor2_gender"])
        data["actor3_name"] = data["actor3_name"]
        data["actor3_gender"] = int(data["actor3_gender"]) 
        data["actor4_name"] = data["actor4_name"]
        data["actor4_gender"] = int(data["actor4_gender"]) 
        data["actor5_name"] = data["actor5_name"]
        data["actor5_gender"] = int(data["actor5_gender"]) 
        data["actor_number"] = int(data["actor_number"])
        data["director_name"] = data["director_name"]
        data["director_gender"] = data["director_gender"] 
        data["director_number"] = int(data["director_number"]) 
        data["producer_name"] = data["producer_name"]
        data["producer_number"] = int(data["producer_number"]) 
        data["screeplay_name"] = data["screeplay_name"]
        data["editor_name"] = data["editor_name"]

def newProductionCompany():
    company = {
        "movies": lt.newList(info["listtype"]),
        "vote_average": 0
        }
    return company

def newDirector():
    director = {
        "movies": lt.newList(info["listtype"]),
        "vote_average": 0
        }
    return director

def newGenres():
    genres = {
        "movies": lt.newList(info["listtype"]),
        "vote_count": 0
        }
    return genres

# ==============================
# Funciones de consulta
# ==============================


def getMovie(catalog, movieId):
    movie = mp.get(catalog["movies"], movieId)
    if movie:
        return me.getValue(movie)
    return None

def getMoviesByCompany(catalog, companyName):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    productionCompany = mp.get(catalog["production_company"], companyName)
    if productionCompany:
        companyData = me.getValue(productionCompany)
        companyMovies = lt.newList(info["listtype"])
        for i in range(lt.size(companyData["movies"])):
            movie = getMovie(catalog, lt.getElement(companyData["movies"], i))
            lt.addLast(companyMovies, movie)
        
        return (companyMovies,companyData["vote_average"])
        
    return (None,None)

def getMoviesByDirector(catalog, directorName):
    directorMov = mp.get(catalog["director_name"], directorName)
    if directorMov:
        directorData = me.getValue(directorMov)
        directorMovies = lt.newList(info["listtype"])
        for i in range(lt.size(directorData["movies"])):
            movie = getMovie(catalog, lt.getElement(directorData["movies"], i))
            lt.addLast(directorMovies, movie)
        
        return (directorMovies,directorData["vote_average"])
        
    return (None,None)

def getMoviesByGenre(catalog, genre):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    genre = mp.get(catalog["genres"], genre)
    if genre:
        genreData = me.getValue(genre)
        genreMovies = lt.newList(info["listtype"])
        for i in range(lt.size(genreData["movies"])):
            movie = getMovie(catalog, lt.getElement(genreData["movies"], i))
            lt.addLast(genreMovies, movie)
        
        return (genreMovies,genreData["vote_count"])
        
    return (None,None)


# Funciones para agregar informacion al catalogo

def addMovie(catalogo, dataD: dict, dataC: dict):
    if mp.contains(catalogo["movies"], dataD["id"]):
        movie = mp.get(catalogo["movies"], dataD["id"])
        movie = me.getValue(movie)
        movie.update(dataD)
        movie.update(dataC)
        
    else:
        mp.put(catalogo["movies"], dataD["id"], dataD)
        addProductionCompany(catalogo,dataD)
        addDirector(catalogo, dataC)
        addGenres(catalogo, dataD)

def addProductionCompany (catalogo, movie) :
    companies = catalogo["production_company"]
    movieId = movie["id"]
    name = movie["production_companies"]
    existauthor = mp.contains(companies, name)
    if existauthor:
        entry = mp.get(companies, name)
        company = me.getValue(entry)
    else:
        company = newProductionCompany()
        mp.put(companies, name, company)
    lt.addLast(company['movies'], movieId)

    companyAvg = company["vote_average"]
    movieAvg = movie["vote_average"]
    if (movieAvg == 0.0):
        company["vote_average"] = float(movieAvg)
    else:
        moviesNum = lt.size(company["movies"])
        company["vote_average"] = ((companyAvg*(moviesNum-1)) + float(movieAvg)) / moviesNum
        
def addDirector(catalogo, movie):
    pass

def addGenres (catalogo, movie) :
    genres = catalogo["genres"]
    movieId = movie["id"]
    name = movie["genres"]
    existauthor = mp.contains(genres, name)
    if existauthor:
        entry = mp.get(genres, name)
        genre = me.getValue(entry)
    else:
        genre = newGenres()
        mp.put(genres, name, genre)
    lt.addLast(genre['movies'], movieId)

    companyAvg = genre["vote_count"]
    movieAvg = movie["vote_count"]
    if (movieAvg == 0.0):
        genre["vote_count"] = float(movieAvg)
    else:
        moviesNum = lt.size(genre["movies"])
        genre["vote_count"] = ((companyAvg*(moviesNum-1)) + float(movieAvg)) / moviesNum

# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id, entry):
    """
    Compara dos ids de peliculas
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return - 1
        
def compareProductionCompanies(id, entry):
    """
    Compara dos ids de compañias productoras
    """
    identry = me.getKey(entry)
    if (id == identry):
        return 0
    elif (id > identry):
        return 1
    else:
        return -1

def compareDirector(id, entry):
    identry = me.getKey(entry)
    if (id == identry):
        return 0
    elif (id > identry):
        return 1
    else:
        return -1
    
def compareGenres(id, entry):
    """
    Compara dos ids de compañias productoras
    """
    identry = me.getKey(entry)
    if (id == identry):
        return 0
    elif (id > identry):
        return 1
    else:
        return -1

# ___________________________________________________
#  Requerimientos
# ___________________________________________________

def descubrirProductoras(catalogo, Productora):
    movies = getMoviesByCompany(catalogo, Productora)
    try:
        moviesNum = lt.size(movies[0])
    except:
        moviesNum = 0
    
    return (movies[0],movies[1],moviesNum)

def conocerDirector(catalogo, director):
    movies = getMoviesByDirector(catalogo, director)
    try:
        total = lt.size(movies[0])
    except:
        total = 0
    
    return (movies[0],movies[1],total)

def entenderGenero(catalogo, genero):
    movies = getMoviesByGenre(catalogo, genero)
    try:
        moviesNum = lt.size(movies[0])
    except:
        moviesNum = 0
    
    return (movies[0],movies[1],moviesNum)
