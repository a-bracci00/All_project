'''
print('hello world')
# quit()
print('scemo')

x = 6
print(x)
y = x * 7
print(y)

name = input('Enter file: ')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


print(4)

print(type('Hello World'))
print(type(17))
print(type(3.2))
print(type('17'))
print(type('3.2'))
print(1, 000, 000)

message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931

print(n)
print(pi)

print(type(message))
print(type(n))
print(type(pi))

try:

    hours = int(input('inserisci ore: '))
    rate = int(input('inserisci la paga oraria: '))
    if hours > 40:
        hours1 = hours - 40
        hours1 = hours1 * 1.5
        hours1 = hours1 * rate
        pay = 40 * rate + hours1
        print(pay)
    else:
        pay = hours * rate
        print(pay)

except:
    print('inserisci un valore numerico')

try:
    score = float(input('Enter score: '))

    if score >= 0 and score <= 1.0:

        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        elif score < 0.6:
            print('F')
        else:
            print('Bad score')

    else:
        print('Bad score 2')

except:
    print('Bad score 3')



print(max('hello world'))
print(min('hello world'))
print(len('hello world'))

print(int('32'))
# print(int('hello'))

print(int(3.9999))
print(int(-2.3))

print(float(32))
print(float('3.14159'))

print(str(32))
print(str(3.14159))


import math
print(math)

radians = 0.7
height = math.sin(radians)
print(height)

degrees = 45
radians1 = degrees / 360.0 * 2 * math.pi
print(math.sin(radians1))
print(math.sqrt(2) / 2)


import random

# for i in range(10):
#    x = random.random()
#    print(x)

for i in range(5):
    x = random.randint(1, 90)
    print(x)

t = [1, 2, 3]
x = random.choices(t)
print(x)

def repeat():
    print_lyrics()
    print_lyrics()
    print('repet')


def print_lyrics():
    print('I\'m a lumberjack, and I\'m okay')
    print('I sleep all night and I work all day')

repeat()

import math


def print_twice(bruce):
    print(bruce)
    print(bruce)


print_twice('spam')
print_twice(17)
print_twice(math.pi)
print_twice('spamm' * 4)
print_twice(math.cos(math.pi))

michael = 'Eric, the half a bee'
print_twice(michael)


radians = 0.7
x = math.cos(radians)
golden = (math.sqrt(5)+1) / 2
print(golden)

print(math.sqrt(5))

result = print_twice('bing')
print(result)


def addtwo(a, b):
    added = a + b
    return added


y = addtwo(3, 5)
print(y)

hours = int(input('inserisci ore: '))
rate = int(input('inserisci la paga oraria: '))

def computepay(hours, rate):
    if hours > 40:
        hours1 = hours - 40
        hours1 = hours1 * 1.5
        hours1 = hours1 * rate
        pay = 40 * rate + hours1
        print(pay)
    else:
        pay = hours * rate
        print(pay)

computepay(hours, rate)

def computegrade(score):

    if score >= 0 and score <= 1.0:

        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        elif score < 0.6:
            print('F')
        else:
            print('Bad score')

    else:
        print('Bad score 2')

score = float(input('Enter score: '))
computegrade(score)

x = 0
x = x + 1

n = 5
while n > 0:
    print(n)
    n = n - 1
print('decollo')

# n = 10
# while True:
#    print(n, end=' ')
#    n = n - 1
# print('Done!')

while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)

largest = None
print('Before:', largest)
for itervar in [3, 41, 12,  9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print('Loop:', itervar, largest)
print('Larghest:', largest)

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12,  9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Larghest:', smallest)

# creo una funzione di nome min che accetta dei valori
def min(values):
    # creo una variabile vuota inizializzata con none
    smallest = None
    # per ogni valore nei valori immessi
    for value in values:
        # se la variabile è ancora vuota o il valore è minore
        # di quello attualmente nella variabile
        if smallest is None or value < smallest:
            # sostituisci il valore
            smallest = value
        # ritorna l'ultimo valore
        return smallest


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


programma()


fruit = 'banana'
letter = fruit[1]
print(letter)
letter2 = fruit[0]
print(letter2)

print(len(fruit))

lenght = len(fruit)
last = fruit[lenght-1]
print(last)

print(fruit[-1])
print(fruit[-2])


fruit = 'banana'
# attivare per stinga verso opposto
# fruit = fruit[::-1]
index = 0
# finche il valore di index è minore della
# lunghezza del valore stringa di fruit
while index < len(fruit):
    # immagazzina la lettera all'indice momentaneo in lettera
    letter = fruit[index]
    # stampa la lettera immagazzinata
    print(letter)
    # aggiungi 1 al valore di index ad ogni ciclo
    # così facendo aumenteremo anche l'indice
    # passando alla lettera successiva
    index = index + 1

for char in fruit:
    print(char)

s = 'Monty Python'
print(s[0:5])
print(s[6:12])

fruit = 'banana'
print(fruit[:3])
print(fruit[3:])
print(fruit[3:3])
print(fruit[:])

greeting = 'Hello, world!'
greeting[0]
new_greeting = 'J' + greeting[1:]
print(new_greeting)


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


def count1(stringa, lettera):
    count = 0
    for letter in stringa:
        if letter == lettera:
            count = count + 1
    return count


print(count1('elefante', 'e'))


print('a' in 'banana')
print('seed' in 'banana')


word = 'banana'
if word == 'banana':
    print('All might, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

stuff = 'Hello world'
print(type(stuff))
print(dir(stuff))
print(help(str.capitalize))
print(help(str.zfill))

word = 'banana'
new_word = word.upper()
print(new_word)

word2 = 'banana'
index = word2.find('a')
print(index)
index2 = word2.find('na')
print(index2)
index3 = word2.find('na', 3)
print(index3)

line = '  here we go  '
print(line.strip())

line2 = 'Have a nice day'
print(line2.startswith('Have'))
print(line2.startswith('h'))
print(line2.lower())
print(line2.lower().startswith('h'))

parola = 'banana'
print(parola.count('a'))
print(parola.count('n'))

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

camels = 42
b = '%d' % camels
print(b)
a = 'I have spotted %d camels' % camels
print(a)
c = 'In %d years I have spotted %g %s' % (3, 0.1, 'camels')
print(c)

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

stringa = 'X-DSPAM-Confidence:0.8475'

stringa1 = stringa.find(':')
stringa3 = stringa.find('5', stringa1)
stringa4 = stringa[stringa1 + 1: stringa3]
print(type(stringa4))
new_stringa = float(stringa4)
print(type(new_stringa))

fhand = open('mbox.txt')
print(fhand)
fhand.close()


stuff = 'Hello\nWorld!'
print(stuff)

stuff2 = 'X\nY'
print(stuff2)
print(len(stuff2))

fhand1 = open('mbox-short.txt')
count = 0
for line in fhand1:
    count = count + 1
print('Line Count:', count)
inp = fhand1.read()
print(len(inp))
print(inp[:20])

fhand2 = open('mbox-short.txt')
count = 0
for line in fhand2:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

fhand3 = open('mbox-short.txt')
for line in fhand3:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

fhand4 = open('mbox-short.txt')
for line in fhand4:
    line = line.strip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)

fname = input('Enter the file name: ')
fhand5 = open(fname)
count = 0
for line in fhand5:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

fname1 = input('Enter the file name: ')
try:
    fhand5 = open(fname1)
except:
    print('File cannot be opened:', fname1)
    exit()
count = 0
for line in fhand5:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in', fname1)

fout = open('output.txt', 'w')
print(fout)
line1 = 'These here\'s the wattle,\n'
fout.write(line1)
line2 = 'the emblem of our land.\n'
fout.write(line2)
fout.close()

s = '1 2\t 3\n 4'
print(s)
print(repr(s))

fname = input('inserisci file: ')
file1 = open(fname)
for riga in file1:
    riga = riga.strip()
    riga = riga.upper()
    print(riga)

def conta_media(lista):
    somma = sum(lista)
    media = somma / len(lista)
    return media


fname = input('inserisci file: ')
if fname == 'na na boo boo':
    print('hai trovato l\'Easter Egg scemo')
    exit()
try:
    file1 = open(fname)
    lista_numeri = []
    count = 0
    for riga in file1:
        count += 1
        riga = riga.strip()
        if riga.startswith('X-DSPAM-Confidence:'):
            punti = riga.find(':')+2
            fine = riga.find('\n')
            numero = float(riga[punti:fine])
            lista_numeri.append(numero)
    media = conta_media(lista_numeri)
    print('La media è di:', media)
    print('Il numero di linee è di', count)
    file1.close()
except:
    print('non esiste')

a = [10, 20, 30, 40]
b = ['crunchy frog', 'ram bladder', 'lark vomit']
c = ['spam', 2.0, 5, [10, 20]]


cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print(cheeses, numbers, empty)
print(cheeses[0])
numbers[1] = 5
print(numbers)

print('Edam' in cheeses)
print('Brie' in cheeses)

for cheese in cheeses:
    print(cheese)

for i in range(len(numbers)):
    # Questo ciclo scorre l’elenco e aggiorna ciascun elemento. len restituisce il numero
    # di elementi dell’elenco. range restituisce un elenco di indici da 0 a n−1, dove n è la
    # lunghezza dell’elenco. Ad ogni ripetizione del ciclo, i assume l’indice dell’elemento
    # successivo. L’istruzione di assegnazione nel corpo usa i per leggere il vecchio valore
    # dell’elemento e assegnare quello nuovo
    numbers[1] = numbers[1] * 2

for x in empty:
    print('This never happens.')

e = ['spam', 1, ['Brie', 'Roquefort', 'Pol le veq'], [1, 2, 3]]
print(len(e))

a = [1, 2, 3]
b = [4, 5, 6]
c = a+b
print(c)

d = [0]# * 4
d = d * 4
print(d)
e = [1, 2, 3] * 3
print(e)

t = ['a', 'b', 'c', 'd', 'e', 'f']
t1 = t[1:3]
print(t1)
t2 = t[:4]
print(t2)
t3 = t[3:]
print(t3)
t4 = t[:]
print(t4)
t5 = t.copy()
t5[1:3] = ['x', 'y']
print(t5)

t6 = ['a', 'b', 'c']
t6.append('d')
print(t6)

t7 = ['a', 'b', 'c']
t8 = ['d', 'e']
t7.extend(t8)
print(t7)

t9 = ['d', 'c', 'e', 'b', 'a']
print(t9)
t9.sort()
print(t9)

t10 = ['a', 'b', 'c']
t11 = t10.copy()
# t10.pop() = None
x = t10.pop(1)
print(t10)
print(x)
del t10[1]
print(t10)
t11.remove('b')
print(t11)

t12 = ['a', 'b', 'c', 'd', 'e', 'f']
del t12[1:5]
print(t12)

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)

numlist = list()
while (True):
    inp = input('Enter a nuember: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)


s = 'spam'
t13 = list(s)
print(t13)

s1 = 'pining for the fjords'
# divido la stringa in base agli spazi
t14 = s1.split()
print(t14)
print(t14[2])

s2 = 'spam-spam-spam-spam'
print(s2)
s2 = s2.split('-')
print(s2)

s2 = ('-').join(s2)
print(s2)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

a = 'banana'
b = 'banana'
print(a is b)
print(a == b)


c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)
print(c == d)

e = [1, 2, 3]
f = e
print(f is e)
print(f == e)

e[0] = 17
print(f)

def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t3 = t1 + [3]
print(t3)
print(t2 is t3)

def bad_delete_head(t):
    t = t[1:]

def tail(t):
    return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)

def chop(lista):
    del lista[0]
    del lista[-1]
    return lista


def middle(lista):
    lista2 = []
    chop(lista)
    lista2.append(lista)
    return lista2


lista = [1, 2, 3, 4, 5, 6]
print(middle(lista))

t = []
x = 12
print(t, x)
t.append([x])
print(t)
t = t.append(x)
print(t)

t = [1, 2, 5, 6, 3, 4]
rig = t[:]
rig.sort()
print(rig)

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    print('Debug:', words)
    if words[0] != 'From':
        continue
    print(words[2])

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 or words[0] != 'From':
        continue
    print(words[2])

fhand = open('romeo.txt')
lista = []
for riga in fhand:
    parole = riga.split()
    for parola in parole:
        lista.append(parola)
lista = list(set(lista))
lista.sort()
print(lista)

fhand = open('mbox-short.txt')
count = 0
count1 = 0
for riga in fhand:
    if riga.startswith('From'):
        count += 1
        riga = riga.split()
        print(riga[1])
    else:
        count1 += 1
        continue
print('Le righe con from sono:', count)
print('Le righe senza from sono:', count1)

lista = []
while True:
    inp = input('>>> ')
    if inp == 'done':
        break
    lista.append(int(inp))
print('max:', max(lista))
print('min:', min(lista))

eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
print(len(eng2sp))

print('one' in eng2sp)
print('uno' in eng2sp)

vals = list(eng2sp.values())
print('uno' in vals)


# inserisco il file
fname = input('Enter file name: ')
try:
    # provo il file
    fhand = open(fname)
except:
    # se genera un errore chiudi
    print('File-Error:', fname)
    exit()
# creo un dizionario
counts = {}
# creo una lista
lista_giorni = []
# per ogni riga del file
for riga in fhand:
    # se inizia per From
    if riga.startswith('From '):
        # eliminio gli spazi anteriori e posteriori
        riga = riga.strip()
        # divido la riga in parole
        riga = riga.split()
        # prendo la posizione della parola che mi interessa
        giorno = riga[2]
        # inserisco nella lista la parola ogni volta che si presenta nel file
        lista_giorni.append(giorno)
        # inserisco la parola come chiave del dizionario
        # dandogli valore 0
        counts[giorno] = 0
fhand.close()
# per ogni chiave nel dizioanrio
for i in counts:
    # prendi la chiave ed assegnagli come valore
    # il numero di volte che essa stessa appare nella lista
    counts[i] = lista_giorni.count(i)
# mostra il dizionario contenente
# i giorni ed il numero di modifiche relativo
# al giorno, settimanali o mensili
print(counts)

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File-Error')
    exit()

counts = {}
lista_email = []
for riga in fhand:
    if riga.startswith('From '):
        riga = riga.split()
        email = riga[1]
        lista_email.append(email)
        counts[email] = 0
fhand.close()

for i in counts:
    counts[i] = lista_email.count(i)
# chiave con valore più alto
valore_max = max(counts.items())
print(counts)
print(valore_max)


fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File-Error')
    exit()

counts = {}
lista_domini = []
for riga in fhand:
    if riga.startswith('From '):
        riga = riga.strip()
        # trova la chiocciola
        chiocciola = riga.find('@')
        # trova uno spazio da dopo chiocciola
        spazio = riga.find(' ', chiocciola)
        # il dominio si trova tra la chiocciola e lo spazio
        dominio = riga[chiocciola:spazio]
        lista_domini.append(dominio)
        counts[dominio] = 0
fhand.close()

for i in counts:
    counts[i] = lista_domini.count(i)
print(counts)

t = 'a', 'b', 'c', 'd', 'e'
print(type(t))
t1 = ('a', 'b', 'c', 'd', 'e')
print(type(t1))
t2 = ('a',)
print(type(t2))
t3 = ('a')
print(type(t3))
t4 = tuple()
print(type(t4))
t5 = ()
print(type(t5))
t6 = tuple('lupins')
print(type(t6), t6)
print(t6[2])
print(t6[1:4])

t = ('A',) + t[1:]
print(t)

print((0, 1, 2) < (0, 3, 4))
print((0, 1, 2000000) < (0, 3, 4))

# creo una variabile che contiene una frase
txt = 'but soft what light in yonder window breaks'
# divido la frasein parole in base agli spazi
words = txt.split()
# creo una lista t
t = list()
# per ogni elemento in words
for word in words:
    # aggiungi la lunghezza dell'elemento e la parola
    t.append((len(word), word))
# riordina la lista dalla parola più lunga a quella più corta
t.sort(reverse=True)
# creo una lista
res = list()
# per ogni lunghezza e parola in t aggiungila a res
for lenght, word in t:
    res.append(word)

print(res)

m = ['have', 'fun']
x, y = m
print(x)
print(y)
print(m)

m = ['have', 'fun']
x = m[0]
y = m[1]
print(x)
print(y)
print(m)

m = ['have', 'fun']
(x, y) = m
print(x)
print(y)

# variabile che contiene un email
addr = 'monty@python.org'
# creo due variabili che conterranno
# rispettivamente il nome ed il dominio
# sepeandole tramite la chiocciola
uname, domain = addr.split('@')
print(uname)
print(domain)

d = {'a': 10, 'b': 1, 'c': 22}
t = list(d.items())
t.sort()
print(t)

for key, vals in list(d.items()):
    print(vals, key)
t.sort(reverse=True)
print(t)

import string
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:10]:
    print(key, val)

last = 'john'
first = 'pier'
number = 98658
directory = {}
directory[last, first] = number
for last, first in directory:
    print(first, last, directory[last, first])

fhand = open('mbox-short.txt')
counts = {}
lista_ore = []

for riga in fhand:
    if riga.startswith('From '):
        riga = riga.split()
        ora = riga[5]
        ora = ora[:2]
        lista_ore.append(ora)
        counts[ora] = 0
for i in counts:
    counts[i] = lista_ore.count(i)
lst = list(counts.items())
lst.sort()
for key, vals in lst:
    print(key, vals)

import string
fhand = open('romeo.txt')
counts = {}
numeri = str([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
lista_lettere = []
for riga in fhand:
    # trasfromo tutti i segni di punteggiatura in spazi
    riga = riga.translate(str.maketrans('', '', string.punctuation))
    riga = riga.strip()
    riga = riga.lower()
    for i in riga:
        if i == ' ':
            pass
        if i in numeri:
            pass
        else:
            lista_lettere.append(i)
            counts[i] = 0
for i in counts:
    counts[i] = lista_lettere.count(i)
lst = list(counts.items())
lst.sort()

for key, vals in lst:
    print(key, vals)

#cerca e stampa le righe che contengono from
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #trova le righe in cui è contenuto from
    #il segno '^' specifica che deve iniziare con quella stringa
    if re.search('^From:', line):
        print(line)

#cerca e stampa le righe che contengono
#una stringa che inizia per f seguita da 2 caratteri e da un m finale
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #se nella linea c'è f..m stampala
    if re.search('^F..m', line):
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    # cerca nella riga se c'è from + uno o più caratteri
    # tipo chiocciola
    if re.search('^From:.+@', line):
        print(line)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0:
        print(x)

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)

# modalità iterativa
# print(help())
#utile senza internet
import re
print(dir(re))
print(help(re.search))

import re
search = input('Enter a regular expression: ')
count = 0
with open('mbox.txt') as fhand:
    for line in fhand:
        line = line.strip()
        if re.search(search, line):
            count += 1
print('mbox.txt had', count, 'lines the matched', search)

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
'''
