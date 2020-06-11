from functools import reduce


patio = [["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
         ["c", [], "c", [], "c", [], "c", [], "c", [], "c"],
         ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]]
dimension = {"Estiba": (53/2, 14/2), "Camion": (), "Barco": 360/6}
conteiners_en_patio = {}


class Nodo:
    def __init__(self, ide, tipo):
        self.ide = ide
        self.lleno = False
        self.pos_x = None
        self.pos_y = None
        self.dimension = dimension[tipo]


class Arista(object):
    def __init__(self, elemento, peso):
        self.elemento = elemento
        self.peso = peso

    def __str__(self):
        return str(self.elemento) + str(self.peso)


class Grafo(object):
    def __init__(self):
        self.relaciones = {}

    def __str__(self):
        return str(self.relaciones)

    def agregar(self, elemento):
        self.relaciones.update({elemento: []})

    def relacionar_unilateral(self, origen, destino, peso):
        self.relaciones[origen].append(Arista(destino, peso))

    def relacionar(self, elemento1, elemento2, peso=1):
        self.relacionar_unilateral(elemento1, elemento2, peso)
        self.relacionar_unilateral(elemento2, elemento1, peso)

    def quitar_relaciones(self, elemento):
        self.relaciones[elemento] = []

    def camino_minimo(self, origen, destino):
        etiquetas = {origen: (0, None)}
        self.dijkstra(destino, etiquetas, [])
        return self.construirCamino(etiquetas, origen, destino)

    def construirCamino(self, etiquetas, origen, destino):
        print(origen, destino)
        if origen == destino:
            return [origen]
        return self.construirCamino(etiquetas, origen,
                               self.anterior(etiquetas[destino])) + [
                   destino]

    def dijkstra(self, destino, etiquetas, procesados):
        nodoActual = self.menorValorNoProcesado(etiquetas, procesados)
        if nodoActual == destino:
            return
        procesados.append(nodoActual)
        for vecino in self.vecinoNoProcesado(nodoActual, procesados):
            self.generarEtiqueta(vecino, nodoActual, etiquetas)
        self.dijkstra(destino, etiquetas, procesados)

    def generarEtiqueta(self, nodo, anterior, etiquetas):
        etiquetaNodoAnterior = etiquetas[anterior]
        etiquetaPropuesta = self.peso(anterior, nodo) + self.acumulado(
            etiquetaNodoAnterior), anterior
        if (nodo not in etiquetas.keys() or self.acumulado(
                etiquetaPropuesta) < self.acumulado(etiquetas[nodo])):
            etiquetas.update({nodo: etiquetaPropuesta})

    def peso(self, nodoOrigen, nodoDestino):
        return reduce(lambda x, y: x if x.elemento == nodoDestino else y,
                      grafo.relaciones[nodoOrigen]).peso

    def acumulado(self, etiqueta):
        return etiqueta[0]

    def anterior(self, etiqueta):
        return etiqueta[1]

    def menorValorNoProcesado(self, etiquetas, procesados):
        etiquetadosSinProcesar = filter(lambda nodo: not nodo[0] in procesados,
                                        etiquetas.items())
        return min(etiquetadosSinProcesar, key=lambda acum: acum[1][0])[0]

    def vecinoNoProcesado(self, nodo, procesados):
        aristasDeVecinosNoProcesados = filter(lambda x: not x in procesados,
                                              self.aristas(nodo))
        return [arista.elemento for arista in aristasDeVecinosNoProcesados]

    def aristas(self, nodo):
        return self.relaciones[nodo]


def instanciar_nodos(grafo):
    cant_fila = 0
    valor = 0
    for fila in patio:
        cant_fila += 0.5
        for ele in fila:
            if type(ele) == list:
                valor += 1
                nuevo_nodo = Nodo(str(valor), "Estiba")
                nuevo_nodo.pos_x = 26.5 + 73 * ((valor-1) % 5) + 20
                nuevo_nodo.pos_y = -27 - 34 * (cant_fila - 1)
                grafo.agregar(nuevo_nodo)


def instanciar_relaciones(grafo):
    # elemento = Nodo
    for ele in grafo.relaciones:
        for ele2 in grafo.relaciones:
            if int(ele.ide)+1 == int(ele2.ide):
                if int(ele.ide)%5 != 0:
                    grafo.relacionar(ele, ele2, 73)
            if int(ele.ide)+5 == int(ele2.ide):
                grafo.relacionar(ele, ele2, 34)


def visualizacion_relaciones(grafo):
    for i in grafo.relaciones:
        print(i.ide, list(map(lambda y: y.ide, map(lambda x:
                                                           x.elemento,
                                             grafo.relaciones[i]))))


def instanciar_camiones(grafo):
    nodo_nuevo = Nodo(54, "Camion")
    nodo_nuevo.pos_x = 0
    nodo_nuevo.pos_y = 180
    grafo.agregar(nodo_nuevo)


def instanciar_muelle(grafo):
    for veces in range(0, 3):
        nodo_nuevo  = Nodo(str(51 + veces), "Barco")
        nodo_nuevo.pos_x = 385
        nodo_nuevo.pos_y = 60 * (2*veces + 1)
        grafo.agregar(nodo_nuevo)


def asignar_posicion(grafo, barcos):
    for barco in barcos:
        for ele in filter(
                        lambda x: x.ide == "51" or x.ide == "52" or
                                  x.ide == "53", grafo.relaciones):
            if barco.posicion == [0, 0]:
                if int(ele.ide) == 51 and not ele.lleno:
                    barco.posicion = [ele.pos_x, ele.pos_y]
                    ele.lleno = True
                    for nodo in filter(
                            lambda x: x.ide == "5" or x.ide == "10" or
                                      x.ide == "15", grafo.relaciones):
                        grafo.relacionar(ele, nodo, 20)
                elif int(ele.ide) == 52 and not ele.lleno:
                    barco.posicion = [ele.pos_x, ele.pos_y]
                    ele.lleno = True
                    for nodo in filter(
                            lambda x: x.ide == "20" or x.ide == "25" or
                                      x.ide == "30" or x.ide == "35",
                            grafo.relaciones):
                        grafo.relacionar(ele, nodo, 20)
                elif int(ele.ide) == 53 and not ele.lleno:
                    barco.posicion = [ele.pos_x, ele.pos_y]
                    ele.lleno = True
                    for nodo in filter(
                            lambda x: x.ide == "40" or x.ide == "45" or
                                      x.ide == "50", grafo.relaciones):
                        grafo.relacionar(ele, nodo, 20)



class Barco:
    def __init__(self):
        self.posicion = [0, 0]
b1 = Barco()
b2 = Barco()
b3 = Barco()

grafo = Grafo()
instanciar_nodos(grafo)
instanciar_relaciones(grafo)
instanciar_muelle(grafo)
barcos = [b1, b2]
# asignar_posicion(grafo, barcos)
visualizacion_relaciones(grafo)
nodo1 = [valor for valor in grafo.relaciones if valor.ide == "5"][0]
nodo2 = [valor for valor in grafo.relaciones if valor.ide == "23"][0]
print(list(map(lambda x: x.ide, grafo.camino_minimo(nodo1, nodo2))))

#si el barco se va, aplicar grafo.quitar_relaciones, para el barco que se
# encuentr en esa posición.