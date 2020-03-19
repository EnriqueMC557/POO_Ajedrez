# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ajedrez_GUI_qt.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 700)
        self.canvas = QPyQt5Canvas(Form)
        self.canvas.setGeometry(QtCore.QRect(160, 110, 400, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setObjectName("canvas")
        self.TextoMulti = QtWidgets.QLabel(Form)
        self.TextoMulti.setGeometry(QtCore.QRect(100, 20, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TextoMulti.setFont(font)
        self.TextoMulti.setTextFormat(QtCore.Qt.PlainText)
        self.TextoMulti.setAlignment(QtCore.Qt.AlignCenter)
        self.TextoMulti.setWordWrap(True)
        self.TextoMulti.setObjectName("TextoMulti")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(160, 570, 411, 72))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Iniciar_Button = QtWidgets.QPushButton(self.widget)
        self.Iniciar_Button.setObjectName("Iniciar_Button")
        self.horizontalLayout.addWidget(self.Iniciar_Button)
        spacerItem = QtWidgets.QSpacerItem(50, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.PosIn_LineEdit = QtWidgets.QLineEdit(self.widget)
        self.PosIn_LineEdit.setEnabled(False)
        self.PosIn_LineEdit.setText("")
        self.PosIn_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.PosIn_LineEdit.setObjectName("PosIn_LineEdit")
        self.verticalLayout.addWidget(self.PosIn_LineEdit)
        self.MoverPieza_Button = QtWidgets.QPushButton(self.widget)
        self.MoverPieza_Button.setEnabled(False)
        self.MoverPieza_Button.setObjectName("MoverPieza_Button")
        self.verticalLayout.addWidget(self.MoverPieza_Button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(50, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Salir_Button = QtWidgets.QPushButton(self.widget)
        self.Salir_Button.setObjectName("Salir_Button")
        self.horizontalLayout.addWidget(self.Salir_Button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TextoMulti.setText(_translate("Form", "Bienvenido a nuestro ajedrez. Presionar \"Iniciar juego\" para empezar"))
        self.Iniciar_Button.setText(_translate("Form", "Iniciar juego"))
        self.label_2.setText(_translate("Form", "Pieza a mover"))
        self.MoverPieza_Button.setText(_translate("Form", "Mover pieza"))
        self.Salir_Button.setText(_translate("Form", "Salir"))
from QPyQt5Canvas import QPyQt5Canvas
