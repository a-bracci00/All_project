# Le versioni della funzione `camminas` genera un array unidimensionale seguendo un percorso particolare 
# all'interno della matrice. Inizia dalla metà sinistra dell'ultima riga, poi attraversa 
# la metà destra della matrice muovendosi verso l'alto, cioè dall'ultima riga alla prima, 
# invertendo l'ordine di questi elementi. Infine, termina prendendo gli elementi della 
# parte destra della prima riga, escludendo il centro. L'array risultante combina tutti 
# questi segmenti in un'unica sequenza continua.

import numpy as np

def camminas(mat):
    n,m = mat.shape
    return np.concatenate((mat[-1, :m//2], np.flip(mat[:,m//2]), mat[0, m//2+1:]))

m = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])

print(camminas(m))

def camminas1(mat):
    n,m = mat.shape
    nuova = np.zeros(n+m-1)
    nuova[:m//2] = mat[-1,:m//2]
    nuova[m//2:m//2+n] = mat[::-1,m//2]
    nuova[-m//2:] = mat[0,m//2:]
    return nuova

m = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])

print(camminas1(m))

m1 = np.array([[7]])
assert np.allclose(camminas(m1), np.array([7]))
m2 = np.array([[7,5,2]])
assert np.allclose(camminas(m2), np.array([7,5,2]))
m3 = np.array([[9,3,5,6,0]])
assert np.allclose(camminas(m3), np.array([9,3,5,6,0]))
m4 = np.array([[7,5,2],
[9,3,4]])
assert np.allclose(camminas(m4), np.array([9,3,5,2]))
m5 = np.array([[7,4,6],
[8,2,1],
[0,5,3]])
assert np.allclose(camminas(m5), np.array([0,5,2,4,6]))
m6 = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
assert np.allclose(camminas(m6), np.array([4,3,8,5,2,7,3,8,4,6,5,7]))
print()

def camminas2(mat):
    n,m = mat.shape
    lista = []
    for y in range(n):
        if y == 0:
            for x in range(1,m//2+1):
                lista.append(mat[y][-x])
        if y != 0 and y != n:
            for x in range(1):
                lista.append(mat[y][m//2])
        if y == n-1:
            riga = []
            for x in range(m//2):
                riga.append(mat[y][x])
            riga.reverse()
            [lista.append(x) for x in riga]
    lista.reverse()
    return np.array(lista)

m = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
print(camminas2(m))
print()


#Le versioni della funzione `camminaz` creano un array unidimensionale seguendo un percorso 
# specifico attraverso la matrice e invertendo l'ordine finale degli elementi.  

#Il percorso inizia dalla metà sinistra della prima riga, prosegue lungo la colonna 
# centrale della matrice (dall'alto verso il basso), e termina con la metà destra 
# dell'ultima riga, escludendo il centro. Infine, l'intero array ottenuto viene 
# capovolto per invertire l'ordine degli elementi.

def camminaz(mat):
    n,m = mat.shape
    return np.flip(np.concatenate((mat[0,:m//2], mat[:,m//2], mat[-1, m//2+1:])))

m = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
print(camminaz(m))
m1 = np.array([[7]])
assert np.allclose(camminaz(m1), np.array([7]))
m2 = np.array([[7,5,2]])
assert np.allclose(camminaz(m2), np.array([2,5,7]))
m3 = np.array([[9,3,5,6,0]])
assert np.allclose(camminaz(m3), np.array([0,6,5,3,9]))
m4 = np.array([[7,5,2],
[9,3,4]])
assert np.allclose(camminaz(m4), np.array([4,3,5,7]))
m5 = np.array([[7,4,6],
[8,2,1],
[0,5,3]])
assert np.allclose(camminaz(m5), np.array([3,5,2,4,7]))
m6 = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
assert np.allclose(camminaz(m6), np.array([5,1,6,5,2,7,3,8,4,2,8,5]))

def camminaz1(mat):
    n,m = mat.shape
    nuova = np.zeros(n+m-1)
    nuova[:m//2] = mat[0,:m//2]
    nuova[m//2:m//2+n] = mat[:,m//2]
    nuova[m//2+n:] = mat[-1,m//2+1:]
    return np.flip(nuova)
#importanti
print(camminaz1(m))

def camminaz2(mat):
    n,m = mat.shape
    lista = []
    for y in range(n):
        if y == 0:
            for x in range(m//2+1):
                lista.append(mat[y][x])
        if y != 0 and y != n:
            for x in range(1):
                lista.append(mat[y][m//2])
        if y == n-1:
            riga = []
            for x in range(1,m//2+1):
                riga.append(mat[y][-x])
            riga.reverse()
            [lista.append(x) for x in riga]
    lista.reverse()
    return np.array(lista)

print(camminaz2(m))
print()

def camminaz3(mat):
    n,m = mat.shape
    nuova = np.zeros(n+m-1)
    nuova[:m//2] = mat[-1, -1:-m//2:-1]
    nuova[m//2:m//2+n] = mat[-1::-1, m//2]
    nuova[m//2+n:] = mat[0, m//2-1::-1]
    return nuova

print(camminaz3(m))
m1 = np.array([[7]])
assert np.allclose(camminaz3(m1), np.array([7]))
m2 = np.array([[7,5,2]])
assert np.allclose(camminaz3(m2), np.array([2,5,7]))
m3 = np.array([[9,3,5,6,0]])
assert np.allclose(camminaz3(m3), np.array([0,6,5,3,9]))
m4 = np.array([[7,5,2],
[9,3,4]])
assert np.allclose(camminaz3(m4), np.array([4,3,5,7]))
m5 = np.array([[7,4,6],
[8,2,1],
[0,5,3]])
assert np.allclose(camminaz3(m5), np.array([3,5,2,4,7]))
m6 = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
assert np.allclose(camminaz3(m6), np.array([5,1,6,5,2,7,3,8,4,2,8,5]))
print()