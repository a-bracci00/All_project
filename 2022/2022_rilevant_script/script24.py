#La funzione trova il primo 1 nella matrice e restituisce la distanza in righe 
# dall'ultimo elemento della matrice a quella riga. Se non ci sono 1, restituisce 0.
def gratt(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] == 1:
                return len(mat) - x
    return 0

m = [[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]

print(gratt(m))
assert gratt([[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]) == 4
assert gratt([ [0, 0, 0, 0],
[0, 1, 0, 0],
[0, 1, 1, 0],
[1, 1, 1, 1] ]) == 3
assert gratt([ [0, 1, 0, 0],
[0, 1, 0, 0],
[0, 1, 1, 0],
[1, 1, 1, 1] ]) == 4
assert gratt([ [0, 0, 0, 0],
[0, 0, 0, 0],
[1, 1, 1, 0],
[1, 1, 1, 1] ]) == 2