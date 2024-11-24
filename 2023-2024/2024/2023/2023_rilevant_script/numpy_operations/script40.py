#La funzione quadroslices crea una matrice quadrata 
# di dimensione n x n dove il perimetro è riempito con un valore specificato (k), 
# e gli elementi interni sono lasciati a zero.

import numpy as np

def quadroslices(n, k):
    mat = np.zeros((n, n))
    mat[0, :] = k
    mat[:, 0] = k
    mat[:, n-1] = k
    mat[n-1, :] = k
    return mat

print(quadroslices(4, 7.0))

r1 = np.array( [[7.0, 7.0, 7.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 7.0, 7., 7.0]])
# all_close ritorna True se tutti i valori nella prima matrice sono abbastanza vicini
# (cioè entro una certa tolleranza) ai corrispondenti nella seconda
assert np.allclose(quadroslices(4, 7.0), r1)
r2 = np.array( [ [7.0] ])
assert np.allclose(quadroslices(1, 7.0), r2)
r3 = np.array( [ [7.0, 7.0],
[7.0, 7.0]])
assert np.allclose(quadroslices(2, 7.0), r3)
