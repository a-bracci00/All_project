# trasposta la matrice
def trasposta_2(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    for x in range(len(mat)):
        for y in range(x, len(mat[0])):
            el = mat[x][y]
            mat[x][y] = mat[y][x]
            mat[y][x] = el
m3 = ([  [3,2,5],
        [1,6,2],
        [1,0,4] ])

([print(x) for x in m3])
trasposta_2(m3)
print()
[print(x) for x in m3]
print()