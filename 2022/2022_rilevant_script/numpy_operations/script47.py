# Le verioni della funzione sommano gli elementi delle righe pari con quelli delle righe dispari corrispondenti in una matrice, 
# aggiornando direttamente le righe dispari e restituendo la matrice modificata.

import numpy as np

def somma_alterna_pro(mat):
    #mat = np.array(mat)
    mat[1::2] += mat[::2]
    return mat
m1 = np.array( [ [1.0, 3.0, 2.0, 5.0],
[2.0, 8.0, 5.0, 9.0],
[6.0, 9.0, 7.0, 2.0],
[4.0, 7.0, 2.0, 4.0] ])
r1 = np.array( [ [1.0, 3.0, 2.0, 5.0],
[3.0, 11.0,7.0, 14.0],
[6.0, 9.0, 7.0, 2.0],
[10.0,16.0,9.0, 6.0] ])

#print(m)
print(somma_alterna_pro(m1))
somma_alterna_pro(m1)
#assert np.allclose(m1, r1) # controlla che abbiamo MODIFICATO la matrice originale
m2 = np.array( [ [5.0] ])
r2 = np.array( [ [5.0] ])
somma_alterna_pro(m1)
assert np.allclose(m2, r2)
m3 = np.array( [ [6.0, 1.0],
[3.0, 2.0] ])
r3 = np.array( [ [6.0, 1.0],
[9.0, 3.0] ])
somma_alterna_pro(m3)
assert np.allclose(m3, r3)
print()

def somma_alterna2(mat):
    for y in range(1, len(mat), 2):
        for x in range(len(mat[0])):
            mat[y][x] += mat[y-1][x]

somma_alterna2(m1)
[print(x) for x in m1]
print()