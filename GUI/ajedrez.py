"""
Ajedrez
I.P.O.O
Aguilar C. M. R. & Mena C. E.
"""

from piezas import Peon, Torre, Caballo, Alfil, Rey, Reyna
from tablero import Tablero, Posiciones
from errores import TeamError, SinMovimientos, SeleccionVacia

class Ajedrez:
    """Clase que permite jugar Ajedrez utilizando las clases Piezas y Tablero.
    
    Attributes
    ----------
    piezas : list of Piezas
        Piezas con las cuales se jugará ajedrez.
    tablero : Tablero
        Tablero en el que se desplegaran las piezas de ajedrez.
    figure : QPyQt5Canvas
        Figura para desplegar tablero y piezas."""
    
    def __init__(self, figure):
        """Inicializador de clase Ajedrez.
        
        Parameters
        ----------
        figure : QPyQt5Canvas
            Figura para desplegar tablero y piezas."""
        self.figure = figure
        self.piezas = self.generar_piezas()
        self.tablero = Tablero(self.piezas, self.figure)
    
    def generar_piezas(self):
        """Método generador de piezas de ajedrez en posiciones clásicas.
        
        Returns
        -------
        ListaPiezas : list of Piezas
            Piezas para jugar ajedrez."""
        ListaPiezas = []
        
        for i in range(8): #Iniciar peones
            ListaPiezas.append(Peon('wh', [i+1,7]))
            ListaPiezas.append(Peon('bk', [i+1,2]))
        
        for i in [1,8]: #Iniciar torres
            ListaPiezas.append(Torre('wh', [i,8]))
            ListaPiezas.append(Torre('bk', [i,1]))
        
        for i in [2,7]: #Iniciar caballos
            ListaPiezas.append(Caballo('wh', [i,8]))
            ListaPiezas.append(Caballo('bk', [i,1]))
            
        for i in [3,6]: #Iniciar alfil
            ListaPiezas.append(Alfil('wh', [i,8]))
            ListaPiezas.append(Alfil('bk', [i,1]))
        
        #Iniciar reyes
        ListaPiezas.append(Rey('wh', [5,8]))
        ListaPiezas.append(Rey('bk', [5,1]))
        
        #Iniciar reynas
        ListaPiezas.append(Reyna('wh', [4,8]))
        ListaPiezas.append(Reyna('bk', [4,1]))
        return ListaPiezas
        
    def generar_movimientos(self, PosIn, team, listaMovs):
        """Método responsable de recuperar los movimientos de la pieza seleccionada.
        
        Parameters
        ----------
        PosIn: list
            Posición actual de la pieza a mover.
        PosFi: list
            Posición destino de la pieza a mover.
        listaMovs : QComboBox
            Visualizador de movimientos posibles en GUI."""
            
        #Búsqueda de pieza con posición solicitada
        NullSelection = True
        for i in self.piezas:
            if i.posicion == PosIn:
                NullSelection = False
                if i.team != team:
                    raise TeamError('Equipo contrario')
                
                #Obtención de movimientos posibles de pieza
                movimientos = i.mover(self.tablero.posiciones)
                
                #Recuperación de posiciones de equipos
                if team == 'wh':
                    posiciones = self.tablero.posiciones.wh
                    self.posiciones_c =self.tablero.posiciones.bk
                else:
                    posiciones = self.tablero.posiciones.bk
                    self.posiciones_c = self.tablero.posiciones.wh
                
                #Validación posiciones ocupadas por equipo propio
                quitar = []
                for mov in movimientos:
                    for pos in posiciones:
                        if mov == pos:
                            quitar.append(mov)
                            break
                for q in quitar:
                    movimientos.remove(q)
                
                #Si la pieza no tiene movimientos posibles
                if not movimientos:
                    raise SinMovimientos('Pieza sin movimientos')
                
                #Actualización de lista de movimientos
                col = {1 : 'A', 2 : 'B', 3 : 'C', 4: 'D',
                       5 : 'E', 6 : 'F', 7 : 'G', 8 : 'H'}
                listaMovs.clear()
                for mov in movimientos:
                    listaMovs.addItem(col[mov[0]] + str(mov[1]))
                self.movimientos = movimientos
                
                #Regreso de pieza seleccionada
                return i
        
        #Selección de posición vacía
        if NullSelection:
            raise SeleccionVacia('Posición sin pieza')
    
    def mover_pieza(self, pieza, idx):
        """Método para realizar cambio de posición de pieza y comer piezas.
        
        Parameters
        ----------
        pieza : Piezas
            Pieza encontrada con posición solicitada.
        idx : int
            Posición dentro de lista de opciones de movimiento seleccionada.
        """
        
        #Obtención de coordenada destino
        PosFi = self.movimientos[idx]
        
        #Búsqueda de pieza equipo contrario en PosFi para comer (retirar de lista)
        if PosFi in self.posiciones_c:
            for pc in self.piezas:
                if pc.posicion == PosFi:
                    self.piezas.remove(pc)
                    break
        
        #Cambio de posición de pieza seleccionada
        pieza.posicion = PosFi
        
        #Caso especial para peón llegando a extremo de tablero (coronación)
        if type(pieza) == Peon:
            if pieza.posicion[1] == 1 or pieza.posicion == 8:
                self.coronacion(pieza)
        
        #Mostar tablero y actualizar posiciones globales
        self.tablero.mostrar(self.piezas, self.figure)
        self.tablero.posiciones = Posiciones(self.piezas)
        
    def coronacion(self,pieza):
        Pos = pieza.posicion
        Team = pieza.team
        self.piezas.remove(pieza)
        if Team == 'wh':
            self.piezas.append(Reyna('wh', Pos))
        else:
            self.piezas.append(Reyna('bk', Pos))
        