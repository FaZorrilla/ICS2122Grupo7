from collections import deque
from functools import reduce
from random import random
from imports import probabilidades
from statistics import mean
from puerto import Puerto
from entidades import lista_barco, lista_contenedores
from simulacion import lista_teps # Los teps después
# vendrán de otra parte y de otra forma, ojo con eso. Lo importnte para lo
# que viene es que se entregue en forma de lista con clases dentro


class Simulacion:

    STR_TEMPLATE = ('[COLA] Llega {} en tiempo de simulación t={} min. '
                    'Hay {} barcos en cola')

    def __init__(self, max_tiempo):
        self.max_tiempo = max_tiempo
        self.barcos_en_puerto = []
        self.barcos_en_espera = deque()
        self.puerto = Puerto()
        self.demora_total = {} #(barco ide: tiempo espera, tiempo atencion)
        self.lista_contenedores_atendidos = []

    def llega_barco(self, dia):
        llegan_hoy = filter(lambda x: int(x.arribo) == dia, lista_barco)
        self.barcos_en_espera += list(llegan_hoy)
        # ordenar prioridad de lista, mientras está ordenada como una cola.
        # Que puede no tener sentido de momento.

    @property
    def cantidad_barcos(self):
        return len(self.barcos_en_puerto)

    def esta_lleno(self):
        if self.cantidad_barcos >= 3:
            print("Hay {} en el puerto".format(len(self.barcos_en_puerto)))
            return True
        else:
            print("Hay {} en el puerto".format(len(self.barcos_en_puerto)))
            return False

    def entra_barco(self, dia):
        """
        Esta función lo que hace es determinar si hay en un barco en espera
        para entrar y si logra entrar o no
        :param dia: medida de tiempo en que corre la simulacion, esto debe
        modelarse o cambiarse con la librería tiempo de momento es un int
        :return: de momento solo dice que son prints que dice en qué está
        """
        probabilidad_por_dia = probabilidades[0][dia]
        for barco in self.barcos_en_espera:
            if barco.tipo == "A":
                i = 0
            elif barco.tipo == "B":
                i = 1
            else:
                i = 2
            if random() <= probabilidad_por_dia[i]:
                print("La marea lo permite")
                if not self.esta_lleno():
                    print("Un barco ha entrado")
                    self.barcos_en_puerto.append(barco)
                    print(self.STR_TEMPLATE.format(barco.ide, dia,
                                                   len(self.barcos_en_espera)))
                    self.demora_total[barco.ide] = (dia - int(barco.arribo),
                                                    dia) #asumismos que se
                    # va el mismo dia hasta que calculamos realmente cuando
                    # se va y le hacemos filter, map(dia-el valor que tiene)
                else:
                    print("el puerto está lleno")
            else:
                print("La marea no lo permite")

        for barcos in self.barcos_en_puerto:
            if barcos in self.barcos_en_espera:
                self.barcos_en_espera.remove(barcos)

    def cargar_barco(self, barco):
        """
        Lo que hace es llamar teps para contenedores que se deben cargar al barco
        :param barco: namedtuple que tiene la información de barcos.
        :return: prints que señala en qué está
        """
        for contenedor in barco.lista_carga:
            if contenedor not in self.puerto.contenedor_esperando:
                print("buscando y cargando el contenedor {}".format(contenedor))

                if list(filter(lambda x: x.trabajando==False, lista_teps)):
                    # la
                    # funcion llamar
                    # debería marcalo como ocupado y hacer que se acercara
                    tep_seleccionado = list(filter(lambda x:
                                                  x.trabajando==False,
                                              lista_teps))[0]
                    tep_seleccionado.trabajando = True
                    # lo siguiente se quita después
                    for contenedor_x in lista_contenedores:
                        if contenedor_x.ide == barco.ide + contenedor[1]:
                            print(contenedor_x)
                            contenedor_x.posicion[0] = 385
                            tep_seleccionado.ubicacion = contenedor_x.posicion
                            ubicacion_contenedor = contenedor_x.posicion
                            # ubicacion_contenedor =
                            # self.puerto.ubicar_contenedor(contenedor)
                    if tep_seleccionado.ubicacion != \
                            ubicacion_contenedor:
                        tep_seleccionado.ruta += [
                            ubicacion_contenedor, self.puerto.pos_barcos[
                                barco]]
                        self.puerto.contenedor_esperando.append(contenedor)
                        print("El contenedor está a la espera que el tep "
                              "llegue por él")
                    else:
                        print("El contenedor está en un tep hacia el barco")
                        tep_seleccionado.ruta.append(barco)
                        # self.puerto.pos_barcos[barco]
                        # el tep debe avisarle al barco que llegó y cargó al
                        # llegar a su destino final y cambiando el valor
                        # self.barco_en_puerto.lista_carga
                else:
                    print("De momento no hay un tep disponible, deberá "
                          "esperar")
            else:
                print("El contendor está esperando o siendo trasladado")

            # esto va en otro lado o puede ser un if
            # contenedor.pos in barco.pos barco.lista_carga.remove(
            # contenedor) pero recuerden que de momento solo es su ide en el
            # primer for, no es una namedtuple aun

    def descargar_barco(self, barco):
        """
        Lo que hace es llamar teps para contenedores que se deben descargar
        al barco
        :param barco: namedtuple que tiene la información de barcos.
        :return: prints que señala en qué están
        """
        for contenedor in barco.lista_descarga:
            print("buscando y descargando el contenedor {}".format(contenedor))
            if list(filter(lambda x: x.trabajando == False, lista_teps)):
                # la
                # funcion llamar
                # debería marcalo como ocupado y hacer que se acercara
                tep_seleccionado = list(filter(lambda x:
                                               x.trabajando == False,
                                               lista_teps))[0]
                tep_seleccionado.trabajando = True
                self.lista_contenedores_atendidos.append(contenedor)
                for contenedor_x in lista_contenedores:
                    if contenedor_x.ide == barco.ide+contenedor:
                        contenedor_x.posicion = [385, 0]
                        tep_seleccionado.ubicacion = contenedor_x.posicion
                        ubicacion_contenedor = contenedor_x.posicion
                #ubicacion_contenedor = self.puerto.ubicar_contenedor(
                # contenedor)  # Esta
                if tep_seleccionado.ubicacion != \
                        ubicacion_contenedor:
                    tep_seleccionado.ruta += [
                        ubicacion_contenedor, self.puerto.pos_barcos]
                    self.puerto.contenedor_esperando.append(contenedor)
                    print("El contenedor está a la espera que el tep "
                          "llegue por él")
                else:
                    print("El contenedor está siendo descargado justo ahora")
                    tep_seleccionado.definir_destino() # aqui hay un problema
                    # de opti
            else:
                print("De momento no hay un tep disponible, deberá "
                      "esperar")
        for contenedor_x in self.lista_contenedores_atendidos:
            if contenedor_x in barco.lista_descarga:
                barco.lista_descarga.remove(contenedor_x)

    def salida_barco(self, dia, barco):
        if int(barco.partida)+1 == dia or (not barco.lista_carga and
                                           not barco.lista_descarga):
            print("El barco se fue, quedó {} conteiners por cargar y {} "
                  "conteiners por descargar".format(barco.lista_carga,
                                                    barco.lista_descarga))
            self.barcos_en_puerto.remove(barco)

    def imprimir_estadisticas(self):
        """
        Esto falta editarlo por completo, pero basicamente es darse cuneta
        que tiempo de atencion ya no es una lista sino un diccionario con
        tupla sino me equivoco, acomodar datos y está
        :return:
        """
        # tiempo_promedio = mean(self.tiempos_atencion)
        # tiempo_total = sum(self.tiempos_atencion)
        print()
        print('Estadísticas:')
        print(f'Tiempo  total de espera {reduce(lambda x, y: x+y,list(zip(*self.demora_total.values()))[0])} dias')
        print(f'Tiempo total de atención {reduce(lambda x, y: x+y,list(zip(*self.demora_total.values()))[1])} dias')
        print(f'Total de barcos atendidos: {len(self.demora_total)}')

    def atencion_barco(self):
        """Esta función corre todas las funciones para cada día"""

        # Hacemos avanzar el reloj de la simulación día por día.
        # No importa si en ese día no pasa nada.
        for dia in range(1, self.max_tiempo):
            self.llega_barco(dia)
            self.entra_barco(dia)
            for i in range(24):
                for barco in self.barcos_en_puerto:
                    if barco.lista_carga:
                        self.cargar_barco(barco)
                    if barco.lista_descarga:
                        self.descargar_barco(barco)
                    else:
                        print("El barco ha terminado sus operaciones")
                        self.demora_total[barco.ide][1] = dia - self.demora_total[
                            barco.ide][1]
                    self.salida_barco(dia, barco)
                for tep in filter(lambda x: x.trabajando == True, lista_teps):
                    tep.mover()
                #Aqui falta la función mover teps... yo creo que eso necesita
                # ticks o algo, se mueven muchas veces en un día. Igual ojo,
                # porque la funcion cargar y descargar cambia la condicion de un
                # tep por dia, no por sub unidad de tiempo, hay que modificar
                # eso pronto.


if __name__ == '__main__':
    # Define los tipos de vehículos y su tiempo de atención promedio
    # vehículos = {'moto': 1 / 8, 'auto': 1 / 15, 'camioneta': 1 / 20}
    max_tiempo = 30

    simulacion = Simulacion(max_tiempo)
    simulacion.atencion_barco()
    simulacion.imprimir_estadisticas()
