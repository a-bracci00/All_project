# controlla formattazione date
def raggi(calendario):
    nuova = []
    nuova3 = []
    for data in calendario:
        data = data.split('/')
        nuova.append(data)
    for lista in nuova:
        nuova2 = []
        for i in lista:
            i = int(i)
            nuova2.append(i)
        nuova3.append(nuova2)
    for lista in nuova3:
        try:
            if lista[0] and lista[1] and lista[2]:
                if lista[0] <= 31:
                    if lista[1] <= 12:
                        if 2020 <= lista[2] <= 2023:
                            print('Parsing', '/'.join(map(str, lista)))
                            print('     Riconosciuto!', tuple(lista))
                        else:
                            print('Parsing', '/'.join(map(str, lista)))
                            print('     ERRORE: anno non valido')
                    else:
                        print('Parsing', '/'.join(map(str, lista)))
                        print('     ERRORE: mese non valido')
                else:
                    print('Parsing', '/'.join(map(str, lista)))
                    print('     ERRORE: giorno non valido')
            else:
                print('Parsing', '/'.join(map(str, lista)))
                try:
                    raise Exception()#('ERRORE: formato non valido')
                except:
                    print('     ERRORE: formato non valido')
        except:
            print('Parsing', '/'.join(map(str, lista)))
            print('     ERRORE: formato non valido')

calendario = [
'07/11/2021',
'30/04/2020',
'02/100/2022',
'082/11/2023',
'25/01',
'29/05/2029',
]
raggi(calendario)
print()