#La funzione media_righe calcola la media aritmetica di ogni riga di una matrice e 
# restituisce una nuova matrice contenente queste medie. 
# Ogni elemento della nuova matrice corrisponde alla media della riga corrispondente 
# nella matrice originale

import numpy as np

def media_righe(mat):
    nuova = [[0]*1 for x in range(len(mat))]
    for y in range(len(mat)):
        riga = []
        for x in range(len(mat[0])):
            riga.append(mat[y][x])
        nuova[y] = [sum(riga) / len(mat[0])] # type: ignore
    return nuova

m =[ [3, 2, 1, 4],
    [6, 2, 3, 5],
    [4, 3, 6, 2],
    [4, 6, 5, 4],
    [7, 2, 9, 3]]

print(media_righe(m))

m1 = np.array([ [5.0] ])
r1 = np.array([ [5.0] ])
assert np.allclose(media_righe(m1), r1)
m2 = np.array([ [5.0, 3.0] ])
r2 = np.array([ [4.0] ])
assert np.allclose(media_righe(m2), r2)
m3 = np.array(
[[3,2,1,4],
[6,2,3,5],
[4,3,6,2],
[4,6,5,4],
[7,2,9,3]])
r3 = np.array([ [(3+2+1+4)/4],
[(6+2+3+5)/4],
[(4+3+6+2)/4],
[(4+6+5+4)/4],
[(7+2+9+3)/4] ])
assert np.allclose(media_righe(m3), r3)

def media_righe2(mat):
    righe, colonne = len(mat), len(mat[0])
    ret = np.zeros((righe, 1))
    for y in range(righe):
        for x in range(colonne):
            ret[y] += mat[y][x]
        ret[y] = ret[y] / colonne
    return ret

print(media_righe2(m))
print()
def media_righe3(mat):
    righe, colonne = len(mat), len(mat[0])
    nuova = np.mean(mat, axis = 1)
    nuova = nuova.reshape((righe, 1))
    return nuova

[print(x) for x in media_righe3(m)]


def media_righe4(mat):
    righe, colonne = len(mat), len(mat[0])
    media = np.mean(mat, axis = 1)
    media = media.reshape(righe, 1)
    return media

[print(x) for x in media_righe4(m)]

m =[ [3, 2, 1, 4],
    [6, 2, 3, 5],
    [4, 3, 6, 2],
    [4, 6, 5, 4],
    [7, 2, 9, 3]]

def media_righe5(mat):
    mat = np.array(mat)
    righe, colonne = mat.shape
    media = np.mean(mat, axis = 1)
    media = media.reshape(righe, 1)
    return media

[print(x) for x in media_righe5(m)]
print()
m = np.array( [
[0,1,0],
[1,1,0],
[0,0,0],
[0,1,1]
])