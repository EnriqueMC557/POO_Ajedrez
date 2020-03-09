"""
Ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
"""

import sys
from tablero import *

class LenError(Exception):
    pass

class Menu:
    """Clase que permite jugar ajedrez desde la consola."""
    def __init__(self):
        """Inicializador de clase Menu"""
        #Inicialización de piezas
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
        
        #Incialización de jugadores
        print("""Bienvenido a nuestro ajedrez. Vamos a jugar :D \n""")
        self.jugadorW = input('Ingrese nombre de jugador 1 (blancas): ')
        self.jugadorB = input('Ingrese nombre de jugador 2 (negras): ')
        
        #Inicio de juego
        self.ajedrez = Ajedrez(ListaPiezas)
    
    def run(self):
        """Solicita movimientos de piezas"""
        while(True):
            print("----------")
            print('Es el turno de %s (blancas).'%self.jugadorW)
            print('Escriba salir si desea terminar.')
            self.SolicitarCoordenada('Ingrese la coordenada de la pieza a mover, Ej. A8: ', 'wh')
            print("----------")
            print('Es el turno de %s (negras).'%self.jugadorB)
            print('Escriba salir si desea terminar.')
            self.SolicitarCoordenada('Ingrese la coordenada de la pieza a mover, Ej. A1: ', 'bk')
    
    def SolicitarCoordenada(self, mensaje, team):
        while(True):
            try:
                C = input(mensaje)
                if C == 'salir':
                    print('salir')
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
                self.ajedrez.mover_pieza(C,team)
                
                return C
                break
            except LenError:
                print('Longitud de coordenada invalida.')
            except KeyError:
                print('Letra fuera de rango o ingresaste dos números.')
            except ValueError:
                print('Número fuera de rango o ingresaste dos letras.')
            except TeamError:
                print('Pieza seleccionada de equipo contrario.')
            except SinMovimientos:
                print('Pieza sin movimientos posibles.')

if __name__ == '__main__':
    Menu().run()