from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QGridLayout, QHBoxLayout)
from Patio import patio


class MiMapa(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grilla = QGridLayout()
        self.setWindowTitle('Mapa')
        self.mapa = patio
        self.boton = QPushButton()

    def cambiar(self, label_ele):
        if label_ele.text() == "l":
            label_ele.setPixmap(QPixmap(
                'espacio_contenedor.jpg').scaled(106, 28))

        if label_ele.text() == "c":
            label_ele.setPixmap(QPixmap(
                'espacio_camino_c.jpg').scaled(106, 40))

        if label_ele.text() == "d":
            label_ele.setPixmap(QPixmap(
                'espacio_camino_d.jpg').scaled(40, 28))

        if label_ele.text() == "e":
            label_ele.setPixmap(QPixmap(
                'espacio_camino_d.jpg').scaled(40, 40))


    def hacer(self):
        valores_1 = self.mapa

        valores = []
        for i in valores_1:
            valores.extend(i)

        posiciones = []
        for i in range(0, len(valores_1)):
            for j in range(0, len(valores_1[0])):
                posiciones.append((i, j))

        for posicion, valor in zip(posiciones, valores):
            if valor == '':
                continue
            boton = QLabel(valor)
            self.cambiar(boton)

            """                                                             
                Aquí conectamos el evento clicked() de cada boton con el slot   
                correspondiente. En este ejemplo todos los botones usan el      
                mismo slot.                                                     
            """
            self.grilla.addWidget(boton, *posicion)
            self.grilla.setSpacing(0)
            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.addLayout(self.grilla)
            hbox.addStretch(1)
            self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication([])
    form = MiMapa()
    form.hacer()
    form.show()
    sys.exit(app.exec_())
