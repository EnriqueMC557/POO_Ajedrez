"""
GUI para ajedrez
I.P.O.O
Aguilar C. M. R. & Mena C. E.
"""

import sys
from Ajedrez_GUI import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox
from main import Menu

class mpl_gui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #Dialogo de error multi uso
        self.error = QMessageBox()
        self.error.setIcon(QMessageBox.Critical)
        self.error.setText('Ha ocurrido un error')
        
        #Conexiones
        self.ui.Iniciar_Button.clicked.connect(self.Iniciar)
        self.ui.Salir_Button.clicked.connect(self.Salir)
        self.ui.MoverPieza_Button.clicked.connect(self.GenerarMovimiento)
        self.ui.Movimientos_List.activated.connect(self.MoverPieza)
        self.iniciar = True
    
    
    def Iniciar(self):
        if self.iniciar:
            #Iniciar nombre de jugadores
            text, ok = QInputDialog.getText(self, 'Jugador1', 'Ingrese nombre (blancas): ')
            self.jugador1 = str(text)
            text, ok = QInputDialog.getText(self, 'Jugador2', 'Ingrese nombre (negras): ')
            self.jugador2 = str(text)
            
            #Inicia equipo blanco
            self.ActualTeam = 'wh'
            
            #Habilita ingreso de coordenada
            self.ui.PosIn_LineEdit.setEnabled(True)
            self.ui.label_2.setEnabled(True)
            self.ui.MoverPieza_Button.setEnabled(True)
            
            #Pinta tablero inicial con piezas
            self.juego = Menu(self.ui.canvas.canvas)
            
            #Actualiza mensaje a jugador en turno
            self.ui.TextoMulti.setText('Es el turno de {} (blancas)'.format(self.jugador1))
            
            self.ui.Iniciar_Button.setText('Terminar juego')
            self.iniciar = False
        
        else:
            if self.ActualTeam == 'wh':
                ganador = self.jugador1
                perdedor = self.jugador2
            else:
                ganador = self.jugador2
                perdedor = self.jugador1
            
            TerminarJuego = QMessageBox.question(self,
                                                 'Terminar partida',
                                                 """El jugador {0} desea declararse
                                                 ganador. ¿{1} estás de acuerdo?
                                                 """.format(ganador,perdedor),
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if TerminarJuego == QMessageBox.Yes:
                self.ui.TextoMulti.setText('¡FELICIDADES! {} ha ganado la partida'.format(ganador))
                
                self.ui.PosIn_LineEdit.setEnabled(False)
                self.ui.label_2.setEnabled(False)
                self.ui.MoverPieza_Button.setEnabled(False)
                self.ui.Iniciar_Button.setText('Iniciar juego')
                self.iniciar = True
    
    def GenerarMovimiento(self):
        #Recibe texto en LineEdit
        C = self.ui.PosIn_LineEdit.text()
        
        #Envía coordenada y cambia equipo de ser necesario
        self.ActualTeam, self.pieza = self.juego.SolicitarCoordenada(C, self.ActualTeam, self.error, self.ui.Movimientos_List)
    
    def MoverPieza(self):
        idx = self.ui.Movimientos_List.currentIndex()
        self.juego.ajedrez.mover_pieza(self.pieza, idx)
        self.ui.Movimientos_List.clear()
        self.ui.PosIn_LineEdit.clear()
        
        #Actualiza mensaje a jugador en turno
        if self.ActualTeam == 'wh':
            self.ui.TextoMulti.setText('Es el turno de {} (blancas)'.format(self.jugador1))
        else:
            self.ui.TextoMulti.setText('Es el turno de {} (negras)'.format(self.jugador2))
    
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
