from collections import namedtuple
from Proyecto.imports import info_barco, trabajo, cont_enviado, \
    tiempo_teps, info_patio, cont_gral, teps_gral, probabilidades, prog_arribos


# BARCOS
Barcos = namedtuple("Barcos_type", ["ide", "tipo",
                                    "capacidad", "pen", "lista_descarga",
                                    "lista_carga", "arribo", "partida",
                                    "entro"])

# base de datos
lista = [("grande", 1), ("chico", 2), ("mediano", 3)]

# implementación forma 1
#Lista_Barcos = map(lambda x: Barcos(*x), lista)

# visualización
#print(list(Lista_Barcos))

# CAMIONES
Camiones = namedtuple("Camiones_type", ["ide", "capacidad", "carga"])

# CONTEINERS

Cointeiners = namedtuple("Conteiners_type", ["ide", "posicion", "tipo"])


def crear_barcos(info_barco, info_contenedores, info_probabilidades,
                 info_arribos):
    print(info_barco)
    ides = info_arribos.keys()
    capacidad = [info_arribos[i][1] for i in info_arribos.keys()]
#barcos()
#crear_barcos(info_barco)
#Lista_Barcos = map(lambda x: Barcos(*x), lista)
print(prog_arribos)