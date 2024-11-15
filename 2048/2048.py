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
            if i == 0:
                TableroNuevo[(j,3)] = Tablero[(i, j)]

            elif i == 1:
                TableroNuevo[(j, 2)] = Tablero[(i, j)]
                
            elif i == 2:
                TableroNuevo[(j, 1)] = Tablero[(i, j)]

            elif i == 3:
                TableroNuevo[(j, 0)] = Tablero[(i,j)]
    return TableroNuevo

def RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, Rotaciones):
    TableroNuevo = np.zeros((4,4), int)

    for _ in range(Rotaciones):
        TableroNuevo = RotarTableroHorizontalmenteNoventaGrados(TableroNuevo)

    return TableroNuevo
    
    



def EfectuarMovimiento(Tablero, Movimiento):
    if Movimiento == "Izquierda":
        MoverHaciaIzquierdaTodo(Tablero)
    
    elif Movimiento == "Derecha":
        RotarTableroHorizontalmenteNoventaGrados(Tablero, 2)
        MoverHaciaIzquierdaTodo(Tablero)
        RotarTableroHorizontalmenteNoventaGrados(Tablero, 2)
    
    elif Movimiento == "Arriba":
        RotarTableroHorizontalmenteNoventaGrados(Tablero, 3)
        MoverHaciaIzquierdaTodo(Tablero)
        RotarTableroHorizontalmenteNoventaGrados(Tablero, 1)
    
    elif Movimiento == "Abajo":
        RotarTableroHorizontalmenteNoventaGrados(Tablero, 1)
        MoverHaciaIzquierdaTodo(Tablero)
        RotarTableroHorizontalmenteNoventaGrados(Tablero, 3)

    LlenarCasilleroVacio(Tablero)



Tablero = CrearTablero()
print(Tablero, '\n')
Tablero = np.flip(Tablero)
print(Tablero, '\n')
Tablero = np.flipud(Tablero)
print(Tablero, '\n')



#EfectuarMovimiento(Tablero, "Derecha")

