# scambio le righe di una matrice
def scambia_righe(mat, i1, i2):
    nuova = [x[:] for x in mat]
    buf = nuova[i1]
    nuova[i1] = nuova[i2]
    nuova[i2] = buf
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(m)
print(scambia_righe(m, 0, 2))
print(m)
m = [ ['a','d'],
['b','e'],
['c','f'] ]
res = scambia_righe(m, 0, 2)
assert res == [ ['c','f'],
['b','e'],
['a','d'] ]
print()


# scambio le colonne
def scambia_colonne(mat, j1, j3):
    nuova = [x[:] for x in mat]
    for x in nuova:
        buff = x[j1]
        x[j1] = x[j3]
        x[j3] = buff
    return nuova

m = [   [5,4,7,6],
        [4,7,9,1],
        [3,2,3,6] ]

print(m)
print(scambia_colonne(m, 0, 1))
print(m)
m = [ ['a','b','c'],
['d','e','f'] ]
res = scambia_colonne(m, 0,2)
assert res == [ ['c','b','a'],
['f','e','d'] ]
print()