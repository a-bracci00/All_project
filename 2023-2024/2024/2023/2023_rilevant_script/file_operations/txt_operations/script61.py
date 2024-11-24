# Qualche operazione semplice su dei file txt

with open('people-simple.txt', encoding='utf-8') as f:
    linea = f.readline()
    print(linea)

with open('people-simple.txt', encoding = 'UTF-8') as f:
    linea = f.readline()
    print(linea)
    print('type(f):', type(f))
    print()
    help(f.readline)
    help(f)

with open('people-simple.txt', encoding='UTF-8') as f:
    nome = f.readline().rstrip()
    cognome = f.readline().rstrip()
    print(nome + ' ' + cognome)
    #help(nome.lstrip)

with open('people-simple.txt', encoding='utf-8') as f:
    linea = f.readline()
    while linea != '':
        nome = linea.rstrip()
        cognome = f.readline().rstrip()
        print(nome + ' ' + cognome)
        linea = f.readline()
print()

with open('people-simple.txt', encoding='utf-8') as f:
    linea = f.readline()
    while linea != '':
        nome = linea.rstrip()
        cognome = f.readline().rstrip()
        print(nome + ' ' + cognome)
        linea = f.readline()
print()

with open('people-complex.txt', encoding='utf-8') as f:
    linea = f.readline()
    while linea != '':
        nome = linea.rstrip()[len('nome: '):]
        cognome = f.readline().rstrip()[len('cognome: '):]
        data = f.readline().rstrip()[len('data di nascita: '):]
        print(nome + ' ' + cognome + ' ' + data)
        linea = f.readline()

print()
from pprint import pprint
with open('people-complex.txt', encoding='utf-8') as f:
    tabella = []
    linea = f.readline()
    while linea != '':
        riga = []
        nome = linea.rstrip()[len('nome: '):]
        riga.append(nome)
        cognome = f.readline().rstrip()[len('cognome: '):]
        riga.append(cognome)
        nato = f.readline().rstrip()[len('data di nascita: '):]
        riga.append(nato)
        tabella.append(riga)
        linea = f.readline()
    pprint(tabella)
    #[print(x) for x in tabella]
print()

tabella = []
with open('people-complex.txt', encoding='utf-8') as f:
    linea = f.readline()

    while linea != '':
        nome = linea.rstrip()[len('nome: '):]
        cognome = f.readline().rstrip()[len('cognome: '):]
        nato = f.readline().rstrip()[len('data di nascita: '):]
        tabella.append([nome, cognome, nato])
        linea = f.readline()

pprint(tabella)
print()

with open('people-simple.txt', encoding='utf-8') as f:
    for linea in f:
        print(linea.rstrip())
print()

with open('people-simple.txt', encoding= 'utf-8') as f:
    print(f.readlines())
print()

with open('people-simple.txt', encoding='utf-8') as f:
    print([x.rstrip('\n') for x in f])
print()

with open('people-simple.txt', encoding='utf-8') as f:
    print(list(f))
    print(list(f))
print()

with open('people-complex.txt', encoding='utf-8') as f:
    tabella = [['Nome', 'Cognome', 'Data di nascita']]
    linea = f.readline()
    while linea != '':
        nome = linea.rstrip()[len('nome: '):]
        cognome = f.readline().rstrip()[len('cognome: '):]
        nato = f.readline().rstrip()[len('data di nascita: '):]
        tabella.append([nome, cognome, nato])
        linea = f.readline()
    pprint(tabella)
print()


with open('people-complex.txt', encoding='utf-8') as f:
    tab = [['Nome', 'Cognome', 'Data di nascita']]
    i = 0
    for riga in f:
        riga_divisa = riga.split(':')
        valore = riga_divisa[1][1:].rstrip('\n')
        if i % 3 == 0:
            nome = valore
        elif i % 3 == 1:
            cognome = valore
        else:
            data = valore
            tab.append([nome, cognome, data])
        i += 1
    pprint(tab)
print()

with open('people-complex.txt', encoding='utf-8') as f:
    i = 0
    tab = [['nome', 'cognome', 'data di nascita']]
    for riga in f:
        riga_divisa = riga.split(':')
        valore = riga_divisa[1][1:].rstrip()
        if i % 3 == 0:
            nome = valore
        elif i % 3 == 1:
            cognome = valore
        else:
            data = valore
            tab.append([nome, cognome, data])
        i += 1
    pprint(tab)
print()