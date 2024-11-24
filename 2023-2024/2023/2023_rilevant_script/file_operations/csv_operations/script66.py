# Qualche operazione semplice su dei file csv
from pprint import pprint
import csv

def selcir(lista):
    with open('strutture-comune-trento.csv', encoding='utf-8', newline='') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        nuova = []
        for riga in lettore:
            for el in lista:
                if el in riga[16].lower():
                    nuova.append([riga[3], riga[16]])
        print('Trovati', len(nuova), 'risultati')
        return nuova

pprint(selcir(['argentario', 'gardolo']))
print()

def selcir1(filtro):
    with open('strutture-comune-trento.csv', encoding='utf-8', newline='') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        ret = []
        for riga in lettore:
            nome = riga[3]
            circoscrizione = riga[16]

            tieni = False
            for el in filtro:
                if el.lower() in circoscrizione.lower():
                    tieni = True
            if tieni:
                ret.append([nome, circoscrizione])
        print('Trovati', len(ret), 'risultati')
        return ret
    
pprint(selcir1(['argentario', 'gardolo', 'RAVINA']))
print()