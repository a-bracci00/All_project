# Le versioni della funzione moltiplicano ogni elemento di una matrice (mat) per un array (arr) di uguale lunghezza, 
# elemento per elemento. Restituisce una nuova matrice risultante da questa operazione

import numpy as np

def matxarr(mat, arr):
    nuova = np.zeros((mat.shape))
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            nuova[y,x] = mat[y,x] * arr[x]
    return nuova

m1 = np.array( [ [3,2,1],
[6,2,3],
[4,3,6],
[4,6,5] ] )
a1 = np.array([5, 2, 6])

print(matxarr(m1, a1))
r1 = np.array([ [3*5, 2*2, 1*6],
[6*5, 2*2, 3*6],
[4*5, 3*2, 6*6],
[4*5, 6*2, 5*6] ])
assert np.allclose(matxarr(m1,a1), r1)

def matxarr_pro(mat, arr):
    return np.array(mat) * arr
    #return np.array(arr) * mat

print(matxarr_pro(m1, a1))
print()