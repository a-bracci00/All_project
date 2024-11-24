# unisco 2 matrici mettendo la seconda a destra
def attacca_dx(mat1, mat2):
    nuova = []
    for x in mat1:
        nuova.append(x[:])
    for riga in range(len(nuova)):
        for y in range(len(mat2[0])):
            nuova[riga].append(mat2[riga][y])
    return nuova

m3 = [ ['a','b'],
['c','d'],
['e','f'] ]

m4 = [[1,2],
      [3,4],
      [5,6]]
print(attacca_dx(m3,m4))

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
assert attacca_dx(m1, m2) == [ ['a','b','c','f','b'],
['d','b','a','g','h'] ]