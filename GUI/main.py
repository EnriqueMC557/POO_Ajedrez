"""
main para ajedrez
I.P.O.O
Aguilar C. M. R. & Mena C. E.
"""

import sys
from errores import LenError, TeamError, SinMovimientos, SeleccionVacia
from ajedrez import Ajedrez

class Menu:
    """Clase que permite jugar ajedrez desde la consola."""
    def __init__(self, figure):
        #Inicio de juego
        self.figure = figure
        self.ajedrez = Ajedrez(self.figure)
    
    def run(self):
        """Solicita movimientos de piezas."""
        #while(True):
        print("----------")
        print('Es el turno de %s (blancas).'%self.jugadorW)
        print('Escriba salir si desea terminar.')
        self.SolicitarCoordenada('Ingrese la coordenada de la pieza a mover, Ej. A8: ', 'wh')
        print("----------")
        print('Es el turno de %s (negras).'%self.jugadorB)
        print('Escriba salir si desea terminar.')
        self.SolicitarCoordenada('Ingrese la coordenada de la pieza a mover, Ej. A1: ', 'bk')
    
    def SolicitarCoordenada(self, C, team='', error=None):
        """Método que permite realizar la solicitud de una coordenada desde
        consola y maneja los posibles errores."""
        try:
            if len(C) != 2:
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
            self.ajedrez.mover_pieza(C,team,self.figure)
        except KeyError:
            error.setInformativeText('Letra fuera de rango o ingresaste dos números.')
            error.exec_()
        except ValueError:
            error.setInformativeText('Número fuera de rango o ingresaste dos letras.')
            error.exec_()
        except TeamError:
            error.setInformativeText('Pieza seleccionada de equipo contrario.')
            error.exec_()
        except SinMovimientos:
            error.setInformativeText('Pieza sin movimientos posibles.')
            error.exec_()
        except SeleccionVacia:
            error.setInformativeText('Seleccionó posición vacía.')
            error.exec_()
        except LenError:
            error.setInformativeText('Longitud de coordenada invalida.')
            error.exec_()
        else: #Si no ocurrieron errores
            if team == 'wh':
                team = 'bk'
            else:
                team = 'wh'
        finally:
            return team

if __name__ == '__main__':
    Menu().run()
