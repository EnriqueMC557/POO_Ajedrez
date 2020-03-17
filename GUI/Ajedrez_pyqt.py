"""
GUI para Ajedrez
IPOO
MRAC & EMC
"""

import sys
from Ajedrez_GUI import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget

class mpl_gui(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #Conexiones
        self.ui.pushButton.clicked.connect(self.grafica1)
        self.ui.pushButton_2.clicked.connect(self.grafica2)
    
    def grafica1(self):
        x = [0, 1, 2, 3, 4, 5]
        y = [5, 19, 25, 32, 40, 48]
        self.ui.canvas.canvas.ax.plot(x,y,'ok')
        self.ui.canvas.canvas.draw()
    
    def grafica2(self):
        x = [0, 1, 2, 3, 4, 5]
        y = [-5, -19, -25, -32, -40, -48]
        self.ui.canvas.canvas.ax.plot(x,y,'*r')
        self.ui.canvas.canvas.draw()


if __name__ == '__main__':
    # crea la instancia de la aplicación
    app = QApplication(sys.argv)
    # crea la instancia de la GUI
    gui = mpl_gui()
    # nuestra la GUI
    gui.show()
    # ejecuta la aplicación
    sys.exit(app.exec_())
