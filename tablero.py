"""
Tablero para ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
"""
import numpy as np 
import matplotlib.pyplot as plt

class TeamError(Exception):
    pass

class SinMovimientos(Exception):
    pass

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
    
    def DentroTablero(self, movimientos):
        quitar = []
        for x,y in movimientos:
            if (x < 1 or x > 8) or (y < 1 or y > 8):
                quitar.append([x,y])
        for q in quitar:
            movimientos.remove(q)
        return movimientos

class Peon(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2659$'
        self.primer = True
    
    def mover(self, posiciones):
        #Generar movimientos
        x,y = self.posicion[0], self.posicion[1]
        movimientos = []
        if self.team == 'wh':
            pos_c = posiciones.bk
            movimientos.append([x,y-1])
            if [x+1,y-1] in pos_c:
                movimientos.append([x+1,y-1])
            if [x-1,y-1] in pos_c:
                movimientos.append([x-1,y-1])
            if self.primer:
                movimientos.append([x,y-2])
                self.primer = False
        else:
            pos_c = posiciones.wh
            movimientos.append([x,y+1])
            if [x+1,y+1] in pos_c:
                movimientos.append([x+1,y+1])
            if [x-1,y+1] in pos_c:
                movimientos.append([x-1,y+1])
            if self.primer:
                movimientos.append([x,y+2])
                self.primer = False
        #Validar dentro de tablero
        movimientos = self.DentroTablero(movimientos)
        return movimientos
        
        
class Torre(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2656$'
    
    def mover(self, posiciones):
        movimientos = []
        return movimientos

class Caballo(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u265E$'
    
    def mover(self, posiciones):
        movimientos = []
        return movimientos

class Alfil(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2657$'
    
    def mover(self, posiciones):
        movimientos = []
        return movimientos

class Rey(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2654$'
    
    def mover(self, posiciones):
        movimientos = []
        return movimientos

class Reyna(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2655$'
    
    def mover(self, posiciones):
        movimientos = []
        return movimientos

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
        
    def mover_pieza(self, PosIn, team):
        """Método responsable de cambiar la posición de la pieza seleccionada.
        
        Parameters
        ----------
        PosIn: list
            Posición actual de la pieza a mover.
        PosFi: list
            Posición destino de la pieza a mover."""
        for i in self.piezas:
            if i.posicion == PosIn:
                if i.team != team:
                    raise TeamError('Equipo contrario')
                
                movimientos = i.mover(self.tablero.posiciones)
                
                #Validación propio equipo
                if team == 'wh':
                    posiciones = self.tablero.posiciones.wh
                    posiciones_c = self.tablero.posiciones.bk
                else:
                    posiciones = self.tablero.posiciones.bk
                    posiciones_c = self.tablero.posiciones.wh
                quitar = []
                for mov in movimientos:
                    for pos in posiciones:
                        if mov == pos:
                            quitar.append(mov)
                            break
                for q in quitar:
                    movimientos.remove(q)
                
                if not movimientos:
                    raise SinMovimientos('Pieza sin movimientos')
                
                col = {1 : 'A', 2 : 'B', 3 : 'C', 4: 'D',
                       5 : 'E', 6 : 'F', 7 : 'G', 8 : 'H'}
                j = 0
                for k in movimientos:
                    print(str(j) + '.' + col[k[0]] + str(k[1]))
                    j += 1
                
                idx = int(input('Seleccione posición destino: '))
                PosFi = movimientos[idx]
                
                if PosFi in posiciones_c:
                    for pr in self.piezas:
                        if pr.posicion == PosFi:
                            self.piezas.remove(pr)
                            break
                
                i.posicion = PosFi
                
                break
        self.tablero.mostrar(self.piezas)
        self.tablero.posiciones = Posiciones(self.piezas)
    