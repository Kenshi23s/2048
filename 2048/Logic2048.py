import numpy as np
from random import randint as rd


def LlenarCasilleroVacio(Tablero): #Busca todos los casilleros vacios, y elige uno al azar para poner el numero dos
    CasillasVacias = []
    for i in range(Tablero.shape[0]):
        for j in range(Tablero.shape[1]):
            if Tablero[i][j] == 0:
                CasillasVacias.append((i,j))
    
    Tablero[CasillasVacias[rd(0, len(CasillasVacias) - 1)]] = 2


def CrearTablero(): #Crea una matriz de 4x4 con ints y llena dos posiciones azarosas diferentes con el valor 2
    Tablero = np.zeros((4,4), int)

    LlenarCasilleroVacio(Tablero)
    LlenarCasilleroVacio(Tablero)

    return Tablero 

def MoverHaciaIzquierdaTodo(Tablero):
    for i in range(0, Tablero.shape[1]):
        for j in range(Tablero.shape[1]):
            MoverHaciaIzquierda(i, j, Tablero)
    


def MoverHaciaIzquierda(i, j, Tablero):
    while j >= 0:
        if(j - 1) == -1: return

        if Tablero[(i, j - 1)] == Tablero[(i, j)]: #Fusionar
            Tablero[(i, j)] = 0
            Tablero[(i, j - 1 )] *= Tablero[(i, j - 1 )]
            return
        
        if Tablero[(i, j - 1)] != 0 and Tablero[(i, j - 1)] != Tablero[(i, j)]: #Colision entre fichas de diferente valor
            return
        
        else: #Desplazar hacia la izquierda
            Tablero[(i, j-1)] = Tablero[(i, j)]
            Tablero[(i, j)] = 0

        j -= 1

def RotarTableroHorizontalmenteNoventaGrados(Tablero):
    TableroNuevo = np.zeros((4,4), int)
    for i in range(4):
        for j in range(4):
            TableroNuevo[(j, abs(i - 3))] = Tablero[(i, j)]
            
    return TableroNuevo

def RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, Rotaciones):
    if Rotaciones == 1: return RotarTableroHorizontalmenteNoventaGrados(Tablero)
    
    TableroNuevo = np.zeros((4,4), int)
    TableroNuevo = RotarTableroHorizontalmenteNoventaGrados(Tablero)

    for _ in range(Rotaciones - 1):
        TableroNuevo = RotarTableroHorizontalmenteNoventaGrados(TableroNuevo)

    return TableroNuevo

def EfectuarMovimiento(Tablero, Movimiento):
    if Movimiento == "Izquierda":
        MoverHaciaIzquierdaTodo(Tablero)
    
    elif Movimiento == "Derecha":
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 2)
        MoverHaciaIzquierdaTodo(Tablero)
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 2)
    
    elif Movimiento == "Arriba":
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 3)
        MoverHaciaIzquierdaTodo(Tablero)
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 1)
    
    elif Movimiento == "Abajo":
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 1)
        MoverHaciaIzquierdaTodo(Tablero)
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 3)

    LlenarCasilleroVacio(Tablero)
    return Tablero



Tablero = CrearTablero()
print(Tablero, '\n')

Tablero = EfectuarMovimiento(Tablero, "Arriba")

print(Tablero)
