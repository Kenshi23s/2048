import numpy as np
import keyboard as input  # para escuchar inputs
import Logic2048 as GameLogic
from Logic2048 import LlenarCasilleroVacio, MoverHaciaIzquierdaTodo


# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
# https://pypi.org/project/keyboard/

def FinDelJuego(tablero):
    if not 0 in tablero: return True
    if 2048 in tablero: return True
    return False


# para testear lo jugariamos nosotros
def JugarConInputs():
    tablero = GameLogic.CrearTablero()
    print("Toca las flechas para jugar!")
    print(tablero)
    while not FinDelJuego(tablero):
        # escuchar inputs de flechas
        # si es flecha izquierda no hacer nada
        if input.is_pressed('right'):  # flecha derecha
            tablero = Jugar(tablero)

        if input.is_pressed('up'):  # flecha arriba
            tablero = Jugar(np.rot90(tablero, 1))
            tablero = np.rot90(tablero, -1)

        if input.is_pressed('left'):  # flecha izquierda
            tablero = Jugar(np.rot90(tablero, 2))
            tablero = np.rot90(tablero, -2)

        if input.is_pressed('down'):  # flecha abajo
            tablero = Jugar(np.rot90(tablero, 3))
            tablero = np.rot90(tablero, -3)

    print("se termino el juego!")
    return tablero


def Jugar(tablero):
    tablero = MoverHaciaIzquierdaTodo(tablero)
    tablero = LlenarCasilleroVacio(tablero)
    print(tablero)

    return tablero


def JugarConEstrategia():
    return GameLogic.CrearTablero()
