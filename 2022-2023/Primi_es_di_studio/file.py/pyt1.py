'''
import dbm
import os

db = dbm.open('didascalie', 'c')
db['cleese.png'] = 'foto di cleese'
db.close()
os.remove('didascalie.dat')
os.remove('didascalie.dir')
os.remove('didascalie.bak')

import pickle
t = [1, 2, 3]
s = pickle.dumps(t)
t1 = pickle.loads(s)
print(s)
print(t1)

# pipe UNIX
import os

cmd = 'ls -1'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(stat)
# return none se tutto apposto

# check sum UNIX
nomefile = 'book.tex'
cmd = 'md5sum' + nomefile
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)
#return none se tutto apposto

import wc
print(wc.contarighe('wc.py'))

s = '1 2\t 3\n 4'
print(repr(s))

with open('test.txt') as f:
    a = f.read()
    print(repr(a))

def sed(stringa, sec_stringa, file1, file2):
    with open(file1) as f1:
        with open(file2, 'w') as f2:
            a = f1.read()
            b = f2.write(a)


print(sed('ao', 'ao1', 'test.txt', 'nuovo'))

import os
import ntpath

#funzione walk
def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.
    dirname: string name of directory
    """
    #creo una lista di nome names
    names = []
    #se la cartella python è nella cartella di input
    if '__pycache__' in dirname:
        #ritorna la lista nome
        return names
    #per ogni nome nella lista della cartella
    for name in os.listdir(dirname):
        #unisci il nome della cartella più il nome del file
        path = os.path.join(dirname, name)
        #se il path finale è un file
        if os.path.isfile(path):
            #aggiungilo alla lista names
            names.append(path)
        #altrimenti
        else:
            #estendi la lista
            names.extend(walk(path))
    #ritorna la lista
    return names

#funzione compara checksum
def compute_checksum(filename):
    """Computes the MD5 checksum of the contents of a file.
    filename: string
    """
    # Note: installing md5sha1sum is required
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    """Computes the difference between the contents of two files.
    name1, name2: string filenames
    """
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)


def pipe(cmd):
    """Runs a command in a subprocess.
    cmd: string Unix command
    Returns (res, stat), the output of the subprocess and the exit status.
    """
    # Note: os.popen is deprecated
    # now, which means we are supposed to stop using it and start using
    # the subprocess module.  But for simple cases, I find
    # subprocess more complicated than necessary.  So I am going
    # to keep using os.popen until they take it away.

    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    """Computes checksums for all files with the given suffix.
    dirname: string name of directory to search
    suffix: string suffix to match
    Returns: map from checksum to list of files with that checksum
    """
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    """Checks whether any in a list of files differs from the others.
    names: list of string filenames
    """
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    """Checks for duplicate files.
    Reports any files with the same checksum and checks whether they
    are, in fact, identical.
    d: map from checksum to list of files with that checksum
    """
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')


if __name__ == '__main__':
    d = compute_checksums(dirname='.', suffix='.py')
    print_duplicates(d)


import math


class Punto:
    """rappresenta un punto in un piano"""


nuovo = Punto()
nuovo.x = 3.0
nuovo.y = 4.0

print('(%d, %f)' % (nuovo.x, nuovo.y))
distanza = math.sqrt(nuovo.x**2 + nuovo.y**2)
print(distanza)


def stampa_punto(p):
    print('(%d, %f)' % (nuovo.x, nuovo.y))


stampa_punto('d')



import copy


class Punto():
    """"""


nuovo = Punto()
nuovo.x = 3.0
nuovo.y = 4.0


class Rettangolo:
    """Rappresenta un rettangolo.

    attributi: larghezza, altezza, angolo.
    """


box = Rettangolo()
box.larghezza = 100.0
box.altezza = 200.0
box.angolo = Punto()
box.angolo.x = 0.0
box.angolo.y = 0.0


def trova_centro(rett):
    p = Punto()
    p.x = rett.angolo.x + rett.larghezza/2
    p.y = rett.angolo.y + rett.altezza/2
    return p


def stampa_punto(p):
    print('(%d, %f)' % (nuovo.x, nuovo.y))


centro = trova_centro(box)
stampa_punto(centro)

box.larghezza = box.larghezza+50
box.altezza = box.altezza+100


def accresci_rettangolo(rett, dlargh, dalt):
    rett.larghezza += dlargh
    rett.altezza += dalt


def sposta_rettangolo(rett, x, y):
    rett.angolo.y += y
    rett.angolo.x += x


accresci_rettangolo(box, 50, 100)
sposta_rettangolo(box, 20, 40)

p1 = Punto()
p1.x = 3.0
p1.y = 4.0

p2 = copy.copy(p1)

print(p1 is p2)
print(p1 == p2)

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.angolo is box.angolo)

print(isinstance(box3, Punto))

print(hasattr(p1, 'x'))
print(hasattr(p1, 'y'))
try:
    x=p1.x
except AttributeError:
    x=0

class Punto:
    """"""


p = Punto()


def cerchio(centro, raggio):
    pass
centro=Punto()
centro=(150,100)
cerchio(centro, 75)


class Tempo:
    """Rappresenta un'ora del giorno

    attributi: ora, minuto, secondo
    """


tempo = Tempo()
tempo.ora = 11
tempo.minuto = 59
tempo.secondo = 30


def stampa_tempo(oggetto):
    print(oggetto.ora, ':', oggetto.minuto, ':', oggetto.secondo)


o = 0
stampa_tempo(tempo)
t1 = Tempo()
t2 = Tempo()


def viene_dopo(t1, t2):
    pass


def somma_tempo2(t1, t2):
    somma = Tempo()
    somma.ora = t1.ora + t2.ora
    somma.minuto = t1.minuto + t2.minuto
    somma.secondo = t1.secondo + t2.secondo
    return somma


inizio = Tempo()
inizio.ora = 9
inizio.minuto = 45
inizio.secondo = 0

durata = Tempo()
durata.ora = 1
durata.minuto = 35
durata.secondo = 0


def somma_tempo1(t1, t2):
    somma = Tempo()
    somma.ora = t1.ora + t2.ora
    somma.minuto = t1.minuto + t2.minuto
    somma.secondo = t1.secondo + t2.secondo

    if somma.secondo >= 60:
        somma.secondo -= 60
        somma.minuto += 1

    if somma.minuto >= 60:
        somma.minuto -= 60
        somma.ora += 1
    return somma


def incremento(tempo, secondi):
    tempo.secondo += secondi

    if tempo.secondo >= 60:
        tempo.secondo -= 60
        tempo.minuto += 1

    if tempo.minuto >= 60:
        tempo.minuto -= 60
        tempo.ora += 1


def tempo_in_int(tempo):
    minuti = tempo.ora * 60 + tempo.minuto
    secondi = minuti * 60 + tempo.minuto
    return secondi


def int_in_tempo(secondi):
    tempo = Tempo()
    minuti, tempo.secondo = divmod(secondi, 60)
    tempo.ora, tempo.minuto = divmod(minuti, 60)
    return tempo


def somma_tempo3(t1, t2):
    secondi = tempo_in_int(t1) + tempo_in_int(t2)
    return int_in_tempo(secondi)


def tempo_valido(tempo):
    if tempo.ora < 0 or tempo.minuto < 0 or tempo.secondo < 0:
        return False
    if tempo.minuto >= 60 or tempo.secondo >= 60:
        return False
    return True


def somma_tempo4(t1, t2):
    if not tempo_valido(t1) or not tempo_valido(t2):
        raise ValueError
        print('oggetto tempo non valido in somma_tempo')
    secondi = tempo_in_int(t1) + tempo_in_int(t2)
    return int_in_tempo(secondi)

def somma_tempo(t1,t2):
    assert tempo_valido(t1) or not tempo_valido(t2)
    secondi = tempo_in_int(t1) + tempo_in_int(t2)
    return int_in_tempo(secondi)

fine = somma_tempo(inizio, durata)
stampa_tempo(fine)


class Tempo():
    """ora del giorno"""

    def stampa_tempo(self):
        print('%.2d:%.2d:%.2d' % (self.ora, self.minuto, self.secondo))

    def tempo_in_int(self):
        minuti = self.ora * 60 + self.minuto
        secondi = minuti * 60 + self.minuto
        return secondi

    def int_in_tempo(self):
        tempo = Tempo()
        minuti, tempo.secondo = divmod(secondi, 60)
        tempo.ora, tempo.minuto = divmod(minuti, 60)
        return tempo

    def incremento(self, secondi):
        secondi += self.tempo_in_int()
        return int_in_tempo(secondi)

    def viene_dopo(self, other):
        return self.tempo_in_int() > other.tempo_in_int()
    
inizio = Tempo()
inizio.ora = 9
inizio.minuto = 45
inizio.secondo = 00


Tempo.stampa_tempo(inizio)
inizio.stampa_tempo()
fine = inizio.incremento(1337)
fine.stampa_tempo()
fine.viene_dopo(inizio)



class Tempo():

    def __init__(self, ora=0, minuto=0, secondo=0):
        self.ora = ora
        self.minuto = minuto
        self.secondo = secondo

    def stampa_tempo(self):
        print('%.2d:%.2d:%.2d' % (self.ora, self.minuto, self.secondo))


tempo = Tempo()
tempo.stampa_tempo()


from collections import namedtuple
from inspect import signature
from collections import defaultdict
import collections as coll


class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def stampa_x_y(self):
        print(str(self.x) + ':' + str(self.y))


punto = Punto()
punto.stampa_x_y()


class Tempo():

    def __init__(self, ora=0, minuto=0, secondo=0):
        self.ora = ora
        self.minuto = minuto
        self.secondo = secondo

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.ora, self.minuto, self.secondo)

    def __add__(self, ini, dur):
        self.ini = ini
        self.dur = dur
        return self.ini + self.dur


tempo = Tempo(9, 45)
print(tempo)


class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ':' + str(self.y)


punto = Punto()
print(punto)

inizio = Tempo(9, 45)
durata = Tempo(1, 35)
print(inizio, durata)


class Tempo():
    def __add__(self, other):
        if isinstance(other, Tempo):
            return self.somma_tempo(other)
        else:
            return self.incremento(other)

    def somma_tempo(self, other):
        secondi = self.tempo_in_int() + other.tempo_in_int()
        return int_in_tempo(secondi)

    def incremento(self, secondi):
        secondi += self.tempo_in_int()
        return int_in_tempo(secondi)

    def __radd__(self, other):
        return self.__add__(other)


def istogramma(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c]+1
    return d


s = ['spam', 'uovo', 'spam', 'spam', 'bacon', 'spam']
print(istogramma(s))


class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def stampa_attributi(oggetto):
    for attr in vars(oggetto):
        print(attr, getattr(oggetto, attr))


p = Punto(3, 4)

print(vars(p))
stampa_attributi(p)


class Canguro():
    def __init__(self, contenuto_tasca):
        contenuto_tasca = []
        self.contenuto_tasca = contenuto_tasca

    def instasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)

    def __str__(self):
        return str(self.contenuto_tasca)


can = Canguro('can')
guro = Canguro('guro')
can.instasca('wallet')
can.instasca('car key')
can.instasca(guro)
print(can)


class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)


class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        # The problem is the default value for contents.
        # Default values get evaluated ONCE, when the function
        # is defined; they don't get evaluated again when the
        # function is called.

        # In this case that means that when __init__ is defined,
        # [] gets evaluated and contents gets a reference to
        # an empty list.

        # After that, every Kangaroo that gets the default
        # value gets a reference to THE SAME list.  If any
        # Kangaroo modifies this shared list, they all see
        # the change.

        # The next version of __init__ shows an idiomatic way
        # to avoid this problem.
        self.name = name
        self.pouch_contents = contents

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        # In this version, the default value is None.  When
        # __init__ runs, it checks the value of contents and,
        # if necessary, creates a new empty list.  That way,
        # every Kangaroo that gets the default value gets a
        # reference to a different list.

        # As a general rule, you should avoid using a mutable
        # object as a default value, unless you really know
        # what you are doing.
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)


class Carta():
    # Rappresenta una carta da gioco standard

    def __init__(self, seme=0, valore=2):
        self.seme = seme
        self.valore = valore

    nomi_semi = ['fiori', 'Quadri', 'Cuori', 'Picche']
    nomi_valori = [None, 'Asso', '2', '3', '4', '5', '6', '7',
                   '8', '9', '10', 'Fante', 'Regina', 'Re']

    def __str__(self):
        return '%s di %s' % (Carta.nomi_valori[self.valore],
                             Carta.nomi_semi[self.seme])

    def __lt__(self, other):
        # controlla semi
        if self.seme < other.seme:
            return True
        if self.seme > other.seme:
            return False

        # controlla semi uguali
        return self.valore < other.valore

    def __lt__2(self, other):
        t1 = self.seme, self.valore
        t2 = other.seme, other.valore
        return t1 < t2 < t2


regina_di_quadri = Carta(1, 12)
print(regina_di_quadri)
carta1 = Carta(2, 5)
print(carta1)


if x > 0:
    y = math.log(x)
else:
    y = float('nan')

y = math.log(x) if x > 0 else float('nan')


def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n-1)


def fattoriale1(n):
    return 1 if n == 0 else n * fattoriale1(n-1)


def __init__(self, nome, contenuti=None):
    self.nome = nome
    if contenuti == None:
        contenuti = []
        self.contenuto_tasca = contenuti


def __init__(self, nome, contenuti=None):
    self.nome = nome
    self.contenuto_tasca = [] if contenuti == None else contenuti


def tutte_maiuscole(t):
    res = []
    for s in t:
        res.append(s.capitalize)
    return res


def tutte_maiuscole1(t):
    return [s.capitalize() for s in t]


def solo_maiuscole(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


def solo_maiuscole1(t):
    return [s for s in t if s.isupper()]


g = (x**2 for x in range(5))
d = next(g)
for val in g:
    print(val)


f = min(x**2 for x in range(5))
print(f)

print(any([False, False, True]))
print(any(lettera == 't' for lettera in 'monty'))


def evita(parola, vietate):
    return not any(lettera in vietate for lettera in parola)


def sottrai(d1, d2):
    res = dict()
    for chiave in d1:
        if chiave not in d2:
            res[chiave] = None
    return res


def sottra1(d1, d2):
    return set(d1) - set(d2)


def ha_duplicati(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def ha_duplicati1(t):
    return len(set(t)) < len(t)


def usa_solo(parola, valide):
    for lettera in parola:
        if lettera not in valide:
            return False
    return True


def usa_solo1(parola, valide):
    return set(parola) <= set(valide)


conta = coll.Counter('parrot')
print(conta)
print(conta['d'])


def anagramma(parola1, parola2):
    return coll.Counter(parola1) == coll.Counter(parola2)


for valore, frequenza in count.most_common(3):
    print(valore, frequenza)


d = defaultdict(list)
t = d['nuova chiave']
print(t)


def tutti_anagrammi(nomefile):
    d = {}
    for riga in open(nomefile):
        parola = riga.strip().lower()
        t = signature(parola)
        if t not in d:
            d[t] = [parola]
        else:
            d[t].append(parola)
    return d


def tutti_anagrammi1(nomefile):
    d = {}
    for riga in open(nomefile):
        parola = riga.strip().lower()
        t = signature(parola)
        d.setdefault(t, []).append(parola)
    return d


def tutti_anagrammi2(nomefile):
    d = defaultdict(list)
    for riga in open(nomefile):
        parola = riga.strip().lower()
        t = signature(parola)
        d[t].append(parola)
    return d


class Punto1():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)


p1 = Punto1(2, 3)
Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(1, 2)
print(p)
print(p1)

print(p.x, p.y)
print(p[0], p[1])


class IperPunto(Punto):
    # aggiungere qui altri metodi
    pass


class MappaLineare:

    def __init__(self):
        self.items = []

    def add(self, k, v):
        self.items.append((k, v))

    def get(self, k):
        for chiave, valore in self.items:
            if chiave == k:
                return valore
        raise KeyError


class MappaMigliore:

    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(MappaLineare())

    def trova_mappa(self, k):
        indice = hash(k) % len(self.maps)
        return self.maps[indice]

    def add(self, k, v):
        m = self.trova_mappa(k)
        m.add(k, v)

    def get(self, k):
        m = self.trova_mappa(k)
        return m.get(k)


class MappaHash:

    def __init__(self):
        self.maps = MappaMigliore(2)
        self.num = 0

    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):
        if self.num == len(self.maps.maps):
            self.ridimensiona()

        self.maps.add(k, v)
        self.num += 1

    def ridimensiona(self):
        new_maps = MappaMigliore(self.num * 2)

        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k, v)

        self.maps = new_maps
'''
