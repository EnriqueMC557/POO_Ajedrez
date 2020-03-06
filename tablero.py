"""
Tablero para ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
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


class Piezas:
    """Clase que permite almacenar las caracteristicas de una pieza de ajedrez.
    
    Attributes
    ----------
    team : str
        Equipo al que pertence la pieza ('wh' o 'bk').
    pieza : str
        Tipo de pieza de ajedrez ('peon','torre','caballo','alfil','rey','reyna').
    posicion : list of int
        Posición actual de la pieza.
    marker : str
        Marcador con el cual se visualizará la pieza en el tablero."""
    
    def __init__(self, team, posicion):
        """Inicializador de la clase Piezas.
        
        Parameters
        ----------
        team : str
            Equipo al que pertence la pieza ('wh' o 'bk').
        pieza : str
            Tipo de pieza de ajedrez ('peon','torre','caballo','alfil','rey','reyna').
        posicion : list of int
            Posición inicial de la pieza.
        marker : str
            Marcador con el cual se visualizará la pieza en el tablero."""
        self.team  = team
        #self.pieza = pieza
        self.posicion = posicion
        #self.marker = marker

class Peon(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2659$'

class Torre(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2656$'

class Caballo(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u265E$'

class Alfil(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2657$'

class Rey(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2654$'

class Reyna(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2655$'

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

class Ajedrez:
    """Clase que permite jugar Ajedrez utilizando las clases Piezas y Tablero.
    
    Attributes
    ----------
    piezas : list of Piezas
        Piezas con las cuales se jugará ajedrez.
    tablero : Tablero
        Tablero en el que se desplegaran las piezas de ajedrez."""
    
    def __init__(self, ListaPiezas):
        """Inicializador de clase Ajedrez."""
        self.piezas = ListaPiezas
        self.tablero = Tablero(ListaPiezas)
        
    def mover_pieza(self, PosIn, PosFi):
        """Método responsable de cambiar la posición de la pieza seleccionada.
        
        Parameters
        ----------
        PosIn: list
            Posición actual de la pieza a mover.
        PosFi: list
            Posición destino de la pieza a mover."""
        PosIn = self.decodificar(PosIn)
        PosFi = self.decodificar(PosFi)
        for i in self.piezas:
            if i.posicion == PosIn:
                i.posicion = PosFi
                break
        self.tablero.mostrar(self.piezas)
        self.tablero.posiciones = Posiciones(self.piezas)
    
    def decodificar(self, pos_n):
        """Método diseñado para permitir que el usuario ingrese coordenadas en el
        orden que él desee y sin importar si ingresa letra en mayuscula o no.
        
        Parameters
        ----------
        pos_n = list
            Posición a decodificar"""
        if type(pos_n[0]) == int:
            pos_n[0], pos_n[1] = pos_n[1], pos_n[0]
        pos_n[0] = pos_n[0].upper()
        col = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4,
               'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8}
        pos_n[0] = col[pos_n[0]]
        return pos_n



# """Parte del menú"""
# ListaPiezas = []

# for i in range(8): #Iniciar peones
#     ListaPiezas.append(Piezas('wh', 'peon', [i+1,7],'$\u2659$'))
#     ListaPiezas.append(Piezas('bk', 'peon', [i+1,2],'$\u2659$'))

# for i in [1,8]: #Iniciar torres
#     ListaPiezas.append(Piezas('wh', 'torre', [i,8], '$\u2656$'))
#     ListaPiezas.append(Piezas('bk', 'torre', [i,1], '$\u2656$'))

# for i in [2,7]: #Iniciar caballos
#     ListaPiezas.append(Piezas('wh', 'caballo', [i,8], '$\u265E$'))
#     ListaPiezas.append(Piezas('bk', 'caballo', [i,1], '$\u265E$'))
    
# for i in [3,6]: #Iniciar alfil
#     ListaPiezas.append(Piezas('wh', 'alfil', [i,8], '$\u2657$'))
#     ListaPiezas.append(Piezas('bk', 'alfil', [i,1], '$\u2657$'))

# #Iniciar reyes
# ListaPiezas.append(Piezas('wh', 'rey', [5,8], '$\u2654$'))
# ListaPiezas.append(Piezas('bk', 'rey', [5,1], '$\u2654$'))

# #Iniciar reynas
# ListaPiezas.append(Piezas('wh', 'reina', [4,8], '$\u2655$'))
# ListaPiezas.append(Piezas('bk', 'reina', [4,1], '$\u2655$'))

# #Iniciar tablero
# juego = Ajedrez(ListaPiezas)

# #Movimientos para prueba
# juego.mover_pieza(['b',8],['C',6])
# juego.mover_pieza(['F',2],['f',4])
# juego.mover_pieza([7,'A'],[6,'a'])
# juego.mover_pieza([1,'g'],[3,'F'])