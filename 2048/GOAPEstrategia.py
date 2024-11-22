import copy
import copy as cp
import numpy as np

import Logic2048
import Logic2048 as GameLogic
import pandas as pd
import random as rand

movimientos = ["arriba", "derecha", "izquierda", "abajo"]


# https://es.stackoverflow.com/questions/403245/c%C3%B3mo-unir-dataframes-en-pandas

# esto es muy "bongo sorting" quisiera ver como hacerlo en simultaneo en varios hilos
# no esperaba q esto funcione, fue mas un experimento de hacerlo por la fuerza bruta
# numero de bucles en 3 horas:6341031

def GoapSimulacion():
    tablero = GameLogic.crear_tablero(4)
    tablero = GameLogic.llenar_pos_vacias(tablero, 2)
    finDeJuego = False
    while not finDeJuego:
        tablero = GameLogic.crear_tablero(4)
        tablero = GameLogic.llenar_pos_vacias(tablero, 2)
        i = 0
        while not finDeJuego and not GameLogic.esta_atascado(
                tablero) and i < 1000:  # es un watch dog

            tablerosSimulados = ObtenerTablerosPosibles(tablero)
            tablero = MejorTablero(tablerosSimulados)
            tablero = GameLogic.llenar_pos_vacias(tablero, 1)

            finDeJuego = 2048 in tablero
            
        print(tablero)

def MejorTablero(tableros):
    tablerosDic = {}
    for tablero in tableros:
        # print("tablero a evaluar", tablero)
        if TendraMovimiento(tablero):
            key = np.sum(tablero)
            tablerosDic = {key: tablero}

  
    
    if len(tablerosDic) > 0:
        col = tablerosDic.keys()#lo puse en un if para testear, pero siempre deberia haber un tablero
        maximaKey = max(col)
        return tablerosDic[maximaKey]
    return tableros[0]


# ---------- Preguntas---------
def TendraMovimiento(tablero):  # nose si la ultima condicion esta de mas, pero queria ver el otro posible outcome
    tablerosCopia = ObtenerTablerosPosibles(tablero)

    MovimientoPosible = len(tablerosCopia) > 0 or TendraMovimientoSiRellenoCon0(tablero)
    if not MovimientoPosible:
        i = len(tablerosCopia) - 1
        while i >= 0 and not MovimientoPosible:
            MovimientoPosible = len(
                ObtenerTablerosPosibles(tablerosCopia[i]) > 0 or TendraMovimientoSiRellenoCon0(tablerosCopia[i]))
            i -= 1

    return MovimientoPosible


def TendraMovimientoSiRellenoCon0(tablero):  # buscar otro nombre
    posicionesVacias = Logic2048.listar_pos_vacias(tablero)
    i = len(posicionesVacias) - 1
    movimientoPosible = False
    while not movimientoPosible and i >= 0:
        tableroCopia = copy.deepcopy(tablero)
        tableroCopia[posicionesVacias[i]] = 2
        movimientoPosible = len(ObtenerTablerosPosibles(tableroCopia)) > 0
        print(movimientoPosible)
        i -= 1

    posicionesVacias = Logic2048.listar_pos_vacias(tablero)
    i = len(posicionesVacias) - 1
    movimientoPosible = False
    while not movimientoPosible and i >= 0:
        tableroCopia = copy.deepcopy(tablero)
        tableroCopia[posicionesVacias[i]] = 2
        movimientoPosible = len(ObtenerTablerosPosibles(tableroCopia)) > 0
        print(movimientoPosible)
        i -= 1


def TendranMovimientosSiRellenoCon0(tableros):  # buscar otro nombre

    i = len(tableros) - 1
    movimientoPosible = False
    while i >= 0 and not movimientoPosible:
        movimientoPosible = TendraMovimientoSiRellenoCon0(tableros[i])
        i -= 1
    return movimientoPosible


def ObtenerTablerosPosibles(tablero):
    tableros = []
    for movimiento in movimientos:
        tableroSimulado = cp.deepcopy(tablero)
        if GameLogic.mover(tableroSimulado, movimiento):
            tableros.append(tableroSimulado)
    return tableros


# -----------------

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


# ------------Estrategias----------
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


# ----------------------

# --------NormalizarTexto-------
def PasarAString(comandos):
    palabra = ""
    for x in comandos:
        palabra += x[0:3] + ","
    return palabra


def NormalizarMovimientos(listaDeComandos):
    for i in range(len(listaDeComandos)):
        listaDeComandos[i] = listaDeComandos[i].lower()
    return listaDeComandos


# -----------------------------------

GoapSimulacion()
