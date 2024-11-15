import numpy as np
# import keyboard as input  # para escuchar inputs
import Logic2048 as GameLogic
from Logic2048 import LlenarCasilleroVacio, MoverHaciaIzquierdaTodo
import gui


# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
# https://pypi.org/project/keyboard/

def esta_atascado(tablero):
    if not 0 in tablero: return True
    if 2048 in tablero: return True
    return HayMovimientoPosible(tablero)


def HayMovimientoPosible(matriz):
    movimientoposible = False
    j = 0
    i = 0
    # si soy un 0 no hace falta seguir
    while not movimientoposible and i < matriz.shape[0] and j < matriz.shape[1]:
        j = 0
        while j < matriz.shape[1]:
            vecinos = ObtenerVecinos(matriz, (i, j))
            for vecino in vecinos:
                if vecino == matriz[i, j] or vecino == 0:
                    movimientoposible = True
            j += 1

    i += 1
    return movimientoposible


# pasar a gamelogic
def ObtenerVecinos(matriz, posicion):
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    posicionesVecinas = []
    for dir in direcciones:
        NuevaPosicion = dir + posicion
        if EnTablero(matriz, NuevaPosicion):
            posicionesVecinas.append(NuevaPosicion)

    return posicionesVecinas


def EnTablero(matriz, Posicion):
    for n in range(2):
        if matriz[n].shape < Posicion[0] or Posicion[n] < 0:
            return False

    return True


# # para testear lo jugariamos nosotros
# def JugarConInputs():
#     tablero = GameLogic.CrearTablero()
#     print("Toca las flechas para jugar!")
#     print(tablero)
#     while not FinDelJuego(tablero):
#         # escuchar inputs de flechas
#         # si es flecha izquierda no hacer nada
#         if input.is_pressed('right'):  # flecha derecha
#             tablero = Jugar(tablero)
#
#         if input.is_pressed('up'):  # flecha arriba
#             tablero = Jugar(np.rot90(tablero, 1))
#             tablero = np.rot90(tablero, -1)
#
#         if input.is_pressed('left'):  # flecha izquierda
#             tablero = Jugar(np.rot90(tablero, 2))
#             tablero = np.rot90(tablero, -2)
#
#         if input.is_pressed('down'):  # flecha abajo
#             tablero = Jugar(np.rot90(tablero, 3))
#             tablero = np.rot90(tablero, -3)
#
#     print("se termino el juego!")
#     return tablero


def Jugar(tablero):
    tablero = MoverHaciaIzquierdaTodo(tablero)
    tablero = LlenarCasilleroVacio(tablero)
    print(tablero)

    return tablero


def JugarConEstrategia():
    return GameLogic.CrearTablero()
