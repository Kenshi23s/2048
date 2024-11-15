import numpy as np
# import keyboard as input  # para escuchar inputs
import Logic2048 as GameLogic
import copy
import pandas as pd


# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
# https://pypi.org/project/keyboard/
def probarestrategias(n):
    #generar n estrategias 
    return 

def ProbarEstrategia(listaDeComandos):  # lista de strings con comandos a usar en bucle

    listaDeComandos = NormalizarMovimientos(listaDeComandos)
    tablero = GameLogic.crear_tablero(3)
    tablero = GameLogic.llenar_pos_vacias(tablero, 1)
    i = 1000  # lo uso como watchdog
    historial = []
    largo = len(listaDeComandos)

    while not GameLogic.esta_atascado(tablero) and i >= 0:
        comandoActual = listaDeComandos[i % largo]
        tablero = GameLogic.mover(tablero, comandoActual)
        i -= 1
        historial.append(copy.deepcopy(tablero))


#llenar un data frame en vez de esto
    print("La sumatoria de la estrategia da un total de", sum(tablero))
    print("El juego termino en ", i, "jugadas")
    print("El juego termino en ", i, "jugadas")
    return historial


def NormalizarMovimientos(listaDeComandos):
    for i in range(len(listaDeComandos)):
        listaDeComandos[i] = listaDeComandos[i].lower()
    return listaDeComandos
