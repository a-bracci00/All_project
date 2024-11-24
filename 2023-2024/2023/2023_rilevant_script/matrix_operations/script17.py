# rimuovo gli elementi in diagonale
def no_diag(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    
    nuova = [x[:] for x in mat]
    for x in range(len(mat)):
        nuova[x].pop(x)
            
    return nuova

m = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
[print(x) for x in m]
print(no_diag(m))
[print(x) for x in m]

m1 = [[3,4],
[8,7]]
assert no_diag(m1) == [[4],
[8]]
assert m1 == [[3,4], # verifica che non abbia cambiato l'originale
[8,7]]
m2 = [[9,4,3],
[8,5,6],
[0,2,7]]
assert no_diag(m2) == [[4,3],
[8,6],
[0,2]]
m3 = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
assert no_diag(m3) == [[5,3,4],
[7,4,1],
[9,8,5],
[6,0,4]]
try:
    no_diag([[2,3,5],
[1,5,2]])
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass
