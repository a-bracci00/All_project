# ordina mecha in base al valore

def bestmecha(diz):
    # nuova ha tanti elementi none quanti sono gli elementi di diz
    nuova = [None] * len(diz)
    #print(nuova)
    #per ogni chiave in diz
    for chiave in diz:
        #sostituisco il nome alla posizione n con la chiave del dizionario
        nuova[diz[chiave]-1] = chiave
    return nuova

# printo i risultati e controllo se la funzione è corretta tramite gli assert
print(bestmecha( {'Patlabor' : 2, 'Evangelion' : 1} ))
assert bestmecha( {'Macross' : 1} ) == ['Macross']
assert bestmecha( {'Patlabor' : 2,
'Evangelion' : 1} ) == ['Evangelion','Patlabor']
assert bestmecha( {'Gundam' : 3,
'Evangelion': 2,
'Patlabor' : 4,
'Macross' : 1} ) == ['Macross', 'Evangelion', 'Gundam', 'Patlabor']