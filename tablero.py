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
    """Clase que permite almacenar las caracteristicas de una pieza de ajedrez y 
    validar que los movimientos válidos se encuentren dentro del tablero.
    
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
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u265E$'
    
    def mover(self, posiciones):
        x,y = self.posicion[0], self.posicion[1]
        movimientos = [[x-2,y+1],[x+2,y+1],[x-1,y+2],[x+1,y+2],[x-2,y-1],[x-1,y-2],[x+1,y-2],[x+2,y-1]]
        movimientos = self.DentroTablero(movimientos)
        return movimientos

class Alfil(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2657$'
    
    def mover(self, posiciones):
        x,y = self.posicion[0], self.posicion[1]
        movimientos = []
        i=1
        diag1, diag2, diag3, diag4 = True, True, True, True
        while(diag1 or diag2 or diag3 or diag4):
            if diag1:
                if (x+i > 8) or (y-i < 1): #Diagonal superior derecha
                    diag1 = False
                else:
                    if ([x+i,y-i] in posiciones.bk) or ([x+i,y-i] in posiciones.wh):
                        movimientos.append([x+i,y-i])
                        diag1 = False
                    else:
                        movimientos.append([x+i,y-i])
            if diag2:
                if (x+i > 8) or (y+i > 8): #Diagonal inferior derecha
                    diag2 = False
                else:
                    if ([x+i, y+i] in posiciones.bk) or ([x+i, y+i] in posiciones.wh):
                        movimientos.append([x+i, y+i])
                        diag2 = False
                    else:
                        movimientos.append([x+i, y+i]) 
            if diag3:
                if (x-i < 1) or (y+i > 8): #Diagonal inferior izquierda
                    diag3 = False
                else:
                    if ([x-i, y+i] in posiciones.bk) or ([x-i, y+i] in posiciones.wh):
                        movimientos.append([x-i, y+i])
                        diag3 = False
                    else:
                        movimientos.append([x-i, y+i])    
            if diag4:
                if (x-i < 1) or (y-i > 8): #Diagonal superior izquierda
                    diag4 = False
                else:
                    if ([x-i, y-i] in posiciones.bk) or ([x-i, y-i] in posiciones.wh):
                        movimientos.append([x-i, y-i])
                        diag4 = False
                    else:
                        movimientos.append([x-i, y-i])   
            i+=1
        movimientos = self.DentroTablero(movimientos)                
        return movimientos

class Rey(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2654$'
    
    def mover(self, posiciones):
        x,y = self.posicion[0], self.posicion[1]
        movimientos = [[x-1,y+1],[x,y+1],[x+1,y+1],[x-1,y],[x+1,y],[x-1,y-1],[x,y-1],[x+1,y-1]]
        movimientos = self.DentroTablero(movimientos)
        return movimientos

class Reyna(Piezas):
    def __init__(self, team, posicion):
        super().__init__(team, posicion)
        self.marker = '$\u2655$'
    
    def mover(self, posiciones):
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
                    if ([x+i,y-i] in posiciones.bk) or ([x+i,y-i] in posiciones.wh):
                        movimientos.append([x+i,y-i])
                        diag1 = False
                    else:
                        movimientos.append([x+i,y-i])
            if diag2:
                if (x+i > 8) or (y+i > 8): #Diagonal inferior derecha
                    diag2 = False
                else:
                    if ([x+i, y+i] in posiciones.bk) or ([x+i, y+i] in posiciones.wh):
                        movimientos.append([x+i, y+i])
                        diag2 = False
                    else:
                        movimientos.append([x+i, y+i]) 
            if diag3:
                if (x-i < 1) or (y+i > 8): #Diagonal inferior izquierda
                    diag3 = False
                else:
                    if ([x-i, y+i] in posiciones.bk) or ([x-i, y+i] in posiciones.wh):
                        movimientos.append([x-i, y+i])
                        diag3 = False
                    else:
                        movimientos.append([x-i, y+i])    
            if diag4:
                if (x-i < 1) or (y-i > 8): #Diagonal superior izquierda
                    diag4 = False
                else:
                    if ([x-i, y-i] in posiciones.bk) or ([x-i, y-i] in posiciones.wh):
                        movimientos.append([x-i, y-i])
                        diag4 = False
                    else:
                        movimientos.append([x-i, y-i])   
            i += 1
        
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
        self.tablero.mostrar(self.piezas)
        self.tablero.posiciones = Posiciones(self.piezas)
    