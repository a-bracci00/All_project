#La funzione scambiattori inverte le chiavi e i valori di un dizionario, 
# tranne per le chiavi 'titolo' e 'anno', 
# che rimangono invariate. Restituisce una lista di dizionari con questa modifica applicata.

lista = [
{'titolo':'Jerry Maguire',
'anno':1996,
'Jerry':'Dorothy',},
{'titolo':'Superman',
'Kent':'Lois',
'anno': 1978},
{'titolo':'The Lord of the Rings',
'anno': 2001,
'Aragorn':'Arwen',},
{'Ron Weasley':'Hermione',
'titolo': 'Harry Potter and the Deathly Hallows, Part 2',
'anno': 2011}
]

def scambiattori(lista):
    nuova = []
    for diz in lista:
        nuovo_diz = {}
        nuova.append(nuovo_diz)
        for chiave in diz:
            if chiave == 'titolo' or chiave == 'anno':
                nuovo_diz[chiave] = diz[chiave]
            else:
                nuovo_diz[diz[chiave]] = chiave
    return nuova
        
[print(x) for x in scambiattori(lista)]

l1 = []
assert scambiattori(l1) == []
l2 = [ {'titolo': 'Pretty Woman',
'anno': 1990,
'Edward':'Vivian'},
{'titolo': 'Titanic',
'anno': 1997,
'Jack' : 'Rose'}
]
orig_film = l2[0]
res2 = scambiattori(l2)
assert res2 == [ {'titolo': 'Pretty Woman',
'anno': 1990,
'Vivian':'Edward'},
{'titolo': 'Titanic',
'anno': 1997,
'Rose' : 'Jack'}
]
assert id(l2) != id(res2) # deve produrre NUOVA lista
assert id(orig_film) != id(res2[0]) # deve produrre NUOVO dizionario
l3 = [
{'titolo':'Jerry Maguire',
'anno':1996,
'Jerry':'Dorothy',},
{'titolo':'Superman',
'Kent':'Lois',
'anno': 1978},
{'titolo':'The Lord of the Rings',
'anno': 2001,
'Aragorn':'Arwen',},
{'Ron Weasley':'Hermione',
'titolo': 'Harry Potter and the Deathly Hallows, Part 2',
'anno': 2011}
]
assert scambiattori(l3) == [{'titolo': 'Jerry Maguire',
'anno': 1996,
'Dorothy': 'Jerry'},
{'titolo': 'Superman',
'anno': 1978,
'Lois': 'Kent'},
{'titolo': 'The Lord of the Rings',
'anno': 2001,
'Arwen': 'Aragorn'},
{'titolo': 'Harry Potter and the Deathly Hallows, Part 2',
'anno': 2011,
'Hermione': 'Ron Weasley',
}]
print()