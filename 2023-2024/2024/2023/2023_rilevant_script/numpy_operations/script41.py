#La funzione quadroriemp crea una matrice quadrata di dimensione n x n 
# in cui il perimetro è riempito con un valore specificato (k), 
# mentre gli elementi interni sono impostati a 0.0

import numpy as np

def quadroriemp(n, k):
    mat = np.full((n,n), k)
    mat[1:-1, 1:-1] = 0.0
    return mat

print(quadroriemp(4, 7.0))

r1 = np.array( [[7.0, 7.0, 7.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 7.0, 7., 7.0]])
# all_close ritorna True se tutti i valori nella prima matrice sono abbastanza vicini
# (cioè entro una certa tolleranza) ai corrispondenti nella seconda
assert np.allclose(quadroriemp(4, 7.0), r1)
r2 = np.array( [ [7.0] ])
assert np.allclose(quadroriemp(1, 7.0), r2)
r3 = np.array( [ [7.0, 7.0],
[7.0, 7.0]])
assert np.allclose(quadroriemp(2, 7.0), r3)
print()