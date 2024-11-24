# elimina caratteri superflui
def nobulli(stringa):
    #divido la stringa in una lista di stringhe
    stringa_divisa = stringa.split()
    #variabile con in char da mantenere
    ok = 'waka'
    #lista nuova per metterci le parole giuste
    nuova = []
    #pr ogni parola nella lista
    for parola in stringa_divisa:
        nuova2 = [] #lista per contenere le parole formate parzialmantre
        for char in parola: # per ogni char in parola
            if char in ok: # se il char sta in ok
                nuova2.append(char) # aggiungi il carattere nalla lista parziali
        nuova.append(''.join(nuova2)) # per ogni parola parziale divisa da spazi
        # la metto in una lista togliendo gli spazi, così otterò sempre una stringa
    return ' '.join(nuova) # ora ritorno la stringa formata dalle parole divise da spazi

bullo1 = "waekai waekai waekai waekai"
res1 = nobulli(bullo1)
print(res1)

def nobulli2(stringa, ok):
    #divido la stringa in una lista di stringhe
    stringa_divisa = stringa.split()
    #variabile con in char da mantenere
    #lista nuova per metterci le parole giuste
    nuova = []
    #pr ogni parola nella lista
    for parola in stringa_divisa:
        nuova2 = [] #lista per contenere le parole formate parzialmantre
        for char in parola: # per ogni char in parola
            if char in ok: # se il char sta in ok
                nuova2.append(char) # aggiungi il carattere nalla lista parziali
        nuova.append(''.join(nuova2)) # per ogni parola parziale divisa da spazi
        # la metto in una lista togliendo gli spazi, così otterò sempre una stringa
    return ' '.join(nuova) # ora ritorno la stringa formata dalle parole divise da spazi

bullo1 = "waekai waekai waekai waekai"
res1 = nobulli2(bullo1, 'waka')
print(res1)
bullo1 = "waekai waekai waekai waekai"
bullo2 = "bwaka rwaka swaka twaka zwaka mmmwatka"
bullo3 = "eweaekea zwxarkma qwoagkpa"
res1 = nobulli(bullo1) # Deve RITORNARE il verso pulito "waka waka waka waka"
print(res1)
res2 = nobulli(bullo2) # Deve RITORNARE il verso pulito "waka waka waka waka waka waka"
print(res2)
res3 = nobulli(bullo3) # Deve RITORNARE il verso pulito "waka waka waka"
print(res3)
print()