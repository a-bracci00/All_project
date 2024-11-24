# Qualche operazione semplice su dei file csv

import csv

province = {
'TN': 'Trento',
'PI': 'Pisa',
'MC': 'Macerata',
'CO': 'Como',
'ME': 'Messina',
'MI': 'Milano'
}

from pprint import pprint 
with open('personaggi-storici-trentino.csv', encoding='latin-1') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    lista = []
    for riga in lettore:
        if 'sconosciuto' in riga[6]:
            riga[6] = ''
        elif 'sconosiuto' in riga[4]:
            riga[4] = ''
        elif len(riga[6].split()) > 1 and riga[6].split()[1] in province:
            riga[6] = riga[6].split()[0] + ' (' + province[riga[6].split()[1]] + ')'
        else:
            pass
        lista.append([riga[3], riga[6], riga[4]])
    [print(' '.join(x)) for x in lista]
print()

secoli = {
'I': 0,
'II':100,
'III':200,
'IV':300,
'V':400,
'VI':500,
'VII':600,
'VIII':700,
'IX':800,
'X':900,
'XI':1000,
'XII':1100,
'XIII':1200,
'XIV': 1300,
'XV':1400,
'XVI':1500,
'XVII':1600,
'XVIII':1700,
'XIX':1800,
'XIX':1900,
'XX':2000,
}

with open('output-personaggi.csv', 'w', encoding='utf-8', newline='') as f:
    f.write('nome, luogo di nascita, data di nascita, secolo \n')
    scrittore = csv.writer(f, delimiter=',')
    #i = 0
    for x in lista:
        if x[-1].isdigit():
            scrittore.writerow(x + [int(x[-1]) // 100 * 100])
        elif '/' in x[-1]:
            numero = int(x[-1].split('/')[-1]) // 100 * 100
            scrittore.writerow(x + [numero])
        elif x[-1] == '':
            scrittore.writerow(x)
        elif x[-1].isdigit() == False:
            if x[-1].isdigit():
                numero1 = int(x[-1].split()[-1]) // 100 * 100
                scrittore.writerow(x + [numero1])
            elif x[-1].split('\'')[-1].isdigit():
                numero3 = int(x[-1].split('\'')[-1]) // 100 * 100
                scrittore.writerow(x + [numero3])
            elif '\'' in x[-1]:
                if len(x[-1].split('\'')[-1]) <=9:
                    numero4 = x[-1].split('\'')[-1][:2]
                    scrittore.writerow(x + [secoli[numero4]])
                else:
                    if 'XI' in x[-1]:
                        numero5 = x[-1].split('\'')[-1][len('xi e il '):len('xi e il ')+3]
                        scrittore.writerow(x + [secoli[numero5]])
                    else:
                        scrittore.writerow(x + [x[-1].split()[-1]])
            else:
                if x[-1].split()[-1].isdigit():
                    numero6 = int(x[-1].split()[-1]) // 100 * 100
                    scrittore.writerow(x + [numero6])
                elif len(x[-1].split()) > 1:
                    if '(' in x[-1]:
                        scrittore.writerow(x + [secoli[x[-1].split()[-2][1:]]])
                    else:
                        scrittore.writerow(x + [secoli[x[-1][:2]]])
                else:
                    scrittore.writerow(x + [int(x[-1].split('.')[1]) // 100 * 100])
        else:
            print('problema con', x)
        #i += 1
    #print(i)