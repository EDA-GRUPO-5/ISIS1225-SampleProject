import config as cf
from App import model
import csv

#Inicializacion del catalogo

def initCatalog(): 
    #Llama la funcion de inicializacion del catalogo del modelo.
    # catalog es utilizado para interactuar con el modelo.
    catalog = model.newCatalog()
    return catalog

#Funciones para la carga de datos y almacenamiento en los modelos

def loadData(catalog, castingfile, detailsfile): #Carga los datos al modelo
    loadCasting(catalog, castingfile)
    loadDetails(catalog, detailsfile)

def loadCasting(catalog, castingfile):
    castingfile = cf.data_dir + castingfile
    input_file = csv.DictReader(open(castingfile,'r',encoding='utf-8', errors='ignore'))
    for tag in input_file:
        model.addCasting(catalog, tag)

def loadDetails(catalog, detailsfile):
    detailsfile = cf.data_dir + detailsfile
    input_file = csv.DictReader(open(detailsfile,'r',encoding='utf-8', errors='ignore'))
    for tag in input_file:
        model.addDetails(catalog, tag)

#Funciones para consultas

def productionCompanySize(catalog):
    return model.productionCompanySize(catalog)

def directorSize(catalog):
    return model.directorSize(catalog)

def actorSize(catalog):
    return model.actorSize(catalog)

def generosSize(catalog):
    return model.generosSize(catalog)

def countrySize(catalog):
    return model.countrySize(catalog)

def getMoviesByProductionCompany(catalog, productionName):
    productioninfo = model.getMoviesByProductionCompany(catalog, productionName)
    return productioninfo

def getMoviesByDirector(catalog, directorName):
    directorinfo = model.getMoviesByDirector(catalog, directorName)
    return directorinfo

def getMoviesByActor(catalog, actorName):
    actorinfo = model.getMoviesByActor(catalog, actorName)
    return actorinfo

def getMoviesByGenre(catalog, genreName):
    generoinfo = model.getMoviesByGenre(catalog, genreName)
    return generoinfo

def getMoviesByCountry(catalog, countryName):
    countryinfo = model.getMoviesByCountry(catalog, countryName)
    return countryinfo
