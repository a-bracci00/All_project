#La funzione lab(lista, mat) ordina la lista lista e la inserisce nella matrice mat, riga per riga. 
# Solleva un'eccezione se la lista è più grande della matrice.
def lab(lista, mat):
    if len(lista) > len(mat) * len(mat[0]):
        raise ValueError
    lista.sort()
    j = 0
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if j < len(lista):
                mat[x][y] = lista[j]
                j += 1

st = ['b', 'd', 'e', 'g', 'c', 'a', 'h', 'f' ]
mat = [
[None, None, None],
[None, None, None],
[None, None, None],
[None, None, None]
]
lab(st, mat)
print(mat)
print(st)
try:
    lab(['a','b'], [[None]])
    raise Exception("TEST FALLITO: Mi aspettavo un ValueError!")
except ValueError:
    "Test passato"
try:
    lab(['a','b','c'], [[None,None]])
    raise Exception("TEST FALLITO: Mi aspettavo un ValueError!")
except ValueError:
    "Test passato"
m0 = [ [None] ]
r0 = lab([],m0)
assert m0 == [ [None] ]
assert r0 == None # si suppone la funzione non ritorni nulla
# (perciò ritorna None di default)
m1 = [ [None] ]
r1 = lab(['a'], m1)
assert m1 == [ ['a'] ]
assert r1 == None # si suppone la funzione non ritorni nulla
# (perciò ritorna None di default)
m2 = [ [None, None] ]
lab(['a'], m2) # 1 studente 2 sedie in una fila
assert m2 == [ ['a', None] ]
m3 = [ [None],
[None] ]
lab(['a'], m3) # 1 studente 2 sedie in una colonna
assert m3 == [ ['a'],
[None] ]
ss4 = ['b', 'a']
m4 = [ [None, None] ]
lab(ss4, m4) # 2 studenti 2 sedie in una fila
assert m4 == [ ['a','b'] ]
assert ss4 == ['a', 'b'] # modificato anche lista di input
# come richiesto dal testo della funzione
m5 = [ [None, None],
[None, None] ]
lab(['b', 'c', 'a'], m5) # 3 studenti 2x2 sedie
assert m5 == [ ['a','b'],
['c', None] ]
m6 = [ [None, None],
[None, None] ]
lab(['b', 'd', 'c', 'a'], m6) # 4 studenti 2x2 sedie
assert m6 == [ ['a','b'],
['c','d'] ]
m7 = [ [None, None, None],
[None, None, None] ]
lab(['b', 'd', 'e', 'c', 'a'], m7) # 5 studenti 3x2 sedie
assert m7 == [ ['a','b','c'],
['d','e',None] ]
ss8 = ['b', 'd', 'e', 'g', 'c', 'a', 'h', 'f' ]
m8 = [ [None, None, None],
[None, None, None],
[None, None, None],
[None, None, None] ]
lab(ss8, m8) # 8 studenti 3x4 sedie
assert m8 == [ ['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', None],
[None, None, None] ]
assert ss8 == ['a','b','c','d','e','f','g','h']