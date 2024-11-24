# Le versioni della funzione prendono una matrice con un numero pari di colonne e 
# crea una nuova matrice in cui ogni colonna è la somma delle coppie di 
# colonne adiacenti della matrice originale. Se il numero di colonne non è pari, 
# genera un errore.

import numpy as np

def compricol(mat):
    n,m = mat.shape
    if m % 2 != 0:
        raise ValueError
    
    nuova = np.zeros((n, m//2))
    for y in range(n):
        for x in range(0, m, 2):
            nuova[y][x//2] = mat[y][x] + mat[y][x+1]
    return nuova

m = np.array([[5,4,2,6,4,2],
[7,5,1,0,6,1],
[6,7,9,2,3,7],
[5,2,4,6,1,3],
[7,2,3,4,2,5]])

print(compricol(m))
m1 = [[7,9]]
res = compricol(np.array(m1))
assert type(res) == np.ndarray
assert np.allclose(res, np.array([[16]]))
m2 = np.array([[5,8],
[7,2]])
assert np.allclose(compricol(m2), np.array([[13],
[9]]))
assert np.allclose(m2, np.array([[5,8],
[7,2]])) # non cambia la matrice originale
m3 = np.array([[5,4,2,6,4,2],
[7,5,1,0,6,1],
[6,7,9,2,3,7],
[5,2,4,6,1,3],
[7,2,3,4,2,5]])
assert np.allclose(compricol(m3), np.array([[ 9, 8, 6],
[12, 1, 7],
[13,11,10],
[ 7,10, 4],
[ 9, 7, 7]]))
try:
    compricol(np.array([[7,1,6],[5,2,4]]))
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass

def compricol1(mat):
    n,m = mat.shape
    if m % 2 != 0:
        raise ValueError
    
    nuova = np.zeros((n,m//2))
    nuova[:,:] = mat[:,::2] + mat[:, 1::2]
    return nuova

m = np.array([[5,4,2,6,4,2],
[7,5,1,0,6,1],
[6,7,9,2,3,7],
[5,2,4,6,1,3],
[7,2,3,4,2,5]])
print(compricol1(m))

def compricol2(mat):
    n,m = mat.shape
    if m % 2 != 0:
        raise ValueError
    
    nuova = mat[:, ::2].copy()
    nuova += mat[:, 1::2]
    return nuova

m = np.array([[5,4,2,6,4,2],
[7,5,1,0,6,1],
[6,7,9,2,3,7],
[5,2,4,6,1,3],
[7,2,3,4,2,5]])
print(compricol2(m))
print()