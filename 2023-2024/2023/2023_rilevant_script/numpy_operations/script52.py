# Le versioni della funzione 
# calcolano la media dei valori nei 4 quadranti di una matrice quadrata e 
# restituisce una matrice 2×2 con queste medie.

import numpy as np

m = np.array( [ [1.0, 2.0 , 5.0 , 7.0],
[4.0, 1.0 , 8.0 , 0.0],
[2.0, 0.0 , 5.0 , 1.0],
[0.0, 2.0 , 1.0 , 1.0] ])

def quadranti_pro(mat):
    n = mat.shape[0] // 2
    nuova = np.zeros((2,2))
    nuova[0,0] = np.sum(mat[:n, :n]) / (n*n)
    nuova[0,1] = np.sum(mat[:n, n:]) / (n*n)
    nuova[1,1] = np.sum(mat[n:, n:]) / (n*n)
    nuova[1,0] = np.sum(mat[n:, :n]) / (n*n)
    return nuova

print(quadranti_pro(m))

m1 = np.array( [ [3.0, 5.0],
[4.0, 9.0] ])
r1 = np.array([ [3.0, 5.0],
[4.0, 9.0],
])
assert np.allclose(quadranti_pro(m1),r1)
m2 = np.array( [ [1.0, 2.0 , 5.0 , 7.0],
[4.0, 1.0 , 8.0 , 0.0],
[2.0, 0.0 , 5.0 , 1.0],
[0.0, 2.0 , 1.0 , 1.0] ])
r2 = np.array( [ [2.0, 5.0],
[1.0, 2.0] ] )
assert np.allclose(quadranti_pro(m2),r2)

def quadranti(mat):
    n = len(mat) // 2
    m = n*n
    nuova = []
    zeze = []
    zeun = []
    unze = []
    unun = []
    for y in range(n):
        for x in range(n):
            zeze.append(mat[y][x])
        for x in range(n):
            zeun.append(mat[y][x+n])
    for y in range(n, n+n):
        for x in range(n):
            unze.append(mat[y][x])
        for x in range(n):
            unun.append(mat[y][x+n])
    riga = [sum(zeze)/m, sum(zeun)/m]
    riga1 = [sum(unze)/m, sum(unun)/m]
    nuova.append(riga)
    nuova.append(riga1)
    return nuova

print(quadranti(m))

m1 = np.array( [ [3.0, 5.0],
[4.0, 9.0] ])
r1 = np.array([ [3.0, 5.0],
[4.0, 9.0],
])
assert np.allclose(quadranti(m1),r1)
m2 = np.array( [ [1.0, 2.0 , 5.0 , 7.0],
[4.0, 1.0 , 8.0 , 0.0],
[2.0, 0.0 , 5.0 , 1.0],
[0.0, 2.0 , 1.0 , 1.0] ])
r2 = np.array( [ [2.0, 5.0],
[1.0, 2.0] ] )
assert np.allclose(quadranti(m2),r2)
print()