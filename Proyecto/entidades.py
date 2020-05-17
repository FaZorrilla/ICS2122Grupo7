from collections import namedtuple
from imports import info_barco, trabajo, cont_enviado, \
    tiempo_teps, info_patio, cont_gral, teps_gral, probabilidades, prog_arribos


# ENTIDADES
Barcos = namedtuple("Barcos_type", ["ide", "capacidad", "arribo", "partida",
                                    "lista_carga", "lista_descarga",
                                    "tipo", "pen", "entro"])
Camiones = namedtuple("Camiones_type", ["ide", "carga"])
Containers = namedtuple("Conteiners_type", ["ide", "posicion", "tipo"])


def crear_barcos(info_contenedores, info_arribos, info_barco):
    ide_capacidad_arribo_partida_listacarga_listadescarga = \
        [(i, *info_arribos[i][1:4], list(filter(lambda x: x[0]=="Carga",
                                           info_contenedores[0][i])),
         list(filter(lambda x: x[0]=="Descarga", info_contenedores[0][i])),
         *info_barco[0][info_arribos[i][1]], False) for i in
         info_arribos.keys()]

    datos_barcos = ide_capacidad_arribo_partida_listacarga_listadescarga
    Lista_Barcos = list(map(lambda x: Barcos(*x), datos_barcos))
    return Lista_Barcos


def crear_conteiners(info_contenedores):
    ide_posicion_tipo = [[(i+j[1], [0, 0], j[1][-1:]) for j in
                          info_contenedores[0][i]] for i in
                         info_contenedores[0].keys()]
    Lista_Contenedores = []
    for ele in ide_posicion_tipo:
        Lista_Contenedores += list(map(lambda x: Containers(*x), ele))
    return Lista_Contenedores


lista_barco = list(crear_barcos(cont_enviado, prog_arribos, info_barco))
lista_contenedores = list(crear_conteiners(cont_enviado))

if __name__ == "__main__":
    print(list(crear_barcos(cont_enviado, prog_arribos, info_barco)))
    # print(crear_conteiners(cont_enviado))

