#La funzione toepliz(mat) verifica se la matrice mat è una matrice di Toeplitz, 
# cioè se ogni elemento è uguale all'elemento diagonale superiore sinistro. 
# Restituisce True se la matrice soddisfa questa condizione, altrimenti False.

def toepliz(mat):
    for x in range(1,len(mat)):
        for y in range(1,len(mat[0])):
            if mat[x][y] != mat[x-1][y-1]:
                return False
    return True

m1 = [
[1,2,3,4],
[5,1,2,3],
[9,5,1,2]
]
print(toepliz(m1))

# INIZIO TEST - NON TOCCARE !
assert toepliz([ [1] ]) == True
assert toepliz([ [3,7],
[5,3] ]) == True
assert toepliz([ [3,7],
[3,5] ]) == False
assert toepliz([ [3,7],
[3,5] ]) == False
assert toepliz([ [3,7,9],
[5,3,7] ]) == True
assert toepliz([ [3,7,9],
[5,3,8] ]) == False
assert toepliz([ [1,2,3,4],
[5,1,2,3],
[9,5,1,2] ]) == True
assert toepliz([ [1,2,3,4],
[5,9,2,3],
[9,5,1,2] ]) == False
# FINE TEST
print()