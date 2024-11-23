# sostituisco le righe di una matrice in base agli elementi in una lista
def repcol(mat, lista):
    count = 0
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            mat[x][y] = lista[x]

m = [
['z','a','p','p','a'],
['c','a','r','t','a'],
['p','a','l','l','a']
]
[print(x) for x in m]
print()
repcol(m, ['E', 'H', '?'])
[print(x) for x in m]
m1 = [ ['a'] ]
v1 = ['Q']
repcol(m1,v1) # non ritorna niente!
assert m1 == [['Q']]
m2 = [
['a','b'],
['c','d'],
['e','f'],
['g','h'],
]
salvata = m2[0] # salviamo puntatore alla prima riga originale
v2 = ['P','A','L','A']
repcol(m2,v2) # non ritorna niente!
assert m2 == [['P', 'P'],
['A', 'A'],
['L', 'L'],
['A', 'A']]
assert id(salvata) == id(m2[0]) # non deve creare nuove liste
m3 = [
['z','a','p','p','a'],
['c','a','r','t','a'],
['p','a','l','l','a']
]
v3 = ['E','H','?']
repcol(m3,v3) # non ritorna niente!
assert m3 == [['E', 'E', 'E', 'E','E'],
['H', 'H', 'H', 'H','H'],
['?', '?', '?', '?','?']]
print()