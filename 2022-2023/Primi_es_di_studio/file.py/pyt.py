
persona = {
    'nome': 'luca',
    'cognome': 'rossi',
    'eta': 25
}

operazioni = ('aggiungere', ' modificare', 'eliminare', 'terminare')


def start():
    operazione = input('Cosa vuoi fare? ')
    if operazione == operazioni[0]:
        x = input('aggiungi chiave valore separati da una virgola: ')
        aggiungi(x.split(','))
    elif operazione == operazioni[1]:
        pass
    elif operazione == operazioni[2]:
        pass
    elif operazione == operazioni[3]:
        return 'terminare'


def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)


while True:
    if start() == 'terminare':
        break
    else:
        start()
