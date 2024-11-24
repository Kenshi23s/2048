
import Logic2048
import random as rand

# https://es.stackoverflow.com/questions/403245/c%C3%B3mo-unir-dataframes-en-pandas

# esto es muy "bongo sorting" quisiera ver como hacerlo en simultaneo en varios hilos
# no esperaba q esto funcione, fue mas un experimento de hacerlo por la fuerza bruta
# numero de bucles en 3 horas:6341031


def ObtenerMovimientoEsquinaDerecha(tablero):
    ComandosASeguir = ["arriba", "derecha", "izquierda", "abajo"]
    return ProbarComando(tablero, ComandosASeguir)


def ObtenerMovimientoEsquinaIzquierda(tablero):
    ComandosASeguir = ["izquierda", "abajo", "arriba", "derecha"]
    return ProbarComando(tablero,ComandosASeguir)

def EjecutarMovimientoAleatorio(tablero):
    ComandosASeguir = ["izquierda", "abajo", "arriba", "derecha"]
    rand.shuffle(ComandosASeguir)
    return ProbarComando(tablero, ComandosASeguir)

def ProbarComando(tablero, comando):
    MovimientoPosible = False
    comandoActual = ""
    while len(comando) > 0 and not MovimientoPosible:
        comandoActual = comando.pop(0)
        MovimientoPosible = Logic2048.mover(tablero, comandoActual)

    return comandoActual
