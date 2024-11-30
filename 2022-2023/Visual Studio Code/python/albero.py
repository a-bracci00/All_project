import random
import turtle
tartaruga = turtle.Turtle()


def albero(tartaruga, tronco, livelli):
    '''
    Disegna un albero e ne torna la lunghezza

    Parameters
    ----------
    tartaruga : turtle.turlte

    tronco : numero lunghezza tronco

    livelli : intero
        numero di livelli dell'albero'

    Returns
    -------
    int
        la lunghezza totale disegnata
    '''
    if livelli > 0:
        lunghezza = 0
        tartaruga.color(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        tartaruga.pendown()
        tartaruga.forward(tronco)
        tartaruga.penup()
        lunghezza += tronco  # lunghezza + tronco
        tartaruga.left(30)
        lunghezza += albero(tartaruga, tronco*0.8, livelli-1)
        tartaruga.right(60)
        lunghezza += albero(tartaruga, tronco*0.7, livelli-1)
        tartaruga.left(30)
        tartaruga.back(tronco)
        # lunghezza espressa in pixel
        return lunghezza
    else:
        return 0
        '''
        senza questo il programma risulterebbe None,
        quindi darebbe errore, 
        return 0 va sempre messo per evitare questo problema
        '''


''' Struttura di un problema ricorsivo

-il problema è riducibile a sottoproblemi simili
-esiste un problema elementare con soluzione (caso base)
-convergenza: a forza di ridurre si arriva sempre al caso base
-la soluzione del problema più grande è ottenibile
dalle soluzioni dei sottoproblemi
'''


def albero2(tartaruga, tronco, livelli, asx=30, adx=45, psx=0.8, pdx=0.7):
    '''
    Disegna un albero e ne torna la lunghezza

    Parameters
    ----------
    tartaruga : turtle.turlte

    tronco : numero lunghezza tronco

    livelli : intero
        numero di livelli dell'albero'

    Returns
    -------
    int
        la lunghezza totale disegnata
    '''
    if livelli > 0:
        lunghezza = 0
        tartaruga.color(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        tartaruga.pendown()  # scrivere in avanti
        tartaruga.forward(tronco)
        tartaruga.penup()  # non scrivere quando ritorna
        lunghezza += tronco  # lunghezza + tronco
        tartaruga.left(asx)
        lunghezza += albero2(tartaruga, tronco*psx,
                             livelli-1, asx, adx, psx, pdx)
        tartaruga.right(asx+adx)
        lunghezza += albero2(tartaruga, tronco*pdx,
                             livelli-1, asx, adx, psx, pdx)
        tartaruga.left(adx)
        tartaruga.back(tronco)
        # lunghezza espressa in pixel
        return lunghezza
    else:
        return 0
