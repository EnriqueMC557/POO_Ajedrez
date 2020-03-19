"""
Tablero para ajedrez
I.P.O.O
Aguilar C. M. R. & Mena C. E.
"""

import numpy as np 
import matplotlib.pyplot as plt

class Posiciones():
    """Clase que permite conocer todas las posiciones que ocupan las piezas
    separadas por equipos.
    
    Attributes
    ----------
    bk : list of list of int
        Contiene las posiciones de las piezas negras en forma de listas.
    wh : list of list of int
        Contiene las posiciones de las piezas blancas en forma de listas."""
    def __init__(self, piezas):
        """Inicializador de clase Posiciones.
        
        Parameters
        ----------
        piezas : list of Piezas
            Piezas actuales dentro del tablero"""
        #Listas para separar posicones
        self.bk = []
        self.wh = []
        
        #Separación de posiciones
        for i in piezas:
            if i.team == 'bk': #Piezas negras
                self.bk.append(i.posicion)
            else: #Piezas blancas
                self.wh.append(i.posicion)

class Tablero:
    """Clase que permite generar y desplegar un tablero donde jugar ajedrez.
    
    Attributes
    ----------
    fondo : numpy array
        Matriz que permite generar un tablero de ajedrez.
    pos : Posiciones
        Objeto que permite conocer las posiciones que ocupan las piezas de
        ambos equipos de ajedrez."""
    
    def __init__(self, piezas, figure):
        """Inicializador de clase Tablero.
        
        Parameteres
        ----------
        piezas : list of Piezas
            Piezas con las cuales se jugará ajedrez"""
        self.fondo = np.array([[0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.]])
        self.posiciones = Posiciones(piezas)
        self.mostrar(piezas, figure)
    
    def mostrar(self,piezas,figure):
        """Método que permite realizar el despliegue del tablero con las piezas
        con las que se jugará ajedrez.
        
        Parameters
        ----------
        piezas : list of Piezas
            Piezas a desplegar en tablero"""
        #Despliegue de fondo y etiquetas de tablero
        figure.ax.clear()
        figure.ax.set_xticks(np.arange(8))
        figure.ax.set_xticklabels(['A', 'B', 'C', 'D', 'E','F','G','H'])
        figure.ax.set_yticks(np.arange(8))
        figure.ax.set_yticklabels(['1', '2', '3', '4', '5','6','7','8'])
        figure.ax.imshow(self.fondo,cmap = 'binary',alpha=0.5)
        
        #Despliegue de piezas
        for i in piezas:
            if i.team == 'wh': #Blancas
                figure.ax.plot(i.posicion[0]-1, i.posicion[1]-1, marker=i.marker,
                         mfc = 'white', mec='silver', ls='', ms=10)
            else: #Negras
                figure.ax.plot(i.posicion[0]-1, i.posicion[1]-1, marker=i.marker,
                         mfc = 'white', mec='black', ls='', ms=10)
        figure.draw()
