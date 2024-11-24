'''contenuto='oggi è una bella giornata'
file1= open ('esempio1.txt', 'w')
file1.write(contenuto)
file1.close()
nuova_stringa=('\npython è una bomba')
file1 = open ('esempio1.txt','a')
file1.write(nuova_stringa)
file1.close()
'''
import string

def elabora_file(nomefile):
    #dizionario di nome isto
    isto = dict()
    #fp contiene il file in lettura
    fp = open(nomefile)
    #per ogni riga nel file
    for riga in fp:
        #richiama la funzione
        elabora_riga(riga,isto)
    #ritorna il dizionario
    return isto

def elabora_riga(riga,isto):
    #in gni riga sostituisco '-' con '' 
    riga=riga.replace('-','')
    #per ogni parola riga divisa da spazi
    for parola in riga.split():
        #elimina dalla parola eventali segni di punteggiatura e gli spazi vuoti
        parola= parola.strip(string.punctuation + string.whitespace)
        #facciamola diventare tutta minuscola
        parola= parola.lower()
        #immagazino nella chiave la parola assegnandogli +1 al valore
        isto[parola]= isto.get(parola,0)+1

def parole_totali(isto):
    #ritorno la somma tutti i valori in isto
    return sum(isto.values())

def parole_diverse(isto):
    #ritorno la lunghezza totale del dizionario isto
    return len(isto)

isto = elabora_file('words.txt')
print('Numero totale di parole:', parole_totali(isto))
print('Numero di parole diverse:', parole_diverse(isto))

