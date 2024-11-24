# Qualche operazione semplice su dei file csv

import csv
from pprint import pprint

with open('esempio-1.csv', encoding='utf-8') as f:
    #creiamo un oggetto 'lettore' che pescherà righe dal file
    lettore = csv.reader(f, delimiter=',')
    for riga in lettore:
        print('Abbiamo appenaletto una riga!')
        print(riga) #stamperà la variabile 'riga', che è una lista di stringhe
        print('') #stampa una stringa vuota, per separare in verticale
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    for riga in lettore:
        print(riga)


with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    for riga in lettore:
        print('Abbiamo appena letto una riga!')
        print(riga)
        print('')
print()


with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    listona = []
    for riga in lettore:
        listona.append(riga)
    pprint(listona)
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    listona = []
    for riga in lettore:
        mini = []
        mini.append(riga[0])
        mini.append(int(riga[1]))
        listona.append(mini)
    pprint(listona)
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    listona = []
    for riga in lettore:
        listona.append([riga[0], int(riga[1])])
    pprint(listona)
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    print(list(lettore))
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    pprint([ x for x in lettore])
print()


import itertools
with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    pprint([[riga[0], int(riga[1]), riga[2]] for riga in itertools.islice(lettore, 1, None)])
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.DictReader(f, delimiter= ',')
    for diz in lettore:
        print(diz)
print()

with open('file-scritto.csv', 'w', newline= '') as f: 
    scrittore = csv.writer(f, delimiter=',')
    scrittore.writerow(['This', 'is', 'a header'])
    scrittore.writerow(['some', 'example', 'data'])
    scrittore.writerow(['some', 'other', 'example data'])
print()

with open('esempio-1-arricchito.csv', 'w', encoding='utf-8', newline='') as csv_da_scrivere:
    scrittore = csv.writer(csv_da_scrivere, delimiter=',')
    with open('esempio-1.csv', encoding='utf-8', newline='') as csv_da_leggere:
        lettore = csv.reader(csv_da_leggere, delimiter=',')
        for riga in lettore:
            riga.append('qualco\'altro')
            scrittore.writerow(riga)
            scrittore.writerow(riga)
            scrittore.writerow(riga)
print()
with open('esempio-1-arricchito.csv', 'r', encoding='utf-8', newline='') as f:
    lettore = csv.reader(f, delimiter=',')
    for riga in lettore:
        print(riga)
print()
