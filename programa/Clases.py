from collections import namedtuple


Barco = namedtuple("Barco", ["codigo", "llegada", "partida",
                             "desc", "cargar"])

Container = namedtuple("Container", ["tipo", "nombre", "i", "j"])


class TEPs:
    def __init__(self, i, j):
        self.ocupado = False
        self.cargando = None
        self.i = i
        self.j = j
        self.vel = 333  # m/min

    def calcular_cont(self, container):
        dist = 0
        print("i", self.i, self.j, dist)
        if self.j == container.j:
            dist += self.t_arriba_abajo(container)
        elif self.i == container.i:
            dist += self.t_izq_der(container)
        print("p", self.i, self.j, dist)
        dist += self.mover(container)
        return dist

    def mover(self, cont):
        dist = 0
        while True:
            print("T", self.i, self.j, dist)
            if self.i >= cont.i + 2:
                self.i -= 1
                dist += self.sumar_dist_i()
            elif self.i <= cont.i - 2:
                self.i += 1
                dist += self.sumar_dist_i()
            elif self.j >= cont.j + 1:
                self.j -= 1
                dist += self.sumar_dist_j()
            elif self.j <= cont.j - 1:
                dist += self.sumar_dist_j()
                self.j += 1
            elif self.j == cont.j and (self.i == cont.i + 1
                                       or self.i == cont.i - 1):
                return dist

    def sumar_dist_i(self):
        if self.i % 2 != 0:
            return 14
        else:
            return 20

    def sumar_dist_j(self):
        if self.j % 2 == 0:
            return 53
        else:
            return 20

    def t_arriba_abajo(self, con):
        if self.j == con.j and (self.i != con.i + 1 or self.i == con.i - 1):
            self.j += 1
            return 20
        else:
            return 0

    def t_izq_der(self, con):
        if self.i == con.i and (self.j != con.j or self.j == con.j):
            self.i += 1
            return 20
        else:
            return 0


class Puerto:
    def __init__(self, i, j):
        self.ocupado = False
        self.barco = None
        self.i = i
        self.j = j


class Mapa:
    def __init__(self):
        self.cajas = self.crear_diccionario()

    @staticmethod
    def crear_diccionario():
        dictio = dict()
        for i in range(1, 6):
            for j in range(1, 11):
                dictio.update({str(2*i)+"_"+str(2*j): [2*i, 2*j, set()]})
        return dictio


if __name__ == "__main__":
    mapita = Mapa()
    print(mapita.cajas)
    T1 = TEPs(0, 4)  # arriba
    T2 = TEPs(10, 4)  # abajo
    T3 = TEPs(7, 1)  # izq
    T4 = TEPs(7, 9)  # derecha
    T5 = TEPs(0, 1)  # arriba izq
    T6 = TEPs(1, 9)  # arriba der
    T7 = TEPs(10, 1)  # abajo izq
    T8 = TEPs(10, 8)  # abajo der
    C1 = Container("ja", "2", 7, 4)
    print(T1.calcular_cont(C1))
    print(T2.calcular_cont(C1))
    print(T3.calcular_cont(C1))
    print(T4.calcular_cont(C1))
    print(T5.calcular_cont(C1))
    print(T6.calcular_cont(C1))
    print(T7.calcular_cont(C1))
    print(T8.calcular_cont(C1))
