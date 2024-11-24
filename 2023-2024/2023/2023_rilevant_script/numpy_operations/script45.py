# le seguenti versione di funzione moltiplicano per 2 gli elementi di tutte le righe con 
# indice pari (0, 2, 4, ...) di una matrice e restituisce la matrice risultante, 
# lasciando inalterati gli altri elementi.

import numpy as np

m = np.array( [                # indice
                [ 2, 5, 6, 3], # 0 pari
                [ 8, 4, 3, 5], # 1 dispari
                [ 7, 1, 6, 9], # 2 pari
                [ 5, 2, 4, 1], # 3 dispari
                [ 6, 3, 4, 3] # 4 pari
])

def radalt1(mat):
    righe, colonne = mat.shape
    ret = mat.copy()
    for y in range(righe):
        for x in range(colonne):
            if y % 2 == 0:
                ret[y][x] *= 2
    return ret

print(radalt1(m))

def radalt(mat):
    nrighe, ncolonne = mat.shape
    ret = np.zeros((nrighe, ncolonne))
    for i in range(nrighe):
        for j in range(ncolonne):
            if i % 2 == 0:
                ret[i,j] = mat[i,j] * 2
            else:
                ret[i,j] = mat[i,j]
    return ret

print(radalt(m))
m1 = np.array([ [2] ])
r1 = np.array([ [4] ])
assert np.allclose(radalt(m1),r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [ 2, 5, 6],
[ 8, 4, 3]])
r2 = np.array( [ [ 4,10,12],
[ 8, 4, 3]])
assert np.allclose(radalt(m2), r2)
m3 = np.array( [ [ 2, 5, 6, 3],
[ 8, 4, 3, 5],
[ 7, 1, 6, 9],
[ 5, 2, 4, 1],
[ 6, 3, 4, 3] ])
r3 = np.array( [ [ 4,10,12, 6],
[ 8, 4, 3, 5],
[14, 2,12,18],
[ 5, 2, 4, 1],
[12, 6, 8, 6] ])
assert np.allclose(radalt(m3), r3)
# FINE TEST

def radalt_pro(mat):
    ret = mat.copy()
    ret[::2] *= 2
    return ret

print(radalt_pro(m))
m1 = np.array([ [2] ])
r1 = np.array([ [4] ])
assert np.allclose(radalt_pro(m1),r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [ 2, 5, 6],
[ 8, 4, 3]])
r2 = np.array( [ [ 4,10,12],
[ 8, 4, 3]])
assert np.allclose(radalt_pro(m2), r2)
m3 = np.array( [ [ 2, 5, 6, 3],
[ 8, 4, 3, 5],
[ 7, 1, 6, 9],
[ 5, 2, 4, 1],
[ 6, 3, 4, 3] ])
r3 = np.array( [ [ 4,10,12, 6],
[ 8, 4, 3, 5],
[14, 2,12,18],
[ 5, 2, 4, 1],
[12, 6, 8, 6] ])
assert np.allclose(radalt_pro(m3), r3)
print()