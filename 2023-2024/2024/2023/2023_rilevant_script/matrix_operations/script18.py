# rimuovo gli elementi nell'antidiagonale
def no_anti_diag(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    nuova = [x[:] for x in mat]
    for x in range(len(mat)):
        nuova[x].pop(-1-x)
    return nuova

m = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
[print(x) for x in m]
print()
[print(x) for x in no_anti_diag(m)]
print()
[print(x) for x in m]    

m1 = [[3,4],
[8,7]]
assert no_anti_diag(m1) == [[3],
[7]]
assert m1 == [[3,4], # verifica che non abbia cambiato l'originale
[8,7]]
m2 = [[9,4,3],
[8,5,6],
[0,2,7]]
assert no_anti_diag(m2) == [[9,4],
[8,6],
[2,7]]
m3 = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
assert no_anti_diag(m3) == [[8,5,3],
[7,2,1],
[9,3,5],
[0,4,7]]
try:
    no_anti_diag([[2,3,5],
[1,5,2]])
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass
print()