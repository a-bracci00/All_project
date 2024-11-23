# Le funzioni seguenti ruotano le colonne di una matrice verso sinistra di una posizione, 
# spostando il primo elemento di ogni colonna alla fine di quella colonna. 
# La matrice risultante ha le stesse dimensioni della matrice originale.

import numpy as np

m = np.array( [
[0,1,0],
[1,1,0],
[0,0,0],
[0,1,1]
])

def matrot1(mat):
    ret = np.zeros(mat.shape)
    for i in range(mat.shape[0]):
        ret[i,0] = mat[i, -1]
        for j in range(1, mat.shape[1]):
            ret[i, j] = mat[i, j-1]
    return ret

print(m)
print(matrot1(m))

def matrot(mat):
    nuova = np.zeros(mat.shape)
    for y in range(mat.shape[0]):
        nuova[y, 0] = mat[y, -1]
        for x in range(mat.shape[1]):
            nuova[y, x] = mat[y, x-1]
    return nuova

print(m)
print(matrot(m))

m1 = np.array( [ [1] ])
r1 = np.array( [ [1] ])
assert np.allclose(matrot(m1), r1)
m2 = np.array( [ [0,1] ])
r2 = np.array( [ [1,0] ])
assert np.allclose(matrot(m2), r2)
m3 = np.array([ [0,1,0] ])
r3 = np.array([ [0,0,1] ])
assert np.allclose(matrot(m3), r3)
m4 = np.array( [[0,1,0],
[1,1,0]])
r4 = np.array( [[0,0,1],
[0,1,1]])
assert np.allclose(matrot(m4), r4)
m5 = np.array([ [0,1,0],
[1,1,0],
[0,0,0],
[0,1,1]])
r5 = np.array([ [0,0,1],
[0,1,1],
[0,0,0],
[1,0,1]])
assert np.allclose(matrot(m5), r5)
print()

def matrot_pro(mat):
    m = mat.shape[0]
    n = mat.shape[1]

    ret = np.zeros((m,n))
    ret[:, 0] = mat[:, -1]
    #print(ret)
    ret[:, 1:] = mat[:, :-1]
    #print(ret)
    return ret

print(m)
print(matrot_pro(m))
m1 = np.array( [ [1] ])
r1 = np.array( [ [1] ])
assert np.allclose(matrot_pro(m1), r1)
m2 = np.array( [ [0,1] ])
r2 = np.array( [ [1,0] ])
assert np.allclose(matrot_pro(m2), r2)
m3 = np.array([ [0,1,0] ])
r3 = np.array([ [0,0,1] ])
assert np.allclose(matrot_pro(m3), r3)
m4 = np.array( [[0,1,0],
[1,1,0]])
r4 = np.array( [[0,0,1],
[0,1,1]])
assert np.allclose(matrot_pro(m4), r4)
m5 = np.array([ [0,1,0],
[1,1,0],[0,0,0],
[0,1,1]])
r5 = np.array([ [0,0,1],
[0,1,1],
[0,0,0],
[1,0,1]])
assert np.allclose(matrot_pro(m5), r5)
print()