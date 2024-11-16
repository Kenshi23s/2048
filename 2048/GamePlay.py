import numpy as np
import Logic2048 as GameLogic
import pandas as pd
import random as rand

movimientos = ["arriba", "derecha", "izquierda", "abajo"]

#https://es.stackoverflow.com/questions/403245/c%C3%B3mo-unir-dataframes-en-pandas
def ProbarEstrategias(n):
    # generar n estrategias 

    masterFrame = ProbarEstrategia()

    for _ in range(n - 1):
        masterFrame.ProbarEstrategia()
    # me gusta esto de _ cuando no usas el parametro, es como el descarte de c#

    return


def ProbarEstrategia():
    estrategiaActual = GenerarEstrategia(rand.randint(1, 10))
    return EjecutarEstrategia(estrategiaActual)  # data frame


def GenerarEstrategia(largo):
    max = len(movimientos) - 1
    estrategia = [""] * largo
    for i in range(largo):
        estrategia[i] = rand.randint(0, max)
    return estrategia


def EjecutarEstrategia(listaDeComandos):  # lista de strings con comandos a usar en bucle
    df = pd.DataFrame()
    listaDeComandos = NormalizarMovimientos(listaDeComandos)
    tablero = GameLogic.crear_tablero(3)
    tablero = GameLogic.llenar_pos_vacias(tablero, 1)
    i = 1000  # lo uso como watchdog para q no siga hasta el infinito
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
