import numpy as np
import random
import Logic2048
import copy as cp

from Logic2048 import LlenarCasilleroVacio, HayMovimientoPosible


def SimulacionGOAP(tablero):
    tablerosSimulados = ObtenerTablerosPosibles(tablero)  # devuelve dic de {movimiento, tablero}

    if len(tablerosSimulados) <= 0:
        # print("no se pudieron simular tableros para", tablero)
        return ""
    tablero2 = MejorTablero(tablerosSimulados.values(), tablero.shape[0])

    for key in tablerosSimulados.keys():
        if (tablerosSimulados[key] == tablero2).all():
            return key

    return ""


def MejorTablero(tableros, dimTablero):
    n = 3
    ramificado = 1
    mejorTableroActualmente = (-1, np.zeros((dimTablero, dimTablero), dtype=int))
    for tablero in tableros:
        if TendraMovimiento(tablero):
            tablerosPosibles = CantidadMovimientosFuturos(cp.deepcopy(tablero), n, ramificado) / n * ramificado
            tablerosPosibles += np.max(tablero) / 2048
            # tablerosPosibles += np.sum(tablero) / 2048
            # print("el tablero", tablero, "tiene", tablerosPosibles, "movimientosPosibles")
            if tablerosPosibles > mejorTableroActualmente[0]:
                mejorTableroActualmente = (tablerosPosibles, tablero)
    return mejorTableroActualmente[1]


# https://www.geeksforgeeks.org/python-random-sample-function/
def AgarrarRandom(lista, n):
    if n > len(lista):
        n = len(lista)
    return random.sample(lista, n)


def TendraMovimiento(tablero):
    tablerosCopia = ObtenerTablerosPosibles(tablero)
    MovimientoPosible = len(tablerosCopia) > 0
    return MovimientoPosible


def CantidadMovimientosFuturos(tablero, n, ramificado):
    if ramificado <= 0: return 0
    exitos = 0

    posicionesVacias = AgarrarRandom(Logic2048.listar_pos_vacias(tablero), n)
    if len(posicionesVacias) <= 0: return exitos

    for i in range(len(posicionesVacias) - 1):
        tableroCopia = cp.deepcopy(tablero)
        tableroCopia[posicionesVacias[i]] = 2
        posibles = len(ObtenerTablerosPosibles(tableroCopia))
        if posibles > 0:  # aca ya no estoy chequeando adentro de los mismos arboles, 
            # quizas necesito otro parametro para chequear mas adentro del arbol y voy haciendo recursion con fibonacci?
            exitos += posibles / 4
            exitos += CantidadMovimientosFuturos(tableroCopia, n, ramificado - 1)
        
    return exitos


def ObtenerTablerosPosibles(tablero):
    tableros = {}
    for movimiento in ["izquierda", "derecha", "arriba", "abajo"]:
        tableroSimulado = cp.deepcopy(tablero)
        if Logic2048.mover(tableroSimulado, movimiento) and HayMovimientoPosible(tableroSimulado):
            tableros[movimiento] = tableroSimulado
        # else:
        #     print("descarto tablero", tableroSimulado, movimiento)

    return tableros
