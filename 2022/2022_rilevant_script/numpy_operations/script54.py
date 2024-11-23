# Le versioni della funzione creano un array 1D che alterna gli elementi della diagonale principale e 
# della sovradiagonale di una matrice quadrata.

import numpy as np

def gradini(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    n = len(mat)
    nuova = np.zeros(n+n-1)
    for y in range(n):
        nuova[2*y] = mat[y,y]
    
    for y in range(n-1):
        nuova[2*y+1] = mat[y, y+1]

    return nuova

print(gradini(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))

def gradini2(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = []
    for y in range(n):
        nuova.append(mat[y][y])
        try:
            nuova.append(mat[y][y+1])
        except:
            pass
    return nuova

print(gradini2(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))

def gradini3(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = np.zeros(n+n-1)
    for y in range(n):
        nuova[y*2] = mat[y][y]
        try:
            nuova[y*2+1] = mat[y][y+1]
        except:
            pass
    return nuova

print(gradini3(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))

def gradini_pro(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = np.zeros(n+n-1)
    nuova[::2] = np.diag(mat)
    nuova[1::2] = np.diag(mat,1)
    return nuova

print(gradini_pro(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))

def gradini4(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    
    res = np.zeros(n+n-1)
    for i in range(n):
        res[2*i] = mat[i,i]
    
    for i in range(n-1):
        res[2*i+1] = mat[i, i+1]
    
    return res

def gradini_pro2(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    a = np.diag(mat)
    b = np.diag(mat,1)
    ret = np.zeros((1, a.shape[0] + b.shape[0]))
    ret[:, ::2] = a
    ret[:, 1::2] = b
    return ret

print(gradini_pro2(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))
print()

def gradini5(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = np.zeros(n+n-1)
    for y in range(n):
        nuova[y*2] = mat[y][y]
    for y in range(n-1):
        nuova[y*2+1] = mat[y][y+1]
    return nuova

print(gradini5(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] ))
)

def gradini_pro3(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = np.zeros(n+n-1)
    nuova[::2] = np.diag(mat)
    nuova[1::2] = np.diag(mat, 1)
    return nuova

print(gradini_pro3(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] ))
)
print()