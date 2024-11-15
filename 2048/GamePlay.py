import numpy as np
# import keyboard as input  # para escuchar inputs
import Logic2048 as GameLogic
import copy
import pandas as pd


# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
# https://pypi.org/project/keyboard/
def probarestrategias(n):
    # generar n estrategias 
    return


def ProbarEstrategia(listaDeComandos):  # lista de strings con comandos a usar en bucle
    df = pd.DataFrame()
    listaDeComandos = NormalizarMovimientos(listaDeComandos)
    tablero = GameLogic.crear_tablero(3)
    tablero = GameLogic.llenar_pos_vacias(tablero, 1)
    i = 1000  # lo uso como watchdog
    # historial = []
    largo = len(listaDeComandos)

    while not GameLogic.esta_atascado(tablero) and i >= 0:
        comandoActual = listaDeComandos[i % largo]
        if not GameLogic.mover(tablero, comandoActual):
            i = 0
        i -= 1
        # historial.append(copy.deepcopy(tablero))

    df["Estrategia"] = listaDeComandos
    df["Cantidad de turnos"] = i
    df["SumatoriaTotal"] = sum(tablero)
    df["NumeroMasAlto"] = np.max(tablero)
    df["TableroFinal"] = tablero

    return df


def NormalizarMovimientos(listaDeComandos):
    for i in range(len(listaDeComandos)):
        listaDeComandos[i] = listaDeComandos[i].lower()
    return listaDeComandos
