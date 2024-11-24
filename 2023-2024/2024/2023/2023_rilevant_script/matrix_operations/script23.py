#La funzione rimuove l'ultimo elemento di ogni riga, li ordina,
# e poi li reinserisce come ultimi elementi nelle rispettive righe della matrice.

def ordinul(mat):
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x].pop(-1))
    nuova.sort()
    for j in range(len(mat)):
        mat[j].append(nuova[j])
    
m = [[8,5,3,2,4],
[7,2,4,1,1],
[9,8,3,3,7],
[6,0,4,2,5]]

[print(x) for x in m]
print()
ordinul(m)
[print(x) for x in m]

m1 = [[3]]
ordinul(m1)
assert m1 == [[3]]
m2 = [[9,3,7],
[8,5,4]]
ordinul(m2)
assert m2 == [[9,3,4],
[8,5,7]]
m3 = [[8,5,9],
[7,2,3],
[9,8,7]]
ordinul(m3)
assert m3 == [[8,5,3],
[7,2,7],
[9,8,9]]
m4 = [[8,5,3,2,4],
[7,2,4,1,1],
[9,8,3,3,7],
[6,0,4,2,5]]
ordinul(m4)
assert m4 == [[8, 5, 3, 2, 1],
[7, 2, 4, 1, 4],
[9, 8, 3, 3, 5],
[6, 0, 4, 2, 7]]
assert ordinul([[3]]) == None
print()