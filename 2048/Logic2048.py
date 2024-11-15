import numpy as np
from random import randint as rd


def listar_pos_vacias(tablero):
    CasillasVacias = []
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if tablero[i][j] == 0:
                CasillasVacias.append((i,j))

    return CasillasVacias

#
def llenar_pos_vacias(tablero, cantidad):
    CasillasVacias = listar_pos_vacias(tablero)
    if cantidad > len(CasillasVacias): cantidad = len(CasillasVacias)

    for i in range(cantidad):
        Indice = rd(0, len(CasillasVacias) - 1)
        tablero[CasillasVacias[Indice]] = 2
        CasillasVacias.pop(Indice)



def LlenarCasilleroVacio(Tablero): #Busca todos los casilleros vacios, y elige uno al azar para poner el numero dos
    CasillasVacias = listar_pos_vacias(Tablero)    
    Tablero[CasillasVacias[rd(0, len(CasillasVacias) - 1)]] = 2
#

##
def crear_tablero(n): #Crea una matriz de 4x4 con ints y llena dos posiciones azarosas diferentes con el valor 2
    Tablero = np.zeros((4,4), int)

    llenar_pos_vacias(Tablero, 2)

    return Tablero 
##

###
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
###

####
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
####

#####
def mover(Tablero, Movimiento):
    if Movimiento == "izquierda":
        MoverHaciaIzquierdaTodo(Tablero)
    
    elif Movimiento == "derecha":
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 2)
        MoverHaciaIzquierdaTodo(Tablero)
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 2)
    
    elif Movimiento == "arriba":
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 3)
        MoverHaciaIzquierdaTodo(Tablero)
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 1)
    
    elif Movimiento == "abajo":
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 1)
        MoverHaciaIzquierdaTodo(Tablero)
        Tablero = RotarTableroHorizontalmenteNoventaGradosVariasVeces(Tablero, 3)

    LlenarCasilleroVacio(Tablero)
    return Tablero
#####


Tablero = crear_tablero(4)
llenar_pos_vacias(Tablero, 2)
print(Tablero, '\n')
Tablero = mover(Tablero, "arriba")
print(Tablero, '\n')
Tablero = mover(Tablero, "derecha")
print(Tablero, '\n')
Tablero = mover(Tablero, "izquierda")
print(Tablero, '\n')