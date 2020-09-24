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

    for link in data_link:
            loadCSVFile(link,data,sep)

def loadCSVFile(link, data, sep=";"):
    dialect = csv.excel()
    dialect.delimiter = sep
    with open(link, encoding="utf-8-sig") as csvfile:
            buffer = csv.DictReader(csvfile, dialect=dialect)
            cont = 0
            for movie in buffer:
                cont += 1
                if cont == elements:
                    break
                model.addMovie(data, movie)
        
    

# ___________________________________________________
#  Requerimientos
# ___________________________________________________



def iniciarDescubrirProductoras(catalogo, productora):
    companyData = model.descubrirProductoras(catalogo, productora)
    titulos=array.newList()
    for i in range(lt.size(companyData[0])):
        movie = lt.getElement(companyData[0], i)
        titulos["elements"].append(movie['title'])

    print("\n",productora,"cuenta con",companyData[2],"películas. Sus títulos son:",titulos["elements"],". Su promedio de votos es:",companyData[1])


def iniciarEntenderGenero(catalogo, genero):
    genreData = model.entenderGenero(catalogo, genero)
    titulos=array.newList()
    for i in range(lt.size(genreData[0])):
        movie = lt.getElement(genreData[0], i)
        titulos["elements"].append(movie['title'])
    
    print("\nEl género",genero,"cuenta con",genreData[2],"peliculas. Sus títulos son:",titulos["elements"],". Su promedio de votos (vote_count) es:,",genreData[1])
