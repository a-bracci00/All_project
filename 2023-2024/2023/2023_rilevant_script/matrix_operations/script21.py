# inverto il valore e la matrice
def flip(mat):
    nuova = [x[:] for x in mat]
    for x in range(len(nuova)):
        for y in range(len(nuova[0])):
            if nuova[x][y] == 0:
                nuova[x][y] = 1
            else:
                nuova[x][y] = 0
        nuova[x] = nuova[x][::-1]
    return nuova

m = [[0,1,0,0],
     [1,0,0,1],
     [0,0,1,0]]
print(flip(m))

assert flip([[]]) == [[]]
assert flip([[1]]) == [[0]]
assert flip([[1,0]]) == [[1,0]]
m1 = [ [1,0,0],
[1,0,1] ]
r1 = [ [1,1,0],
[0,1,0] ]
assert flip(m1) == r1
m2 = [ [1,1,0,0],
[0,1,1,0],
[0,0,1,0] ]
r2 = [ [1,1,0,0],
[1,0,0,1],
[1,0,1,1] ]
assert flip(m2) == r2
# verifica che l'm originale non sia cambiato !
assert m2 == [ [1,1,0,0],
[0,1,1,0],
[0,0,1,0] ]
print()