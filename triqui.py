# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Triqui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from random import randrange

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventana(object):
    tablero = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    movimientos = 0

    def setupUi(self, Ventana):
        Ventana.setObjectName("Ventana")
        Ventana.resize(500, 320)
        Ventana.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Ventana.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.b0 = QtWidgets.QPushButton(Ventana)
        self.b0.setGeometry(QtCore.QRect(10, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b0.setFont(font)
        self.b0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b0.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b0.setText("")
        self.b0.setObjectName("b0")
        self.b3 = QtWidgets.QPushButton(Ventana)
        self.b3.setGeometry(QtCore.QRect(10, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b3.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.b6 = QtWidgets.QPushButton(Ventana)
        self.b6.setGeometry(QtCore.QRect(10, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b6.setFont(font)
        self.b6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b6.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.b1 = QtWidgets.QPushButton(Ventana)
        self.b1.setGeometry(QtCore.QRect(110, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b1.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.b4 = QtWidgets.QPushButton(Ventana)
        self.b4.setGeometry(QtCore.QRect(110, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b4.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.b7 = QtWidgets.QPushButton(Ventana)
        self.b7.setGeometry(QtCore.QRect(110, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b7.setFont(font)
        self.b7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b7.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.b2 = QtWidgets.QPushButton(Ventana)
        self.b2.setGeometry(QtCore.QRect(210, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b2.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.b5 = QtWidgets.QPushButton(Ventana)
        self.b5.setGeometry(QtCore.QRect(210, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b5.setFont(font)
        self.b5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b5.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.b8 = QtWidgets.QPushButton(Ventana)
        self.b8.setGeometry(QtCore.QRect(210, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.b8.setFont(font)
        self.b8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b8.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "backgrouNd-color: #0E7AC4; ")
        self.b8.setText("")
        self.b8.setObjectName("b8")
        self.ePuntaje = QtWidgets.QLabel(Ventana)
        self.ePuntaje.setGeometry(QtCore.QRect(360, 30, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ePuntaje.setFont(font)
        self.ePuntaje.setObjectName("ePuntaje")
        self.eMaquina = QtWidgets.QLabel(Ventana)
        self.eMaquina.setGeometry(QtCore.QRect(330, 80, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eMaquina.setFont(font)
        self.eMaquina.setStyleSheet("color: rgb(226, 0, 0);")
        self.eMaquina.setObjectName("eMaquina")
        self.eEmpates = QtWidgets.QLabel(Ventana)
        self.eEmpates.setGeometry(QtCore.QRect(330, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eEmpates.setFont(font)
        self.eEmpates.setStyleSheet("color: rgb(226, 0, 0);")
        self.eEmpates.setObjectName("eEmpates")
        self.eJugador = QtWidgets.QLabel(Ventana)
        self.eJugador.setGeometry(QtCore.QRect(330, 200, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eJugador.setFont(font)
        self.eJugador.setStyleSheet("color: rgb(226, 0, 0);")
        self.eJugador.setObjectName("eJugador")
        self.lMaquina = QtWidgets.QLineEdit(Ventana)
        self.lMaquina.setEnabled(False)
        self.lMaquina.setGeometry(QtCore.QRect(390, 80, 51, 25))
        self.lMaquina.setAlignment(QtCore.Qt.AlignCenter)
        self.lMaquina.setObjectName("lMaquina")
        self.lEmpate = QtWidgets.QLineEdit(Ventana)
        self.lEmpate.setEnabled(False)
        self.lEmpate.setGeometry(QtCore.QRect(390, 140, 51, 25))
        self.lEmpate.setAlignment(QtCore.Qt.AlignCenter)
        self.lEmpate.setObjectName("lEmpate")
        self.lJugador = QtWidgets.QLineEdit(Ventana)
        self.lJugador.setEnabled(False)
        self.lJugador.setGeometry(QtCore.QRect(390, 200, 51, 25))
        self.lJugador.setAlignment(QtCore.Qt.AlignCenter)
        self.lJugador.setObjectName("lJugador")
        self.bReiniciar = QtWidgets.QPushButton(Ventana)
        self.bReiniciar.setGeometry(QtCore.QRect(360, 270, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bReiniciar.setFont(font)
        self.bReiniciar.setObjectName("bReiniciar")

        self.b0.clicked.connect(self.hacer_clic_0)
        self.b1.clicked.connect(self.hacer_clic_1)
        self.b2.clicked.connect(self.hacer_clic_2)
        self.b3.clicked.connect(self.hacer_clic_3)
        self.b4.clicked.connect(self.hacer_clic_4)
        self.b5.clicked.connect(self.hacer_clic_5)
        self.b6.clicked.connect(self.hacer_clic_6)
        self.b7.clicked.connect(self.hacer_clic_7)
        self.b8.clicked.connect(self.hacer_clic_8)
        self.bReiniciar.clicked.connect(self.reiniciar)

        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def hacer_clic_0(self):
        self.jugada(self.b0)

    def hacer_clic_1(self):
        self.jugada(self.b1)

    def hacer_clic_2(self):
        self.jugada(self.b2)

    def hacer_clic_3(self):
        self.jugada(self.b3)

    def hacer_clic_4(self):
        self.jugada(self.b4)

    def hacer_clic_5(self):
        self.jugada(self.b5)

    def hacer_clic_6(self):
        self.jugada(self.b6)

    def hacer_clic_7(self):
        self.jugada(self.b7)

    def hacer_clic_8(self):
        self.jugada(self.b8)

    def colocar_ficha_maquina(self):
        while self.tablero.count(0):
            i = randrange(9)
            boton_maquina = self.__dict__['b' + str(i)]
            if not self.tablero[i]:
                self.tablero[i] = 2
                boton_maquina.setText('O')
                boton_maquina.setEnabled(False)
                return True

    def jugada(self, boton):
        boton.setEnabled(False)
        boton.setText('X')
        self.tablero[int(list(boton.objectName())[1])] = 1
        self.movimientos += 1
        if self.verificar_jugada(1):
            jugador = str(int(self.lJugador.displayText()) + 1)
            self.lJugador.setText(jugador)
            self.congelar()
            return
        elif self.colocar_ficha_maquina():
            self.movimientos += 1
            if self.verificar_jugada(2):
                maquina = str(int(self.lMaquina.displayText()) + 1)
                self.lMaquina.setText(maquina)
                self.congelar()
                return
        if self.movimientos == 9:
            empate = str(int(self.lEmpate.displayText()) + 1)
            self.lEmpate.setText(empate)

    def congelar(self):
        i = 0
        while i < 9:
            self.__dict__['b' + str(i)].setEnabled(False)
            i += 1

    def verificar_jugada(self, valor):
        if self.tablero[0] == self.tablero[1] == self.tablero[2] == valor:
            self.pintar(0, 1, 2)
            return 1
        if self.tablero[3] == self.tablero[4] == self.tablero[5] == valor:
            self.pintar(3, 4, 5)
            return 1
        if self.tablero[6] == self.tablero[7] == self.tablero[8] == valor:
            self.pintar(6, 7, 8)
            return 1
        if self.tablero[0] == self.tablero[3] == self.tablero[6] == valor:
            self.pintar(0, 3, 6)
            return 1
        if self.tablero[1] == self.tablero[4] == self.tablero[7] == valor:
            self.pintar(1, 4, 7)
            return 1
        if self.tablero[2] == self.tablero[5] == self.tablero[8] == valor:
            self.pintar(2, 5, 8)
            return 1
        if self.tablero[0] == self.tablero[4] == self.tablero[8] == valor:
            self.pintar(0, 4, 8)
            return 1
        if self.tablero[6] == self.tablero[4] == self.tablero[2] == valor:
            self.pintar(6, 4, 2)
            return 1

    def pintar(self, a, b, c):
        self.__dict__['b' + str(a)].setStyleSheet("color: rgb(100, 0, 100);")
        self.__dict__['b' + str(b)].setStyleSheet("color: rgb(100, 0, 100);")
        self.__dict__['b' + str(c)].setStyleSheet("color: rgb(100, 0, 100);")

    def reiniciar(self):
        self.tablero = [0 for i in range(9)]
        self.movimientos = 0
        i = 0
        while i < 9:
            self.__dict__['b' + str(i)].setEnabled(True)
            self.__dict__['b' + str(i)].setText('')
            self.__dict__['b' + str(i)].setStyleSheet("background-color: #0E7AC4;color: rgb(255, 255, 255);")
            i += 1

    def retranslateUi(self, Ventana):
        _translate = QtCore.QCoreApplication.translate
        Ventana.setWindowTitle(_translate("Ventana", "Triqui"))
        self.ePuntaje.setText(_translate("Ventana", "PUNTAJE"))
        self.eMaquina.setText(_translate("Ventana", "Maquina"))
        self.eEmpates.setText(_translate("Ventana", "Empates"))
        self.eJugador.setText(_translate("Ventana", "Jugador"))
        self.lMaquina.setText(_translate("Ventana", "0"))
        self.lEmpate.setText(_translate("Ventana", "0"))
        self.lJugador.setText(_translate("Ventana", "0"))
        self.bReiniciar.setText(_translate("Ventana", "Reiniciar"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Ventana = QtWidgets.QWidget()
    ui = Ui_Ventana()
    ui.setupUi(Ventana)
    Ventana.show()
    sys.exit(app.exec_())
