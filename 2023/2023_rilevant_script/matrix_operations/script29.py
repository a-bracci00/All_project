#La funzione verifica se la disposizione delle regine in una matrice mat di dimensione n x n 
# è una soluzione valida al problema delle N regine, senza che le regine si attacchino tra loro.

def queen_check(mat):
    if len(mat) != len(mat[0]):
        return ValueError
    n = len(mat)
    for y in range(n):
        for x in range(n):
            if mat[y][x]:
                for y1 in range(n): #verticale
                    if y1 != y and mat[y1][x]:
                        return False
                for x1 in range(n): #orizzontale
                    if x1 != x and  mat[y][x1]:
                        return False
                for j in range(n):
                    z = j + x + y # alto sinistra basso destra
                    if z >= 0 and z < n and z != y and j != x and mat[z][j]:
                        return False
                    z = j - x + y #alto destra basso sinistra
                    if z >= 0 and z < n and z != y and j != x and mat[z][j]:
                        return False
                    
    return True

m = ([  [False, False, False, False ],
        [False, False, False, False ],
        [False, False, True, False ],
        [False, True, False, False ],])

print(queen_check(m))
assert queen_check([ [True, False],
[False, True] ]) == False
assert queen_check([ [True] ])
assert queen_check([ [True, True],
[False, False] ]) == False
assert queen_check([ [True, False],
[False, True] ]) == False
assert queen_check([ [True, False],
[True, False] ]) == False
assert queen_check([ [True, False, False],
[False, False, True],
[False, False, False] ]) == True
assert queen_check([ [True, False, False],
[False, False, False],
[False, False, True] ]) == False
assert queen_check([ [False, True, False],
                    [False, False, False],
                    [False, False, True] ]) == True
assert queen_check([ [False, True, False],
[False, True, False],
[False, False, True] ]) == False
print()