# Qualche operazione semplice su dei file csv

import csv

def terme(file):
    with open(file, encoding='utf-8') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        diz = {}
        for cliente_servizi in lettore:
            diz[cliente_servizi[0]] = 0
            for servizio in cliente_servizi[1:]:
                if int(servizio) > 0:
                    diz[cliente_servizi[0]] += 100
        return diz
print(terme('centro-benessere.csv'))

res1 = terme('centro-benessere.csv')
print(res1)
assert res1 == {'Marco': 400,
'Andrea': 300,
'Sara': 600,
'Rosa': 200,
'Cristina': 300,
'Roberto': 100}
print()