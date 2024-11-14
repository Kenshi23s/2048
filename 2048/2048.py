import numpy as np


def MoverHaciaIzquierdaTodo(matriz):
    for i in range(1, matriz.shape[1]):
        for j in range(matriz.shape[1]):
            MoverHaciaIzquierda(i, j, matriz)
    return matriz


def MoverHaciaIzquierda(i, j, Matriz):
    while Matriz[i, j] == 0


def Fusionar():
