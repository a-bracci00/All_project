# controlla se ogni elemento di una riga è strettamente minore dell'elemento successivo nella stessa riga.
def matinc(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])-1):
            if mat[x][y] >= mat[x][y+1]:
                return False
    return True

m = [[1,4,6,7,9],
[0,1,2,4,8],
[2,6,8,9,10]]
print(matinc(m))
m = [[0,1,3,4],
[4,6,9,10],
[3,7,7,15]]
print(matinc(m))
m1 = [[5]]
assert matinc(m1) == True
m2 = [[7],
[4]]
assert matinc(m2) == True
m3 = [[2,3],
[3,5]]
assert matinc(m3) == True
m4 = [[9,4]]
assert matinc(m4) == False
m5 = [[5,5]]
assert matinc(m5) == False
m6 = [[1,4,6,7,9],
[0,1,2,4,8],
[2,6,8,9,10]]
assert matinc(m6) == True
m7 = [[0,1,3,4],
[4,6,9,10],
[3,7,7,15]]
assert matinc(m7) == False
m8 = [[1,4,8,7,9],
[0,1,2,4,8]]
assert matinc(m8) == False