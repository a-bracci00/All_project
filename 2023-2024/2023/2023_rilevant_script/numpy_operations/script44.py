# Le versioni delle funzioni seguenti incrementano di 1 tutti gli elementi pari di una matrice 
# e restituisce la matrice risultante. 
# Gli elementi dispari non vengono modificati.

import numpy as np

dim = np.array( [
[2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])
def disp(mat):
    righe, colonne = mat.shape
    nuova = np.zeros((righe, colonne))

    for y in range(righe):
        for x in range(colonne):
            if mat[y][x] % 2 == 0:
                nuova[y][x] = mat[y][x] + 1
            else:
                nuova[y][x] = mat[y][x]
    return nuova

print(disp(dim))
m1 = np.array([ [2] ])
r1 = np.array([ [3] ])
assert np.allclose(disp(m1), r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])
r2 = np.array( [ [3,5,7,3],
[9,5,3,5],
[7,1,7,9]])
assert np.allclose(disp(m2), r2)


def disp_pro1(mat):
    ret = np.array(np.where(mat % 2 == 0, mat+1, mat))
    return ret

print(disp_pro1(dim))

m1 = np.array([ [2] ])
r1 = np.array([ [3] ])
assert np.allclose(disp_pro1(m1), r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])
r2 = np.array( [ [3,5,7,3],
[9,5,3,5],
[7,1,7,9]])
assert np.allclose(disp_pro1(m2), r2)

def disp_pro2(mat):
    ret = mat.copy()
    ret[ret % 2 == 0] += 1
    return ret

print(disp_pro2(dim))
m1 = np.array([ [2] ])
r1 = np.array([ [3] ])
assert np.allclose(disp_pro2(m1), r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])
r2 = np.array( [ [3,5,7,3],
[9,5,3,5],
[7,1,7,9]])
assert np.allclose(disp_pro2(m2), r2)
print()