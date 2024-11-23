#La funzione verifica se la disposizione delle regine in una matrice mat di dimensione n x n 
# è una soluzione valida al problema delle N regine, senza che le regine si attacchino tra loro.

def check_nqueen(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j]: # queen is found at i,j
                for y in range(n): # vertical scan
                    if y != i and mat[y][j]:
                        return False
                for x in range(n): # horizontal scan
                    if x != j and mat[i][x]:
                        return False
                for x in range(n):
                    y = x + j + i # top-left to bottom-right
                    if y >= 0 and y < n and y != i and x != j and mat[y][x]:
                        return False
                    y = x - j + i # bottom-left to top-right
                    if y >= 0 and y < n and y != i and x != j and mat[y][x]:
                        return False
    return True

m = ([  [True, False, False],
        [False, False, True],
        [False, False, False] ])
print(check_nqueen(m))