# Le versioni della funzione scacchiera creano una matrice quadrata di dimensione n x n con un pattern a scacchiera, 
# dove le celle agli indici pari contengono 1 e quelle agli indici dispari contengono 0.

import numpy as np

def scacchiera(n):
    nuova = np.zeros((n,n))
    nuova[::2, ::2] = 1.0
    nuova[1::2, 1::2] = 1.0
    return nuova

print(scacchiera(4))
r1 = np.array( [ [1.0, 0.0, 1.0, 0.0],
[0.0, 1.0, 0.0, 1.0],
[1.0, 0.0, 1.0, 0.0],
[0.0, 1.0, 0.0, 1.0] ])
assert np.allclose(scacchiera(4), r1)
r2 = np.array( [ [1.0] ])
assert np.allclose(scacchiera(1), r2)
r3 = np.array( [ [1.0, 0.0],
[0.0, 1.0] ])
assert np.allclose(scacchiera(2), r3)

def scacchiera1(n):
    nuova = np.zeros((n,n))
    for y in range(0, len(nuova), 2):
        for x in range(0, len(nuova), 2):
            nuova[y][x] = 1.0
    for y in range(1, len(nuova), 2):
        for x in range(1, len(nuova), 2):
            nuova[y][x] = 1.0
    return nuova

print(scacchiera1(4))
print()