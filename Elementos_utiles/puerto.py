
from Elementos_utiles import patio


class Puerto:
    """ Esta clase modela la línea de revisión en el taller."""

    def __init__(self):
        self.dimensiones = 10 # inventado, se debe cambiar
        self.patio = patio
        self.contenedor_esperando = []
        self.pos_barcos = [385, 0]#

    def ubicar_contendor(self, contendor):
        for i in self.patio:
            for j in i:
                if j[contendor] == contendor:
                    print("contenedor hubicado!")
                    # return i,j
                else:
                    print("llegó por camniones")
                    # return 0,0
