# Qualche operazione semplice su dei file txt

from pprint import pprint

def ordina_file(nome_file):
    with open(nome_file, encoding='utf-8') as f:
        tab = []
        for riga in f:
            diz = {}
            for el in riga.split():
                #el = el.split('=')
                #diz[el[0]] = el[1]
                diz[el[:el.index('=')]] = el[el.index('=')+1:]
            
            tab.append(diz)
        return tab


print(ordina_file('quartiere1.txt'))
pprint(ordina_file('quartiere1.txt'), depth=2)
[print(x) for x in ordina_file('quartiere1.txt')]

diz = [{'a':'b',
       'c':{'a':'b'},
       'd':{'a':{'b':'c'}}}]
pprint(diz, width=2)
print()

nome_file = 'quartiere1.txt'

with open(nome_file, encoding='utf-8') as f:
    edifici = []
    for riga in f:
        diz = {}
        elementi = riga.split()
        for elemento in elementi:
            kv = elemento.split('=')
            diz[kv[0]] = kv[1]
        edifici.append(diz)

#pprint(edifici)