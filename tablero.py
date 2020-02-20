"""
Tablero para ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
"""
import numpy as np 
import matplotlib.pyplot as plt 

class Posiciones():
    def __init__(self, piezas):
        self.bk = []
        self.wh = []
        for i in piezas:
            if i.team == 'bk':
                self.bk.append(i.PosIn)
            else:
                self.wh.append(i.PosIn)
                
    
    def mover(self,team,pos_i,pos_f):
        self.decodificar(pos_i)
        self.decodificar(pos_f)
        pos = eval('self.%s.tolist()'%team)
        for i in range(16):
            if pos[i] == pos_i:
                exec('self.%s[i,:] = pos_f'%team)
                break
    
    def decodificar(self, pos_n):
        if type(pos_n[0]) == int:
            pos_n[0], pos_n[1] = pos_n[1], pos_n[0]
        pos_n[0] = pos_n[0].upper()
        col = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4,
               'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8}
        pos_n[0] = col[pos_n[0]]
        return pos_n

class Piezas:
    def __init__(self, team, pieza, PosIn, marker):
        self.team  = team
        self.pieza = pieza
        self.PosIn = PosIn
        self.marker = marker
        
    def mover(self,team,pos_i,pos_f):
        self.decodificar(pos_i)
        self.decodificar(pos_f)
        pos = eval('self.%s.tolist()'%team)
        for i in range(16):
            if pos[i] == pos_i:
                exec('self.%s[i,:] = pos_f'%team)
                break

class Tablero:
    def __init__(self, piezas):
        self.fondo = np.array([[0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.]])
        self.it = piezas
        self.pos = Posiciones(piezas)
        self.mostrar()
    
    def mostrar(self):
        fig, ax = plt.subplots()
        ax.set_xticks(np.arange(8))
        ax.set_xticklabels(['A', 'B', 'C', 'D', 'E','F','G','H'])
        ax.set_yticks(np.arange(8))
        ax.set_yticklabels(['1', '2', '3', '4', '5','6','7','8'])
        ax.imshow(self.fondo,cmap = 'binary',alpha=0.5)
        
        for i in self.it:
            if i.team == 'wh':
                plt.plot(i.PosIn[0]-1, i.PosIn[1]-1, marker=i.marker, mfc = 'white', mec='silver', ls='', ms=15)
            else:
                plt.plot(i.PosIn[0]-1, i.PosIn[1]-1, marker=i.marker, mfc = 'white', mec='black', ls='', ms=15)
        plt.show()


"parte del Menú"
ListaPiezas = []

for i in range(8): #Iniciar peones
    ListaPiezas.append(Piezas('wh', 'peon', [i+1,7],'$\u2659$'))
    ListaPiezas.append(Piezas('bk', 'peon', [i+1,2],'$\u2659$'))

for i in [1,8]: #Torres
    ListaPiezas.append(Piezas('wh', 'torre', [i,8], '$\u2656$'))
    ListaPiezas.append(Piezas('bk', 'torre', [i,1], '$\u2656$'))

for i in [2,7]: #Caballos
    ListaPiezas.append(Piezas('wh', 'caballo', [i,8], '$\u265E$'))
    ListaPiezas.append(Piezas('bk', 'caballo', [i,1], '$\u265E$'))
    
for i in [3,6]: #Alfil
    ListaPiezas.append(Piezas('wh', 'alfil', [i,8], '$\u2657$'))
    ListaPiezas.append(Piezas('bk', 'alfil', [i,1], '$\u2657$'))
    
ListaPiezas.append(Piezas('wh', 'rey', [5,8], '$\u2654$'))
ListaPiezas.append(Piezas('bk', 'rey', [5,1], '$\u2654$'))
ListaPiezas.append(Piezas('wh', 'reina', [4,8], '$\u2655$'))
ListaPiezas.append(Piezas('bk', 'reina', [4,1], '$\u2655$'))
