# Le versioni della funzione sostituiscono tutti gli elementi della matrice 
# mat con il valore massimo di ciascuna colonna.

import numpy as np

def sostmax(mat):
    #mx = np.max(mat, axis = 0)
    #mat[:] = mx
    mat[:] = np.max(mat, axis = 0)

m = np.array([[5,4,2],
[8,5,1],
[6,7,9],
[3,6,4],
[4,3,7]])

print(sostmax(m))
m1 = np.array([[6]])
sostmax(m1)
assert np.allclose(m1, np.array([6]))
ret = sostmax(m1)
assert ret == None # non ritorna nulla!
m2 = np.array([[6,8]])
sostmax(m2)
assert np.allclose(m2, np.array([6,8]))
m3 = np.array([[2],
[5]])
sostmax(m3)
assert np.allclose(m3, np.array([[5],
[5]]))
m4 = np.array([[5,7],
[2,9]])
sostmax(m4)
assert np.allclose(m4, np.array([[5,9],
[5,9]]))
m5 = np.array([[4,7],
[4,9]])
sostmax(m5)
assert np.allclose(m5, np.array([[4,9],
[4,9]]))
m6 = np.array([[5,2],
[3,7],
[9,0]])
sostmax(m6)
assert np.allclose(m6, np.array([[9,7],
[9,7],
[9,7]]))
m7 = np.array([[5,4,2],
[8,5,1],
[6,7,9],
[3,6,4],
[4,3,7]])
sostmax(m7)
assert np.allclose(m7, np.array([[8, 7, 9],
[8, 7, 9],
[8, 7, 9],
[8, 7, 9],
[8, 7, 9]]))


def sostmax1(mat):
    nuova = []
    for x in range(len(mat[0])):
        riga = []
        for y in range(len(mat)):
            riga.append(mat[y][x])
        nuova.append(max(riga))
    
    for x in range(len(mat[0])):
        for y in range(len(mat)):
            mat[y][x] = nuova[x]


print(sostmax1(m))
print(m)