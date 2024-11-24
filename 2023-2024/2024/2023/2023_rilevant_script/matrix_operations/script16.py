# sommo le righe eliminando i valori in diagonale
def evita_diag(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    nuova = []
    for x in range(len(mat)):
        nuova.append(sum(mat[x]) - mat[x][x])
    return nuova

print(evita_diag([ [5,6,2],
                   [4,7,9],
                   [1,9,8]]))

assert evita_diag([[5]]) == [0]
m2 = [[5,7],
[9,1]]
assert evita_diag(m2) == [7,9]
assert m2 == [[5,7],
[9,1]]
assert evita_diag([ [5,6,2],
[4,7,9],
[1,9,8]]) == [8, 13, 10]
try:
    evita_diag([[2,3,5],
    [1,5,2]])
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass