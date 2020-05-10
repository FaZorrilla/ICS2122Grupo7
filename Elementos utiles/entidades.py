from collections import namedtuple
from imports.py import info_barco, trabajo, cont_enviado, \
    tiempo_teps, \
    info_patio, cont_gral, teps_gral, probabilidades, prog_arribos

## BARCOS
Barcos = namedtuple("Barcos_type", ["ide", "tamano", "lista_conteines",
                                    "entro"])

# base de datos
lista = [("grande", 1), ("chico", 2), ("mediano", 3)]

# implementación forma 1
Lista_Barcos = map(lambda x: Barcos(*x), lista)

# visualización
print(list(Lista_Barcos))

## CAMIONES
Camiones = namedtuple("Camiones_type", ["ide", "capacidad", "carga"])

## CONTEINERS

Cointeiners = namedtuple("Conteiners_type", ["ide", "posicion", "tipo"])



#Barcos = namedtuple("Barcos_type", ["ide", "tamano", "lista_conteines",
 #                                   "entro"])
#Barco= tipo, capacidad, Pen; ide, lista de descarga, lista de carga, \
 #                                                             dia de
#                                                             arribo,\                                                               día de
#partida

def crear_barcos(info_barco, info_contenedores, info_probabilidades,
                 info_arribo):
    pass


"""
def seleccion():
    funciones = [leer_info_barco, leer_trabajo, leer_container_enviado,
                 leer_tiempo_teps, leer_info_patio, leer_container_gral,
                 leer_teps_gral, leer_probabilidades, leer_prog_arribos]
    sec2 = tuple(zip(archivos, funciones))
    dict_foo = dict(sec2)
    return dict_foo
    """
