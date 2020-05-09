#Imports de excel
import pandas as pd
arch1 = pd.ExcelFile("info_barcos.xlsx")
archivos = arch1.sheet_names
final = len(archivos)
valores = [i for i in range(0, final)]
sec1 = tuple(zip(archivos, valores))
hojas_excel = dict(sec1)


def leer_info_barco(info_barco):
    print(list(zip(*tuple(map(lambda x: list(info_barco[x]), info_barco.keys(
    ))))))


def leer_trabajo(info_barco):
    print(list(zip(*tuple(map(lambda x: list(info_barco[x]), info_barco.keys(
    ))))))
    pass


def leer_container_enviado():
    pass


def leer_tiempo_teps():
    pass


def leer_info_patio():
    pass


def leer_container_gral():
    pass


def leer_teps_gral():
    pass


def leer_probabilidades():
    pass


def leer_prog_arribos():
    pass


def seleccion():
    funciones = [leer_info_barco, leer_trabajo, leer_container_enviado,
                 leer_tiempo_teps, leer_info_patio, leer_container_gral,
                 leer_teps_gral, leer_probabilidades, leer_prog_arribos]
    sec2 = tuple(zip(archivos, funciones))
    dict_foo = dict(sec2)
    return dict_foo


def leer_archivo(lectura):
    if lectura in hojas_excel:
        info = arch1.parse(archivos[hojas_excel[lectura]])
        leer_info_barco(info)
        #seleccion()[lectura](info)
    else:
        print("Ese archivo no existe")


leer_archivo(" info_barco")
leer_archivo("Trabajo")
leer_archivo("lista_container_enviado")
leer_archivo("Tiempo_teps")
leer_archivo("Info_patio")
leer_archivo("Contenedores_gral")
leer_archivo("teps_gral")
leer_archivo("Probabilidades")
leer_archivo("Programa de arribos")