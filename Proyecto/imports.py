# Imports de excel
import pandas as pd
arch1 = pd.ExcelFile("info_barcos.xlsx")
archivos = arch1.sheet_names
final = len(archivos)
valores = [i for i in range(0, final)]
sec1 = tuple(zip(archivos, valores))
hojas_excel = dict(sec1)


def leer_hoja(info_excel):
    """
    :param info_excel: información del excel del excel
    :return: diccionario {titulo: (elementos)
    """
    return {y[0]: y[1:len(y)] for y in zip(*map(lambda x: list(
            info_excel[x]), info_excel.keys()))}


def leer_hoja_1(info_excel):
    return {y[2]: y[0:2]+y[3:len(y)] for y in list(zip(*map(lambda x:
            list(info_excel[x]), info_excel.keys())))}


def leer_archivo(lectura):
    if lectura in hojas_excel:
        info = arch1.parse(archivos[hojas_excel[lectura]])
        if lectura == "Programa de arribos":
            return leer_hoja_1(info)
        else:
            return leer_hoja(info)
    else:
        print("Ese archivo no existe")


info_barco = leer_archivo("info_barco"),
trabajo = leer_archivo("Trabajo"),
cont_enviado = leer_archivo("lista_container_enviado"),
tiempo_teps = leer_archivo("Tiempo_teps"),
info_patio = leer_archivo("Info_patio"),
cont_gral = leer_archivo("Contenedores_gral"),
teps_gral = leer_archivo("teps_gral"),
probabilidades = leer_archivo("Probabilidades"),
prog_arribos = leer_archivo("Programa de arribos")
