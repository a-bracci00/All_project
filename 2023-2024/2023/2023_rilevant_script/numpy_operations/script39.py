# La funzione quadrofor crea una matrice quadrata con un perimetro di un valore specificato, 
# mentre gli elementi interni sono impostati a zero. 
# La dimensione della matrice e il valore del perimetro 
# sono determinati dai parametri nm e valore.

import numpy as np

def quadrofor(nm, valore):
    nuova = [[0]*nm for x in range(nm)]
    for y in range(len(nuova)):
        for x in range(len(nuova[0])):
            if y == 0 or x == 0 or y == len(nuova)-1 or x == len(nuova)-1:
                nuova[y][x] = valore
            else:
                pass
    return nuova

[print(x) for x in quadrofor(4, 7.0)]

def quadrofor1(nm, valore):
    nuova = np.zeros((nm, nm))
    nuova[:, 0] = valore
    nuova[:, -1] = valore
    nuova[0] = valore
    nuova[-1] = valore
    return nuova

[print(x) for x in quadrofor1(4, 7.0)]
r1 = np.array( [[7.0, 7.0, 7.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 7.0, 7.0, 7.0]])
# all_close ritorna True se tutti i valori nella prima matrice sono abbastanza vicini
# (cioè entro una certa tolleranza) ai corrispondenti nella seconda
assert np.allclose(quadrofor1(4, 7.0), r1)
r2 = np.array( [ [7.0] ])
assert np.allclose(quadrofor1(1, 7.0), r2)
r3 = np.array( [ [7.0, 7.0],
[7.0, 7.0]])
assert np.allclose(quadrofor1(2, 7.0), r3)


def quadrofor2(n, k):
    mat = np.zeros((n,n))
    for i in range(n):
        mat[0, i] = k
        mat[i, 0] = k
        mat[i, n-1] = k
        mat[n-1, i] = k
    return mat

print(quadrofor2(4, 7.0))