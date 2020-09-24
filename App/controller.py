import config as cf
from App import model
import csv
from DISClib.ADT import list as lt
from model import elements as elements
from DISClib.DataStructures import arraylist as array

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalogo():
    catalogo = model.newCatalog()
    return catalogo

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData (data_link, data, sep=";"):
    print(data_link)
    linkD, linkC = data_link
    loadCSVFile(linkC, linkD, data,sep)

def loadCSVFile(linkC, linkD, data, sep=";"):
    dialect = csv.excel()
    dialect.delimiter = sep
    with open(linkC, encoding="utf-8-sig") as csvfileC, open(linkD, encoding="utf-8-sig") as csvfileD:
            bufferC = csv.DictReader(csvfileC, dialect=dialect)
            bufferD = csv.DictReader(csvfileD, dialect=dialect)
            cont = 0
            for movieC, movieD in zip(bufferC, bufferD):
                cont += 1
                if cont == elements:
                    break
                model.addMovie(data, movieD, movieC)         
    
# ___________________________________________________
#  Requerimientos
# ___________________________________________________

def iniciarDescubrirProductoras(catalogo, productora):
    companyData = model.descubrirProductoras(catalogo, productora)
    titulos=array.newList()
    for i in range(lt.size(companyData[0])):
        movie = lt.getElement(companyData[0], i)
        titulos["elements"].append(movie['title'])

    print("\n" + productora,"cuenta con" + str(companyData[2]) + "películas. Sus títulos son: " + str(titulos["elements"]) + ". Su promedio de votos (vote_average) es: " + str(companyData[1]))

def iniciarConocerDirector(catalogo, director):
    directorData = model.conocerDirctor(catalogo, director)
    titles=array.newList()
    for i in range(lt.size(directorData[0])):
        movie = lt.getElement(directorData[0], i)
        titles["elements"].append(movie['title'])

    print("\n" + director,"tiene" + str(directorData[2]) + "películas. Los nombres son: " + str(titles["elements"]) + ". Su promedio de votos es: " + str(directorData[1]))
    
def iniciarEntenderGenero(catalogo, genero):
    genreData = model.entenderGenero(catalogo, genero)
    titulos=array.newList()
    for i in range(lt.size(genreData[0])):
        movie = lt.getElement(genreData[0], i)
        titulos["elements"].append(movie['title'])
    
    print("\nEl género" + genero,"cuenta con" + str(genreData[2]) + "peliculas. Sus títulos son: " + str(titulos["elements"]) + ". Su promedio de votos (vote_count) es: " + str(genreData[1]))
