import copy as cp
import numpy as np
import Logic2048 as GameLogic
import pandas as pd
import random as rand

movimientos = ["arriba", "derecha", "izquierda", "abajo"]

stencil = np.array([
    [4, 2, 2, 4],
    [3, 1, 1, 3],
    [3, 1, 1, 3],
    [4, 2, 2, 4]
])


# https://es.stackoverflow.com/questions/403245/c%C3%B3mo-unir-dataframes-en-pandas

# esto es muy "bongo sorting" quisiera ver como hacerlo en simultaneo en varios hilos
# no esperaba q esto funcione, fue mas un experimento de hacerlo por la fuerza bruta
# numero de bucles en 3 horas:6341031

def GoapSimulacion():
    tablero = GameLogic.crear_tablero(4)
    tablero = GameLogic.llenar_pos_vacias(tablero, 2)

    i = 0
    finJuego = False
    while not finJuego and not GameLogic.esta_atascado(tablero) and i < 1000:  # es un watch dog

        tablerosSimulados = ObtenerTablerosPosibles(tablero)
        tablero = MejorTablero(tablerosSimulados)
        tablero = GameLogic.llenar_pos_vacias(tablero, 1)
        print(tablero)


def MejorTablero(tableros):
    tablerosDic = {}
    for tablero in tableros:
        key = np.sum(tablero * stencil)
        tablerosDic = {key: tablero}

    maximaKey = max(tablerosDic.keys())
    return tablerosDic[maximaKey]


def ObtenerTablerosPosibles(tablero):
    tableros = []
    for movimiento in movimientos:
        tableroSimulado = cp.deepcopy(tablero)
        if GameLogic.mover(tableroSimulado, movimiento):
            tableros.append(tableroSimulado)
    return tableros


# --------------GOAP-----------
def JugarHastaGanar():
    tablero = GameLogic.crear_tablero(3)
    tablero = GameLogic.llenar_pos_vacias(tablero, 1)
    i = 0
    estrategia = GenerarEstrategia(len(tablero))
    while not 2048 in tablero:
        estrategia = GenerarEstrategia(len(tablero))
        EjecutarEstrategia(estrategia)
        i += 1
        print(i)

    print(tablero, "Se tardaron ", i, "intentos en llegar a este resultado")
    print(estrategia)


def ProbarEstrategias(n):
    # generar n estrategias 

    masterFrame = ProbarEstrategia()

    for _ in range(n - 1):
        frameActual = ProbarEstrategia()
        masterFrame = pd.concat([masterFrame, frameActual])
    # me gusta esto de _ cuando no usas el parametro, es como el descarte de c#

    return masterFrame


def ProbarEstrategia():
    estrategiaActual = GenerarEstrategia(rand.randint(1, 10))
    return EjecutarEstrategia(estrategiaActual)  # data frame


def GenerarEstrategia(largo):
    max = len(movimientos) - 1
    estrategia = [""] * largo
    for i in range(largo):
        estrategia[i] = movimientos[rand.randint(0, max)]
    return estrategia


def EjecutarEstrategia(listaDeComandos):  # lista de strings con comandos a usar en bucle
    df = pd.DataFrame()
    listaDeComandos = NormalizarMovimientos(listaDeComandos)

    tablero = GameLogic.crear_tablero(3)
    tablero = GameLogic.llenar_pos_vacias(tablero, 1)

    i = 0
    largo = len(listaDeComandos)
    finJuego = False
    while not finJuego and not GameLogic.esta_atascado(tablero) and i < 1000:  # es un watch dog
        comandoActual = listaDeComandos[i % largo]
        if not GameLogic.mover(tablero, comandoActual):
            finJuego = True
        i += 1
        # historial.append(copy.deepcopy(tablero))

    # Relleno Data frame
    df["Estrategia"] = [PasarAString(listaDeComandos)]
    df["Cantidad de turnos"] = [i]
    df["SumatoriaTotal"] = [sum(tablero)]
    df["NumeroMasAlto"] = [np.max(tablero)]
    # df["TableroFinal"] = tablero nose si lo quiero

    return df


def PasarAString(comandos):
    palabra = ""
    for x in comandos:
        palabra += x[0:3] + ","
    return palabra


def NormalizarMovimientos(listaDeComandos):
    for i in range(len(listaDeComandos)):
        listaDeComandos[i] = listaDeComandos[i].lower()
    return listaDeComandos
