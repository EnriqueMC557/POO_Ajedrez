"""
Tablero para ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
"""
import numpy as np 
import matplotlib.pyplot as plt 

class Posiciones:
    def __init__(self):
        self.wh = np.array([ [1,2], [2,2], [3,2], [4,2],
                             [5,2], [6,2], [7,2], [8,2],
                             [1,1], [8,1], [2,1], [7,1],
                             [3,1], [6,1], [4,1], [5,1] ])
        self.bk = np.array([ [1,7], [2,7], [3,7], [4,7],
                             [5,7], [6,7], [7,7], [8,7],
                             [1,8], [8,8], [2,8], [7,8],
                             [3,8], [6,8], [4,8], [5,8] ])

class Piezas:
    def __init__(self):
        self.wh = {'peon' : 'ok','torre' : 'sk', 'alfil' : 'dk',
                   'caballo' : '^k', 'rey' : '+k', 'reyna' : '*k'}
        self.bk = {'peon' : 'oy','torre': 'sy', 'alfil' : 'dy',
                   'caballo' : '^y', 'rey' : '+y', 'reyna' : '*y'}

class Tablero:
    def __init__(self):
        self.fondo = np.array([[0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.],
                               [0.,1.,0.,1.,0.,1.,0.,1.],
                               [1.,0.,1.,0.,1.,0.,1.,0.]])
        self.it = Piezas()
        self.pos = Posiciones()
        self.mostrar()
    
    def tablero(self):
        self.fig, self.ax = plt.subplots()
        #self.ax.set_xlim(0,7)
        #self.ax.set_ylim(0,7)
        self.ax.set_xticks(np.arange(8))
        self.ax.set_xticklabels(['A', 'B', 'C', 'D', 'E','F','G','H'])
        self.ax.set_yticks(np.arange(8))
        self.ax.set_yticklabels(['8', '7', '6', '5', '4','3','2','1'])
        self.ax.imshow(self.fondo,cmap = 'binary',alpha=0.5)
        
        for i in self.it.wh.keys():
            if i == 'peon':
                plt.plot(self.pos.wh[0:8,0]-1,self.pos.wh[0:8,1]-1,self.it.wh[i])
            elif i == 'torre':
                plt.plot(self.pos.wh[8:10,0]-1,self.pos.wh[8:10,1]-1,self.it.wh[i])
            elif i == 'caballo':
                plt.plot(self.pos.wh[10:12,0]-1,self.pos.wh[10:12,1]-1,self.it.wh[i])
            elif i == 'alfil':
                plt.plot(self.pos.wh[12:14,0]-1,self.pos.wh[12:14,1]-1,self.it.wh[i])
            elif i == 'rey':
                plt.plot(self.pos.wh[14,0]-1,self.pos.wh[14,1]-1,self.it.wh[i])
            else:
                plt.plot(self.pos.wh[15,0]-1,self.pos.wh[15,1]-1,self.it.wh[i])
        
        for i in self.it.bk.keys():
            if i == 'peon':
                plt.plot(self.pos.bk[0:8,0]-1,self.pos.bk[0:8,1]-1,self.it.bk[i])
            elif i == 'torre':
                plt.plot(self.pos.bk[8:10,0]-1,self.pos.bk[8:10,1]-1,self.it.bk[i])
            elif i == 'caballo':
                plt.plot(self.pos.bk[10:12,0]-1,self.pos.bk[10:12,1]-1,self.it.bk[i])
            elif i == 'alfil':
                plt.plot(self.pos.bk[12:14,0]-1,self.pos.bk[12:14,1]-1,self.it.bk[i])
            elif i == 'rey':
                plt.plot(self.pos.bk[14,0]-1,self.pos.bk[14,1]-1,self.it.bk[i])
            else:
                plt.plot(self.pos.bk[15,0]-1,self.pos.bk[15,1]-1,self.it.bk[i])
        #self.ax.plot(self.pos.wh[:,0]-1,self.pos.wh[:,1]-1, '^r')
        #self.ax.plot(self.pos.bk [:,0]-1,self.pos.bk [:,1]-1, '^b')
        #self.ax.grid(True,color='k')
        #self.ax.set_aspect('equal')
        return self.ax
    
    def mostrar(self):
        self.tablero() 
        # tab.plot(x0-0.5,y0-0.5, '^r')
        # tab.grid(True)
        plt.show()



