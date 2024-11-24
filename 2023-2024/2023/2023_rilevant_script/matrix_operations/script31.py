#La funzione incarta ogni elemento della matrice scaf, 
# aggiungendo a sinistra e a destra il corrispondente valore di conf. 
# Se le dimensioni di scaf e conf non corrispondono, solleva un'eccezione

from pprint import pprint

def incarta(scaf, conf):
    if len(conf) != len(scaf):
        raise ValueError

    for y in range(len(scaf)):
        for x in range(len(scaf[0])):
            scaf[y][x] = conf[y] + scaf[y][x] + conf[y]



m = [['f','e','a','b'],
['a','c','g','f'],
['b','c','d','f']]

c =  ['/','|','!']
[print(x) for x in m]
incarta(m,c)
pprint(m)
m1 = [['a']]
riga_zero_m1 = m1[0]
res = incarta(m1, ['|'])
assert res == None
assert m1 == [['|a|']]
# controlla che la riga zeresima punti ancora esattamente alla stessa regione di memoria originale
assert id(m1[0]) == id(riga_zero_m1)
m2 = [['f','g']]
incarta(m2, ['|'])
assert m2 == [['|f|','|g|']]
m3 = [['a'],
['b'],]
incarta(m3, ['?','|'])
assert m3 == [['?a?'],
['|b|']]
m3 = [['f','e','a','b'],
['a','c','g','f'],
['b','c','d','f']]
incarta(m3, ['/','|','!'])

assert m3 == [['/f/', '/e/', '/a/', '/b/'],
['|a|', '|c|', '|g|', '|f|'],
['!b!', '!c!', '!d!', '!f!']]
try:
    incarta([['a']], ['/','!'])
    raise Exception('Avrei dovuto fallire prima !')
except ValueError:
    pass
print()