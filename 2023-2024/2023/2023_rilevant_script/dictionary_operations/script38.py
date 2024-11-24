# La funzione ricme crea una lista di sotto-liste, 
# dove ogni sotto-lista contiene una chiave del dizionario seguita dai suoi valori. 
# La lista finale è ordinata in base alle chiavi e ai valori associati.

valori = {'c':'xzwy',
'a':'yxzw',
'b':'zxwy'}

from pprint import pprint

def ricme(diz):
    nuova = []
    for x in diz:
        riga = [x]
        riga.sort()
        nuova.append(riga)
        x = diz[x]
        for y in x:
            riga.append(y)
    nuova.sort()
    return nuova
            
pprint(ricme(valori))
assert ricme({}) == []
assert ricme({'d':'q'}) == [['d','q']]
assert ricme({'d':'pq',
'e':'qp'}) == [['d','p','q'],
['e','q','p']]
assert ricme({'c':'xzwy',
'a':'yxzw',
'b':'zxwy'}) == [['a', 'y', 'x', 'z', 'w'],
['b', 'z', 'x', 'w', 'y'],
['c', 'x', 'z', 'w', 'y']]