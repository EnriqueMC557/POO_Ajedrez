"""
GUI para ajedrez
I.P.O.O
Aguilar C. M. R. & Mena C. E.
"""

import sys
from Ajedrez_GUI import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from main import Menu

class mpl_gui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #Conexiones
        self.ui.Iniciar_Button.clicked.connect(self.Iniciar)
        self.ui.Salir_Button.clicked.connect(self.Salir)
        self.ui.MoverPieza_Button.clicked.connect(self.MoverPieza)
    
    def Iniciar(self):
        #Iniciar nombre de jugadores
        text, ok = QInputDialog.getText(self, 'Jugador1', 'Ingrese nombre (blancas): ')
        self.jugador1 = str(text)
        text, ok = QInputDialog.getText(self, 'Jugador2', 'Ingrese nombre (negras): ')
        self.jugador2 = str(text)
        print(self.jugador1)
        print(self.jugador2)
        self.ActualTeam = 'wh'
        self.ui.PosIn_LineEdit.setEnabled(True)
        self.ui.label_2.setEnabled(True)
        self.ui.MoverPieza_Button.setEnabled(True)
        
        self.juego = Menu(self.ui.canvas.canvas)
    
    def MoverPieza(self):
        C = self.ui.PosIn_LineEdit.text()
        print(C)
        print(self.ActualTeam+'\n')
        self.ActualTeam = self.juego.SolicitarCoordenada(C, self.ActualTeam)
            
    
    def Salir(self):
        QApplication.quit()
        self.close()


if __name__ == '__main__':
    # crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # crea la instancia de la GUI
    gui = mpl_gui()
    # nuestra la GUI
    gui.show()
    # ejecuta la aplicación
    sys.exit(app.exec_())
