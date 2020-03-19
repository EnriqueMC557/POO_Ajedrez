# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ajedrez_GUI_qt.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from QPyQt5Canvas import QPyQt5Canvas

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(676, 648)
        self.canvas = QPyQt5Canvas(Form)
        self.canvas.setGeometry(QtCore.QRect(90, 10, 500, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setObjectName("canvas")
        self.Iniciar_Button = QtWidgets.QPushButton(Form)
        self.Iniciar_Button.setGeometry(QtCore.QRect(170, 540, 75, 23))
        self.Iniciar_Button.setObjectName("Iniciar_Button")
        self.Salir_Button = QtWidgets.QPushButton(Form)
        self.Salir_Button.setGeometry(QtCore.QRect(430, 540, 75, 23))
        self.Salir_Button.setObjectName("Salir_Button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Iniciar_Button.setText(_translate("Form", "Iniciar juego"))
        self.Salir_Button.setText(_translate("Form", "Salir"))

