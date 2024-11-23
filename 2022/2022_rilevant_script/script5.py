# leggere matrice verticalmente
def matriverba(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x].upper())
        for y in range(1,len(mat)):
            nuova.append(mat[y][x])
    return ''.join(nuova)


m = [['p','c','z','g','b', 'd'],
    ['o','a','a','i','o', 'e'],
    ['r','l','n','a','r', 'n'],
    ['t','m','n','r','s', 't'],
    ['o','a','a','a','e', 'e']];

print(matriverba(m))