# prendo solo gli elementi in diagonale negativa
def diag(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x][x])
    return nuova

m = [   [5,4,7],
        [4,7,9],
        [3,2,3] ]

print(m)
print(diag(m))
print(m)
m = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
assert diag(m) == ['a','e','i']
print()

# prendo solo gli elementi in diagonale positiva
def anti_diag(mat):
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x][-1-x])
    return nuova

m = [   [5,4,7],
        [4,7,9],
        [3,2,3] ]

print(m)
print(anti_diag(m))
print(m)
m = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
assert anti_diag(m) == ['c','e','g']
print()