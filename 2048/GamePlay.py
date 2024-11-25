import copy as cp
import numpy as np

import GOAPEstrategia
import Logic2048 as GameLogic
import pandas as pd
import random as rand
import GOAPEstrategia as Goap
import UPRIGHTEstrategia
import UPRIGHTEstrategia as Secuencia
import matplotlib.pyplot as plt
import collections

movimientos = ["arriba", "derecha", "izquierda", "abajo"]


# https://es.stackoverflow.com/questions/403245/c%C3%B3mo-unir-dataframes-en-pandas

# esto es muy "bongo sorting" quisiera ver como hacerlo en simultaneo en varios hilos
# no esperaba q esto funcione, fue mas un experimento de hacerlo por la fuerza bruta
# numero de bucles en 3 horas:6341031
# podria sacar un promedio entre todos los tableros de que movimiento se uso mas

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

def ProbarEstrategias(funcionObtenerMovimiento, n):
    # generar n estrategias 

    masterFrame = ProbarEstrategia()

    for _ in range(n - 1):
        frameActual = ProbarEstrategia()
        masterFrame = pd.concat([masterFrame, frameActual])
    # me gusta esto de _ cuando no usas el parametro, es como el descarte de c#

    return masterFrame


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


# la funcion que se pasa por aca recibe un tablero y debe devolver un string con el comando
def EjecutarEstrategia(obtenerMovimiento):
    df = pd.DataFrame()

    tablero = GameLogic.crear_tablero(4)
    tablero = GameLogic.llenar_pos_vacias(tablero, 2)

    i = 0
    finJuego = False
    while not finJuego and not GameLogic.esta_atascado(tablero) and i < 1000:  # es un watch dog
        comandoActual = obtenerMovimiento(cp.deepcopy(tablero))
        if not GameLogic.mover(tablero, comandoActual):
            finJuego = True
        i += 1
        tablero = GameLogic.llenar_pos_vacias(tablero, 1)

    df["Cantidad de turnos"] = [i]
    # df["SumatoriaTotal"] = [sum(tablero)]
    df["NumeroMasAlto"] = [np.max(tablero)]
    # print(tablero)
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


# https://micro.recursospython.com/recursos/como-obtener-el-nombre-de-una-funcion.html
# https://www.hackerrank.com/challenges/collections-counter/problem
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
# cosas que encontre que me parecieron interesantes 
def GraficarEstrategia(estrategia, k):
    valoresMasAltos = []
    # potencias2 = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048])
    for _ in range(k):
        resultado = EjecutarEstrategia(estrategia)
        valoresMasAltos.append(resultado["NumeroMasAlto"].iloc[0])
        # print(resultado["NumeroMasAlto"])

    contador = dict(collections.Counter(valoresMasAltos))
    titulo = estrategia.__name__ + "Simulaciones:" + str(k)
    plt.title(titulo)  # devuelve el nombre de la estrategia
    plt.bar(contador.keys(), contador.values())
    plt.show()


