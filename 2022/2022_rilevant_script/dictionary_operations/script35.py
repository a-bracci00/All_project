#La funzione sagra crea una tabella che contiene i nomi delle persone, 
# le quantità di ciascun dolce da loro scelto, e infine calcola i totali per ogni dolce.

def sagra(lista, dolci):
    nuova = [['Nome'] + dolci[:]]
    ultima = ['Totali']
    for x in lista:
        riga = []
        riga.append(x['nome'])
        for y in dolci:
            riga.append(x[y])
        nuova.append(riga)
    j = 1
    for dolce in dolci:
        tot = 0
        for x in range(1, len(nuova)):
            tot += nuova[x][j]
        ultima.append(tot) # type: ignore
        j += 1
    nuova.append(ultima)
    return nuova

pasticcerie = [{'babbà':3,
'bignè':4,
'zippole':2,
'nome':'Da Gigi'},
{'babbà':5,
'bignè':3,
'zippole':9,
'nome':'La Delizia'},
{'babbà':1,
'bignè':2,
'zippole':6,
'nome':'Gnam gnam'},
{'babbà':7,
'bignè':8,
'zippole':4,
'nome':'Il Dessert'}]

[print(x) for x in sagra(pasticcerie, ['bignè', 'babbà', 'zippole'])]
print()
from pprint import pprint
pprint(sagra(pasticcerie, ['bignè', 'babbà', 'zippole']))

dolci1 = ['cornetti']
res1 = sagra([{'nome':'La Patisserie',
'cornetti':2},
{'cornetti':5,
'nome':'La Casa Del Cioccolato'}], dolci1)
assert res1 == [['Nome', 'cornetti' ],
['La Patisserie', 2 ],
['La Casa Del Cioccolato', 5 ],
['Totali', 7 ]]
assert dolci1 == ['cornetti'] # verifica che l'input non cambi
pasticcerie2 = [{'babbà':3,
'bignè':4,
'zippole':2,
'nome':'Da Gigi'},
{'babbà':5,
'bignè':3,
'zippole':9,
'nome':'La Delizia'},
{'babbà':1,
'bignè':2,
'zippole':6,
'nome':'Gnam gnam'},
{'babbà':7,
'bignè':8,
'zippole':4,
'nome':'Il Dessert'}]
res2 = sagra(pasticcerie2, ['bignè', 'babbà', 'zippole'])
assert res2 == [['Nome', 'bignè', 'babbà', 'zippole'],
['Da Gigi', 4, 3, 2 ],
['La Delizia', 3, 5, 9 ],
['Gnam gnam', 2, 1, 6 ],
['Il Dessert', 8, 7, 4 ],
['Totali', 17, 16, 21 ]]
print()