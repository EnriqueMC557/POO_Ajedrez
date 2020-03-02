"""
Ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
"""

import os
from tablero import Posiciones, Piezas, Tablero, Ajedrez

class Menu:
    """Clase que permite jugar ajedrez desde la consola."""
    def __init__(self):
        """Inicializador de clase Menu"""
        #Inicialización de piezas
        ListaPiezas = []

        for i in range(8): #Iniciar peones
            ListaPiezas.append(Piezas('wh', 'peon', [i+1,7],'$\u2659$'))
            ListaPiezas.append(Piezas('bk', 'peon', [i+1,2],'$\u2659$'))
        
        for i in [1,8]: #Iniciar torres
            ListaPiezas.append(Piezas('wh', 'torre', [i,8], '$\u2656$'))
            ListaPiezas.append(Piezas('bk', 'torre', [i,1], '$\u2656$'))
        
        for i in [2,7]: #Iniciar caballos
            ListaPiezas.append(Piezas('wh', 'caballo', [i,8], '$\u265E$'))
            ListaPiezas.append(Piezas('bk', 'caballo', [i,1], '$\u265E$'))
            
        for i in [3,6]: #Iniciar alfil
            ListaPiezas.append(Piezas('wh', 'alfil', [i,8], '$\u2657$'))
            ListaPiezas.append(Piezas('bk', 'alfil', [i,1], '$\u2657$'))
        
        #Iniciar reyes
        ListaPiezas.append(Piezas('wh', 'rey', [5,8], '$\u2654$'))
        ListaPiezas.append(Piezas('bk', 'rey', [5,1], '$\u2654$'))
        
        #Iniciar reynas
        ListaPiezas.append(Piezas('wh', 'reina', [4,8], '$\u2655$'))
        ListaPiezas.append(Piezas('bk', 'reina', [4,1], '$\u2655$'))
        
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
            C_i = self.SolicitarCoordenada('Ingrese la coordenada de la pieza a mover, Ej. A8: ')
            C_o = self.SolicitarCoordenada('Ingrese la coordenada destino, Ej. A8: ')
            self.ajedrez.mover_pieza(C_i,C_o)
            print("----------")
            print('Es el turno de %s (negras).'%self.jugadorB)
            print('Escriba salir si desea terminar.')
            C_i = self.SolicitarCoordenada('Ingrese la coordenada de la pieza a mover, Ej. A1: ')
            C_o = self.SolicitarCoordenada('Ingrese la coordenada destino, Ej. A1: ')
            self.ajedrez.mover_pieza(C_i,C_o)
    
    def SolicitarCoordenada(self, mensaje):
        """ Método encargado de solicitar una coordenada y validar su longitud.
        
        Parameters
        ----------
        mensaje : str
            Mensaje a mostrar para solicitar coordenada.

        Returns
        ----------
        C : list
            Coordenada validada."""
        
        while(True):
            try:
                C = input(mensaje)
                if C == 'salir':
                    os.sys.exit()
                elif len(C) != 2:
                    raise Exception('Longitud inválida')
                C = [C[0], C[1]]
                if C[1].isnumeric():
                    C[1] = int(C[1])
                else:
                    C[0] = int(C[0])
                return C
                break
            except:
                print('Longitud de coordenada fuera de rango. Intente otra vez')

if __name__ == '__main__':
    Menu().run()