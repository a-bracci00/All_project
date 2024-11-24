#Comportamento Generale:
#Le funzioni permettono di estrarre informazioni specifiche 
#(nomi dei manager, nomi delle aziende, settori) e calcolare statistiche 
#(media dell'età) su una lista di manager.
#Sono inclusi anche dei test per verificare che le funzioni gestiscano correttamente 
# liste vuote e restituiscano i risultati attesi.

managers_db = [
        {
            "nome":"Alessandro",
            "cognome": "Borgoloso",
            "età": 34,
            "azienda": {
            "nome": "Aringhe Candite Spa",
            "settore":"Alimentari" }
    },
        {
            "nome":"Matilda",
            "cognome": "Delle Sòle",
            "età": 25,
            "azienda": {
            "nome": "Calzature Pitonate Srl",
            "settore":"Abbigliamento" }
    },
        {
            "nome":"Alfred",
            "cognome": "Pennyworth",
            "età": 20,
            "azienda": {
            "nome": "Batworks",
            "settore":"Abbigliamento" }
    },
        {
            "nome":"Arianna",
            "cognome": "Schei",
            "età": 37,
            "azienda": {
            "nome": "Diamantoni Unlimited",
            "settore":"Pietre preziose"
            }
    },
        {
        "nome":"Antonione",
        "cognome": "Cannavacci",
        "età": 25,
        "azienda": {
        "nome": "Aringhe Candite Spa",
        "settore":"Alimentari" }
    },
]

[print(x,'\n') for x in managers_db]

def estrai_manager(lista):
    nomi = []
    for x in lista:
        nomi.append(x['nome'])
    return nomi

print(estrai_manager(managers_db))
assert estrai_manager([]) == []
# se non trova db_impiegati, ricordati di eseguire la cella sopra che lo definisce
assert estrai_manager(managers_db) == ['Alessandro', 'Matilda', 'Alfred', 'Arianna','Antonione']

def estrai_aziende(lista):
    nomi = []
    for x in lista:
        nomi.append(x['azienda']['nome'])
    return nomi

print(estrai_aziende(managers_db))

assert estrai_aziende([]) == []
# se non trova db_impiegati, ricordati di eseguire la cella sopra che lo definisce
assert estrai_aziende(managers_db) == ["Aringhe Candite Spa","Calzature Pitonate Srl","Batworks","Diamantoni Unlimited","Aringhe Candite Spa"]

def eta_media(lista):
    eta = []
    for x in lista:
        eta.append(x['età'])
    return sum(eta) // len(eta)

print(eta_media(managers_db))

import math
assert math.isclose(eta_media(managers_db), (34 + 25 + 20 + 37 + 25) // 5)

def settori(lista):
    settori = []
    for x in lista:
        if x['azienda']['settore'] not in settori:
            settori.append(x['azienda']['settore'])
    settori.sort()
    return settori

print(settori(managers_db))
assert settori([]) == []
assert settori(managers_db) == ["Abbigliamento", "Alimentari","Pietre preziose"]
print()