# inserisco una determinata colonna
def insercol(mat, j, nuova_col):
    for x in range(len(mat)):
        mat[x].insert(j, nuova_col[x])

m = [
[5,4,6],
[4,7,1],
[3,2,6],
]
print(m)  
insercol(m, 2, [7,9,3])
print(m)
print()

# rimuovo una determinata colonna
def remcol(mat, j):
    if j < 0 or j > len(mat):
        raise ValueError
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x].pop(j))
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(m)
print(remcol(m,2))
print(m)
print()