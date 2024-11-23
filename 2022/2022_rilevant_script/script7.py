# unisco 2 matrici mettendo la seconda alla fine
def attacca_sotto(mat1, mat2):
    nuova = []
    for riga in mat1:
        nuova.append(riga[:])
    for riga in mat2:
        nuova.append(riga[:])
    return nuova


m3 = [ ['a','b'],
['c','d'],
['e','f'] ]

m4 = [[1,2],
      [3,4],
      [5,6]]
print(attacca_sotto(m3,m4))