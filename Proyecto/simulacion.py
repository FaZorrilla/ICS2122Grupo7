#yes, esto es una simulacion
from threading import Thread
from time import sleep
from random import random
from imports import *
from entidades import *


numero = [1, 2]
dias = 5

class simulacion(Thread):
    def __init__(self, dias):
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

class tep:#
    def __init__(self, numero):
        self.numero = numero
        self.trabajando = False # cambiar a True
        self.ruta = []
        self.posicion = [0, 0]

    def run(self):
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
                if self.posicion != [0, 0]:
                    print("en camino")
                    self.posicion[0] -= 20
                else:
                    print("Ya llegué al camión, soy libre")
                    self.trabajando = False
            else:
                if self.posicion != [385, 0]:
                    print("en camino")
                    self.posicion[0] += 20
                else:
                    print("ya llegué al barco, soy libre")
                    self.trabajando = False

    def definir_destino(self):
        # mientras solo son camiones para no usar el patio aun
        self.ruta.append("camion")


lista_teps = [tep(i) for i in range(3000)]



if __name__ == "__main__":
    puerto = simulacion(dias)
    puerto.start()
