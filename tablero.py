"""
Tablero para ajedrez
I.P.O.O
Aguilar C. M. R., Mena C. E.
"""
import numpy as np 
import matplotlib.pyplot as plt 

class Tablero:
    def Tablero(self,x0,y0):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0,9)
        self.ax.set_ylim(0,9)
        self.ax.set_xticks(np.arange(10))
        self.ax.set_xticklabels(self.x)
        self.ax.set_yticks(np.arange(10))
        self.ax.set_yticklabels(self.y)
        self.ax.plot(x0-0.5,y0-0.5, '^r')
        # plot(pos['x'],pos['y'],marker=piezas['peon'],color = 'r')
        self.ax.grid(True)
        return self.ax
        # plt.show()
    def Mostrar(self,x0,y0):
        self.Tablero(x0,y0) 
        # tab.plot(x0-0.5,y0-0.5, '^r')
        # tab.grid(True)
        plt.show()

    def __init__(self, pb, pn):
        self.x = ['', 'A', 'B', 'C', 'D', 'E','F','G','H','']
        self.y = ['', '1', '2', '3', '4', '5','6','7','8','']
        self.Mostrar(pb,pn)


# class Piezas:
#     self.blancas = {'peon': 'ob',}

    


# for i in blancas.keys:
#     if i == 'peon':
#         for j in range(8):
#             plt.plot(pos[0:8,:2],blancas['peon'])
#     elif i == 'torre' | i == 'alfil' | i == 'caballo':
#         for j in range(2):
#             plt.plot(pos[0:8,:2],blancas['torre'])
    
# pos = [ [p1x,p1y] , [p2x,p2y] ] 

class Posiciones:
    def __init__(self):
        self.blancas = np.array([ [1,2], [2,2], [3,2], [4,2], [5,2], [6,2], [7,2], [8,2] 
                                  [1,1], [8,1], [2,1], [7,1], [3,1], [3,6], [4,1], [5,1]])
        self.negras  = np.array([ [1,7], [2,7], [3,7], [4,7], [5,7], [6,7], [7,7], [8,7] 
                                  [1,8], [8,8], [2,8], [7,8], [3,8], [3,8], [4,8], [5,8]])