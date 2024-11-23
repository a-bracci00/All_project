# controllo se i valori sono maggiori di e ritorno una matrice di true e false
def soglia(mat, t):
    nuova = [x[:] for x in mat]
    for x in range(len(nuova)):
        for y in range(len(nuova[0])):
                nuova[x][y] = nuova[x][y] > t
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(m)
print(soglia(m, 4))
print(m)
print()