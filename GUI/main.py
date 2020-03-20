"""
main para ajedrez
I.P.O.O
Aguilar C. M. R. & Mena C. E.
"""

from errores import LenError, TeamError, SinMovimientos, SeleccionVacia
from ajedrez import Ajedrez

class Menu:
    """Clase que permite jugar ajedrez.
    
     Attributes
     ----------
     figure : QPyQt5Canvas
        Figura para desplegar tablero y piezas.
     ajedrez : Ajedrez
         Juego completo de ajedrez (tablero y piezas)."""
    
    def __init__(self, figure):
        """ Inicializador de clase Menu
        
        Parameters
        ----------
        figure : QPyQt5Canvas
            Figura para desplegar tablero y piezas."""
        
        #Inicio de juego
        self.figure = figure
        self.ajedrez = Ajedrez(self.figure)
    
    def SolicitarCoordenada(self, C, team, error, listaMovs):
        """Método que permite recuperar coordenada de pieza seleccionada y
        generar lista de movimientos posibles. Responsable del manejo de 
        errores.
        
        Parameters
        ----------
        C : str
            Coordenada actual de pieza a mover
        team : str
            Equipo que juega en turno actual.
        error : QMessageBox
            Mensaje para mostrar avisos de errores.
        listaMovs : QComboBox
            Visualizador de movimientos posibles en GUI.
        
        Returns
        -------
        team : str
            Equipo de turno siguiente. Si ocurrió algún error se queda el
            mismo equipo.
        pieza : Piezas
            Pieza asociada a coordenada solicitada."""
        try:
            pieza = None
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
                
            pieza = self.ajedrez.generar_movimientos(C,team,listaMovs)
            
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
            return team, pieza
        
