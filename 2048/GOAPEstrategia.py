import numpy as np
import random
import Logic2048
import copy as cp


def GoapSimulacion(tablero):
    tablerosSimulados = ObtenerTablerosPosibles(tablero)  # devuelve dic de {movimiento, tablero}
    tablero = MejorTablero(tablerosSimulados.values(), tablero.shape[0])

    for key in tablerosSimulados.keys():
        if (tablerosSimulados[key] == tablero).all():
            return key
    return ""


def MejorTablero(tableros, dimTablero):
    mejorTableroActualmente = (-1, np.zeros((dimTablero, dimTablero), dtype=int))
    for tablero in tableros:
        if TendraMovimiento(tablero):
            tablerosPosibles = CantidadMovimientosFuturos(cp.deepcopy(tablero), 100, 2)
            # print("el tablero", tablero, "tiene", tablerosPosibles, "movimientosPosibles")
            if tablerosPosibles > mejorTableroActualmente[0]:
                mejorTableroActualmente = (tablerosPosibles, tablero)

    return mejorTableroActualmente[1]


def AgarrarRandom(lista, n):
    if n > len(lista):
        n = len(lista)
    return random.sample(lista, n)


def TendraMovimiento(tablero):  # nose si la ultima condicion esta de mas, pero queria ver el otro posible outcome
    tablerosCopia = ObtenerTablerosPosibles(tablero)

    MovimientoPosible = len(tablerosCopia) > 0
    if not MovimientoPosible:
        i = len(tablerosCopia) - 1
        while i >= 0 and not MovimientoPosible:
            MovimientoPosible = len(ObtenerTablerosPosibles(tablerosCopia[i]) > 0)
            i -= 1

    return MovimientoPosible


def CantidadMovimientosFuturos(tablero, n, ramificado):
    if ramificado <= 0: return 0
    exitos = 0
    posicionesVacias = AgarrarRandom(Logic2048.listar_pos_vacias(tablero), n)

    for i in range(len(posicionesVacias) - 1):
        tableroCopia = cp.deepcopy(tablero)
        tableroCopia[posicionesVacias[i]] = 2
        if len(ObtenerTablerosPosibles(tableroCopia)) > 0:  # aca ya no estoy chequeando adentro de los mismos arboles, 
            # quizas necesito otro parametro para chequear mas adentro del arbol y voy haciendo recursion con fibonacci?
            exitos += 1
            exitos += CantidadMovimientosFuturos(tableroCopia, n, ramificado - 1) 
        i += 1
    return exitos / n


def ObtenerTablerosPosibles(tablero):
    tableros = {}
    for movimiento in ["izquierda", "derecha", "arriba", "abajo"]:
        tableroSimulado = cp.deepcopy(tablero)
        if Logic2048.mover(tableroSimulado, movimiento):
            tableros = {movimiento: tableroSimulado}

    return tableros
