#La funzione precario somma i guadagni ricevuti e quelli da ricevere, 
# determinando anche il lavoro più pagato finora. Stampa questi dati al termine

lavori = [
{"nome": "Pettinatura pitoni", "valore": 1000, "status": "pagato"},
{"nome": "Straordinari in fonderia", "valore": 175.13, "status": "non pagato"},
{"nome": "Part time gelateria", "valore": 450, "status": "non pagato"},
{"nome": "Rendita investimenti", "valore": 500, "status": "pagato"},
{"nome": "Installazione artistica", "valore": 600, "status": "non pagato"},
{"nome": "Noleggio scarpe eleganti", "valore": 100, "status": "non pagato"}
]

def precario(lista):
    lavori_pagati = []
    miglior_lavoro = None
    guadagni_ricevuti = 0
    guadagni_da_ricevere = 0
    confronto = 0
    for lavoro in lista:
        if lavoro['status'] == 'pagato':
            lavori_pagati.append(lavoro)
            guadagni_ricevuti += lavoro['valore']
        else:
            guadagni_da_ricevere += lavoro['valore']
        if lavoro['valore'] > confronto:
            confronto = lavoro['valore']
            miglior_lavoro = lavoro['nome']
    print('1.   Totale ricevuto:', guadagni_ricevuti)
    print('     Totale da ricevere:', guadagni_da_ricevere)
    print('2.   Il lavoro più pagato finora è:', miglior_lavoro)

precario(lavori)
print()