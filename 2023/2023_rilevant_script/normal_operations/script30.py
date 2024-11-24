#La funzione calcola il totale degli importi pagati e non pagati,
# e determina il lavoro con l'importo più alto tra quelli pagati, stampando i risultati.
def totale(liste):
    lista_pagati = []
    lista_nonpagati = []
    piu_pagato = []
    tot_ricevuto = 0
    tot_daricevere = 0

    for lista in liste:
        if lista[-1] == 'pagato':
            lista_pagati.append(lista)
            tot_ricevuto += lista[1]
            piu_pagato.append(lista[1])
        else:
            lista_nonpagati.append(lista)
            tot_daricevere += lista[1]

    lavoro_migliore = None
    for el in lista_pagati:
        if el[1] == max(piu_pagato):
            lavoro_migliore = el[0]
        
    print('Totale ricevuto:', tot_ricevuto)
    print('Totale da ricevere:', tot_daricevere)
    print('Il lavoro più pagato finora è:', lavoro_migliore )

lavori = [
    ["Straordinari in fonderia", 175.13, "non pagato"],
    ["Part time gelateria", 450, "non pagato"],
    ["Rendita investimenti", 500, "pagato"],
    ["Pettinatura pitoni", 1000, "pagato"],
    ["Installazione artistica", 600, "non pagato"],
    ["Noleggio scarpe eleganti", 100, "non pagato"]
]
totale(lavori)
print()