"""
Errores para ajedrez
I.P.O.O.
Aguilar C. M. R. & Mena C. E.
"""

class TeamError(Exception):
    """Clase generadora de error para selección de pieza de equipo contrario."""
    pass

class SinMovimientos(Exception):
    """Clase generadora de error para selección de pieza sin movimientos."""
    pass

class SeleccionVacia(Exception):
    """Clase generadora de error para selección de posiciónn sin pieza."""
    pass

class LenError(Exception):
    """Clase generadora de error para ingreso de coordenada con longitud no
    válida."""
    pass

class SeleccionError(Exception):
    """Clase generadora de error para selección de coordenada destino inválida."""
    pass