# Scrivi un programma che classifichi ogni messaggio di posta in base
# al giorno della settimana in cui è stato inviato. Per fare ciò, cerca le righe che
# iniziano con “From”, quindi cerca la terza parola e aggiorna il conteggio di ciascuno
# dei giorni della settimana. Alla fine del programma visualizza i contenuti del tuo
# dizionario

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File-Error:', fname)
    exit()

counts = {}
count = 0
lista_giorni = []
for riga in fhand:
    if riga.startswith('From '):
        riga = riga.strip()
        riga = riga.split()
        giorno = riga[2]
        lista_giorni.append(giorno)
        counts[giorno] = 0
fhand.close()
for i in counts:
    counts[i] = lista_giorni.count(i)

print(counts)
