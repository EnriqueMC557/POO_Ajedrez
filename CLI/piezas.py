"""
Piezas para ajedrez
I.P.O.O.
Aguilar C. M. R. & Mena C. E.
"""

class Piezas:
    """Clase que permite almacenar las caracteristicas de una pieza de ajedrez
    y validar que los movimientos válidos se encuentren dentro del tablero.
    
    Attributes
    ----------
    team : str
        Equipo al que pertence la pieza ('wh' o 'bk').
    posicion : list of int
        Posición actual de la pieza."""
        
    
    def __init__(self, team, posicion):
        """Inicializador de la clase Piezas.
        
        Parameters
        ----------
        team : str
            Equipo al que pertence la pieza ('wh' o 'bk').
        posicion : list of int
            Posición inicial de la pieza."""

        self.team  = team
        self.posicion = posicion
    
    def DentroTablero(self, movimientos):
        """Método que permite validar que los momvimientos generados se
        encuentren dentro del tablero."""
        quitar = []
        for x,y in movimientos:
            if (x < 1 or x > 8) or (y < 1 or y > 8):
                quitar.append([x,y])
        for q in quitar:
            movimientos.remove(q)
        return movimientos

class Peon(Piezas):
    """Clase para crear piezas tipo Peón."""
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2659$'
        self.primer = True
    
    def mover(self, posiciones):
        """Método generador de movimientos de Peón."""
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
    """Clase que permite crear piezas tipo Torre."""
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2656$'
    
    def mover(self, posiciones):
        """Método generador de movimientos de Torre."""
        x,y = self.posicion[0], self.posicion[1]
        movimientos = []
        b1, b2, b3, b4 = True, True, True, True
        i = 1
        
        while(b1 or b2 or b3 or b4):
            if b1: #Movimiento arriba
                mov = [x,y+i]
                if mov in posiciones.bk or mov in posiciones.wh: #Pieza cerca
                    movimientos.append(mov)
                    b1 = False
                elif mov[1] > 8: #Fuera de tablero
                    b1 = False
                else:
                    movimientos.append(mov)
            if b2: #Movimiento abajo
                mov = [x,y-i]
                if mov in posiciones.bk or mov in posiciones.wh: #Pieza cerca
                    movimientos.append(mov)
                    b2 = False
                elif mov[1] < 1: #Fuera de tablero
                    b2 = False
                else:
                    movimientos.append(mov)
            if b3: #Movimiento derecha
                mov = [x+i,y]
                if mov in posiciones.bk or mov in posiciones.wh: #Pieza cerca
                    movimientos.append(mov)
                    b3 = False
                elif mov[0] > 8: #Fuera de tablero
                    b3 = False
                else:
                    movimientos.append(mov)
            if b4: #Movimientos izquierda
                mov = [x-i,y]
                if mov in posiciones.bk or mov in posiciones.wh: #Pieza cerca
                    movimientos.append(mov)
                    b4 = False
                elif mov[0] < 1: #Fuera de tablero
                    b4 = False
                else:
                    movimientos.append(mov)
            i += 1

        return movimientos

class Caballo(Piezas):
    """Clase que permite crear piezas tipo Caballo."""
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u265E$'
    
    def mover(self, posiciones):
        """Método generador de movimientos de Caballo."""
        x,y = self.posicion[0], self.posicion[1]
        movimientos = [[x-2,y+1],[x+2,y+1],[x-1,y+2],[x+1,y+2],[x-2,y-1],
                       [x-1,y-2],[x+1,y-2],[x+2,y-1]]
        movimientos = self.DentroTablero(movimientos)
        return movimientos

class Alfil(Piezas):
    """Clase que permite crear piezas tipo Alfil."""
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2657$'
    
    def mover(self, posiciones):
        """Método generador de movimientos de Alfil."""
        x,y = self.posicion[0], self.posicion[1]
        movimientos = []
        i=1
        diag1, diag2, diag3, diag4 = True, True, True, True
        while(diag1 or diag2 or diag3 or diag4):
            if diag1:
                if (x+i > 8) or (y-i < 1): #Diagonal superior derecha
                    diag1 = False
                else:
                    if (([x+i,y-i] in posiciones.bk) or
                        ([x+i,y-i] in posiciones.wh)):
                        movimientos.append([x+i,y-i])
                        diag1 = False
                    else:
                        movimientos.append([x+i,y-i])
            if diag2:
                if (x+i > 8) or (y+i > 8): #Diagonal inferior derecha
                    diag2 = False
                else:
                    if (([x+i, y+i] in posiciones.bk) or
                        ([x+i, y+i] in posiciones.wh)):
                        movimientos.append([x+i, y+i])
                        diag2 = False
                    else:
                        movimientos.append([x+i, y+i])
            if diag3:
                if (x-i < 1) or (y+i > 8): #Diagonal inferior izquierda
                    diag3 = False
                else:
                    if (([x-i, y+i] in posiciones.bk) or
                        ([x-i, y+i] in posiciones.wh)):
                        movimientos.append([x-i, y+i])
                        diag3 = False
                    else:
                        movimientos.append([x-i, y+i])
            if diag4:
                if (x-i < 1) or (y-i < 1): #Diagonal superior izquierda
                    diag4 = False
                else:
                    if (([x-i, y-i] in posiciones.bk) or
                        ([x-i, y-i] in posiciones.wh)):
                        movimientos.append([x-i, y-i])
                        diag4 = False
                    else:
                        movimientos.append([x-i, y-i])
            i+=1
        movimientos = self.DentroTablero(movimientos)
        return movimientos

class Rey(Piezas):
    """Clase que permite crear piezas tipo Rey."""
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2654$'
    
    def mover(self, posiciones):
        """Método generador de movimientos de Rey."""
        x,y = self.posicion[0], self.posicion[1]
        movimientos = [[x-1,y+1],[x,y+1],[x+1,y+1],[x-1,y],[x+1,y],[x-1,y-1],
                       [x,y-1],[x+1,y-1]]
        movimientos = self.DentroTablero(movimientos)
        return movimientos

class Reyna(Piezas):
    """Clase que permite crear piezas tipo Reyna."""
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2655$'
    
    def mover(self, posiciones):
        """Método generador de movimientos de Reyna."""
        x,y = self.posicion[0], self.posicion[1]
        movimientos = []
        b1, b2, b3, b4 = True, True, True, True
        diag1, diag2, diag3, diag4 = True, True, True, True
        i = 1
        
        while(b1 or b2 or b3 or b4 or diag1 or diag2 or diag3 or diag4):
            if b1: #Movimiento arriba
                mov = [x,y+i]
                if mov in posiciones.bk or mov in posiciones.wh: #Pieza cerca
                    movimientos.append(mov)
                    b1 = False
                elif mov[1] > 8: #Fuera de tablero
                    b1 = False
                else:
                    movimientos.append(mov)
            if b2: #Movimiento abajo
                mov = [x,y-i]
                if mov in posiciones.bk or mov in posiciones.wh: #Pieza cerca
                    movimientos.append(mov)
                    b2 = False
                elif mov[1] < 1: #Fuera de tablero
                    b2 = False
                else:
                    movimientos.append(mov)
            if b3: #Movimiento derecha
                mov = [x+i,y]
                if mov in posiciones.bk or mov in posiciones.wh: #Pieza cerca
                    movimientos.append(mov)
                    b3 = False
                elif mov[0] > 8: #Fuera de tablero
                    b3 = False
                else:
                    movimientos.append(mov)
            if b4: #Movimientos izquierda
                mov = [x-i,y]
                if mov in posiciones.bk or mov in posiciones.wh: #Pieza cerca
                    movimientos.append(mov)
                    b4 = False
                elif mov[0] < 1: #Fuera de tablero
                    b4 = False
                else:
                    movimientos.append(mov)
            if diag1:
                if (x+i > 8) or (y-i < 1): #Diagonal superior derecha
                    diag1 = False
                else:
                    if (([x+i,y-i] in posiciones.bk) or
                        ([x+i,y-i] in posiciones.wh)):
                        movimientos.append([x+i,y-i])
                        diag1 = False
                    else:
                        movimientos.append([x+i,y-i])
            if diag2:
                if (x+i > 8) or (y+i > 8): #Diagonal inferior derecha
                    diag2 = False
                else:
                    if (([x+i, y+i] in posiciones.bk) or
                        ([x+i, y+i] in posiciones.wh)):
                        movimientos.append([x+i, y+i])
                        diag2 = False
                    else:
                        movimientos.append([x+i, y+i])
            if diag3:
                if (x-i < 1) or (y+i > 8): #Diagonal inferior izquierda
                    diag3 = False
                else:
                    if (([x-i, y+i] in posiciones.bk) or
                        ([x-i, y+i] in posiciones.wh)):
                        movimientos.append([x-i, y+i])
                        diag3 = False
                    else:
                        movimientos.append([x-i, y+i])
            if diag4:
                if (x-i < 1) or (y-i < 1): #Diagonal superior izquierda
                    diag4 = False
                else:
                    if (([x-i, y-i] in posiciones.bk) or
                        ([x-i, y-i] in posiciones.wh)):
                        movimientos.append([x-i, y-i])
                        diag4 = False
                    else:
                        movimientos.append([x-i, y-i])
            i += 1
        
        return movimientos
