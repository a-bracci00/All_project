# La funzione pareggio verifica se, per ogni riga di una matrice binaria, 
# il numero di 1 è uguale alla metà del numero totale di colonne. 
# Restituisce un array con valori booleani, 
# dove ogni elemento indica se la condizione è soddisfatta per quella riga.

import numpy as np

mat = np.array([[1,0,0,0,0,1,1,0],
[1,1,1,0,1,1,0,0],
[1,0,1,0,1,0,0,1],
[1,1,0,0,0,1,1,0],
[0,1,0,1,1,1,1,0],
[0,0,1,1,0,0,1,1]])
#importante
def pareggio(mat):
    return np.reshape(np.sum(mat, axis = 1) == len(mat[0]) // 2, (len(mat),1))

print(pareggio(mat))
print(type(pareggio(mat)))
print()

m1 = np.array([[0,0]])
res = pareggio(m1)
print(res) # strano qua stampa float, mentre in pareggio_pro dei boolean
assert type(res) == np.ndarray
assert np.allclose(res, np.array([ [False] ]))
m2 = np.array([[1,0]])
assert np.allclose(pareggio(m2), np.array([ [True] ]))
m3 = np.array([[0,1]])
assert np.allclose(pareggio(m3), np.array([ [True] ]))
m4 = np.array([[1,1]]) # True
assert np.allclose(pareggio(m4), np.array([ [False] ]))
m5 = np.array([[1,1],
[0,1]])
assert np.allclose(pareggio(m5), np.array([ [False],
[True] ]))
m6 = np.array([[0,1],
[1,0]])
assert np.allclose(pareggio(m6), np.array([ [True],
[True] ]))
m7 = np.array([[1,1,0,0],
[1,1,0,1],
[1,0,0,1]])
assert np.allclose(pareggio(m7), np.array([ [True],
[False],
[True] ]))
m8 = np.array([[1,0,0,0,0,1,1,0],
[1,1,1,0,1,1,0,0],
[1,0,1,0,1,0,0,1],
[1,1,0,0,0,1,1,0],
[0,1,0,1,1,1,1,0],
[0,0,1,1,0,0,1,1]])
assert np.allclose(pareggio(m8), np.array([ [False],
[False],
[ True],
[ True],
[False],
[ True] ]))
print()