
import sys
from Ajedrez_GUI import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
from main import Menu

class mpl_gui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #Conexiones
        self.ui.Iniciar_Button.clicked.connect(self.Iniciar)
        self.ui.Salir_Button.clicked.connect(self.Salir)
    
    def Iniciar(self):
        #juego = Menu(self.ui.canvas.canvas)
        #juego.run()
        Menu(self.ui.canvas.canvas).run()
    
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
