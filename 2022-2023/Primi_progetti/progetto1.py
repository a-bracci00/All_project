def programma():
    tot = []
    while True:
        a = input('>>> ')
        if a == 'finito':
            break
        elif isinstance(a, str):
            try:
                a = int(a)
            except:
                print('Invalid input, insert a number')
            if isinstance(a, int):
                tot.append(a)
    return calcoli(tot)


def calcoli(tot):
    try:
        a = sum(tot)
        b = (len(tot))
        c = sum(tot) / len(tot)
        d = max(tot)
        e = min(tot)
        print('La somma è:', a)
        print('Gli elementi sono:', b)
        print('La media è:', c)
        print('Il numero più grande è:', d)
        print('Il numero più piccolo è:', e)
    except:
        print('Errore, mancanza di numeri')


programma()
