from collections import namedtuple
from Proyecto.imports import info_barco, trabajo, cont_enviado, \
    tiempo_teps, info_patio, cont_gral, teps_gral, probabilidades, prog_arribos


# ENTIDADES
Barcos = namedtuple("Barcos_type", ["ide", "capacidad", "arribo", "partida",
                                    "lista_carga", "lista_descarga",
                                    "tipo", "pen", "entro"])
Camiones = namedtuple("Camiones_type", ["ide", "capacidad", "carga"])
Cointeiners = namedtuple("Conteiners_type", ["ide", "posicion", "tipo"])


def crear_barcos(info_contenedores, info_arribos, info_barco):
    ide_capacidad_arribo_partida_listacarga_listadescarga = \
        [(i, *info_arribos[i][1:4], filter(lambda x: x[0]=="Carga",
                                           info_contenedores[0][i]),
         filter(lambda x: x[0]=="Descarga", info_contenedores[0][i]),
         *info_barco[0][info_arribos[i][1]], False) for i in
         info_arribos.keys()]

    datos_barcos = ide_capacidad_arribo_partida_listacarga_listadescarga
    Lista_Barcos = map(lambda x: Barcos(*x), datos_barcos)
    return Lista_Barcos


def crear_conteiners():
    pass


if __name__ == "__main__":
    print(list(crear_barcos(cont_enviado, prog_arribos, info_barco)))
