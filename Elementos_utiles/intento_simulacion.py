from collections import deque
from random import random
from Proyecto.imports import probabilidades
from statistics import mean
from Proyecto.puerto import Puerto
from Proyecto.entidades import lista_barcos
from Proyecto.simulacion import lista_teps# Los teps después
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

    def llega_barco(self, dia):
        llegan_hoy = filter(lambda x: int(x.arribo) == dia, lista_barcos)
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
        Esta property modela si llega o no un barco a la cola.
        Se muestrea de una distribución de probabilidad uniforme. El método retorna
        True si el valor entregado por la función random es mayor a un valor dado.
        En este caso, es sencillo ver que retornará True un 20% de las veces.
        """
        probabilidad_por_dia = probabilidades[dia]
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
                    self.barcos_en_espera.remove(barco)
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

    def cargar_barco(self, barco):
        for contenedor in barco.lista_carga:
            if contenedor not in self.puerto.contenedor_esperando:
                print("buscando y cargando el contenedor {}".format(contenedor))
                ubicacion_contenedor = self.puerto.ubicar_contenedor(
                    contenedor) # Esta
                # función
                # debería
                # localizar al contenedor que necesita el barco
                if filter(lambda x: x.trabajando==False, lista_teps):
                    # la
                    # funcion llamar
                    # debería marcalo como ocupado y hacer que se acercara
                    tep_seleccionado = list(filter(lambda x:
                                                  x.trabajando==False,
                                              lista_teps))[0]
                    tep_seleccionado.trabajando = True
                    if tep_seleccionado.ubicacion != \
                            ubicacion_contenedor:
                        tep_seleccionado.ruta += [
                            ubicacion_contenedor, self.puerto.pos_barcos]
                        self.puerto.contenedor_esperando.append(contenedor)
                        print("El contenedor está a la espera que el tep "
                              "llegue por él")
                    else:
                        print("El contenedor está en un tep hacia el barco")
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
        for contenedor in barco.lista_descarga:
            print("buscando y descargando el contenedor {}".format(contenedor))
            barco.lista_descarga.remove(contenedor)


    def imprimir_estadisticas(self):
        tiempo_promedio = mean(self.tiempos_atencion)
        tiempo_total = sum(self.tiempos_atencion)

        print()
        print('Estadísticas:')
        print(f'Tiempo promedio de atención {tiempo_promedio:6.2f} min.')
        print(f'Tiempo total de atención {tiempo_total:6.2f} min')
        print(f'Total de vehículos atendidos: {len(self.tiempos_atencion)}')

    def atencion_barco(self):
        """Esta función maneja todo el proceso"""

        # Hacemos avanzar el reloj de la simulación día por día.
        # No importa si en ese día no pasa nada.
        for dia in range(self.max_tiempo):
            self.llega_barco(dia)
            self.entra_barco(dia)
            for barco in self.barcos_en_puerto:
                if barco.lista_carga:
                    self.cargar_barco(barco)
                if barco.lista_descarga:
                    self.descargar_barco(barco)
                else:
                    print("El barco ha terminado sus operaciones")
                    self.demora_total[barco.ide][1] = dia - self.demora_total[
                        barco.ide][1]


if __name__ == '__main__':
    # Define los tipos de vehículos y su tiempo de atención promedio
    # vehículos = {'moto': 1 / 8, 'auto': 1 / 15, 'camioneta': 1 / 20}
    max_tiempo = 30

    simulacion = Simulacion(max_tiempo)
    simulacion.atencion_barco()
