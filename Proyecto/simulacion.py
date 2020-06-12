#yes, esto es una simulacion
from threading import Thread
from time import sleep
from random import random
from imports import *
from entidades import *
import Patio


numero = [1, 2]
dias = 5


class simulacion(Thread):
    def __init__(self, dias):
        super().__init__()
        self.dia = 0
        self.teps = list()
        self.max = dias

    def agregarTeps(self):
        for i in numero:
            self.teps.append(tep(i))

    def simular(self):
        while self.dia <= self.max:
            for i in self.teps:
                i.start()

class tep(Thread):#
    def __init__(self, numero):
        super().__init__()
        self.numero = numero
        self.trabajando = False # cambiar a True, este es para ver si esta haciendo algo o no
        self.ruta = []
        self.posicion = [0, 0]
        self.contador_camion = 0
        self.contador_barco = 0
        self.corriendo = True #este es para parar el thread, while self.corriendo

    def run(self): #cambiar el run por lo que es djikstra, agregar los movimientos, etc. Crear funciones para cosas con importancia que se llamen en el run
        print(f"Hola soy {self.numero}")
        while self.trabajando:
            print("Estoy trabajando wei")
            sleep(random(1,5))
            self.trabajando = False
        print("Recorcholis, se me acabo el trabajo")

    # invencion nata
    def mover(self):
        for ele in self.ruta:
            if ele == "camion":
                self.contador_barco += 1
                if self.contador_barco == 18:
                    if self.posicion[0] > 0:
                        print("en camino")
                        self.posicion[0] -= 333
                    else:
                        self.contador_camion += 1
                        print("Ya llegué al camión")
                        if self.contador_camion == 10:
                            print("Ya llegué al camión y soy libre")
                            self.trabajando = False
                            self.contador_barco = 0
                            self.contador_camion = 0
            else:
                self.contador_camion += 1
                if self.contador_camion == 10:
                    if self.posicion[0] < 385:
                        print("en camino")
                        self.posicion[0] += 333
                    else:
                        self.contador_barco += 1
                        if self.contador_barco == 18:
                            print("ya llegué al barco, soy libre")
                            self.trabajando = False
                            self.contador_barco = 0
                            self.contador_camion = 0

    def definir_destino(self):
        # mientras solo son camiones para no usar el patio aun
        self.ruta.append("camion")

    def run(self):
        while self.corriendo:
            pass

    def iterative_deepening_a_star(tree, heuristic, start, goal):
    """
    Performs the iterative deepening A Star (A*) algorithm to find the shortest path from a start to a target node.
    Can be modified to handle graphs by keeping track of already visited nodes.
    :param tree:      Patio
    :param heuristic: distancia entre start y goal
    :param start:      root.
    :param goal:      The node we're searching for.
    :return: number shortest distance to the goal node. Can be easily modified to return the path.
    """
    threshold = heuristic[start][goal]
    while True:
        print("Iteration with threshold: " + str(threshold))
        distance = iterative_deepening_a_star_rec(tree, heuristic, start, goal, 0, threshold)
        if distance == float("inf"):
            # Node not found and no more nodes to visit
            return -1
        elif distance < 0:
            # if we found the node, the function returns the negative distance
            print("Found the node we're looking for!")
            return -distance
        else:
            # if it hasn't found the node, it returns the (positive) next-bigger threshold
            threshold = distance


lista_teps = [tep(i) for i in range(15)]



if __name__ == "__main__":
    puerto = simulacion(dias)
    puerto.start()
