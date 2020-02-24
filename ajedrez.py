"""
Ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
"""

import os
from tablero import decodificar, Posiciones, Piezas, Tablero, Ajedrez

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
            CW_i = input('Ingrese las coordenadas de la pieza a mover, Ej., A,8: ')
            if CW_i == 'salir':
                os.sys.exit()
            CW_i =[CW_i[0], CW_i[2]]
            if CW_i[1].isnumeric():
                CW_i[1] = int(CW_i[1])
            else:
                CW_i[0] = int(CW_i[0])
            CW_o = input('Ingrese las coordenadas destino, Ej., A,8: ')
            CW_o =[CW_o[0], CW_o[2]]
            if CW_o[1].isnumeric():
                CW_o[1] = int(CW_o[1])
            else:
                CW_o[0] = int(CW_o[0])
            self.ajedrez.mover_pieza(CW_i,CW_o)
            print("----------")
            print('Es el turno de %s (negras).'%self.jugadorB)
            print('Escriba salir si desea terminar.')
            CW_i = input('Ingrese las coordenadas de la pieza a mover, Ej., A,8: ')
            if CW_i == 'salir':
                os.sys.exit()
            CW_i =[CW_i[0], CW_i[2]]
            if CW_i[1].isnumeric():
                CW_i[1] = int(CW_i[1])
            else:
                CW_i[0] = int(CW_i[0])
            CW_o = input('Ingrese las coordenadas destino, Ej., A,8: ')
            CW_o =[CW_o[0], CW_o[2]]
            if CW_o[1].isnumeric():
                CW_o[1] = int(CW_o[1])
            else:
                CW_o[0] = int(CW_o[0])
            self.ajedrez.mover_pieza(CW_i,CW_o)

if __name__ == '__main__':
    Menu().run()