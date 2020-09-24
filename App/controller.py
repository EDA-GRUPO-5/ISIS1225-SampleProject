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
        
    


def descubrirProductoras(catalogo, Productora):
    movies = model.getMoviesByCompany(catalogo, Productora)
    try:
        moviesNum = lt.size(movies[0])
    except:
        moviesNum = 0
    
    return (movies[0],movies[1],moviesNum)

def ejecutarDescubrirProductoras(catalogo):
    companyName = input("ingrese el nombre de la productora: ")
    companyData = descubrirProductoras(catalogo, companyName)
    if companyData[0]:
        print(f"{companyName} cuenta con {companyData[2]} peliculas y una puntuacion total de {companyData[1]}.")
        print("Sus titulos son: \n")
        for i in range(lt.size(companyData[0])):
            movie = lt.getElement(companyData[0], i)
            print(f"{movie['title']}")
            print(f"Con una puntuacion de {movie['vote_average']} por {movie['director_name']} \n")
    else:
        print("No hay informacion de esta productora")
