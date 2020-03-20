"""
Ajedrez
I.P.O.O
Aguilar C. M. R. & Mena C. E.
"""

import sys
from piezas import Peon, Torre, Caballo, Alfil, Rey, Reyna
from tablero import Tablero, Posiciones
from errores import LenError, TeamError, SinMovimientos
from errores import SeleccionVacia, SeleccionError

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
                    posiciones_c =self.tablero.posiciones.bk
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
                while(True):
                    try:
                        print('\nPosibles movimientos de pieza seleccionada:')
                        for k in movimientos:
                            print('\t' + col[k[0]] + str(k[1]))
                        PosFi = self.SolCoor('Ingrese coordenada destino: ')
                        if PosFi not in movimientos:
                            raise SeleccionError('')
                    except LenError:
                        print('\nLongitud de coordenada invalida.')
                    except SeleccionError:
                        print('\nSelección inválida.')
                    except KeyError:
                        print('\nLetra fuera de rango o ingresaste dos números.')
                    except ValueError:
                        print('\nNúmero fuera de rango o ingresaste dos letras.')
                    else:
                        if PosFi in posiciones_c:
                            for pc in self.piezas:
                                if pc.posicion == PosFi:
                                    self.piezas.remove(pc)
                                    break
                        i.posicion = PosFi
                        break
        if NullSelection:
            raise SeleccionVacia('Posición sin pieza')
        self.tablero.mostrar(self.piezas)
        self.tablero.posiciones = Posiciones(self.piezas)
    
    def SolCoor(self, mensaje):
        """Método que permite realizar la solicitud de una coordenada desde
        consola y maneja los posibles errores."""
        C = input(mensaje)
        if C == 'salir':
            sys.exit()
        elif len(C) != 2:
            raise LenError('Longitud inválida')
        C = [C[0], C[1]]
        col = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4,
               'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8}
        if C[1].isnumeric():
            C[1] = int(C[1])
            if C[1] < 1 or C[1] > 8:
                raise ValueError('Número invalido')
            C[0] = col[C[0].upper()] #KeyError
        else:
            C[0] = int(C[0])
            if C[0] < 1 or C[0] > 8:
                raise ValueError('Número invalido')
            C[1] = col[C[1].upper()] #KeyError
            C[0],C[1] = C[1],C[0]
        return C