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
    
    def __init__(self, piezas):
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
        self.mostrar(piezas)
    
    def mostrar(self,piezas):
        """Método que permite realizar el despliegue del tablero con las piezas
        con las que se jugará ajedrez.
        
        Parameters
        ----------
        piezas : list of Piezas
            Piezas a desplegar en tablero"""
        #Despliegue de fondo y etiquetas de tablero
        fig, ax = plt.subplots()
        ax.set_xticks(np.arange(8))
        ax.set_xticklabels(['A', 'B', 'C', 'D', 'E','F','G','H'])
        ax.set_yticks(np.arange(8))
        ax.set_yticklabels(['1', '2', '3', '4', '5','6','7','8'])
        ax.imshow(self.fondo,cmap = 'binary',alpha=0.5)
        
        #Despliegue de piezas
        for i in piezas:
            if i.team == 'wh': #Blancas
                plt.plot(i.posicion[0]-1, i.posicion[1]-1, marker=i.marker,
                         mfc = 'white', mec='silver', ls='', ms=15)
            else: #Negras
                plt.plot(i.posicion[0]-1, i.posicion[1]-1, marker=i.marker,
                         mfc = 'white', mec='black', ls='', ms=15)
        plt.show()
