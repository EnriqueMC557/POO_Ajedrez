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
        Tablero en el que se desplegaran las piezas de ajedrez."""
    
    def __init__(self):
        """Inicializador de clase Ajedrez."""
        self.piezas = self.generar_piezas()
        self.tablero = Tablero(self.piezas)
    
    def generar_piezas(self):
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
        
    def mover_pieza(self, PosIn, team):
        """Método responsable de cambiar la posición de la pieza seleccionada.
        
        Parameters
        ----------
        PosIn: list
            Posición actual de la pieza a mover.
        PosFi: list
            Posición destino de la pieza a mover."""
        NullSelection = True
        for i in self.piezas:
            if i.posicion == PosIn:
                NullSelection = False
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
                while(True):
                    try:
                        idx = int(input('Seleccione posición destino: '))
                        PosFi = movimientos[idx]
                        
                        if PosFi in posiciones_c:
                            for pr in self.piezas:
                                if pr.posicion == PosFi:
                                    self.piezas.remove(pr)
                                    break
                        
                        i.posicion = PosFi
                        break
                    except IndexError:
                        print('Selección inválida')
                break
        if NullSelection:
            raise SeleccionVacia('Posición sin pieza')
        self.tablero.mostrar(self.piezas)
        self.tablero.posiciones = Posiciones(self.piezas)
