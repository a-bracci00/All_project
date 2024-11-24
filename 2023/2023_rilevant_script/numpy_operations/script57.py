# Le versioni della funzione lavorano su una matrice quadrata (\( n \times n \)) 
# e modifica la parte triangolare inferiore (sotto la diagonale principale).  
#Per ogni riga sotto la diagonale, gli elementi a sinistra della diagonale 
# vengono invertiti nell’ordine orizzontale. La funzione restituisce una copia 
# modificata della matrice originale. Se la matrice non è quadrata, solleva un errore.

import numpy as np

m = np.array([ [5,4,2,6,4],
[3,5,1,0,6],
[6,4,9,2,3],
[5,2,8,6,1],
[7,9,3,2,2] ])

def revtriang(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    
    nuova = mat.copy()
    for y in range(1,n):
        nuova[y,:y] = np.flip(mat[y,:y])
    return nuova
    

print(revtriang(m))
print()

def revtriang2(mat):
    n,m = mat.shape

    if n != m:
        raise ValueError
    
    nuova = mat.copy()
    for y in range(n):
        nuova[y,:y] = np.flip(mat[y,:y])
    return nuova

print(m)
print(revtriang2(m))
print()

def revtriang3(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    
    nuova = mat.copy()

    for y in range(1,n):
        riga = []
        for x in range(y):
            riga.append(nuova[y][x])
        riga.reverse()
        for x in range(y):
            nuova[y][x] = riga[x]

    return nuova
print(m)
print(revtriang3(m))
            
m1 = np.array([[8]])
assert np.allclose(revtriang3(m1), np.array([[8]]))
m3 = np.array([[1,5],
[9,6]])
assert np.allclose(revtriang3(m3), np.array([[1,5],
[9,6]]))
m4 = np.array([[1,5,8],
[9,6,2],
[3,2,5]])
assert np.allclose(revtriang3(m4), np.array([[1,5,8],
[9,6,2],
[2,3,5]]))
assert np.allclose(m4, np.array([[1,5,8],
[9,6,2],
[3,2,5]])) # non cambia l'originale
m5 = np.array([[5,4,2,6,4],
[3,5,1,0,6],
[6,4,9,2,3],
[5,2,8,6,1],
[7,9,3,2,2]])
assert np.allclose(revtriang3(m5), np.array([[5, 4, 2, 6, 4],
[3, 5, 1, 0, 6],
[4, 6, 9, 2, 3],
[8, 2, 5, 6, 1],
[2, 3, 9, 7, 2]]))
try:
    revtriang3(np.array([[7,1,6],[5,2,4]]))
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass
print()