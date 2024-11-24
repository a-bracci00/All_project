# Qualche operazione semplice su dei file csv

import csv

def cercat(file):
    with open(file, encoding='latin-1', newline='') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        nuova = []
        for riga in lettore:
            for el in riga[3].split('-'):
                if el.strip() != '':
                    nuova.append(el.strip())
        nuova1 = list(dict.fromkeys(nuova))
        return sorted(nuova1)

risultato = cercat('punti-interesse.csv')
#print('ristorante'.split('-'))
atteso = ['Affitta Camere', 'Agriturismo', 'Alimentari', 'Appartamento Vacanze',
'Autostazione', 'Banca', 'Bancomat', 'Bar', 'Bed & Breakfast', 'Biblioteca',
'Birreria', 'Bus Navetta', 'Cambiovaluta', 'Camping', 'Centro Wellness',
'Centro commerciale', 'Corrieri', 'Discoteca', 'Editoria', 'Farmacia','Funivia',
'Gelateria', 'Grande magazzino', 'Hotel', 'Istituzioni', 'Mercatini','Mercato',
'Monumento', 'Museo', 'Noleggio Sci', 'Numeri utili', 'Parcheggio','Pasticceria',
'Piscina', 'Posta', 'Prodotti tipici', 'Pub', 'Residence', 'Rifugio','Ristorante',
'Scuola Sci', 'Sede Trentino Trasporti', 'Snow Park', 'Souvenir', 'Sport','Stadio',
'Stadio del ghiaccio', 'Stazione dei Treni', 'Taxi', 'Teatro', 'Ufficio,informazioni turistiche']
#TEST
print()
for i in range(len(atteso)):
    if risultato[i] != atteso[i]:
        print("ERRORE ALL'ELEMENTO %s:" % i)
        print(' ATTESO:', atteso[i])
        print(' TROVATO:', risultato[i])
        break
print()

def cercat1(file):
    with open(file, encoding='latin-1', newline='') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        ret = set()
        for riga in lettore:
            for el in riga[3].split('-'):
                if el.strip() != '':
                    ret.add(el.strip())
        return sorted(ret)

risultato1 = cercat1('punti-interesse.csv')

atteso = ['Affitta Camere', 'Agriturismo', 'Alimentari', 'Appartamento Vacanze',
'Autostazione', 'Banca', 'Bancomat', 'Bar', 'Bed & Breakfast', 'Biblioteca',
'Birreria', 'Bus Navetta', 'Cambiovaluta', 'Camping', 'Centro Wellness',
'Centro commerciale', 'Corrieri', 'Discoteca', 'Editoria', 'Farmacia','Funivia',
'Gelateria', 'Grande magazzino', 'Hotel', 'Istituzioni', 'Mercatini','Mercato',
'Monumento', 'Museo', 'Noleggio Sci', 'Numeri utili', 'Parcheggio','Pasticceria',
'Piscina', 'Posta', 'Prodotti tipici', 'Pub', 'Residence', 'Rifugio','Ristorante',
'Scuola Sci', 'Sede Trentino Trasporti', 'Snow Park', 'Souvenir', 'Sport','Stadio',
'Stadio del ghiaccio', 'Stazione dei Treni', 'Taxi', 'Teatro', 'Ufficio,informazioni turistiche']
#TEST
print()
for i in range(len(atteso)):
    if risultato1[i] != atteso[i]:
        print("ERRORE ALL'ELEMENTO %s:" % i)
        print(' ATTESO:', atteso[i])
        print(' TROVATO:', risultato1[i])
        break
print()