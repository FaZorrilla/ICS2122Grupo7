import xlrd as x
from Clases import Barco, TEPs


def crear_barcos():
    barcos = []
    for ele in leer_descrip_barcos():
        barcos.append(Barco(*ele))
    return barcos


def crear_vacios():
    lista = []
    for i in range(16):
        lista.append([0, 0, 0, 0])
    return lista


def crear_lista_barco(hoja, valor):
    lista = []
    for j in range(48, 64):
        lista.append(hoja.cell(j, valor).value)
    return tuple(lista)


def leer_descrip_barcos():
    workbook = x.open_workbook("info_barcos.xlsx")
    worksheet = workbook.sheet_by_name("info")
    cod = crear_lista_barco(worksheet, 8)
    llegada = crear_lista_barco(worksheet, 9)
    salida = crear_lista_barco(worksheet, 10)
    t_desc = crear_lista_barco(worksheet, 11)
    t_carga = crear_lista_barco(worksheet, 12)
    del worksheet
    del workbook
    return zip(cod, llegada, salida, t_desc, t_carga)


def leer_probabilidades():
    workbook = x.open_workbook("info_barcos.xlsx")
    worksheet = workbook.sheet_by_name("info")
    return tuple([crear_lista_prob(2, worksheet),
                  crear_lista_prob(3, worksheet),
                  crear_lista_prob(4, worksheet)])


def crear_lista_prob(j, hoja):
    lista = []
    for i in range(48, 78):
        lista.append(hoja.cell(i, j).value)
    return tuple(lista)


def crear_set_descarga(hoja, vi, vf):
    lista = []
    for j in range(vi, vf):
        lista.append(hoja.cell(j, 2).value)
    return tuple(lista)


def lista_carga_barco(codigo):
    workbook = x.open_workbook("lista_container_enviado.xls")
    worksheet = workbook.sheet_by_name("lista_container")
    if codigo == "B-1-1200":
        return crear_set_descarga(worksheet, 5831, 6876)
    elif codigo == "B-2-1200":
        return crear_set_descarga(worksheet, 6876, 7726)
    elif codigo == "B-3-1200":
        return crear_set_descarga(worksheet, 7726, 8572)
    elif codigo == "B-4-1200":
        return crear_set_descarga(worksheet, 8572, 9765)
    elif codigo == "B-1-800":
        return crear_set_descarga(worksheet, 9765, 10360)
    elif codigo == "B-2-800":
        return crear_set_descarga(worksheet, 10360, 11061)
    elif codigo == "B-3-800":
        return crear_set_descarga(worksheet, 11061, 11857)
    elif codigo == "B-4-800":
        return crear_set_descarga(worksheet, 11857, 12622)
    elif codigo == "B-5-800":
        return crear_set_descarga(worksheet, 12622, 13240)
    elif codigo == "B-1-600":
        return crear_set_descarga(worksheet, 13240, 13802)
    elif codigo == "B-2-600":
        return crear_set_descarga(worksheet, 13802, 14367)
    elif codigo == "B-3-600":
        return crear_set_descarga(worksheet, 14637, 14884)
    elif codigo == "B-4-600":
        return crear_set_descarga(worksheet, 14884, 15310)
    elif codigo == "B-5-600":
        return crear_set_descarga(worksheet, 15310, 15768)
    elif codigo == "B-6-600":
        return crear_set_descarga(worksheet, 15768, 16334)
    elif codigo == "B-7-600":
        return crear_set_descarga(worksheet, 16334, 16902)


def crear_teps():
    lista = []
    for i in range(15):
        lista.append(TEPs(0, i))
    return lista


if __name__ == "__main__":
    leer_descrip_barcos()
    b = crear_barcos()
    b1 = lista_carga_barco(b[0].codigo)
    b2 = lista_carga_barco(b[1].codigo)
    b3 = lista_carga_barco(b[2].codigo)
    b4 = lista_carga_barco(b[3].codigo)
    b5 = lista_carga_barco(b[4].codigo)
    b6 = lista_carga_barco(b[5].codigo)
    b7 = lista_carga_barco(b[6].codigo)
    b8 = lista_carga_barco(b[7].codigo)
    b9 = lista_carga_barco(b[8].codigo)
    b10 = lista_carga_barco(b[9].codigo)
    b11 = lista_carga_barco(b[10].codigo)
    b12 = lista_carga_barco(b[11].codigo)
    b13 = lista_carga_barco(b[12].codigo)
    b14 = lista_carga_barco(b[13].codigo)
    b15 = lista_carga_barco(b[14].codigo)
    b16 = lista_carga_barco(b[15].codigo)
    print("Ct_1_R" in b1, "1"), print("Ct_1045_C" in b1, "2")
    print("Ct_1_I" in b2, "3"), print("Ct_699_I" in b2, "4")
    print("Ct_1_R" in b3, "5"), print("Ct_646_L" in b3, "6")
    print("Ct_1_R" in b4, "7"), print("Ct_526_R" in b4, "8")
    print("Ct_1_L" in b5, "9"), print("Ct_335_R" in b5, "10")
    print("Ct_1_I" in b6, "11"), print("Ct_284_I" in b6, "12")
    print("Ct_1_L" in b7, "13"), print("Ct_410_R" in b7, "14")
    print("Ct_1_R" in b8, "15"), print("Ct_400_L" in b8, "16")
    print("Ct_1_C" in b9, "17"), print("Ct_261_I" in b9, "18")
    print("Ct_1_L" in b10, "19"), print("Ct_291_C" in b10, "20")
    print("Ct_1_C" in b11, "21"), print("Ct_296_L" in b11, "22")
    print("Ct_1_L" in b12, "23"), print("Ct_236_R" in b12, "24")
    print("Ct_1_C" in b13, "25"), print("Ct_226_L" in b13, "26")
    print("Ct_1_L" in b14, "27"), print("Ct_215_L" in b14, "28")
    print("Ct_1_R" in b15, "29"), print("Ct_566_C" in b15, "30")
    print("Ct_1_C" in b16, "31"), print("Ct_568_C" in b16, "32")
