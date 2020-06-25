from Lectura import crear_barcos, leer_probabilidades, crear_teps, \
    costo_esperado, dict_carga_barco
from Clases import Mapa, Puerto, Container
from random import random, triangular


class Simulacion:
    def __init__(self, iteraciones, d1, d2):
        self.iter = iteraciones
        self.barcos = sorted(crear_barcos(), key=lambda barco: barco[3])
        self.mapa = Mapa()
        self.barcos_atracados = []
        self.esperando_atracar = []
        self.descargado_en_puerto = [0, 0, 0, 0]
        self.prob = leer_probabilidades()
        self.dia = 0
        self.tiempo = 0
        self.barcos_despachados = 0
        self.barcos_zarpados = 0
        self.barcos_totalmente_cargados = 0
        self.barcos_fueron = 0
        self.eventos = []
        self.teps = crear_teps()
        self.Puertos = [Puerto(7, 12), Puerto(14, 12), Puerto(21, 12)]
        self.cargas_descargas = self.crear_c_d()
        self.conteo_carg = 0
        self.conteo_desc = 0
        self.descargando = True
        self.por_descargar = 0
        # Relevantes para estadísticas
        self.dias_pen = [0, 0, 0]
        self.falto = []
        self.decisiones = [d1, d2]
        self.eventos2 = []

    def crear_c_d(self):
        lista = []
        for _ in self.teps:
            lista.append([0])
        return lista

    def revisar_eventos(self, t):
        if not self.eventos:
            if self.barcos_atracados:
                er = []
                for ele in self.teps:
                    if self.barcos_atracados:
                        if not ele.ocupado:
                            er.append([ele, self.asignaciones_simples() + t])
                self.eventos += er
                self.eventos = sorted(self.eventos, key=lambda cosa: cosa[1])

    def agregar_evento(self, barco, t):
        if self.barcos_atracados:
            self.eventos.append([barco, t + self.asignaciones_simples()])
        self.eventos = sorted(self.eventos, key=lambda ba: ba[1])

    def asignaciones_simples(self):
        t = triangular(8, 18, 12)
        t += 2 * 385 / 333
        t += triangular(5, 10, 8)
        if self.descargando:
            t += triangular(5, 10, 8)
        t += triangular(8, 18, 12)
        return t

    def contar_descargar(self):
        num = 0
        for ele in self.barcos_atracados:
            num += ele.desc
        return num

    def ejecutar__medio_dia(self, dia, t, valor):
        if len(self.barcos_atracados) > 0:
            desc = 0
            self.revisar_eventos(t)
            while self.eventos and t <= valor * 60 * dia:
                if self.eventos[0][1] <= valor * 60 * dia:
                    t = self.eventos.pop(0)[1]
                    desc += 1
                    self.conteo_carg += 1
                    if self.descargando:
                        self.conteo_desc += 1
                        if not self.decisiones[0] and self.conteo_desc == \
                                self.barcos_atracados[0].desc:
                            self.descargando = False
                        if self.decisiones[0] and self.conteo_desc == \
                                self.por_descargar:
                            self.descargando = False

                    if self.barcos_atracados[0].cargar == self.conteo_carg:
                        print(f"El barco {self.barcos_atracados[0].codigo} fue "
                              f"totalmente cargado, por lo que izó anclas y se"
                              f" fue del puerto en el dia {self.dia}.")
                        self.barcos_totalmente_cargados += 1
                        self.barcos_atracados.remove(self.barcos_atracados[0])
                        self.conteo_carg = 0
                        if not self.decisiones[0]:
                            self.descargando = True
                        if self.decisiones[0]:
                            if len(self.barcos_atracados) > 0:
                                self.por_descargar -= \
                                    self.barcos_atracados[0].desc
                            else:
                                self.descargando = True
                    if len(self.barcos_atracados) > 0:
                        self.agregar_evento(self.barcos[0], t)
                    else:
                        self.eventos = []

                else:
                    break
            """
            print(f"ocurrieron {desc} cargas a los barcos y {desc} descargas a"
                  f" los barcos encallados durante el día {self.dia}.")
            """
        else:
            self.alarma(valor, t)
            self.eventos = []
            t += valor * 60
        return t

    def alarma(self, valor, t):
        if valor == 8:
            print("Alarma alarma, a las 00:00")
        else:
            print("Alarma alarma, a las 12:00")


    def metodo_entrada(self, con_costo_esperado, lista):
        if con_costo_esperado:
            provisoria = list(map(lambda x: (x, costo_esperado(x.codigo)[
                self.dia - 1]), lista))
            provisoria = sorted(provisoria, key=lambda ele: ele[1],
                              reverse=False)
            return list(map(lambda barco: barco[0], provisoria))

        else:
            return sorted(lista, key=lambda barco:
            barco.partida)

    def menor_dist(self, cont):
        posibles = []
        for ele in self.teps:
            if not ele.ocupado:
                posibles.append(ele)
        dist = []
        for ele in posibles:
            dist.append(ele.calcular_cont(cont))
        valor = dist.index(min(dist))
        return posibles[valor]

    def corrida(self):
        t = 0
        while self.barcos_despachados != 16:
            self.iniciar_dia()
            t = self.ejecutar__medio_dia(self.dia, t, 8)
            self.medio_dia()
            t = self.ejecutar__medio_dia(self.dia, 8 * 60 * self.dia, 12)
            self.acabar_dia()
        self.falto.append(self.barcos_zarpados)
        return [self.dias_pen, self.falto]

    def resetear(self):
        print(f"\nZarparon {self.barcos_zarpados} barcos sin haber sido "
              f"totalmente cargados.")
        print(f"Se fueron sin atracar {self.barcos_fueron} barcos.")
        print(f"Se fueron habiendo estado totalmente cargados"
              f" {self.barcos_totalmente_cargados} barcos.")
        total = self.dias_pen[0]*3600 + self.dias_pen[1]*2400 \
            + self.dias_pen[0]*1800
        print(f"\nLa penalización total fue de {total}.\nEn donde se tuvieron "
              f"{self.dias_pen[0]} dias de penalización para barcos de 1200"
              f" contenedores de capacidad, {self.dias_pen[1]} dias "
              f"para barcos de 800 y {self.dias_pen[2]} para barcos de 600.")
        self.barcos_atracados = []
        self.esperando_atracar = []
        self.descargado_en_puerto = [0, 0, 0, 0]
        self.dia = 0
        self.tiempo = 0
        self.barcos_despachados = 0
        self.barcos_zarpados = 0
        self.barcos_fueron = 0
        self.eventos = []
        self.dias_pen = [0, 0, 0]
        self.barcos_totalmente_cargados = 0

    def iniciar_dia(self):
        self.dia += 1
        print(f"\n   Comenzó el día {self.dia}.")
        for ele in self.barcos:
            if ele.llegada == self.dia:
                self.esperando_atracar.append(ele)
                self.esperando_atracar = self.metodo_entrada(
                    self.decisiones[1], self.esperando_atracar)
        entro = True
        while entro:
            if len(self.esperando_atracar) > 0:
                barco = self.esperando_atracar[0]
                if len(self.barcos_atracados) < 3 and \
                        self.puede_entrar(barco, self.dia):
                    print(f"Atracó el {barco.codigo} en el día {self.dia} a "
                          f"las 00:00.")
                    self.por_descargar = self.contar_descargar()
                    self.barcos_atracados.append(barco)
                    self.esperando_atracar.remove(barco)
                    self.calc_min(barco)
                else:
                    entro = False

                for barco in self.esperando_atracar:
                    if "1200" in barco.codigo:
                        self.dias_pen[0] += 1
                    elif "800" in barco.codigo:
                        self.dias_pen[1] += 1
                    elif "600" in barco.codigo:
                        self.dias_pen[2] += 1
            else:
                entro = False

    def calc_min(self, barco):
        return ((barco.partida + 1) - self.dia)*20*60

    def medio_dia(self):
        while True:
            if len(self.esperando_atracar) > 0:
                barco = self.esperando_atracar[0]
                if len(self.barcos_atracados) < 3 and \
                        self.puede_entrar(barco, self.dia):
                    print(
                        f"Atracó el {barco.codigo} en el día {self.dia} a "
                        f"las 12:00.")
                    self.por_descargar = self.contar_descargar()
                    self.barcos_atracados.append(barco)
                    self.esperando_atracar.remove(barco)
                    self.calc_min(barco)

                    if "1200" in barco.codigo:
                        self.dias_pen[0] -= 1
                    elif "800" in barco.codigo:
                        self.dias_pen[1] -= 1
                    elif "600" in barco.codigo:
                        self.dias_pen[2] -= 1
                else:
                    break
            else:
                break

    def acabar_dia(self):
        for barco in self.barcos:
            if barco.partida == self.dia:
                self.barcos_despachados += 1
                self.conteo_carg = 0
                # todo
                if barco in self.barcos_atracados:
                    print(f"Zarpó el {barco.codigo} en el día {self.dia} sin"
                          f" haber sido cargado por completo.")
                    self.barcos_atracados.remove(barco)
                    self.barcos_zarpados += 1
                elif barco in self.esperando_atracar:
                    print(f"El {barco.codigo} se fue en el día {self.dia} "
                          f"sin haber podido atracar en el puerto.")
                    self.esperando_atracar.remove(barco)
                    self.barcos_fueron += 1

    def puede_entrar(self, barco, dia):
        if dia < 30:
            if "1200" in barco.codigo:
                return random() >= self.prob[0][dia]
            elif "800" in barco.codigo:
                return random() >= self.prob[1][dia]
            elif "600" in barco.codigo:
                return random() >= self.prob[2][dia]
        else:
            if "1200" in barco.codigo:
                return random() >= self.prob[0][dia % 30]
            elif "800" in barco.codigo:
                return random() >= self.prob[1][dia % 30]
            elif "600" in barco.codigo:
                return random() >= self.prob[2][dia % 30]

    def simular(self):
        i = 0
        estadisticas = []
        # Evaluar el escribir los resultados en un archivo para que sean
        # más simples de comparar posteriormente
        # formato a priori: Parametros: ..., Num_Iteraciones: n, Resultados:...
        # acordarse de cada vez que se corrija el algoritmo borrar este archivo
        while i < self.iter:
            print(f"\n #####  Comenzó la corrida {i + 1}.  #####\n")
            res = self.corrida()
            estadisticas.append(res)
            self.resetear()
            print(f"\n #####  Terminó la corrida {i + 1}.  ##### \n")
            i += 1
        d1200 = 0
        d800 = 0
        d600 = 0
        for ele in estadisticas:
            d1200 += ele[0][0]/self.iter
            d800 += ele[0][1]/self.iter
            d600 += ele[0][2]/self.iter
        print("\n\n" + "#"*100 + "\n\n")
        print(f"-- Se tuvo en promedio {d1200}, {d800} y {d600} dias de "
              f"penalización para los barcos de 1200, 800, 600 contenedores de"
              f" capacidad respectivamente.\n")
        print(f"-- Lo anteior implica un costo promedio de penalizaciones de: "
              f"{d1200*3600 + d800*2400 + d600*1800}.\n")
        print(f"-- Se tuvo en promedio {sum(res[1])/self.iter} barcos que no "
              f"pudieron satisfacer su carga completa.\n")


if __name__ == "__main__":
    """
    Simulacion(iteraciones, d1)
    
        -  iteraciones: número de iteraciones a realizar (valor entero positivo)
        -  d1: (decisión 1) Al realizar el proceso de carga y descarga 
        lo realizamos de la siguiente manera:
            True: Damos prioridad a hacer cada camino a cargar con una 
                descarga (en la medida de lo posible)
            False: Priorizaremos echar al primer barco posible (una vez que un
                barco se terminó de descargar pararemos las descargas hasta que
                se haya terminado de cargar un barco)
    
    """
    simulacion = Simulacion(50, True, True)
    simulacion.simular()
