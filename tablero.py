"""
Tablero para ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
"""
import numpy as np 
import matplotlib.pyplot as plt 

class Posiciones():
    def __init__(self):
        self.bk = np.array([ [1,2], [2,2], [3,2], [4,2],
                             [5,2], [6,2], [7,2], [8,2],
                             [1,1], [8,1], [2,1], [7,1],
                             [3,1], [6,1], [4,1], [5,1] ])
        self.wh = np.array([ [1,7], [2,7], [3,7], [4,7],
                             [5,7], [6,7], [7,7], [8,7],
                             [1,8], [8,8], [2,8], [7,8],
                             [3,8], [6,8], [4,8], [5,8] ])
    
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
        # self.bk = {'peon' : '$\u2659$','torre' : '$\u2656$', 'alfil' : '$\u2657$',
        #            'caballo' : '$\u265E$', 'rey' : '$\u2654$', 'reyna' : '$\u2655$'}
        # self.wh = {'peon' : '$\u2659$','torre' : '$\u2656$', 'alfil' : '$\u2657$',
        #            'caballo' : '$\u265E$', 'rey' : '$\u2654$', 'reyna' : '$\u2655$'}
    
        self.team  = team
        self.pieza = pieza
        self.PosIn = PosIn
        self.marker = marker

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
        #self.it = Piezas()
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
        
        for i in self.it.wh.keys():
            if i == 'peon':
                plt.plot(self.pos.wh[0:8,0]-1,self.pos.wh[0:8,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'silver', ls = '', ms = 15)
            elif i == 'torre':
                plt.plot(self.pos.wh[8:10,0]-1,self.pos.wh[8:10,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'silver', ls = '', ms = 15)
            elif i == 'caballo':
                plt.plot(self.pos.wh[10:12,0]-1,self.pos.wh[10:12,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'silver', ls = '', ms = 15)
            elif i == 'alfil':
                plt.plot(self.pos.wh[12:14,0]-1,self.pos.wh[12:14,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'silver', ls = '', ms = 15)
            elif i == 'rey':
                plt.plot(self.pos.wh[14,0]-1,self.pos.wh[14,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'silver', ls = '', ms = 15)
            else:
                plt.plot(self.pos.wh[15,0]-1,self.pos.wh[15,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'silver', ls = '', ms = 15)
        
        for i in self.it.bk.keys():
            if i == 'peon':
                plt.plot(self.pos.bk[0:8,0]-1,self.pos.bk[0:8,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'black', ls = '', ms = 15)
            elif i == 'torre':
                plt.plot(self.pos.bk[8:10,0]-1,self.pos.bk[8:10,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'black', ls = '', ms = 15)
            elif i == 'caballo':
                plt.plot(self.pos.bk[10:12,0]-1,self.pos.bk[10:12,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'black', ls = '', ms = 15)
            elif i == 'alfil':
                plt.plot(self.pos.bk[12:14,0]-1,self.pos.bk[12:14,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'black', ls = '', ms = 15)
            elif i == 'rey':
                plt.plot(self.pos.bk[14,0]-1,self.pos.bk[14,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'black', ls = '', ms = 15)
            else:
                plt.plot(self.pos.bk[15,0]-1,self.pos.bk[15,1]-1,
                         marker = self.it.wh[i], mfc = 'white',
                         mec = 'black', ls = '', ms = 15)
        plt.show()

ListaPiezas = [ Piezas('wh', 'peon', [1,7], '$\u2659$'), Piezas('wh', 'peon', [2,7], '$\u2659$'),
                Piezas('wh', 'peon', [3,7], '$\u2659$'), Piezas('wh', 'peon', [4,7], '$\u2659$'),
                Piezas('wh', 'peon', [5,7], '$\u2659$'), Piezas('wh', 'peon', [6,7], '$\u2659$'),
                Piezas('wh', 'peon', [7,7], '$\u2659$'), Piezas('wh', 'peon', [8,7], '$\u2659$'),
                ]
bk = np.array([ [1,2], [2,2], [3,2], [4,2],
                [5,2], [6,2], [7,2], [8,2],
                [1,1], [8,1], [2,1], [7,1],
                [3,1], [6,1], [4,1], [5,1] ])
wh = np.array([ [1,7], [2,7], [3,7], [4,7],
                [5,7], [6,7], [7,7], [8,7],
                [1,8], [8,8], [2,8], [7,8],
                [3,8], [6,8], [4,8], [5,8] ])

ListaPiezas = []

for i in range(8): #Iniciar peones
    ListaPiezas.append(Piezas('wh', 'peon', [i,7],'$\u2659$'))
    ListaPiezas.append(Piezas('bk', 'peon', [i,2],'$\u2659$'))

for i in [1,8]: #Torres
    ListaPiezas.append(Piezas('wh', 'torre', [i,8], '$\u2656$'))
    ListaPiezas.append(Piezas('bk', 'torre', [i,1], '$\u2656$'))

for i in [2,7]: #Caballos
    ListaPiezas.append(Piezas('wh', 'caballo', [i,8], '$\u265E$'))
    ListaPiezas.append(Piezas('bk', 'caballo', [i,1], '$\u265E$'))

tablero = Tablero()

tablero.pos.mover('wh',['B',8],['c',6])
tablero.mostrar()

tablero.pos.mover('bk',[2,'b'],[4,'B'])
tablero.mostrar()

