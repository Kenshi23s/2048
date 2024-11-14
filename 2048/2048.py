import numpy as np
from random import randint as rd

def CrearTablero(): #Crea una matriz de 4x4 con ints y llena dos posiciones azarosas distintas con el valor 2
    Tablero = np.zeros((4,4), int)
    
    Pos = (rd(0, 3), rd(0,3))
    Pos2 = Pos

    while Pos2 == Pos: Pos2 = (rd(0, 3), rd(0,3))    
    
    Tablero[Pos] = 2
    Tablero[Pos2] = 2

    return Tablero 



def LlenarCasilleroVacio(Tablero): #Busca todos los casilleros vacios, y elige uno al azar para poner el numero dos
    CasillasVacias = []
    for i in range(Tablero.shape[0]):
        for j in range(Tablero.shape[1]):
            if Tablero[i][j] == 0:
                CasillasVacias.append((i,j))
    
    Tablero[rd(0, len(CasillasVacias) - 1)] = 2

def MoverHaciaIzquierdaTodo(Tablero):
    for i in range(1, Tablero.shape[1]):
        for j in range(Tablero.shape[1]):
            MoverHaciaIzquierda(i, j, Tablero)
    return Tablero


def MoverHaciaIzquierda(i, j, Tablero):
    while Tablero[i, j] == 0


def Fusionar():
