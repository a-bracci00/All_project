# Qualche operazione semplice su dei file csv

import itertools

with open('impianti-bifuni.csv', encoding='utf-8', newline='') as f:
    lettore = csv.reader(f, delimiter=',')
    prima_riga = f.readline().strip().split(',')
    for x in prima_riga:
        print(x + ':', prima_riga.index(x))
    print()
    for riga in lettore:
        print('Abbiamo appena letto una riga!')
        print(riga)
        print('')
print()

with open('impianti-bifuni.csv', 'r', encoding='utf-8', newline='') as f:
    prima = f.readline()
    lista_dopp = []
    #next(f)
    for riga in f:
        lista_dopp.append(riga.strip().split(',')[2])

    lista = list(dict.fromkeys(lista_dopp))
    print(lista)
print()

with open('impianti-bifuni.csv', 'r', encoding='utf-8', newline='') as f:
    lettore = csv.reader(f, delimiter=',')
    comuni = set()
    for riga in itertools.islice(lettore, 1, None):
        comuni.add(riga[2])
    print(comuni)
print()

with open('impianti-bifuni.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    comuni = set()
    for riga in lettore:
        comuni.add(riga[2])
    print(comuni)
print()

with open('impianti-bifuni.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    diz = {}
    next(lettore)
    for riga in lettore:
        if riga[-1] in diz:
            diz[riga[-1]] += 1
        else:
            diz[riga[-1]] = 1
    print(diz)
print()

with open('impianti-bifuni.csv', encoding='utf-8', newline = '') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    for riga in lettore:
        if 'si (frane)' in riga[11]:
            riga[11] = 'si + frane'
        print(riga)

with open('impianti-bifuni.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    for riga in lettore:
        if '#' in riga[11]:
            riga[11] = None
        print(riga)

import csv
with open('impianti-bifuni.csv', encoding='utf-8', newline='') as f:
    lettore = csv.reader(f, delimiter=',')
    with open('impianti-bifuni-sistemato.csv', 'w', encoding='utf-8', newline='')  as f1:
        scrittore = csv.writer(f1, delimiter=',')
        for riga in lettore:
            if '#' in riga[11]:
                riga[11] = 'Non disponibile'
            elif riga[11] == 'si (frane)':
                riga[11] = 'si + frane'
            scrittore.writerow(riga)
print()
print('scrittura completata')
print()