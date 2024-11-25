import numpy as np
from copy import deepcopy as dc
from random import randint as rd

def listar_pos_vacias(tablero):
    CasillasVacias = []
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if tablero[i][j] == 0:
                CasillasVacias.append((i, j))

    return CasillasVacias



def llenar_pos_vacias(tablero, cantidad):
    CasillasVacias = listar_pos_vacias(tablero)
    if cantidad > len(CasillasVacias): cantidad = len(CasillasVacias)

    for i in range(cantidad):
        Indice = rd(0, len(CasillasVacias) - 1)
        tablero[CasillasVacias[Indice]] = 2
        CasillasVacias.pop(Indice)

    return tablero


def LlenarCasilleroVacio(Tablero):  # Busca todos los casilleros vacios, y elige uno al azar para poner el numero dos
    CasillasVacias = listar_pos_vacias(Tablero)
    Tablero[CasillasVacias[rd(0, len(CasillasVacias) - 1)]] = 2
    return Tablero


def crear_tablero(n): 
    Tablero = np.zeros((n, n), int)
    return Tablero


##

###
def MoverHaciaIzquierdaTodo(Tablero):
    for i in range(0, Tablero.shape[1]):
        for j in range(Tablero.shape[1]):
            MoverHaciaIzquierda(i, j, Tablero)


def MoverHaciaIzquierda(i, j, Tablero):
    while j >= 0:
        if (j - 1) == -1: return

        if Tablero[(i, j - 1)] == Tablero[(i, j)]:  # Fusionar
            Tablero[(i, j)] = 0
            Tablero[(i, j - 1)] += Tablero[(i, j - 1)]
            return

        if Tablero[(i, j - 1)] != 0 and Tablero[(i, j - 1)] != Tablero[
            (i, j)]:  # Colision entre fichas de diferente valor
            return

        else:  # Desplazar hacia la izquierda
            Tablero[(i, j - 1)] = Tablero[(i, j)]
            Tablero[(i, j)] = 0

        j -= 1


###

####
def RotarTableroHorizontalmenteNoventaGrados(Tablero):
    n = Tablero.shape[0]
    TableroNuevo = np.zeros((n, n), int)
    for i in range(n):
        for j in range(n):
            TableroNuevo[(j, abs(i - (n - 1)))] = Tablero[(i, j)]

    return TableroNuevo


# como se podria hacer al reves a partir de un parametro?
def RotarTablero90Grados(Tablero, Rotaciones):
    if Rotaciones == 1: return RotarTableroHorizontalmenteNoventaGrados(Tablero)

    # esto se estaba sobrescribiendo con lo de abajo
    # TableroNuevo = np.zeros((4, 4), int)
    TableroNuevo = RotarTableroHorizontalmenteNoventaGrados(Tablero)

    for _ in range(Rotaciones - 1):
        TableroNuevo = RotarTableroHorizontalmenteNoventaGrados(TableroNuevo)

    return TableroNuevo


def mover(Tablero, Movimiento):
    TableroModificado = dc(Tablero)

    if Movimiento == "izquierda":
        MoverHaciaIzquierdaTodo(TableroModificado)

    elif Movimiento == "derecha":
        TableroModificado = RotarTablero90Grados(TableroModificado, 2)
        MoverHaciaIzquierdaTodo(TableroModificado)
        TableroModificado = RotarTablero90Grados(TableroModificado, 2)

    elif Movimiento == "arriba":
        TableroModificado = RotarTablero90Grados(TableroModificado, 3)
        MoverHaciaIzquierdaTodo(TableroModificado)
        TableroModificado = RotarTablero90Grados(TableroModificado, 1)

    elif Movimiento == "abajo":
        TableroModificado = RotarTablero90Grados(TableroModificado, 1)
        MoverHaciaIzquierdaTodo(TableroModificado)
        TableroModificado = RotarTablero90Grados(TableroModificado, 3)

    if not (TableroModificado == Tablero).all():
        Tablero[:, :] = LlenarCasilleroVacio(TableroModificado)[:, :]
        return True
    # diferenciacion de C# :
    # si yo igualo el tablero q tengo de referencia a algo, ya no lo modifico 
    # por referencia sino que se vuelve una instancia independiente
    # q loco no?
    return False


#####

def esta_atascado(tablero):
    atascado = 2048 in tablero
    atascado = atascado or not HayMovimientoPosible(tablero)
    return atascado


def HayMovimientoPosible(matriz):
    movimientoposible = False

    i = 0
    # si soy un 0 no hace falta seguir
    while not movimientoposible and i < matriz.shape[0]:
        j = 0
        while j < matriz.shape[1] and not movimientoposible:
            vecinos = ObtenerVecinos(matriz, (i, j))
            for vecino in vecinos:
                if matriz[vecino[0]][vecino[1]] == matriz[(i, j)] or matriz[vecino[0]][vecino[1]] == 0:
                    movimientoposible = True
            j += 1

        i += 1
    return movimientoposible


# pasar a gamelogic
def ObtenerVecinos(matriz, posicion):
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    posicionesVecinas = []
    for dir in direcciones:
        NuevaPosicion = np.array(dir) + np.array(posicion)
        if EnTablero(matriz, NuevaPosicion):
            posicionesVecinas.append(tuple(NuevaPosicion))

    return posicionesVecinas


def EnTablero(matriz, Posicion):
    for n in range(2):
        if matriz.shape[n] <= Posicion[n] or Posicion[n] < 0:
            return False

    return True
