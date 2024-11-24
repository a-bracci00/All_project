#La funzione crea una nuova matrice nuova in cui ogni riga della matrice 
#mat viene ripetuta un numero di volte specificato dall'elemento corrispondente in lista. 
# Più precisamente, per ogni riga x di mat, la riga viene aggiunta alla matrice nuova un numero di volte pari a lista[x]

def muro(lista, mat):
    nuova = []
    for x in range(len(mat)):
        for j in range(lista[x]):
            nuova.append(mat[x][:])
    return nuova

lista = [3,4,1,2]
m = [['i','a','a'],
['q','r','f'],
['y','e','v'],
['e','g','h']]
[print(x) for x in m]
print()
[print(x) for x in muro(lista, m)]
print()
[print(x) for x in m]
print()

m1 = [['a']]
assert muro([2], m1) == [['a'],
['a']]
m2 = [['a','b','c','d'],
['e','q','v','r']]
r2 = muro([3,2], m2)
assert r2 == [['a','b','c','d'],
['a','b','c','d'],
['a','b','c','d'],
['e','q','v','r'],
['e','q','v','r']]
r2[0][0] = 'z'
m3 = [['i','a','a'],
['q','r','f'],
['y','e','v'],
['e','g','h']]
r3 = muro([3,4,1,2], m3)
assert r3 == [['i', 'a', 'a'],
['i', 'a', 'a'],
['i', 'a', 'a'],
['q', 'r', 'f'],
['q', 'r', 'f'],
['q', 'r', 'f'],
['q', 'r', 'f'],
['y', 'e', 'v'],
['e', 'g', 'h'],
['e', 'g', 'h']]
assert m2 == [['a','b','c','d'], # vogliamo una NUOVA matrice
['e','q','v','r']]
print()