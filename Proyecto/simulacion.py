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

class tep(Thread):
    def __init__(self, numero):
        self.numero = numero
        self.trabajando = True

    def run(self):
        print(f"Hola soy {self.numero}")
        while self.trabajando:
            print("Estoy trabajando wei")
            sleep(random(1,5))
            self.trabajando = False
        print("Recorcholis, se me acabo el trabajo")
        

if __name__ == "__main__":
    puerto = simulacion(dias)
    puerto.start()
