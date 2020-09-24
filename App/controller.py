import config as cf
from App import model
import csv
from DISClib.ADT import list as lt
from model import elements as elements

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
        



