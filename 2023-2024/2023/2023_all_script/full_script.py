'''
animali = ['cani','gatti','scoiattoli','alci']

for animale in animali:
    print('Nella lista ci sono:')
    print(animale)

for indice in range(3):
    print(indice)

print('\t')
for indice in range(6):
    print(indice)

for indice in range(3):
    print('nella lista ci sono:')
    print(animali[indice])

def mia_stampa(x,y):
    print('Ora stamperemo la somma di due numeri')
    print('La somma è %s' % (x + y))

mia_stampa(3,5)

def mia_somma(x,y):
    s = x + y
    return s

print(mia_somma(3,5))

def media(x,y):
    return (x+y) / 2

print(media(3,5))

def iniziab(x):
    if x[0] == 'b':
        print(x, 'inizia con b')
    else:
        print('riprova')
iniziab('dfg')

print(len('ciao'))

mia_variabile = len
print(mia_variabile('ciao'))
mia_variabile = sorted
print(mia_variabile('ciao'))
mia_f = lambda x : x + 1
print(mia_f (5))
mia_somma = lambda x,y: x + y
print(mia_somma(3,5))

media = lambda x,y : x + y / 2
print(media(8,2))

animali = ['cani','gatti','scoiattoli','alci']

nuova_lista = []
for animale in animali:
    nuova_lista.append(animale.capitalize())
print(nuova_lista)

m = []
for animale in animali:
    m.append(animale.upper())
print(m)

lista = [animale.capitalize() for animale in animali]
print(lista)

lista2 = [animale.upper() for animale in animali]
print(lista2)

lista3 = [animale.upper() for animale in animali if len(animale) == 4]
print(lista3)

f = lambda animale : animale.capitalize()
print(list(map(f, animali)))

nuova_lista1 = list(map(lambda animale: animale.capitalize(), animali))
print(nuova_lista1)

numeri = [3,5,2,7]
c = lambda numero : numero * 2
print(list(map(c, numeri)))

numerii = [3,5,2,7]
print(list(map(lambda numero : numero * 2, numerii)))

animali = ['cane','gatto','pellicano','scoiattolo','aquila']
anni = [12,14,30,6,25]

coppie = []
for i in range (len(animali)):
    coppie.append([animali[i], anni[i]])
print(coppie)

coppie2 = []
for i in range(len(animali)):
    if anni[i] > 13:
        coppie2.append([animali[i], anni[i]])
print(coppie2)

coppie3 = []
for i in range (len(animali)):
    if anni[i] > 10 and anni[i] < 27:
        coppie3.append([animali[i], anni[i]])
print(coppie3)

lettere = ['a','b','c']
numeri = [1,2,3]

d=list(zip(lettere,numeri))

b = [list(c) for c in zip(lettere, numeri)]
print(b)

ab = (('ciao', 'soft', 'python'))
print(ab)
abc = list(ab)
print(abc)
print(d)

animali = ['cane','gatto','pellicano','scoiattolo','aquila']
anni = [12,14,30,6,25]

print(list(map(list,zip(animali, anni))))

print([list(c) for c in zip(animali, anni) if c[1] > 13])

dizio = {}
for c in range(len(animali)):
    dizio[animali[c]] = anni[c]
print(dizio)

print(dict(zip(animali,anni)))

vendite = [
    ['pomodori', 'Santini', 5],
    ['pomodori', 'Cirio', 1],
    ['pomodori', 'Mutti', 2],
    ['cereali', 'kelloggs', 3],
    ['cereali', 'Choco Pops', 8],
    ['cioccolata', 'Novi', 9],
    ['cioccolata', 'Milka', 4],
]
print(vendite)

d = {}
for vendita in vendite:
    if vendita[0] in d:
        d[vendita[0]] += vendita[2]
    else:
        d[vendita[0]] = vendita[2]
print(d)

x = 3
y = 5
print(x+y)

castelli = 7
dirigibili = 4
print('Ho costruito', castelli,'castelli per aria')
print('Ho', dirigibili, 'dirigibili a vapore')
print('Ne voglio parcheggiare uno per castello') 
print('perciò ne acquisterò altri', castelli-dirigibili, 'al mercato del vapore')

pirati = 10
ognuno_vuole = 5
barili = 4
capienza_barile = 20

print('nella taverna ci sono', pirati, 'pirati, ognuno vuole', ognuno_vuole, 'boccali di grog')
print('Abbiamo', barili, 'barili di grog pieni')
print('da ogni barile possiamo prendere', capienza_barile, 'boccali')

boccali_avanzati = barili*capienza_barile - pirati*ognuno_vuole

print('stasera i pirati berranno', pirati * ognuno_vuole, 'boccali, ne avanzano', boccali_avanzati, 'per domani')

diamanti = 4
print(type(diamanti))
print(type(4))
print(type(4.0))
print(type('Ciao'))

fiori = 4
fiori += 1
print(fiori)

fiori = 5
fiori -= 1
print(fiori)

fiori = 6
fiori = fiori - 2
print(fiori)

fiori = 3
fiori *= 3
print(fiori)

fiori = 8
fiori //= 2
print(fiori)

a = 5
b = 3
a = 3
b = 5
print(a)
print(b)

a = 5
b = 3
temp = a
a = b
b = temp
print(a,b)

a = 4
b = 7
c = 9

t = b
b = a
a = c
c = t
print(a,b,c)

diamanti = 4
print(diamanti)
diamanti +=2
print(diamanti)
diamanti='quattro'
print(diamanti)

a = 10; print('Tanti comandi!'); b = a + 1;
print(a,b)

x,y = 5,7
print(x)
print(y)

a,b = 5,3
print(a,b)

a,b = b,a
print(a,b)

giorni = 4
ore = 13
minuti = 52

print('in totale mancano', giorni *24*60 + ore*60 + minuti, 'minuti')

tot_minuti = 5000
print('Mancano:')
print(' ', tot_minuti // (60*24), 'giorni')
print(' ', (tot_minuti % (60*24)) // 60, 'ore')
print(' ', (tot_minuti % (60*24)) % 60, 'minuti')

print(min(7,3))
print(max(2,6))
print(min(2,9,-3,5))
print(max(2,9,-3,5))

p1,p2,p3,p4,p5 = 7,2,4,6,3

print('In un viaggio possiamo trasportare', max(min(p1,p2), min(p1,p3,p4), min(p1,p5)), 'tonnellate')

b_mat, b_sch, b_sto, r_mat, rsch, r_sto = 23,54,12,13,37,24
b = max(b_mat, b_sch, b_sto) + 1
c = max(r_mat, rsch, r_sto) + 1
d = min(b,c)
print('il primo divano verrà prodotto dopo', d, 'ore')

b_mat, b_sch, b_sto, r_mat, rsch, r_sto = 81,37,32,54,36,91
b = max(b_mat, b_sch, b_sto) + 1
c = max(r_mat, rsch, r_sto) + 1
d = min(b,c)
print('il primo divano verrà prodotto dopo', d, 'ore')

x = True
print(type(x))
y = False
print(type(y))

print(x or (not x))
print((not x) and (not y))
print(x and (y or y))
print(x and (not y))
print((not x) or y)
print(y or not (y and x))
print(x and(not x) or not(y))
print((not (not x)) and not (x and y))
print(x and (x or (not(x) or not(not(x or not(x))))))

x=True
y=False
print(x or y, not(not x and not y))
print(x and y, not(not x or not y))

print((not x) or y, not(not (not x)) or not(not(y)))
print((not x) and (not y), not(not(x)) and not(not(y)))
print((not x) and (not(x or y)), not(not(x)) and not(x))

print(bool(1))
print(bool(0))
print(bool(72))
print(bool(-5))
print(int(True))
print(int(False))

print(bool(True))
print(bool(False))
print(bool(2+4))
print(bool(4-3-1))
print(int(4-3-1))
print(True + True)
print(True + False)
print(True - True)
print(True * True)

print(True and 5)
print(5 and True)
print(False and 5)
print(5 and False)

print(False or 5)
print(7 or False)
print(3 or True)

print(0 and True)
print(1 and 0)
print(True and -1)
print(0 and False)
print(0 or False)
print(0 or 1)
print(False or -6)
print(0 or True)

print(True and 1/0)
print(1/0 and 1/0)
print(False or 1/0)
print(True or 1/0)
print(1/0 or True)
print(1/0 or 1/0)
print(True or (1/0 and True))
print((not False) or not 1/0)
print(True and 1/0 and True)
print(True and (not True) and 1/0)

print(3 == 3)
print(3 == 5)
a,b = 3,5
print(a == a)
print(a == b)
print(a == b - 2)
print(3 != 5)
print(3 != 3)
print(3 < 5)
print(5 > 5)
print(5 <= 5)
print(8 > 5)
print(8 > 8)
print(8 >= 8)

x = 5 > 3
print(x)

x, y = 7, 5
z = x > 0 and y > 0
print(z)

x = 3 == 4
print(x)
x = False or True
print(x)
x = False and True
print(x)
x,y = 9,10
z = x < y and x == 3**2
print(z)
a,b = 7,6
a = b
x = a >= b + 1
print(x)

x = 3^2
print(x)
y = 9
print(x == y)

d = 100

x,y = 0,0
z = x < d/2 and y > d/2
print(z)
x,y = 25,25
z = x < d/2 and y > d/2
print(z)
x,y = 75,75
z = x < d/2 and y > d/2
print(z)
x,y = 75,25
z = x < d/2 and y > d/2
print(z)
x,y = 25,75
z = x < d/2 and y > d/2
print(z)
x,y = 100,100
z = x < d/2 and y > d/2
print(z)
x,y = 10,90
z = x < d/2 and y > d/2
print(z)
x,y = 60,60
z = x < d/2 and y > d/2
print(z)
x,y = 25,25
z = (x < d/2 and y < d/2) or (x > d/2 and y > d/2)
print(z)

a = 3.14
print(type(a))
b = 75e1
print(b)
c,d,e,f,g,h = 75e2, 75e3, 75e123, 75e0, 75e-1, 753-2
print(c,d,e,f,g,h)

r = 9.15
pi = 3.1415926536
area = pi*r**2
print(area)

import math
r = 50

x,y = 35,20
dist = math.sqrt(x**2 + y**2)
di = dist < r
print(di)

x = 0.000003
a = -math.sqrt(x+3) / ((x+2)**3 / math.log(x))
print(a)

b = ((1**4) / (1+2)) + ((2**4) / (2+2)) + ((3**4) / (3+2))
print(b)

c,d,e,f= 8.7,6.3,2.49,2.51
print(math.floor(c))
print(int(c))
print(math.ceil(d))
print(round(e))
print(round(e))
print('\nNuova riga\n')
print(math.floor(2.3))
print(math.floor(-2.3))
print(round(3.49))
print(round(3.51))
print(round(-3.49))
print(round(-3.51))
print(math.ceil(8.1))
print(math.ceil(-8.1))
x = 10
print(math.floor(math.ceil(x)) == math.ceil(math.floor(x)))
print(math.floor(x) == -math.ceil(-x))

import math
kiwi = 2.4
soia = 4.8
shampoo = 3.1
misurino = 0.0
mixer = 0
bicchiere = 0.0

print('Versao nel misurino', kiwi, 'dl di kiwi, tolgo eccesso\
 fino a tenere', math.floor(kiwi), 'dl')
mixer += int(kiwi)

print('Travaso nel mixer, adesso contiene', mixer, 'dl')
print('Verso nel misurino', soia,'dl di soia, tolgo eccesso\
 fino a tenere', math.floor(soia),'dl')
mixer += int(soia)

print('Travaso nel mixer, adesso contiene', mixer, 'dl')
print('Verso nel misurino', shampoo, 'dl di shampoo, tolgo eccesso\
 fino a tenere', int(shampoo),'dl')
mixer += int(shampoo)
print('Travaso nel mixer, adesso contiene', mixer, 'dl')
bicchiere = mixer/2
print('Travaso metà della miscela (', bicchiere, 'dl ) nel bicchiere')
print('Rabbocco il bicchiere fini al decilitro intero superiore,\
 adesso contiene:', math.ceil(bicchiere), 'dl')

import math
x = -5.51
print(abs(math.ceil(x)) + round(x)**2)

import math
print(4.1)
print(format(4.1,'.55f'))
print(format(7.9 - 3.8, '.55f'))

print(7.9-3.8 == 4.1)
print(math.isclose(7.9 - 3.8, 4.1))
print(math.isclose(7.9 - 3.8, 4.1, abs_tol=0.000001))
print('a)', math.sqrt(3)**2 == 3.0)
print('b)', abs(math.sqrt(3)**2 - 3.0) < 0.0000001)
print('c)', math.isclose(math.sqrt(3)**2, 3.0, abs_tol=0.0000001))

import math
a = 11.0
b = 3.3

x1 = math.sqrt(b/a)
x2 = -math.sqrt(b/a)

print(a, '* x**2-',b,'=0 per x1=', format(x1,'.20f'))
print(a, '* x**2-',b,'=0 per x2=', format(x2,'.20f'))

print(format(x1,'.20f'), 'è una soluzione?', math.isclose(a*(x1**2) -b,0, abs_tol=0.00001))
print(format(x2, '.20f'), 'èuna soluzione?', math.isclose(a*((x2)**2) - b,0, abs_tol=0.00001))

import math
b1,b2,b3,b4,b5 = 'TroppiLike', 'ErMejo United', 'Perditempo Inc', 'Vanità 3.0', 'TronistiPerCaso'
f1,f2,f3,f4,f5 = 0.25, 0.3, 0.1, 0.05, 0.3

mx = max(f1,f2,f3,f4,f5)
print(b1, 'è il più frequente?', math.isclose(f1,mx), '(',f1*100.0, '%)')
print(b2, 'è il più frequente?', math.isclose(f2,mx), '(',f2*100.0, '%)')
print(b3, 'è il più frequente?', math.isclose(f3,mx), '(',f3*100.0, '%)')
print(b4, 'è il più frequente?', math.isclose(f4,mx), '(',f4*100.0, '%)')
print(b5, 'è il più frequente?', math.isclose(f5,mx), '(',f5*100.0, '%)')

from decimal import Decimal
print(Decimal('4.1'))
print(Decimal(4.1))

print(Decimal('7.9') - Decimal('3.8'))
print(Decimal('4.1') == Decimal('7.9') - Decimal('3.8'))
print(Decimal('2').sqrt())
print(Decimal('2').sqrt()**Decimal('2'))

a = 'la mia prima stringa, in doppie virgolette'
print(a)
b = 'la mia seconda stringa, in virgolette singole'
print(b)
c='la mia terza stringa\
 in triple doppie virgolette\
 quindi la posso mettere\
 su più righe'
print(c)
d = 'la mia quarta stringa,\
 in triplici apici\
 può pure essere messa\
 su più linee'
print(d)

print('\'ciao\'')
x = 'ciao'
print(x)
y = 'ciao'
print(y)
z = ''
print(z)
x = 'ciao'
y = 'Python'
z = 3
print(x,y,z)
print(len('ciao'))
print(len(''))
c = "len('ciao')"
print(len(c))
print(len(((((('ciao')))))))
print(len('a\tb'))
print('a\tb')
print('ciao\nmondo')
print('La nebbia a gl\'irti colli\npiovigginando sale,\ne sotto il maestrale\n\
urla e biancheggia il mar;')

print('ciao\tmondo')
print('ciao\tmondo\tcon\ttante\ttab')

print(len('ab\ncd'))
print(len('ab\tcd'))

print('Questa\tè\nuna\n\nsfida\tapparentemente\tsemplice')

print('At\tte\nn\ttis\nsimame\n\nn\nte')

stringa = "Così metto \'apici\' e \"doppie virgolette\" nelle stringhe"
print(stringa)
print("Non c'è problema")

print('Così è "se vi pare"')
print('Questo "genio" delle stringhe vuole /\\\\/ fregarmi \\//\\ con esercizi atroci O_o')

print('\u272A')
print('♥')
print('\u2665')

x = 'ciao'
y = x + 'mondo'
print(y)

x = 'ciao'
y = 'mondo'
x = y
print(x)
print(y)

x = 'ciao'
x = x
print(x)

x = 'ciao'
x = x + 'mondo'
print(x)

z = 'Questo'
w = 'era'
x = 'un problema'
y = 'era'
s = ' '

s = z + s + w + s + x
print(s)

print(type('ciao mondo'))

print('Il carattere 5 rappresenta la cifra cinque, il carattere 3 rappresenta la cifra tre')
print('La sequenza di caratteri 7583 rappresenta il numero settemila cinquecento ottanta tre')

x = '254'
y = 254
print(type(x), type(y))
print(x , y)

z = int(x) + 3
print(z)
print(int('4312'))
print(str(5))

x = 3
y = 1.6
s = 'questa settimana ho fatto jogging' + str(x) + 'volte correndo a una media di' + str(y) + 'km/h'
print(s)

x = 3
y = 'Ho saltato %s volte' % x
print(y)

x = 3
y = 5
z = 'Ho saltato %s volte e fatto %s flessioni' % (x,y)
print(z)

premio = 'Migliore Atleta della Valle'
z = 'Ha saltato %s volte, fatto %s flessioni e vinto il premio \'%s\'' %(x,y,premio)
print(z)

auto1 = 'Jaguar'
auto2 = 'Ferrari'
lun1 = len(auto1)
lun2 = len(auto2)
s = 'Comprerò %s Jaguar e %s Ferrari perchè tengo i dindi' % (lun1, lun2)
print(s)

auto1 = 'Jaguar'
auto2 = 'Ferrari'
s = 'Comprerò %s %s e %s %s perchè tengo i dindi' % (len(auto1), auto1, len(auto2), auto2)
print(s)

print('ciao'[0])
print('ciao'[1])
a = 'ciao'
b = 0
for i in a:
    print(a[b])
    b +=1
    print(b)

x = 'panca'
print(x[0])
print(x[2])
print(type(x[0]))

x = 'say'
y = 'hi!'
print(x[0] + y[0] + x[1] + y[1] + x[2] + y[2])

print('ciao'[-1])
print('ciao'[-2])
print('ciao'[-3])
print('ciao'[-4])
x = 'ciao'
print('ciao'[-len('ciao')])
print('ciao'[len('ciao')-1])

print('ciao' + 'ciao'[len('ciao')-1])
print(('ciao'[0])[0])

x = 'ciao'
print(x)
x = x[0] + x[1] + 'b' + x[3]
print(x)

x = 'ciao'
print(x)
y = x
print(y)
x = y[0] + y[1] + 'b' + y[3]
print(x)

x = 'mercantile'
print(x[3:8])

print('              x è', x)
print('La slice x[3:8] è', x[3:8])
print('              x è', x)

x = '12345'
print(x[3:4])

x = 'abcde'
print(x[3:4], x[3])

x = 'garalampog'
print(x[3:7])

x = 'ifE\te\nfav  lkD lkwe'
print(x[12:14])

print('sedia'[:3])
print('sedia'[:4])
print('sedia'[:5])
print('sedia'[0:6])

print(''[0:len('')])
print(''[0:100])

print('traghetto'[:3])
print('traghetto'[3:])
print('traghetto'[:])

x = 'mistero'
print(x[1:]+x[:-1])
x = 'corale'
print(x[1:]+x[:-1])

print('foresta'[3:0])

print('foresta'[3:-1])

print('foresta'[3:-2])
print('foresta'[3:-3])

print('foresta'[3:-4])

x = 'javarnanda'
print(x[:3] + x [-3:])
x = 'bang'
print(x[:3] + x[-3:])

s = 'il tavolo bianco è al centro della stanza'
print(s)
s = s[0:3] + 'divano' + s[9:]
print(s)

s = 'il tavolo bianco è al centro della stanza'
s = s.split()
print(s)
s[1] = 'divano'
s = ' '.join(s)
print(s)

s = 'la corsa all\'oro è iniziata.'
print(s)
cosa = 'atomo'
verbo = 'finita'
print(s.find('\''))
s = s[:13] + cosa + s[16:19] + verbo + s[27:]
print(s)

print('tra' in 'Cantando per le strade')
print('ca' in 'cantando per le strade')
print('Ca' in 'Cantando per le strade')

x = 'cad'
y = 'ra'
z = 'abracadabra'
print((x in z) and (y in z))

x = 'zam'
y = 'ra'
z = 'abracadabra'
print((x in z) and (y in z))

x = 'tti'
y = 'patti chiari amicizia lunga'
z = 'tutto chiaro?'
print((x in y) or (x in z))

x = 'zio'
y = 'patti chiari amicizia lunga'
z = 'tutto chiaro?'
print((x in y) or (x in z))

x = 'chiaro'
y = 'patti chiari amicizia lunga'
z = 'tutto chiaro?'
print((x in y) or (x in z))

print('gatto' == 'gatto')
print('gatto' == 'cane')
print('gatto' == 'GATTO')
print('\n')
print('gatto' != 'gatto')
print('gatto' != 'cane')
print('gatto' != 'GATTO')
print('\n')
print(not 'gatto' == 'gatto')
print(not 'gatto' == 'cane')
print(not 'gatto' == 'GATTO')

parola = 'rockettaro'
parola1 = 'massima'
parola2 = 'stima'
parola3 = 'baobab'
print(parola[:2] == parola[-2:])
print(parola1[:2] == parola1[-2:])
print(parola2[:2] == parola2[-2:])
print(parola3[:2] == parola3[-2:])

print('a' < 'g')
print('m' > 'c')
print('a' < 'z')
print('a' > '♥')
print(ord('a'))
print(ord('b'))
print(ord('z'))
print('\n')
print(chr(97))
print(ord('A'), chr(65))
print(ord('Z'), chr(90))

print(chr(91), chr(92), chr(93), chr(94), chr(95), chr(96),chr(90))
print('a' < 'b')
print('g' >= 'm')

car = 'G'
print('A:', ord('A'), 'Z:', ord('Z'))
print(car+':', ord(car))
print(ord(car) >= ord('A') and ord(car) <= ord('Z'))

print(ord('♥'))
print('a' > '♥')
print(ord('a') > ord('♥'))

print('mario' > 'luigi')
print('mario' > 'wario')
print('Mario' > 'wario')
print('Wario' < 'mario')

print('troll' < 'trolley')
print('trolley' < 'trolls')

i1 = 'gm'
i2 = 'cp'
res = (i1[0] >= i2[0] and i1[1] <= i2[1] and 'è contenuto in') \
    or (i1[0] < i2[0] and i1[1] > i2[1] and 'contiene') \
    or (i1[0] >= i2[0] and i1[0] <= i2[0] and 'si sovrappone parzialmente a') \
    or (i1[1] >= i2[0] and i1 <= i2[1] and 'si sovrappone parzialmente a') \
    or (i1[0] > i2[1] and 'è dopo')
print(i1, res, i2)

i1 = 'mr'
i2 = 'pt'
res = (i1[0] >= i2[0] and i1[1] <= i2[1] and 'è contenuto in') \
    or (i1[0] < i2[0] and i1[1] > i2[1] and 'contiene') \
    or (i1[0] >= i2[0] and i1[0] <= i2[0] and 'si sovrappone parzialmente a') \
    or (i1[1] >= i2[0] and i1 <= i2[1] and 'si sovrappone parzialmente a') \
    or (i1[0] > i2[1] and 'è dopo')
print(i1, res, i2)

i1 = 'ac'
i2 = 'bd'
res = (i1[0] >= i2[0] and i1[1] <= i2[1] and 'è contenuto in') \
    or (i1[0] < i2[0] and i1[1] > i2[1] and 'contiene') \
    or (i1[0] >= i2[0] and i1[0] <= i2[0] and 'si sovrappone parzialmente a') \
    or (i1[1] >= i2[0] and i1 <= i2[1] and 'si sovrappone parzialmente a') \
    or (i1[0] > i2[1] and 'è dopo')
print(i1, res, i2)

i1 = 'fm'
i2 = 'su'
res = (i1[0] >= i2[0] and i1[1] <= i2[1] and 'è contenuto in') \
    or (i1[0] < i2[0] and i1[1] > i2[1] and 'contiene') \
    or (i1[0] >= i2[0] and i1[0] <= i2[0] and 'si sovrappone parzialmente a') \
    or (i1[1] >= i2[0] and i1 <= i2[1] and 'si sovrappone parzialmente a') \
    or (i1[0] > i2[1] and 'è dopo')
print(i1, res, i2)

i1 = 'xz'
i2 = 'pq'
res = (i1[0] >= i2[0] and i1[1] <= i2[1] and 'è contenuto in') \
    or (i1[0] < i2[0] and i1[1] > i2[1] and 'contiene') \
    or (i1[0] >= i2[0] and i1[0] <= i2[0] and 'si sovrappone parzialmente a') \
    or (i1[1] >= i2[0] and i1 <= i2[1] and 'si sovrappone parzialmente a') \
    or (i1[0] > i2[1] and 'è dopo')
print(i1, res, i2)

i1 = 'dh'
i2 = 'dh'
res = (i1[0] >= i2[0] and i1[1] <= i2[1] and 'è contenuto in') \
    or (i1[0] < i2[0] and i1[1] > i2[1] and 'contiene') \
    or (i1[0] >= i2[0] and i1[0] <= i2[0] and 'si sovrappone parzialmente a') \
    or (i1[1] >= i2[0] and i1 <= i2[1] and 'si sovrappone parzialmente a') \
    or (i1[0] > i2[1] and 'è dopo')
print(i1, res, i2)

i1 = 'bw'
i2 = 'dq'
res = (i1[0] >= i2[0] and i1[1] <= i2[1] and 'è contenuto in') \
    or (i1[0] < i2[0] and i1[1] > i2[1] and 'contiene') \
    or (i1[0] >= i2[0] and i1[0] <= i2[0] and 'si sovrappone parzialmente a') \
    or (i1[1] >= i2[0] and i1 <= i2[1] and 'si sovrappone parzialmente a') \
    or (i1[1] < i2[0] and 'è prima di') \
    or (i1[0] > i2[1] and 'è dopo')
print(i1, res, i2)

libro = 'ciclare all\'aperto'

scaffale = "|a 7|b 5|c 5|d 8|e 2|f 0|g 4|h 8|i 7|j 1|k 6|l 0|m 5|n 0|o 3|p 7|q 2 \
 |r 2|s 4|t 6|u 1|v 3|w 3|x 5|y 7|z 6|"

c = libro[0]

i = ord(c) - ord('a')
n = int(scaffale[(i*4)+3:((i)*4)+4])

scaffale = scaffale[:i*4] + '|' + c + ' ' + str(n-1) + scaffale[(i+1)*4:]
print(scaffale)

a = 'birra' 
print(a * 4)
beviamo = 'birra'
print(beviamo * 4, 'birra')

frase = 'Il numero 7'
sillaba = 'za'
print((sillaba + ' ') * int(frase[-1]))

frase = 'Dammi il 5'
sillaba = 'az'
print((sillaba + ' ') * int(frase[-1]))

print('ciao'.upper())
a = 'ciao'
a = a.upper()
print(a)
print('Sono importante'.upper())

x = 'cammina'
print(x, x.upper(), x, x.upper())
print(x, x.upper(), x, x.upper())

help('ciao'.strip)

stringa = 'ciAo MonDo'
altra_stringa = stringa.lower()
print(stringa, altra_stringa)

x = 'ASCENSORE'
k = len(x)//2
x = x[:k] +x[k:k+1].lower() + x[k+1:]
print(x)

x = 'LAMPADA'
k = len(x)//2
x = x[:k] +x[k:k+1].lower() + x[k+1:]
print(x)

print('ciao'.capitalize())
print('mondo'.capitalize())

x = 'capra'
y = 'capra'.capitalize()
print(x,y)

x = 'vosTRA'
y = 'ecCeLLeNza'
print(x.capitalize() + ' ' + y.capitalize())

x = 'sUa'
y = 'maEStà'
print(x.capitalize(), y.capitalize())

print('il cane abbaia nella strada'.startswith('il cane'))
print('il cane abbaia nella strada'.startswith('abbaia'))
print('il cane abbaia nella strada'.startswith('IL CANE'))
print('IL CANE ABBAIA SULLA STRADA'.startswith('IL CANE'))

x = 'per Giove'
y = 'per Zeus'
z = 'per'
print(x.startswith(z) and y.startswith(z))

x = 'per Giove'
y = 'per Zeus'
z = 'da'
print(x.startswith(z) and y.startswith(z))

x = 'da Giove'
y = 'per Zeus'
z = 'per'
print(x.startswith(z) and y.startswith(z))

print('I miei più cari saluti'.endswith('cari saluti'))
print('I miei più cari saluti'.endswith('cari'))
print('I miei più cari saluti'.endswith('SALUTI'))
print('I MIEI PIU\' CARI SALUTI'.endswith('SALUTI'))

marito, moglie = 'Antonio Snobbonis', 'Carolina Snobbonis'
print(moglie.endswith(marito[8:]), marito[8:])

marito, moglie = 'Camillo De Spaparanzi', 'Matilda Degli Agi'
print(moglie.endswith(marito[8:]))

print('BarrieraCorallina'.isalpha())
print('Route 666'.isalpha())
print('Barriera Corallina'.isalpha())
print('!'.isalpha())
print('♥'.isalpha())
print(''.isalpha())
print('a'.isalpha())

nome, cognome = 'K001', 'H4ck3r'
print(not(nome.isalpha() and cognome.isalpha()))

nome, cognome = 'Cool', 'H4ck3r'
print(not(nome.isalpha() and cognome.isalpha()))

nome, cognome = 'Romina', 'Rossi'
print(not(nome.isalpha() and cognome.isalpha()))

nome, cognome = 'Peppo', 'Sbirilli'
print(not(nome.isalpha() and cognome.isalpha()))

nome, cognome = 'K001', 'Sbirilli'
print(not(nome.isalpha() and cognome.isalpha()))

print('391'.isdigit())
print('400'.isdigit())
print('3.14'.isdigit())
print('4e29'.isdigit())

telefono = '+392574856985'

numero = telefono[3:]
segno_più = telefono.startswith('+')
prefisso_nazionale = telefono[1:].startswith('39')
lungo10 = len(numero) == 10
tutte_cifre = numero.isdigit()
print('Controllo delle variabili:', segno_più, prefisso_nazionale, lungo10, tutte_cifre)
print('E\'un numero di telefono?', segno_più and prefisso_nazionale and lungo10 and tutte_cifre)

print('q'.isupper())
print('q'.islower())
print('Q'.islower())
print('Q'.isupper())
print('GREAT'.isupper())
print('NotSoGREAT'.isupper())

print('TROPPO\nGIUSTO'.isupper())
print('troppo\ngiusto'.islower())
print('à'.islower())
print('à'.isupper())
print('À'.islower())
print('À'.isupper())

avv1, avv2, avv3, avv4 = 'gimli', 'savorlim', 'glazouc', 'hondouni'
a1 = avv1.isupper()
a2 = avv2.isupper()
a3 = avv3.isupper()
a4 = avv4.isupper()

print(not(a1 == a2 == a3 == a4))

avv1, avv2, avv3, avv4 = 'gfts', 'ERTF', 'fdgty', 'ghghh'
a1 = avv1.isupper()
a2 = avv2.isupper()
a3 = avv3.isupper()
a4 = avv4.isupper()

print(not(a1 == a2 == a3 == a4))
print(not(True == False == True == False))

a = 'pollllolo'
print(a.find('o',5))

x = ' \t\n\n\t carpe diem \t  '
print(x, len(x))
x = x.strip()
print(x)

x = 'salsa'.strip('s')
print(x)

x = 'caustic'.strip('aci')
print(x)

print('bouquet  '.strip('b'))

print('\t bouquet  '.strip('b'))

print('   attento! \t'.strip(' '))

print('\ttumultuoso\n'.strip())

print(' a b c '.strip())

riga = '       \t     \n Mario Rossi 0323-454345  \t  \t'
giusto = ' - ' + riga.strip() + '.'
print(giusto)

x = '\n \t la strada \t '
print(x.lstrip(), len(x))
y=x.lstrip()
print(y,len(y))

x = '\n \t il faro \t'
print(x, len(x))
y = x.rstrip()
print(y,len(y))

carattere = 'b'
punteggiatura = '!?.;,'
s = ' \t\n...bbbbbBAD TO THE BONE\n'
s = s.strip()
#s = s.strip(carattere + punteggiatura).strip()
s = s.strip(punteggiatura)
s = s.strip(carattere)
print(s)

print('raggi astrali'.count('a'))
print('raggi astrali'.count('A'))
print('raggi astrli'.count('st'))

print('raggi astrali'.count('a', 4))
print('raggi astrali'.count('a',4,9))

s = '$$$$€€€€€!!'
p1 = 0
d1 = s.count(s[p1])
p2 = p1 + d1
d2 = s.count(s[p2])
p3 = p2 + d2
d3 = s.count(s[p3])

print(s[p1], s[p2], s[p3])
print(d1, d2, d3)

s = 'IIIMMMMMMQQQ'
p1 = 0
d1 = s.count(s[p1])
p2 = p1 + d1
d2 = s.count(s[p2])
p3 = p2 + d2
d3 = s.count(s[p3])

print(s[p1], s[p2], s[p3])
print(d1, d2, d3)

s = 'HAL'
p1 = 0
d1 = s.count(s[p1])
p2 = p1 + d1
d2 = s.count(s[p2])
p3 = p2 + d2
d3 = s.count(s[p3])

print(s[p1], s[p2], s[p3])
print(d1, d2, d3)

# find inizia da sinistra
# rfind inizia da destra
print('bingo bongo bong'.find('ong'))
print('bingo bongo bong'.find('bang'))
print('bingo bongo bong'.find('Bong'))
print('bingo bongo bong'.find('ong',10))
print('bingo bongo bong'.find('ong', 4, 9))

porto = 'The Mad Monkey     |  The Jolly Rasta   |   The Sea Cucumber   |LeChuck\'sGhost Ship|'
larghezza = 21
molo = 2
nave = 'The Jolly Rasta'
print('La Jolly Rasta è attraccata al molo', molo,'?\n')
print(porto,'\n')
bordo1 = porto.find('|')
bordo2 = porto.find('|',20)
molo2 = porto[bordo1+3:bordo2-3]
print('Molo 2:', molo2)
ishere = molo2 == nave
print(ishere,'\n')

porto = "The Mad Monkey | Grog Ship Grog Ship| The Jolly Rasta | The␣Sea Cucumber "
larghezza = 21
molo = 2
nave = 'The Jolly Rasta'
print('La Jolly Rasta è attraccata al molo', molo,'?\n')
print(porto,'\n')
bordo1 = porto.find('|')
bordo2 = porto.find('|',20)
molo2 = porto[bordo1+3:bordo2-3]
print('Molo 2:', molo2)
ishere = molo2 == nave
print(ishere)

porto = " The Jolly Rasta | Grog Ship       | The Jolly Rasta | The␣Jolly Rasta "
larghezza = 21
molo = 2
nave = 'The Jolly Rasta'
print('La Jolly Rasta è attraccata al molo', molo,'?\n')
print(porto,'\n')
bordo1 = porto.find('|')
bordo2 = porto.find('|',20)
molo2 = porto[bordo1+3:bordo2-3]
print('Molo 2:', molo2)
ishere = molo2 == nave
print(ishere,'\n')

s = 'bb bbbbb aaaa'
p1 = s.find(' ')
print(p1)
banane = len(s[:p1])*100
p2 = s.find(' ', p1 + 1)
banane += len(s[p1+1:p2])*10
banane += len(s[p2+1:])*1
print('Le banane sono', banane)
print(type(banane))

print('il treno percorre'.replace('re','RO'))
print('alberello bello'.replace('llo','llini'))
print('parlare e brindare'.replace('ARE','iamo'))
print('PARLIAMO E BRINDIAMO'.replace('ARE','iamo'))
print('PARLARE E BRINDARE'.replace('ARE','iamo'))

x = 'sulla panca'
print(x)
x = x.replace('panca', 'panca la capra crepa')
print(x)
y = x.replace('panca la capra crepa','panca la capra crepa')
print(y)
print('apollo fece una palla di pelle di pollo'.replace('ll','Zz',3))
print('$£mangia il ricco£$'.replace('$','').replace('£',''))
print('$£mangia il ricco£$'.strip('£').strip('$'))

borgo = 'ppp|mm|vvvvvv|mm|sss|mm|dd|mm|sssss|mm|vvvvvv|mm|pppppp'
borgo1 = borgo.replace('mm','MM')
print(borgo1)

i = borgo.find('|mm|')
borgo = borgo[:i] + '|MM|' + borgo[i+4:]
i = borgo.rfind('|mm|')
borgo = borgo[:i] + '|MM|' + borgo[i+4:]
print(borgo)

borgo = 'ppp|mm|vv|mm|v|s|mm|dddddddddddddddddddddddd|mm|ss|mm|vvvvv|mm|pppp'
print(borgo,'\n')
d = borgo.find('d')
print('Membri della famiglia reale:', d)
dpos_sx = borgo.find('d')
c_sx = borgo.count('p', 0, dpos_sx) + borgo.count('v', 0, dpos_sx) + borgo.count('s', 0, dpos_sx)
print('             di sinistra:', c_sx)
dpos_dx = borgo.rfind('d')
c_dx = borgo.count('p', dpos_dx) + borgo.count('v',dpos_dx) + borgo.count('s', dpos_dx)
print('             di destra:', c_dx)

borgo = borgo[:dpos_sx] + 'D'*c_sx + '􀀀'*(d-c_sx+c_dx) + 'D'*c_dx + borgo[dpos_dx+1:]

print()
print('Dopo la lotta fratricida, il nuovo borgo è:')
print()
print(borgo)

borgo = 'ppp|mm|vvvvvv|mm|sss|mm|dd|mm|sssss|mm|vvvvvv|mm|pppppp'
dpos = borgo.find('d')
borgo = borgo[:dpos].replace('p','P').replace('v','V').replace('s','S')+borgo[dpos:]
print(borgo)

borgo = 'ppp|mm|vvvvvv|mm|sss|mm|dd|mm|sssss|mm|vvvvvv|mm|pppppp'
dpos = borgo.rfind('d')
borgo = borgo[:dpos]+borgo[dpos:].replace('p','P').replace('v','V').replace('s','S')
print(borgo)

print('________________------_______________')
print('////\t\tStoria\t\t '+'\\\\\\\\')
print('Il\tcavalire\n\taffronta\n\n\til\tdrago\t\'Smaug\' davanti\n\t\tal\t castello')

#La lunghezza di ogni riga
lunghezza_etichetta = 48
#il database contenente le canzoni
kiss_album = 'Psycho Circus _________________________________ \
within ________________________________________ \
I Pledge Allegiance to the State of Rock & Roll \
Into the Void _________________________________ \
We Are One ____________________________________ \
You Wanted the Best ___________________________ \
Raise Your Glasses ____________________________ \
I Finally Found My Way ________________________ \
Dreamin _______________________________________ \
Journey of 1,000 Years ________________________ '

numero_canzone = 3
print(kiss_album[numero_canzone*48:numero_canzone*48+48])

testo = 'Grazie all\'uso di Cera Splendent tutto brilla'
parola_malefica = 'Splendent'
censura = '*********'
testo_censurato = testo.replace(parola_malefica,censura)
print(testo_censurato)
print('Censurata', testo_censurato.count(censura), 'parola')

testo = "Ed è proprio da questa portentosa crema che nasce la crema al mascarpone\
base del tiramisù, prima classificata al premio Crema dell'Anno insieme\
alla nutella. Il dolce italiano per eccellenza, quello più famoso e amato,\
ma soprattutto che ha dato vita a tantissime altre versioni, anche tiramisù senza uova!\
Poi il Tiramisù alle fragole o quello alla Nutella, giusto per citarne un paio!\
Senza contare le rivisitazioni più raffinate come la crostata morbida o la torta al tiramisù."

parola_malefica1 = "Tiramisù"
parola_malefica2 = "Nutella"
censura = "******"
testo = testo.replace(parola_malefica1, censura)
testo = testo.replace(parola_malefica2, censura)
parola_malefica1 = "tiramisù"
parola_malefica2 = "nutella"
testo = testo.replace(parola_malefica1, censura)
testo = testo.replace(parola_malefica2, censura)
print(testo)
print('Censurata/e', testo.count(censura), 'parola/e')

print([7,4,9])
lista = [7,4,9]

numeri = [1,2,3,1,3]
print(numeri)
frutti = ['mela','pera','fragola','ciliegia']
print(frutti)
misto = ['tavolo',5,4,'sedia',8,'sedia']
print(misto)

misto = ['tavolo',
        5,
        4,
        'sedia',
        8,
        'sedia']
print(misto)

lista_vuota = []
print(lista_vuota)
lista_vuota = list()
print(lista_vuota)

a = []
b = []

la = [8,6,7]
lb = [9,5,6,4]

print(a,b,la,lb)

la = [8,6,7]
lb = [9,5,6,4]
lb = la

print(la)
print(lb)

la = [9,6,1]
lb = [2,3,4,3,5]

lc = la
la = lb
lb = lc

print(la)
print(lb)

tabella = [['a','b','c'], ['d','e','f']]
print(tabella)

tabella = [
            ['a','b','c'],
            ['d','e','f']
          ]
print(tabella)
di_tutto = [
                ['ciao',3,'mondo'],
                'una stringa',
                [9,5,6,7,3,4],
                8
            ]
print(di_tutto)

tessera1 = [1,3]
tessera3 = [1,5]
tessera2 = [3,9]
tessera5 = [9,7]
tessera4 = [8,2]
tessera6 = [5,4]
tessera7 = [1,2]

sequenza = [tessera1,tessera2,tessera5, tessera4]
spaiate = [tessera3, tessera6, tessera7]
lista = [sequenza, spaiate]
print(lista)

la = [8,4]
lb = [4,8,4]
print([[la,la], [lb,la]])

la = [8,5]
lb = [8,[7,7]]
lc = [8,7]

print([[lb,lb,[lc,la]], lc])

la = [3,2]
lb = [8,la]
lc = [la,lb]

print([[la,lc,la], lb])

print(list('treno'))
print(list([7,9,5,6]))

s = 'GuLp'
print([list(s.upper()), list(s.lower())])

s = 'maratona'
x = list(list(list(s)))
print(x)

s = 'catena'
a = list(s)
b = list(a)
c = b
x = list(c)
print(x)

sa = 'ga'
sb = 'ra'
la = ['ga']
print(la)
lb = list(la)
print(lb)
print([list(sa+sb), lb, lb, list(sb+sa)])

a = [7,5,8]
print(len(a))

b = [8,3,6,4,7]
print(len(b))

mista = [
            [4,5,1],
            [8,6],
            [7,6,0,8]
        ]

print(len(mista))

    # 0  1  2  3
la = [70,60,90,50]
x = la
print(la[0])
print(la[1])
print(la[2])
print(la[3])

print(la[-1])
print(la[-2])
print(la[-3])
print(la[-4])

print(len(x))

lettere = ['b', 'e', 'g', 'n', 'r', 't', 'u']

l = lettere
print(l[2].upper(),l[6], l[5], l[1], l[3], l[0], l[1], l[4], l[2])

print(f"{l[2].upper()}{l[6]}{l[5]}{l[1]}{l[3]}{l[0]}{l[1]}{l[4]}{l[2]}")

a = '%s%s%s%s%s%s%s%s%s' % (l[2].upper(),l[6], l[5], l[1], l[3], l[0], l[1], l[4], l[2])
print(a)

la = [7,9,6,8]
la[2] = 5
print(la)

parcheggi = ['Carlo', 'App.3', 'Ernesto', 'App.4', 'App.7', 'Pam', 'Giovanna', 'Camilla', 'Giorgia', 'Jessica', 'Jim']
parcheggi[1] = parcheggi[9]
parcheggi[9] = 'App.3'
parcheggi[3] = parcheggi[10]
parcheggi[10] = 'App.4'
parcheggi[4] = parcheggi[8]
parcheggi[8] = 'App.7'
print(parcheggi)

parcheggi = ['Carlo', 'App.3', 'Ernesto', 'App.4', 'App.7', 'Pam', 'Giovanna', 'Camilla', 'Giorgia', 'Jessica', 'Jim']

parcheggi[1], parcheggi[-2] = parcheggi[-2], parcheggi[1]
parcheggi[3], parcheggi[-1] = parcheggi[-1], parcheggi[3]
parcheggi[4], parcheggi[-3] = parcheggi[-3], parcheggi[4]

print(parcheggi)

la = [7,9,6]
lb = la
print(la)
print(lb)

lb[0] = 5
print(la)
print(lb)

la = [7,9,6]
lb = [7,9,6]
lb[0] = 5
print('la è', la)
print('lb è', lb)
print(la)
print(lb)

verdure = ['pomodori','verze', 'carote', 'cavoli']
print(verdure[2])

print('carote'[0])
print(verdure[2][0])

single = ['tn','mi','to','ro']
print([single[0].upper(),single[1].upper(),single[2].upper(),single[3].upper()])

giochi = ['Monopoli', 'RISIKO', 'Tombola']
giochi[0] = giochi[0][0]
giochi[1] = giochi[1][0]
giochi[2] = giochi[2][0]
print(giochi)

la = [40,30,90,80,60,10,40,20,50,60]
print(la[3:7])
print(la)
print(la[:3])
print(la[:4])

la = [40,30,90,80,60]
print(la[:3])
print(la[:4])
print(la[:6])
print(la[8:12])
print([][:8])
print([][3:8])

treccia = ['n', 'n', 'n', 'n', 'n', 'm', 'm', 'm', 'm', 'm', 'm', 'r', 'r', 'r', 'r']
noci,mirtilli,ribes = 5,6,4

print('Mio:', treccia[noci:noci+mirtilli])
print('Giorgio', treccia[:noci])
print('Camilla:', treccia[noci+mirtilli:])

noci,mirtilli,ribes,treccia = 2,4,3,['N', 'N', 'M', 'M', 'M', 'M', 'R', 'R', 'R']
print('Mio:', treccia[noci:noci+mirtilli])
print('Giorgio', treccia[:noci])
print('Camilla:', treccia[noci+mirtilli:])

la = [90,60,80,70,60,90,60,50,70]
print(la[:3])

print(la[3:])
print(la[:])

la = [7,8,9]
lb = la[:]
lb[0] = 6
print(la)
print(lb)

tempi = ['*****',
         '*******',
         '***',
         '****']

corda1 = ['do', 'do', 'do', 'do', 'do', 're', 'sol', 'fa', 'si', 'si', 'do', 'si']
corda2 = ['re', 'la', 'fa', 'mi', 'si', 'sol', 'si', 'fa', 'fa', 'fa', 'fa', 'fa', 'fa', 'fa']
corda3 = ['si', 'mi', 'sol', 're', 're', 're', 're', 're', 're']
corda4 = ['sol', 'sol', 'sol', 'sol', 're', 're', 'la', 'la', 'si', 'fa', 'si']

corda1_pulito = corda1[:len(tempi[0])]
corda2_pulito = corda2[len(tempi[1]):]
corda3_pulito = corda3[len(tempi[2]):]
corda4_pulito = corda4[:len(tempi[3])]

print(corda1_pulito)
print(corda2_pulito)
print(corda3_pulito)
print(corda4_pulito)

la = [90,60,80,70,60,90,60,50,70]
print(la[3:0])
print(la[3:1])
print(la[3:3])

la = [70,40,10,50,60,10,90]
print(la[3:-1])
print(la[3:-2])
print(la[3:-5])

la = [70,40,10,50,60,10,90]
print(la[-7:3])
print(la[-6:3])
print(la[-5:3])
print(la[-4:3])
print(la[-3:3])
print(la[-2:3])

import pprint
scontrino = ['Negozio La Bislaccheria',
             '21 Luglio 2021 14:54',
             'Articoli acquistati',
             'Vernice verde per insalata        1,12€',
             'Coriandoli piombo anti-vento      4,99€',
             'Pettine per pitoni               12,00€',
             'Accendisigari da immersione      23,00€',
             'Scarpe trasparenti da casa       35,56€',
             'Totale 56,66€',
             'Grazie per aver acquistato il nostro ciarpame!'
             ]

articoli = scontrino[3:-2]
ultimo = scontrino[-3]
pprint.pprint(articoli)
print()
print('La spesa maggiore è stata:', ultimo[:-10])
print('                    costo:', ultimo[-10:].lstrip())

la = [0,10,20,30,40,50,60,70,80,90]
print(la[3:9:2])
print(la[0:10:3])
print(la[::3])

la = [30,40,80,10,70,60,40,20]
la[3:6] = [91,92,93]
print(la)

la = [9,6,5,8,2]
la[1:4] = [4,7,0]
print(la)

la = [7,6,8,4,2,4,2,3,1]
i = 3
lb = la[0:i]
la[i:2*1] = lb
print(la)

colorado = ['Locomotiva CS', 'carbone', 'cowboy','oro','minatori','oro', 'cowboy', 'argento']
fort = ['Locomotiva FC', 'carbone', 'carbone', 'signori', 'dame', 'mucche', 'cavalli']
new_york = ['Locomotiva NY', 'carbone','','','','','','','','','']

new_york = [new_york[:2], colorado[3], colorado[5],colorado[7],\
            colorado[6], colorado[4], colorado[6],fort[3:7]]
print(new_york)

colorado = ['Locomotiva CS', 'carbone', 'cowboy','oro','minatori','oro', 'cowboy', 'argento']
fort = ['Locomotiva FC', 'carbone', 'carbone', 'signori', 'dame', 'mucche', 'cavalli']
new_york = ['Locomotiva NY', 'carbone','','','','','','','','','']
new_york[2:5] = colorado[3::2]
new_york[5:] = colorado[2::2]
new_york[8:] = fort[3:]
print(new_york)

coppie = [      #lista esterna
            [67,95],
            [60,59],
            [86,75],
            [96,90],
            [88,87]
         ]
novanta = coppie[3][1]
print(novanta)

print('punto 1:', coppie[2][0], coppie[0][0], coppie[4][1])
i,j = 3,1
print('Punto 2:', 'i =', i, 'j =', j, 'risultato =', coppie[i][j] * coppie[i+1][j])

import pprint
gladiatori = [
                [67,95],
                [60,23,23,13,59],
                [86,75],
                [96,90,92],
                [88,87]
             ]

premio = 40
i = 1

gladiatori[i][-1] += premio // 2
gladiatori[i+1][-1] += premio // 2

pprint.pprint(gladiatori, width=30)

print(9 in [6,8,9,7])
print(5 in [6,8,9,7])
print('mela' in ['anguria','mela','banana'])
print('carota' in ['anguria','banana','mela'])
print(True in [5 in [6,7,5], 2 in [8,1]])

print('carota' not in ['anguria', 'banana', 'mela'])
print('anguria' not in ['anguria', 'banana', 'mela'])
print(not 'carota' in ['anguria', 'banana', 'mela'])
print(not 'anguria' in ['anguria', 'banana', 'mela'])

ortaggi = ['carota',
           'cavolfiore',
           'mela',
           'melanzana',
           'anguria']

frutta = ['anguria', 'banana', 'mela']

ortaggi = [ortaggi[0] in frutta,
           ortaggi[1] in frutta,
           ortaggi[2] in frutta,
           ortaggi[3] in frutta,
           ortaggi[4] in frutta]
print(ortaggi)

la = [70,60,80]
lb = [90,50]
lc = la + lb
print(lc)
print(lb)
print(la)

la = [18,26,30,45,55]
lb = [16,26,37,45]
lc = la[3:] + lb[:2]

print(la)
print(lb)
print(lc)

print(['4','1','7'] + ['3','1'])

print(max([4,5,3,7,8,6]))
print(min([4,5,3,7,8,6]))

print(min(4,5,3,7,8,6))
print(max(4,5,3,7,8,6))

print(min('sportello'))
print(max('sportello'))

print(min(['il','marinaio', 'cammina','per','le','vie','del','porto']))
print(max(['il','marinaio', 'cammina','per','le','vie','del','porto']))

print(sum([1,2,3]))
print(sum([1.0, 2.0, 0.14]))

bilancia = [4,3,7,1,5,8]
n = len(bilancia)
print(sum(bilancia[:n//2]) == sum(bilancia[n//2:]))

bilancia = [4,3,3,1,9,8]
n = len(bilancia)
print(sum(bilancia[:n//2]) == sum(bilancia[n//2:]))

la = [7,6,8] *2
print(la)
la = la *3
print(la)

la = [7,6,8]
lb = [7,6,8] * 3
print(la, '   ', lb)

la = ['un', 'mondo', 'di', 'parole']
lb = la *2
print(lb)

la = [5,6]
lb = [7,8,9]
lc = [la,lb] *2
print(la)
print(lb)
print(lc)

print([4,3,6] == [4,3,6])
print([4,3,6] == [4,3])
print([4,3,6] == [4,3,6, 'ciao'])
print([4,3,6] == [2,2,8])

print(['mele', 3, ['ciliegie', 2], 6] == ['mele', 3, ['ciliegie', 2], 6])
print(['banane', 3,['ciliegie', 2], 6] == ['mele', 3, ['ciliegie', 2], 6])

print([2,2,8] != [2,2,8])
print([4,6,0] != [2,2,8])
print([4,6,0] != [4,6,0,2])

print([7] [0] == [[7]] [0])
print([9] == [9][0])
print([max(7,9)] , [max([7]),max([9])])
print([[],[]] == [] + [])

la = []
la.append(50)
print(la)
la.append(90)
print(la)
la.append(70)
print(la)
print(None)
print(type(None))

la = []
x = la.append(70)
print(la,x)

la = []
x = la.append(70)
print('la è', la)
print('x è', x)

la = []
la.append(77)
la.append('prova')
la.append([60,93])
print(la)

sa = '  trento  '
sb = sa.strip().capitalize()
print(sb)

sa = '  trento  '
sa = sa.strip()
sa = sa.capitalize()
print(sa)

sa = '  trento  '
x = sa.strip()
sb = x.capitalize()
print(sb)

la = []
lb = []
la.append(lb)

lb.append(90)
lb.append(70)
print(la)

la = [8,4,3,5,7,3,5]
lb = []
lb.append(la[::2])
print(lb)

la = [8,4,3,5,7,3,5]
lb = []
lb.append(la[0])
lb.append(la[2])
lb.append(la[4])
lb.append(la[6])
print(lb)

la = [70,30,50]
lb = [40,90,30,80]
la.extend(lb)
print(la)
print(lb)

la = [30,70,50]
lb = [80,40]
x = la.extend(lb)

print('la è', la)
print('lb è', lb)
print('x è', x)

la = [70,60,80]
s = 'ciao'
la.extend(s)
print(la, s)

la = [60,50]
la.extend([70,90,80])
print(la)

la = [1,2,3]
lb = [4,5]
lc = [6,7,8]
la.extend(lb)
print(la)

la = [5,9,2,4]
lb = [7,1,3]
x = 8
print(id(la))
la.append(x)
la.extend(lb)
print(la)
print(lb)
print(x)
print(id(la))

la = ['a','b','c','d','e','f','g','h','i','l','m','n','o']
lb = ['z']

lb.extend(la[:3])
lb.extend(la[-3:])

print(la)
print(lb)

parole = ["vedo", "una", "zebra", "laggiù"]
la = []

la.extend(parole[0][:3])
la.extend(parole[1][:3])
la.extend(parole[2][:3])
la.extend(parole[3][:3])
print(la)

la = [6,7,8,9]
la.insert(2,55)
print(la)
la.insert(0,77)
print(la)
la.insert(6,88)
print(la)

la.insert(1000,99)
print(la)

x = [3,4]
x.insert(len(x), 66)
print(x)
#x.append(66)

la = [3,4,5,6]
la.insert(0,[1,2])
print(la)

la = [7,6,8,5,6]
la.insert(3,80)
la.insert(1,90)
la.insert(1,70)
la.insert(len(la), 50)
print(la)

la = []
lb = [7,6,9,8]

la.append(lb[-1]*2)
la.append(lb[-2]*2)
la.append(lb[-3]*2)
la.append(lb[-4]*2)

cesta = ['melone', 'fragola', 'anguria']
cesta.pop()
print(cesta)
cesta.pop()
print(cesta)
frutto = cesta.pop()
print(frutto)
print(cesta)

attrezzi = ['martello', 'cacciavite', 'pinza', 'martello']
attrezzi.pop()
print(attrezzi)

corn = ['t', 'o', 'r', 'o']
scatola = []

scatola.append(corn.pop())
scatola.append(corn.pop())
scatola.append(corn.pop())
scatola.append(corn.pop())
print(scatola)

la = ['z', 'o', 'n', 'z', 'o']
lb = [2,4]
la.pop(lb[0])
la.pop(lb[1]-1)
print(la)

la= [7,6,8,4]
la.reverse()
print(la)

lb = [7,6,8,4]
x = lb.reverse()
print(x)
print(lb)

la = ['c', 'o', 'm', 'e']
lb = ['v', 'a', '?']

la.extend(lb)
la.reverse()
print(la)
print(lb)

la = ['c', 'o', 's', 'e']
lb = ['p', 'r', 'e', 'z', 'i', 'o', 's', 'e']
lc = [] #lc = la + lb
lc.extend(la)
lc.extend(lb)
lc.reverse()
print(lc)

x = 2
la = [x]

la.append(la[-1]*2)
la.append(la[-1]*2)
la.append(la[-1]*2)
la.append(la[-1]*2)
la.reverse()
print(la)

la = [8,6,7,9]
la.sort()
print(la)

lb = ['Boccaccio', 'Alighieri', 'Manzoni', 'Leopardi']
lb.sort()
print(lb)

la = [10, 60, 72, 118, 11, 71, 56, 89, 120, 175]
print('la:', la)
pari = la[::2]
print('pari:', pari)
dispari = la[1::2]
print('dispari:', dispari, '\n')

la.sort()
print('ordinati:', la)
pari = la[::2]
print('ordinati pari:', pari)
dispari = la[1::2]
print('ordinati dispari', dispari, '\n')

print('la: Min:', la[0], 'Max:', la[-1], 'Median:', la[5])
print('pari: Min:', pari[0], 'Max:', pari[-1], 'Median',pari[1])
print('dispari: Min:', dispari[0], 'Max:', dispari[-1], 'Median:', dispari[3])

la = [10, 60, 72, 118, 11, 71, 56, 89, 120, 175]
pari = la[::2]
dispari = la[1::2]

print('originale:', la)
print('pari:', pari)
print('dispari:', dispari)

la.sort()
pari.sort()
dispari.sort()

print()
print('ordinata:', la)
print('ordinata pari', pari)
print('ordinata dispari:', dispari)
print()
print('originale: Min:', la[0], 'max:', la[-1], 'Median:', la[len(la) // 2])
print('pari: Min:', pari[0], 'Max', pari[-1], 'Median:', pari[len(pari) // 2])
print('dispari: Min:', dispari[0], 'Max:', dispari[-1], 'Median:', dispari[len(dispari) // 2])

la = ['Quando', 'fuori', 'piove']
la = 'separatore'.join(la)
print(la)

la = ['Quando', 'fuori', 'piove']
la = ' '.join(la)
print(la)

a = 'A'.join('porto')
print(a)

b = '\''.join('mmmm')
print(b)

s = 'ab'
la = ['uief', 'cb', 'sd']
a = len(s)
b = len(s.join(la))
c = s.join(la)
d = a <= b
print(a, b, c, d)

sa = 'barzoletta'
sb = list(sa)
print(sb)
sb.pop(4)
sb.insert(4,'e')
sb.insert(5,'l')
print(sb)
sb = ''.join(sb)
print(sb)

sa = 'barzoletta'
la = list(sa)
la[4] = 'e'
la.insert(5, 'l')
sb = ''.join(la)
print(sb)

sa = 'barzoletta'
la = list(sa)
la[4:6] = 'ell'
sb = ''.join(la)
print(sb)

la = ['dub', 'dab', 'dib', 'dob']
s = ', '.join(la)
print(s)
print(len(s))

la = ['ghi', 'ri', 'go', 'ri']
seps = [',', '_', '+']
lb = seps[0].join(la)
lc = seps[2].join(la)
ld = lb + seps[1] + lc
print(ld)

la = ['ghi', 'ri', 'go', 'ri']
seps = [',', '_', '+']
print(seps[0].join(la)+seps[1]+seps[2].join(la))

la = ['walnut', 'eggplant', 'lemon', 'lime', 'date', 'onion', 'nectarine', 'endvine']
nuova = []

#nuova.insert(0, la[0][0])
#nuova.insert(1, la[1][0])
#nuova.insert(2, la[2][0])
#nuova.insert(3, la[3][0])
#nuova.insert(4, la[4][0])
#nuova.insert(5, la[5][0])
#nuova.insert(6, la[6][0])
#nuova.insert(7, la[7][0])

nuova.append(la[0][0])
nuova.append(la[1][0])
nuova.append(la[2][0])
nuova.append(la[3][0])
nuova.append(la[4][0])
nuova.append(la[5][0])
nuova.append(la[6][0])
nuova.append(la[7][0])
nuova.insert(4,' ')
nuova.append('!')

print(nuova, '\n')
nuova = ''.join(nuova)
print(nuova)

print('E\' giunto il momento di dividere il tesoro'.split('il'))
s = 'E\' giunto il\nmomento di      dividere\til tesoro'
print(s)
s = s.split()
print(s)

s = 'E\' giunto il\nmomento di      dividere\til tesoro'
s = s.split(maxsplit=2)
print(s)

print('Parlo e straparlo senza mai fare una pausa'.split(','))

print('abisso_0000_abisso'.split('abisso')[0])

musica = 'Zam Dam\tZa Bum Bum\tZam\tBam To Tum\tRa Ta Pam\tBar Ra\tRammaGumma Unza\n\t\nTACAUACA \n BOOMBOOM!'
dance = musica.split('\t', maxsplit=6)
dance = dance[:-1] + dance[-1].split()
print(dance)

hits = '6,230,650 - Ti amo come i pomodori ammuffiti nel frigorifero\n \
2,000,123 - Il dolore di vivere pieni di soldi\n \
100,000 - Le groupies non sono mai abbastanza\n \
837 - Ti ricordi i cassonetti l\'estate...'

posizione = 1

lst = hits.split('\n')
ext = lst[posizione-1].split(' - ')

print('la numero', posizione, 'in classifica', '"' + ext[1] + '"',
      'ha venduto', '.'.join(ext[0].split(',')), 'copie')

stringa = 'Questa è una stringa\n\
di testo su\n\
diverse linee che non dice niente.'

print(stringa, '\n')
parole = stringa.split()
righe = stringa.split('\n')
print('Linee:', len(righe), 'parole:', len(parole), 'charatteri:', len(stringa))

s = 'Questa è una stringa\n\
di testo su\n\
diverse linee che non dice niente.'

lines = s.split('\n')
words = lines[0].split(' ') + lines[1].split(' ') + lines[2].split(' ')
num_chars = len(s)
print('Linee:', len(lines), 'parole:', len(words), 'caratteri:', num_chars)

print('')
characters = list(s)
num_chars2 = len(characters)
print(characters)
print(num_chars2)

words.sort()
print('')
print('Prima parola:', words[0])
print('Ultima parola:', words[-1])
print(words)

frase = 'Prendi 4 lettere'
frase1 = frase.split()
print(frase1[2][0:4])

frase = 'Prendere 5 caratteri'
n = int(frase.split()[1])
print(frase.split()[2][:n])

la = 'corroborare'
la = list(la)
c = la.count('c')
print(la)
print(c)

o = la.count('o')
print(o)

r = la.count('r')
print(r)

a = ['A','aa','a','aaAah',"a", "aaaa"[1], " a "]
print(a.count('a'))

parentesi = [[],[],[]].count([])
print(parentesi)

el1, el2 = 'badili', 'zappe'

campagna = ['aratri', 'cariole', 'badili', 'cariole', 'badili', 'zappe', 'cariole',
            'zappe', 'aratri', 'cariole', 'aratri', 'badili', 'aratri', 'zappe']

mid = len(campagna)//2
print(campagna[:mid].count(el1) == campagna[mid:].count(el2))

la = 'paese'
la = list(la)
print(la)
print(la.index('p'))
print(la.index('a'))
print(la.index('e'))

la = 'accaparrare'
la = list(la)
print(la.index('a', 6)) # da sei in un poi
print(la.index('a', 4,8)) # tra quattro e otto

la = ['azzurro', 'blu', 'celeste','puffo'][-1:]#.index('celeste')
print(la)

strada = ['asfalto', 'bitume', 'cemento', 'ghiaia']
print('malta'in strada and strada.index('malta'))

strada = ['asfalto', 'bitume', 'malta', 'ghiaia']
print('malta'in strada and strada.index('malta'))

la = [0,5,10]
la.reverse()
print(la)
print(la.index(5)> la.index(10))

soffitta = [3, '\\', ['quadro'], '---', ['quadro'],
            5.23, ['viti'], ['pattini'], ['quadro'],
            ['lampada']]

primo_quadro = soffitta.index(['quadro'])
secondo_quadro = soffitta.index(['quadro'], primo_quadro+1)
terzo_quadro = soffitta.index(['quadro'], secondo_quadro+1)
print('Scaffale primo quadro:', primo_quadro+1)
print('Scaffale secondo quadro', secondo_quadro+1)
print('Scaffale terzo quadro', terzo_quadro+1)

print()

soffitta = [['quadro'], '---', ['pattini'], ['quadro'], ['status'],
            ['viti'], ['stivali']]

primo_quadro = soffitta.index(['quadro'])
secondo_quadro = soffitta.index(['quadro'], primo_quadro+1)
#terzo_quadro = soffitta.index(['quadro'], secondo_quadro+1)
print('Scaffale primo quadro:', primo_quadro+1)
print('Scaffale secondo quadro', secondo_quadro+1)
#print('Scaffale terzo quadro', terzo_quadro+1)

la = [6,7,9,5,9,8]
la.remove(9)
print(la)

la = [4,5,7,10]
a = 11 in la and la.remove(11)
print(la)
print(a)

lb = [8,7,4]
la = [7,8,11,8,7,4,5,4]
la.remove(lb[0])
la.remove(lb[0])
la.remove(lb[1])
la.remove(lb[1])
la.remove(lb[2])
la.remove(lb[2])
print(la)

parola = 'marsupio'
parola_l = list(parola)
parola_r = parola_l.copy()
parola_r.reverse()
parola_r = parola_r[1:]
parola_mix = parola_l + parola_r
#print(parola, parola_l, parola_r)
print(parola_mix)

faccendiere1, faccendiere2 = 'Sonny', 'Lenny'

registro = ['mortimer','rupert', 'rupert','mortimer','sonny e lenny',
'mortimer', 'rupert', 'lenny e sonny', 'mortimer',
'mortimer e rupert', 'rupert e mortimer']

faccendiere1 = faccendiere1.lower()
faccendiere2 = faccendiere2.lower()

faccendieri = faccendiere1 + ' e ' + faccendiere2
faccendieri_reverse = faccendiere2 + ' e ' + faccendiere1
print(faccendieri)
registro.remove(faccendieri)
registro.remove(faccendieri_reverse)
print(registro)

faccendiere1, faccendiere2 = 'Joey', 'Vincent'
registro = ['rupert','rupert', 'mortimer e rupert','mortimer', 'mortimer', 'vincent e joey', 'rupert','mortimer', 'joey e vincent','mortimer', 'mortimer e rupert',
'rupert e mortimer']

faccendiere1 = faccendiere1.lower()
faccendiere2 = faccendiere2.lower()

faccendieri = faccendiere1 + ' e ' + faccendiere2
faccendieri_reverse = faccendiere2 + ' e ' + faccendiere1
print(faccendieri)
registro.remove(faccendieri)
registro.remove(faccendieri_reverse)
print(registro)

numeri = (6,7,5,7,7,9)
print(numeri)
tuplina = (4,)
print(type(tuplina))

farlocca = (4)
print(type(farlocca))

vuota = ()
print(vuota)
print(type(vuota))

a,b,c = 1,2,3
print(a,b,c)
print(type(a),type(b), type(c))

x = 1,2,3
print()

z,w = 5,6
print(type(z))
print(type(w))

a,b = 5,6
a,b = b,a
print('a=',a)
print('b=', b)

z = 5,
print(type(z))

roba = (4, "carta", 5, 2, 'scatole', 7)
print(roba)
print(type(roba))

insalata = (('cavoli', 3), ('pomodori', 9), ('verze', 4))
print(insalata)
print(type(insalata))

misto = (['quando', 'fuori', 'piove'], ['scrivo', 'programmi'], [7,3,9])
print(misto)

print(tuple([8,2,5]))

print(tuple('abc'))

print(list( (3,4,2,3) ))

x = (4,2,5)
y = tuple(x)
print(y)

x = (4,2,5)
y = x
print(y)

print(len( (4,2,3) ))

print(len( (7,) ))

print(len( ((),()) ))

print(len( () ))

print(len([ ('d','s','c','d'), (('ab')),[('a','b','c')] ]))

tupla = (10, 11, 12, 13)
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
print(tupla[-1])

animali = 'gatto siamese,cane,canarino,porcellino,coniglio,criceto'
animali = animali.split(',')
lista_animali = list(animali)
tupla = ((lista_animali[0], len(lista_animali[0]),
(lista_animali[1], len(lista_animali[1])),
(lista_animali[2], len(lista_animali[2])),
(lista_animali[3], len(lista_animali[3])),
(lista_animali[4], len(lista_animali[4])),
(lista_animali[5], len(lista_animali[5]))))

print(tupla)


tupla = (10,11,12,13,14,15,16,17,18,19)
print(tupla[2:6])

tupla = (10,11,12,13,14,15,16,17)
print(tupla[0:8:5])
print(tupla[0:8:2])
print(tupla[1:8:1])

print((7,6,8,9,5)[1:3])
print((10,11,12,13,14,15,16)[3:100])
print((10,11,12,13,14,15,16)[-3:5])
print((1,0,1,0,1,0)[::2])
print((1,2,3)[::1])
print(tuple('cartolina')[0::2])

t = (1,2,3) + (4,5,6,7,8)
print(t)
print(type(t))

x = (1,2,3)
y = (4,5,6,7,8)
t = x + y
print(t)
print(x,y)

print((2,3,4) + tuple([5,6,7]))
print(type(()+()))

print(len(()+()))

print('a' in (tuple('casco')))
print('z' in tuple('casco'))

print('carota' not in ('anguria', 'banana', 'mela'))
print('anguria' not in ('anguria', 'banana', 'mela'))

print(not 'carota' in ('anguria', 'banana', 'mela'))
print(not 'anguria' in ('anguria', 'banana', 'mela'))

print( 3 in (1.0, 2.0, 3.0))
print(3.0 in (1,2,3))
print(3 not in (3,))
print(6 not in ())
print(0 in (0,))
print([] in ())
print(() in [])
print(not [] in ())
print(() in ())
print(() in ((),))
print('ciao' in tuple('ciao'))

print((7,8,5) * 3)
print((7,8,5) * 1)
print((7,8,9) * 0)

x = (5,6,7)
y = x * 3
print('x=', x)
print('y=', y)

print((5,6,7) * (3))
print((5,6,7) * 3)

print((4,2,3) * int(3.0))

print((1,2) * (3,)[0])


print((1,2) * (3,4)[-1])

print([(9,8)] * 4)

print((1+2, 3+4) * 5)

print((1+2,)*4)

print((1+2) * 4)

print((1,2,3)*0)

print((7)*0)

print((7,) * 0)

x = (2,4,3)
y = (('w','e','l','c'),('o',),('m','e'))
z = y[0]*x[0] + y[1]*x[1] + y[2]*x[2]
print(z)

tupla = (17,54,34,87,26,95,34)
tupla = tupla[0:3] + (12,) + tupla[4:]
print(tupla)

x = ('a', 'b', 'c')
y = x[:2] + ('d','e')
print('x =', x)
print('y =', y)

t = ('C', 'a', 'R', 'i', 'S', 'm', 'A', 't', 'I', 'c', 'O')
t = t[::2] + t[1::2]
print(t)

x = (3,4,2,5,5,5,2,3)
x = list(x)
x.sort()
x = tuple(x)
print(x)

tupla = tuple('barattare')
b = tupla.index('b')
a = tupla.index('a')
#try:
t = tupla.index('t')
#except:
#    pass
print(b,a,t)

print(tuple('barattare').index('r', 3))
print(tuple('barattare').index('r', 1, 7))

print((3,4,-1).index(-1))
print((2.2,.2,2,).index(2))
z = (2.2,.2,2)
print(type(z[1]))
print((3,4,2).index(len([3,8,2,9])))

print((4,2,3).index(3))
#print(tuple('GUG').index('g'))
print((tuple('ci') + ('a', 'o')).index('a'))
print(((),).index(()))

tupla = ('Apri', 'Le', 'Scatole', 'Cinesi', ('Scatole', 'Cinesi', 'Le', 'Apri',('Apri', 'Le', 'Cinesi', 'Scatole')))
cinesi_1 = tupla[:4].index('Cinesi')
cinesi_2 = tupla[4][:4].index('Cinesi')
cinesi_3 = tupla[4][4].index('Cinesi')
print(tupla[:4], 'contiene Cinesi alla posizione', cinesi_1)
print(tupla[4][4], 'contiene cinesi alla posizione', cinesi_2)
print(tupla[4][4], 'contiene cinesi alla posizione', cinesi_3)

t = tuple('guarantigia')
print(t.count('g'))
print(t.count('a'))
print(t.count('z'))

print(('p', 'o', 'r', 't', 'e', 'n', 't', 'o', 's', 'o').count( ('o') ))
print((1,0,(0.0),((0,0),(0,0))).count( ((0,0),(0,0)) ))
print( (1,0,(0,),(0,)).count( (0,) ))

s = 'mela|pera|mela|ciliegia|pera|mela|pera|pera|ciliegia|pera|fragola'
s = s.split('|')
print(s)

conteggi = [('mela', s.count('mela')), ('pera', s.count('pera')), ('ciliegia', s.count('ciliegia')), ('fragola', s.count('fragola'))]
print(conteggi)

print(conteggi[0][0], 'è presente', conteggi[0][1], 'volte')
print(conteggi[1][0], 'è presente', conteggi[1][1], 'volte')
print(conteggi[2][0], 'è presente', conteggi[2][1], 'volte')
print(conteggi[3][0], 'è presente', conteggi[3][1], 'volte')

carta1, carta2, carta3 = (3,'Fiori'), (5,'Quadri'), (10, 'Picche')
print('Prima mano:', (carta1, carta2))
print('Seconda mano:', (carta1, carta2, carta3))

s = 'cannocchiale'
s = list(s)
s.sort()
s = tuple(s)
print(s)
s = set(s)
s = list(s)
s.sort()
s = tuple(s)
print(s)

s = {'b', 'a', 'd', 'c'}
print(type(s))
print(s)

s = {6,7,5,9,5,5,7}
print(s)

print(set('acacia'))

print(set((4,6,1,5,1,4,1,5,4,5)))

print(hash('Questa è una bella giornata'))

print({(1,2), (3,4,5)})

print(set)

s = set()
print(type(s), type({}))

a = set(set(['a', 'b']))
print(a)

print({'oh', 'la', 'la'})

print(set([3,4,2,3,2,2,2,-1]))

print(str({'a'}))

print(set({1,2,3}))

la = list('cabcdbe')
lb = set(la)
print(lb)
lb = list(lb)
lb.sort()
print(lb)

lb = list(set(list('cadgghftklghd')))
lb.sort()
print(lb)

print(len({'a','b','c'}))
print(len(set('a')))

parola = 'ababbbbcdd'
parola_pulita_set = set(parola)
parola_pulita = list(parola_pulita_set)
parola_pulita.sort()
parola_pulita = (',').join(parola_pulita)
print('parola     :', parola)
print(len(parola_pulita_set), 'distinte :', parola_pulita)
print(len(parola) - len(parola_pulita_set), 'duplicate')

parola = 'cccccaaabbbb'
parola_pulita_set = set(parola)
parola_pulita = list(parola_pulita_set)
parola_pulita.sort()
parola_pulita = (',').join(parola_pulita)
print('parola     :', parola)
print(len(parola_pulita_set), 'distinte :', parola_pulita)
print(len(parola) - len(parola_pulita_set), 'duplicate')

print('a' in set('menta'))
print('z' in set('menta'))

print('carota' not in {'anguria', 'banana', 'mela'})
print('anguria' not in {'anguria', 'banana', 'mela'})

print(not 'carota' in {'anguria', 'banana', 'mela'})
print(not 'anguria' in {'anguria', 'banana', 'mela'})

print('a' in set({'a', 'a'}))

print([3 in {3,4}, 6 in {3,4}])

print(4 in set([1,2,3]*4))

print(2 in {len('3.4'.split('.'))})

print(4 not in {1,2,3})

print('3' not in {1,2,3})

print(not 'a' in {'b', 'c'})

#print(not {} in set([]))
print({not 'a' in {'a'}})

print({'a', 'b', 'c'} | {'b', 'c', 'd', 'e'})

print({1|2|3})

print(set('.'.join('pacca')))

s1 = set(list('abcde'))
s2 = set(list('bcfg'))
s3 = set(list('bf'))

s4 = set(s1 | s2)  - s3
print(s4)

s5 = set(s1 & s2)
print(s5)

print({'a', 'b', 'c'} & {'b', 'c', 'd', 'e'})

print({0} & {0,1})
print({0,1} & {0})

print(set('capra') & set('campa'))
print(set('cba') & set('dcb'))
print({1,2} & {1,2})
print('cc' in (set('pacca') & set('zucca')))
print(set('pacca') & set('zucca'))
print(set([1,2,3,4,5][::2]) & set([1,2,3,4,5][2::2]))
print({(())} & {()})
print({(())} & {()})

print('Unione:', '\"|\"', '<Nuovo insieme sommato al secondo>')
print('Intersezione:', '"&"', '<Nuovo insieme contenente\
 gli elementi in comume tra il primo ed il secondo>')
print('Differenza:', '"-"', '<Nuovo insieme togliendo gli elementi del secondo>')
print('Differenza simmetrica:', '"^"', '<Nuovo insieme sommato al seccondo\
 togliendo i valori in comune')

print({'a', 'b', 'c', 'd'} - {'b', 'c', 'e', 'f', 'g'})

print({3,4,2} - {2})

print({1,2,3} - {3,4})

print('{"a"}-{"a"}')

print(set('chiodo')-set('chiave'))

print(set('prova')-set('prova'.capitalize()))

print(set('BarbA')-set('BARBA'.lower()))

print('c' in (set('parco') - set('cassa')))

print('c' in set('parco'))

print(set([(1,2), (3,4), (5,6)]) - set([(3,4), (5,6)]))

print(set([(1,2), (3,4), (5,6)]) - set([(3,4), (5,6)]))

print({1,2,3} - set())

print(set() - {1,2,3})

x = set('rinoceronte')
y = set('sabbia')
print((x & y) | (x-y))

print('Unione:', '\"|\"', '<Nuovo insieme sommato al secondo>')
print('Intersezione:', '"&"', '<Nuovo insieme contenente\
 gli elementi in comume tra il primo ed il secondo>')
print('Differenza:', '"-"', '<Nuovo insieme togliendo gli elementi del secondo>')
print('Differenza simmetrica:', '"^"', '<Nuovo insieme sommato al secondo\
 togliendo i valori in comune')

print({'a','b','c'} ^ {'b', 'c', 'd', 'e'})

s1 = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd', 'e'}
print((s1 | s2) - (s1 & s2))

print({'p', 'e', 'p', 'p', 'o'} ^ {'p', 'a', 'p', 'p', 'e'})

print({'ab', 'cd'} ^ {'ba', 'dc'})

print(set('brodino') ^ set('bordo'))

print(set((1,2,5,3,2,3,1)) ^ set((1,4,3,2)))


A = {'a', 'ab', 'ac', 'abc'}
B = {'b', 'ab', 'bc', 'abc'}
C = {'c', 'ac', 'bc', 'abc'}

print((A & B) | (A & C) | (B & C))

print({4,3,6} == {4,3,6})

print({4,3,6} == {4,6,3})

print({4,3,6} == {4,6,3})

print({4,3,6} == {4,3,6, 'ciao'})

print({4,3,6} == {4,3,6} | {5,7,8} - {5,7,8})

print({2,8} == {2,2,8})

print({2,5} != {2,8})

print({4,6,0} != {4,6,0,2})

print({0,1} != {1,0,0,0,0,0,0,0})

print({2 == 2, 3 == 3})

print({1,2,3,2,1} == {1,1,2,2,3,3})

print({'aa'} == {'a'})

print(set('aa') == {'a'})

print(set('123435'))

print([{1,2,3}] == {1,2,3})

print(set({1,2,3}) == {1,2,3})

print(set((1,2,3)) == {(1,2,3)})

print({'aa'} != {'a', 'aa'})

print({set() != set()})

print(set('scarpa') == set('capras'))

print(set('papa') != set('pappa'))

print(set('pappa') != set('reale'))

print({(),()} == {(())})

print([set()] == [set(), set()])

print((set('gosh') | set('posh')) == (set('shopping') - set('in')))

a = set('cdb')
print(a.union('abc'), '= |')
print(a.intersection('abc'), '= &')
print(a.difference('abc'), '= -')
print(a.symmetric_difference('abc'), '= ^')

b = list('cba')
print(a.update(b))
print(a.intersection_update(b))
print(a.difference_update(b))
print(a.symmetric_difference_update(b))


sa = {'g', 'a', 'r', 'a'}
la = list('agrario')
sb = sa.union(la)
print(sb)

sa = set('gara')
la = list('agrario')
sa.update(la)
print(sa)

print(set('case').intersection('sebo') == 'se')
print(set('naso').difference('caso'))

s = {1,2,3}
s.intersection_update([2,3,4])
print(s)


s = {1,2,3}
s1 = s.intersection([2,3,4])
print(s, s1)

s = set('cartone')
s = s.intersection('parto')
print(s)

sa = set('mastice')
sb = sa.difference('mastro').difference('collo')
print(sa, sb)

sa = set('mastice')
sa.difference_update('mastro')
sa.difference_update('collo')
print(sa)

s1 = set(list('abcde'))
s2 = set(list('bcfg'))
s3 = set(list('bf'))

s1.update(s2)
s1.difference_update(s3)
print(s1)

s = {3,7,4}
s.add(5)
print(s)

s.add(5)
print(s)

s = set('abc')
s.remove('b')
print(s)

try:
    s.remove('z')
except:
    pass

scritta = 'bababiba'
s = set()
s.add(tuple(scritta[0:2]))
s.add(tuple(scritta[2:4]))
s.add(tuple(scritta[4:6]))
s.add(tuple(scritta[6:8]))
print(s)

scritta = 'rubareru'
s = set()
s.add(tuple(scritta[0:2]))
s.add(tuple(scritta[2:4]))
s.add(tuple(scritta[4:6]))
s.add(tuple(scritta[6:8]))
print(s)

s = {'a', 'b', 'c'}
s.discard('a')
print(s)
s.discard('z')
print(s)
s.discard('c')
print(s)

spazzatura = {'alcheni', 'verdura', 'mercurio', 'carta'}
filtri= ['cadmio', 'mercurio', 'alcheni']
separati = spazzatura & set(filtri)
#separati = spazzatura.intersection(filtri)

print('Spazzatura iniziale', spazzatura)
spazzatura.discard(filtri[0])
print('Applico diltro cadmio:', spazzatura)
spazzatura.discard(filtri[1])
print('Applico diltro mercurio:', spazzatura)
spazzatura.discard(filtri[2])
print('Applico diltro alcheni:', spazzatura)

print('\nContaminanti separati:', separati )

print({2,4}.issubset({1,2,3,4}))
print({3,5}.issubset({1,2,3,4}))
print('se tutti gli elementi del primo stanno nel secondo è vero')
print(set().issubset({1,2,3,4}))

print({1,2,3,4,5}.issuperset({1,3,5}))
print({1,2,3,4,5}.issuperset({2,4}))
print('se tutti gli elementi del secondo stanno nel primo è vero')
print(set().issuperset({1,3,5,7,9}))
print({1,2,3,4,5}.issuperset({}))

print({1,3,5}.isdisjoint({2,4}))
print({1,3,5}.isdisjoint({2,3,4}))
print('se tra il primo ed il secondo non ci sono elementi in comune è vero')
print(set().isdisjoint(set()))

insiemi = [{'a','b'},
           {'a','b','c'},
           {'a','b','c','d','e'},
           {'a','b','c','d','e','f','g','h','i'}]

a = (insiemi[0].issubset(insiemi[1]))
b = (insiemi[1].issubset(insiemi[2]))
c = (insiemi[2].issubset(insiemi[3]))
print('La sequenza è a matrioska?', a & b & c)

insiemi = [{'a','b'},
           {'a','b','c'},
           {'a','e','d'},
           {'a','b','d','e'}]

a = (insiemi[0].issubset(insiemi[1]))
b = (insiemi[1].issubset(insiemi[2]))
c = (insiemi[2].issubset(insiemi[3]))
controlli = [a,b,c]
print('La sequenza è a matrioska?', controlli.count(True) == 3)

invitati_miei = ["VittorioG", "LucaB", "DavidL", "GiorgioC", "MichelaF", "GiuliaA","VittorioG", ]
invitati_gianni = ["SamanthaV", "LucaB", "GiorgioC", "MichelaF", "MartaB", "EmmaK"]
invitati_giulia = ["DavidL", "GiorgioC", "MichelaF", "MassimilianoL", "VittorioG","RobertoU", "EmmaK"]

print('Invitati miei:', len(set(invitati_miei)))
print('Invitati gianni:', len(set(invitati_gianni)))
print('Invitati giulia:', len(set(invitati_giulia)))
print('Numero invitati:', len(set(invitati_miei) | set(invitati_gianni) | set(invitati_giulia)))
print('Nomi invitati:', set(invitati_miei) | set(invitati_gianni) | set(invitati_giulia))
#(A & B) | (B & C) | (C & A)
print('Numero amici invitati almeno 2 volte:', len((set(invitati_miei) & set(invitati_gianni)) | (set(invitati_gianni) & set(invitati_giulia)) | (set(invitati_giulia) & set(invitati_miei))))
print('Amici invitati almeno 2 volte:', (set(invitati_miei) & set(invitati_gianni)) | (set(invitati_gianni) & set(invitati_giulia)) | (set(invitati_giulia) & set(invitati_miei)))

a = {'ahha'}
b = {'a':'hgh'}
print(type(a), type(b))

dizionario = {'sedia':'un mobile per sedersi',
              'armadio':'un mobile a ripiani',
              'lampadario':'un apparecchio di illuminazione'}

print(type(dizionario), dizionario)

dizio = {'barca': 'remo',
         'auto': 'ruota',
         'aereo': 'ala'}
print(dizio)

dizio1 = {'sedia':'un mobile per sedersi',
              'armadio':'un mobile a ripiani',
              'lampadario':'un apparecchio di illuminazione'}
db = {'barca': 'remo',
      'auto': 'ruota',
      'aereo': 'ala'}
dc = db
db = dizio1
dizio1 = dc
dc = db
print(dizio1)
print(db)
print(dc)

a = {
    4 : 'gatti',
    3 : 'cani'
}

print(a)

a = {
    4.0 : 'gatti',
    3.0 : 'cani'
}

print(a)

a = {
    'a' : 'gatti',
    'b' : 'cani'
}
print(a)

# a = { [1,2] : 'abc'}

a = {
    (1,2) : 'zam',
    (4,3) : 'zum'
}
print(a)

# a = {{1,2} :'zam'}

#a = {{'a':'x', 'b':'y'} : 'zam'}

a = {
    'navi' : 'porto',
    'aerei' : 'aereoporto',
    'treni' : 'stazione'
}

b = {'aerei': 'aereoporto','navi': 'porto', 'treni': 'stazione'}

print(a == b)

q = set('elefa<ntwe')
q = list(q)
q = set(q)
q = list(q)
q.sort()
print(q)


a = {
    'a':'a',
    'b':'b',
    'b':'b',
    'c':'c'
}
print(a)

a = {
    'a':'a',
    'b':'c',
    'b':'f',
    'c':'c'
}
print(a)

a = {
    'a':3,
    'b':4
}
print(a)

a = {
    'a':3,
    'b':3
}
print(a)

a = {
    'a':3.0,
    'b':4.0
}
print(a)

a = {
    'a':'ghiaccio',
    'b':'fuoco'
}
print(a)

a = {
    'a':['t','w'],
    'b':['x'],
    'c':['y','z','k']
}
print(a)

a = {
    'a':['x','y','z'],
    'b':['x','y','z']
}
print(a)

a = {
    'a':(6,9,7),
    'b':(8,1,7,4)
}
print(a)

a = {
    'a':{6,5,6},
    'b':{2,4,1,5}
}
print(a)

a = {
    'a':{
            'x':3,
            'y':9
        },
    'b':{
            'x':3,
            'y':9,
            'z':10
        }
}
print(a)

a = {}
print(type(a))

a = dict()
print(type(a))

a = {
    'a':3,
    "b":['una', 'lista'],
     7 :('questa', 'è', 'una', 'tupla')
}
print(a)

a = {
    'a':'b',
    'c':'d'
}
print(a)

a = {
    'a b':'c',
    'c d':'e f'
}
print(a)

a = {
    '1':[2,3],
    '2,3':1
}
print(a)

print(type({'a:b,c:d'}))

print({'a:b', 'c:d'})

print({1:2,1:3})

print({2:1,3:1})

print(type({'a':'b', 'c':'d'}))

a = {(1,2):[3,4]}
print(a, a[1,2])

print({'[1,2]':(3,4)})

print({len({1,2}):(3,4)})

print({5:{'a':'b'}})

print({'a':{1:2}})

lista = list('barone')
diz = {lista[0]: lista[1:],
       tuple(lista):set(lista),
       tuple(lista[:2]*2):list(lista[2:4]*2 + lista[4:]*2),
       '/'.join(lista) : {lista[0]:lista[1],
                          lista[2]:lista[3],
                          lista[4]:lista[5]}
}
print(diz)
print()
lista = list('priore')
diz = {lista[0]: lista[1:],
       tuple(lista):set(lista),
       tuple(lista[:2]*2):list(lista[2:4]*2 + lista[4:]*2),
       '/'.join(lista) : {lista[0]:lista[1],
                          lista[2]:lista[3],
                          lista[4]:lista[5]}       
}
print(diz)

a = dict( [
    ('farina',500),
    ('uova',2),
    ('zucchero',200)
])
print(a)

a = dict( (
    ['farina',500],
    ['uova',2],
    ['zucchero',200]
))
print(a)

a = dict( {
    ('a',5),
    ('b',8),
    ('c',3)
})
print(a)

a = dict( (
    {'a',5},
    {'b',8},
    {'c',3}
))
print(a)

print(dict(['ab','cd']))
print(dict(['a1','c2']))
print(dict([]))
print(dict(()))
print(dict(('  ',)))

s = 'Ga'
t = ('La','tt')
l1 = ['Ic', 'Co', 'Ve']
l2 = ['Ra', 'Me', 'Nt']
l3 = [[['EEE','...']]]
n = 43.759

diz = {
    s[0] : s[1],
    t[0] : t[1],
    l1[0][0] : l1[0][1],
    l1[1][0] : l1[1][1],
    l1[2][0] : l1[2][1],
    l2[0][0] : l2[0][1],
    l2[1][0] : l2[1][1],
    l2[2][0] : l2[2][1],
    l3[0][0][0]: l3[0][0][1],
}
diz2 = dict([s,t] + l1 + l2 + l3[0] + [str(n).split('.')])
print(diz, diz2)

s = 'Sp'
t = ('Az','ia')
l1 = ['Le','Si','De']
l2 = ['Ra','Le','In']
l3 = [[['CREDIBBILE','!!!!!']]]
n = 8744.92835

diz = dict([s, t] + l1 + l2 + l3[0] + [str(n).split('.')])

a = dict(a=5, b=6)
print(a)
a = {'a b' : 2,
     'c d' : 6,
}
print(a)

ka = 'a b'
kc = 'c d'
a = dict(ka=2, kc=6)
print(a)

print(dict(_costi=9,_ricavi=15))
print(dict(trentini33=5))
print(dict(trentini_33=5))
print(dict(costi=1==2,ricavi=3==3))
v1 = 6
v2 = 8
print(dict(k1=v1, k2=v2))

da = {'x':3,
      'y':5,
      'z':1
}

db = dict(da)
print(da)
print(db)

print(id(da), id(db))
da = {'x':3,
      'y':5,
      'z':1
}
db = dict(dict(da))
print(da,db)

da = {
    'x':['a','b','c'],
    'y':['d'],
    'z':['e','f']
}
db = dict(da)
print(db)

import copy

da = {
    'x':['a','b','c'],
    'y':['d'],
    'z':['e','f']
}
db = copy.deepcopy(da)

print(da, db)

a = len({
    'a': 5,
    'b':9,
    'c':7
})
print(a)

print(len({3:8,
           1:3}))

print(len({}))

print(len(dict()))
print(len({'a':{}}))
print(len({(1,2):{3},
           (4,5):{6},
           (7,8):{9}}))

print(len({1:2,',':3, ',':4,}))
print(len({1:2,1:2,2:4,2:4,3:6,3:6}))
print(len({3:4,5:6}))

diz = {
    'sedia':'un mobile per sedersi',
    'armadio':'un mobile a ripiani',
    'lampadario':'un apparecchio di illuminazione'
}

print(diz['sedia'])
print(diz)
print(diz['lampadario'])
print(diz.keys())

kabbalah = {
    1:'progresso',
    2:'amore',
    3:'creazione',
}

print(kabbalah[1])
print(kabbalah.keys())

print({1:2,2:3,3:4}[3])

print({'a':1,'b':2})

print({'a':1, 'b' : 2})

print({'a':1, 'b':2, 'c':3}['c'])

print({(3,4):(1,2)})

diz1 = {'a':6, 'b':2, 'c':5}
diz2 = {'z': diz1['b'] + diz1['c']}
print(diz2)

arredo = {
    'sedia' : 'un mobile per sedersi',
    'armadio' : 'un mobile a ripiani',
    'lampadario' : 'un apparechhio di illuminazione'
}
arredo['divano'] = 'mobile per rilassarsi'
print(arredo)
print(arredo.keys())
print(arredo.values())

bidone = {
    'bla':3,
     4:'boh',
     (7,9):['spaz','zatura']
}

bidone[5.0] = 'un float'
print(bidone)
bidone['bidone'] = {
    'bla':3,
     4:'boh',
     (7,9):['spaz','zatura']
}

print(bidone)
print(bidone.keys())
print(bidone.values())

diz1 = {'a':3, 'b' :4}
diz2 = diz1
diz1['a'] = 5
print(diz1)
print(diz2)

diz1 = {'a':3, 'b' :4}
diz2 = dict(diz1)
diz1['a'] = 5
print(diz1)
print(diz2)

la = ['a', 'c']
diz = {
    'a':3,
    'b':4,
    'c':5
    }
diz['d'] = diz[la[0]] + diz[la[1]]
print(diz)

diz = {}
diz[()]:''
diz[('a',)]: 'A'
diz[('a','b')]: 'AB'
print(diz)

la = [5,8,6,9]
diz = {}
diz[la[0]] = la[2]
diz[la[2]] = la[0]
print(diz)

diz = {}
diz[(4,5,6)[2]] = 'c'
diz[(4,5,6)[1]] = 'b'
diz[(4,5,6)[0]] = 'a'
print(diz)

diz = {
    'a':'x',
    'b':'x',
    'c':'y',
    'd':'y'
}
print(diz)
diz2 = {}

diz2[diz['a']] = 'a'
diz2[diz['b']] = 'b'
diz2[diz['c']] = 'c'
diz2[diz['d']] = 'd'
print(diz2)

arredo = {
    'sedia':'un mobile per sedersi',
    'armadio':'un mobile a ripiani',
    'lampadario':'un apparecchio di illuminazione'
}
arredo['lamapadario'] = 'un apparechhio di illuminazione appeso al soffitto'
arredo['mucca'] = 'muu'
arredo.pop('mucca')
print(arredo)

officina = {
    'ruote':3,
    'bulloni':2,
    'tenaglie':5
}
print(officina['ruote'])
officina['ruote'] = officina['ruote'] +1
officina['bulloni'] = officina['tenaglie']
print(officina)

diz = {'a':'b'}
diz['a'] = 'a'
print(diz)

diz = {'1':'2'}
diz['1'] = diz['1'] + 'ab'
print(diz)

diz = {1:2}
diz[1] = diz[1] + 5
print(diz)

d1 = {1:2}
d2 = {2:3}
d1[1] = d2[d1[1]]
print(d1)

cucina = {
    'pentole':3,
    'padelle':7,
    'forcette':20
}

del cucina['padelle']
print(cucina)


diz = {'a':'b'}
#del diz['b']
print(diz)

diz = {'a':'b', 'c':'d'}
del diz['a']
print(diz)

diz = {'a':'b', 'c':'d'}
del diz['a']
#del diz['a']
print(diz)

diz = {'a':'b'}
#new_diz = del diz['a']
print(diz)
#print(new_diz)
print()
diz1 = {'a':'b', 'c': 'd'}
diz2 = diz1
del diz1['a']
print(diz1)
print(diz2)

diz1 = {'a':'b', 'c':'d'}
diz2 = dict(diz1)
del diz1['a']
print(diz1)
print(diz2)

diz = {'a':'b'}
#del diz['c']
print(diz)

diz = {'a':'b'}
#diz.del('a')
print(diz)

diz = {'a':'b'}
diz['a'] = None
print(diz)

scrivania = {
    'carta':5,
    'matite':2,
    'penne':3
}

scrivania['carta'] = scrivania['carta'] -1
del scrivania['penne']
scrivania['temperino'] = 1
print(scrivania)


da_togliere = ['erbacce', 'cartacce']
da_aggiungere = {'tulipani':4,
                 'rose'    :2}

giardino = {
    'ortensie':3,
    'tulipani':7,
    'erbacce' :10,
    'rose'    :5,
    'cartacce':6
}

del giardino[da_togliere[0]]
del giardino[da_togliere[1]]

giardino['tulipani'] = giardino['tulipani'] + da_aggiungere['tulipani']
giardino['rose'] = giardino['rose'] + da_aggiungere['rose']
print(giardino)


en_it = {'hello' : 'ciao',
         'road'  : 'strada'}

it_es = {'ciao' : 'hola',
         'strada' : 'carretera'}

en_es = {}

en_es['hello'] = it_es[en_it['hello']]
en_es['road'] = it_es[en_it['road']]
print(en_es)

print('a' in {'a':5, 'b':7})
print('b' in {'a':5, 'b':7})
print('z' in {'a':5, 'b':7})
print(5 in {'a':5, 'b':7})

print('z' not in {'a':5, 'b':7})
print('a' not in {'a':5, 'b':7})
print(not 'z' in {'a':5, 'b':7})
print(not 'a' in {'a':5, 'b':7})

print(('a', 'b',) in {('a', 'b'):5})
print({'q' not in {'q':0} : 'q' in {'q' : 0}})
print({'a' in 'b'})
print({'a' not in {'b' : 'a'}})
print(len({'a':6, 'b':4}) in {1:2})
print('ab' in {('a','b'):'ab'})
print(None in {})
print(None in {'None':3})
print(None in {None:3})
print(not None in {0:None})

menu = ['aringa', 'burro', 'orata', 'insalata', 'salmone', 'patate',
        'tonno', 'fagioli', 'salmone', 'limone', 'aringa', 'insalata']

cambusa = {'orata':'insalata',
           'salmone':'patate',
           'aringa':'insalata',
           'tonno':'fagioli'}

richiesta = 1

print(menu[richiesta-1] in cambusa and cambusa[menu[richiesta-1]] == menu[richiesta])

richiesta = 3

print(menu[richiesta-1] in cambusa and cambusa[menu[richiesta-1]] == menu[richiesta])

prestiti = {
    'Marco': ['I Miserabili', 'Ulisse'],
    'Gloria': ['Guerra e pace'],
    'Rita': ['Shining', 'Dracula', '1984']
}
print(prestiti['Rita'][1])

lista_rita = prestiti['Rita']
print(lista_rita[2])

prestiti = {
    'Marco': ['I Miserabili', 'Ulisse'],
    'Gloria': ['Guerra e pace'],
    'Rita': ['Shining', 'Dracula', '1984']
}

print('rita ha preso in prestito', len(prestiti['Rita']), 'libri')
print('tutti hanno preso almeno un libro?', len(prestiti['Marco']) > 0 and len(prestiti['Gloria']) > 0 and len(prestiti['Rita']) > 0)
print('primo libro preso in prestito da gloria è', prestiti['Gloria'][0])
print('ultimo libro preso in prestiro da rita è', prestiti['Rita'][-1])

mappa = {
    'Baia dello squalo' : ['squali'],
    'Estuario della Malasorte' : ['coccodrilli', 'pirana'],
    'Fossa del Naufragio' : ['orche assassine', 'pesci tigre']
}

luogo = 'Estuario della Malasorte'
pericoli = ['murene', 'polpo blu maculato']
viaggio = 'Largo delle Vele Sommerse'
esplorazione = ['barracuda', 'meduse']

mappa[luogo].append(esplorazione[1])
mappa[viaggio] = mappa[luogo]
mappa[viaggio].append(esplorazione[0])
print(mappa)

mappa1 = {
    'Baia dello squalo' : ['squali'],
    'Estuario della Malasorte' : ['coccodrilli', 'pirana'],
    "Mare della Burrasca" : ["barracuda", "meduse"],
}

mappa2 = {
    "Estuario della Malasorte" : ["murene", "pesci tigre"],
    "Mare della Burrasca" : ["polipi giganti"],
    "Fossa del Naufragio" : ["orche assassine"],
    "Lago dei Disperati" : ["vortici d'acqua"]
}

nuova = mappa1
nuova['Estuario della Malasorte'].append(mappa2['Estuario della Malasorte'][0])
nuova['Estuario della Malasorte'].append(mappa2['Estuario della Malasorte'][1])
nuova['Mare della Burrasca'].append(mappa2['Mare della Burrasca'][0])

mappa1 = {
    'Baia dello squalo' : ['squali'],
    'Estuario della Malasorte' : ['coccodrilli', 'pirana'],
    "Mare della Burrasca" : ["barracuda", "meduse"],
}

mappa2 = {
    "Estuario della Malasorte" : ["murene", "pesci tigre"],
    "Mare della Burrasca" : ["polipi giganti"],
    "Fossa del Naufragio" : ["orche assassine"],
    "Lago dei Disperati" : ["vortici d'acqua"]
}

luogo1, luogo2 = 'Estuario della Malasorte', 'Mare della Burrasca'

import copy

nuova = copy.deepcopy(mappa1)
nuova[luogo1].extend(mappa2[luogo1])
nuova[luogo2].extend(mappa2[luogo2])

from pprint import pprint
print('Nuova:')
pprint(nuova)
print('Mappa1')
pprint(mappa1)
print('mappa2')
pprint(mappa2)

print({'a':3, 'b':4} == {'a':3, 'b':4})
print({{'a':3, 'b':4} == {'c':3, 'b':4}})
print({'a':3, 'b':4} == {'a':3, 'b':999})
print({'a':3, 'b':4} == {'a':3})
print({'a':3, 'b':4} == {'a':3, 'b':3, 'c':5})
print({'a':3, 'b':4} == {2:('q','p'), 'b':[99,77]})

print({'a':3, 'b':4} == {'b':4, 'a':3})

diz = {}
diz['a'] = 5
diz['b'] = 7

diz1 = {}
diz1['b'] = 7
diz1['a'] = 5

print(diz == diz1)
print({1:2} == {2:1})
print({1:2, 3:4} == {3:4, 1:2})
print({'a'.upper():3} == {'a':3})
print({'A'.lower():3} == {'a':3})
print({'a': {1:2} == {3:4}})

diz1 = {'a':3,'b':8}
diz2 = diz1
diz1['a'] = 7
print(diz1 == diz2)

diz1 = {}
diz1['a'] = 3
diz2 = diz1
diz2['a'] = 4
print(diz1 == diz2)

diz1 = {'a':3, 'b':4, 'c':5}
diz2 = {'a':3, 'c':5}
del diz1['a']
print(diz1 == diz2)

diz1 = {}
diz2 = {'a':3}
diz1['a'] = 3
diz1['b'] = 5
diz2['b'] = 5
print(diz1 == diz2)

diz1 = {'a':3,
        'b':8}
diz2 = {'a':diz1['a'],
        'b':diz1['b']}
diz1['a'] = 6
print('uguali?', diz1 == diz2)
print(diz1)
print(diz2)

diz1 = {'a':[1,2],
        'b':[4,5,6]}
diz2 = dict(diz1)
diz1['a'].append(3)
print('uguali?', diz1 == diz2)
print(diz1)
print(diz2)

import copy
diz1 = {'a':[1,2],
        'b':[4,5,6]}
diz2 = copy.deepcopy(diz1)
diz1['a'].append(3)

print('uguali?', diz1 == diz2)
print(diz1)
print(diz2)

diz1 = {'a':[4,5],
        'b':[6,7]}
diz2 = dict(diz1)
diz2['a'] = diz1['b']
diz2['b'][0] = 9
print(diz1 == diz2)
print(diz1)
print(diz2)

da = {'a':['x', 'y', 'z']}
db = dict(da)
db['a'] = ['w','t']
dc = dict(db)
print(da)
print(db)
print(dc)

la =[1,2,3,4]
lb = la.copy()
la.append(8)
print(la,lb)

la = ['x', 'y', 'z']
diz1 = {'a': la,
        'b': la}
diz2 = copy.deepcopy(diz1)
diz2['a'][0] = 'w'
print(diz1 == diz2)
print(diz1)
print(diz2)

import pprint
s = 'ZOOM'
s = list(s)

diz = {
    'a': s,
    'b': s,
    'c': s
}

diz['a'][0] = 'D'
pprint.pprint(diz)

verdure = {
    'carote':5,
    'pomodori':8,
    'cavoli':3
}

print(verdure.keys())

chiavi = verdure.keys()
verdure['patate'] = 8

print(chiavi)

come_lista = list(verdure.keys())
print(come_lista)
verdure['cetrioli'] = 9
print(come_lista, verdure.keys(), verdure.values())

diz = {
    'a':4,
    'b':5
}
chiavi = diz.keys()

diz = {'a':1,'b':2}
s = set(diz.keys())
s.add(('c',3))
print(diz)
print(s)

diz = {'a':3,'b':4}
k = diz.keys()
diz['c'] = 5
print(len(k))

diz = {'a':'x','b':'y'}
print('a' in diz.keys())

diz1 = {'a':1,'b':2}
chiavi = diz1.keys()
diz2 = dict(diz1)
diz2['c'] = 3
print('diz1=',diz1)
print('diz2=',diz2)
print('chiavi=',chiavi)

diz1 = {'a':'b','c':'d'}
diz2 = {'a':'b','b':'c'}
print( set(diz1.keys()) - set(diz2.keys()) )

diz1 = {'a':'b','c':'d'}
diz2 = {'e':'a','f':'c'}
chiavi = diz1.keys()
del diz1[diz2['e']]
del diz1[diz2['f']]
print(len(chiavi))

diz = {'c':6, 'b':2, 'a':5}
print(list(diz.keys()))

diz = {'c':6, 'b':2, 'a':5}
lista = list(diz.keys())
lista.sort()
print(lista)

diz1 = {
    'a':5,
    'b':9,
    'e':2
}
diz2 = {
    'a':9,
    'c':2,
    'e':2,
    'f':6
}

lista = list(diz1) + list(diz2)
lista = list(set(lista))
lista.sort()
print(lista)

diz1 = {
        'a':5,
        'b':9,
        'e':2,}

diz2 = {
        'a':9,
        'c':2,
        'e':2,
        'f':6}

chiavi = list(set(diz1.keys()) | set(diz2.keys()))
chiavi.sort()
print(chiavi)

veicoli = {
    'AA111AA' : 'Mario',
    'BB222BB' : 'Lidia',
    'CC333CC' : 'Mario',
    'DD444DD' : 'Gino',
    'EE555EE' : 'Gino'
}

proprietari = veicoli.values()
print(proprietari)

veicoli['FF666FF'] = 'Paola'
print(proprietari)

d = {0:'a',
1:'b',
2:'b'}
vs = d.values()
d[2]='c'
print(vs)

diz = {
    0:1,
    1:2,
    2:3
}

diz[list(diz.values())[0]-1]

diz = {
    'a':3,
    'c':6,
    'g':8
}

print(diz.keys(), diz.values())
print(len(diz.keys()) == len(set(diz.values())))

diz = {'x' : 5,
'y' : 7,
'z' : 5}
print(diz.keys(), diz.values())
print(len(diz.keys()) == len(set(diz.values())))

diz = {
'a':'b',
'b':'f',
'c':'b',
'd':'e'
}

borsa = list(set(list(diz.keys()) + list(diz.values())))
borsa.sort()
print(borsa)

diz1 = {
'a':4,
'k':2,
'm':5
}
diz2 = {
'b':2,
'e':3,
'g':9,
'h':1
}

print('Hanno valori uguali?', len(set(diz1.values())) & len(set(diz2.values())) > 0)

diz = {
    14:1,
    11:7,
    7:3,
    70:5
}

chiavi = min(diz.keys())
valori = max(diz.values())
print(chiavi == valori)

vacanza = {
    'Piazza S.Marco':'Venezia',
    'Fontana di Trevi':'Roma',
    'Uffizi':'Firenze'
}

print(vacanza.items())

attrazioni = vacanza.items()
vacanza['Palazzo Ducale'] = ['Venezia']

print(attrazioni)

print({'a':7, 'b':9}.items())

print(dict({'a':7, 'b':5}.items())['a'])

print(len(set({'a':'b', 'a':'B'}.items())))

diz1 = {'a':7,
        'b':5}
diz2 = dict(diz1.items())
diz1['a'] = 6
print(diz1 == diz2)

print(('a','b') in {'a':('a','b'), 'b':('a', 'b')}.items())
print({'a':('a','b'), 'b':('a', 'b')}.items())
print(('a','b') in list({'a':('a','b'), 'b':('a','b')}.items())[0])
print(list({'a':('a','b'), 'b':('a','b')}.items()))

diz1 = {'a':4,
'b':7}
diz2 = {'c':5,
'd':8,
'e':2}

diz1 = list(diz1.items())
diz2 = list(diz2.items())
diz3 = dict(diz1 + diz2)
#diz3 = dict(list(diz1.items()) + list(diz2.items()))
print(diz3)

diz1 = {
    'capre':6,
    'cavoli':9,
    'pastori':1
}

diz2 = {
    'capre':12,
    'cavoli':15,
    'panche':3,
    'fieno':7
}

diz1.update(diz2)
print(diz1)
diz1.update([('fieno', 3), ('panche', 18), ('stalle', 4)])
print(diz1)

diz = {
        'a':'x',
        'b':'y',
        'c':'z',
        'd':'w'
}
s = "bx;cw;ex"

diz[s[0]] = s[1]
diz[s[3]] = s[4]
diz[s[6]] = s[7]

print(diz)

diz = {
        'a':'x',
        'b':'y',
        'c':'z',
        'd':'w'
}
s = "bx;cw;ex"
la = s.split(';')
diz.update(la)
print(diz,la)

from collections import OrderedDict
od = OrderedDict()

od['qualche chiave'] = 5
od['qualche altra chiave'] = 7
od[('una', 'tupla', 'immutabile', 'come chiave')] = 3
od['un\'altra chiave'] = 'adesso una stronga'
od[123] = 'hello'
print(od)

from collections import OrderedDict

od = OrderedDict()
t1 = ('Alice', '143242903')
t2 = ('Bob', '417483437')
t3 = ('Carlo', '423413213')
od[t1[0]] = t1[1]
od[t2[0]] = t2[1]
od[t3[0]] = t3[1]
print(od)

from collections import OrderedDict

t1 = ('Alice', '143242903')
t2 = ('Bob', '417483437')
t3 = ('Carlo', '423413213')
od = OrderedDict([t1,t2,t3])
od1 = dict([t1,t2,t3])
print(od1)
print(dict(od))

from collections import OrderedDict

ord1 = OrderedDict()
ord1['dog'] = 'cane'
ord1['home'] = 'casa'
ord1['table'] = 'tavolo'

ord2 = OrderedDict(ord1)
ord2['water'] = 'acqua'
print('ord1=', ord1)
print('ord2=', ord2)

from collections import Counter

a = list('cantarellando')
isto = Counter(a)
print(isto)

print(isto.most_common(4))

ct = Counter((50,70,40,60,40,50,40,70,50,50,50,60,50,30,50,30,40,50,60,70))
print(ct)

cs = Counter('rebbrividirai')
print(cs)

from collections import Counter

s = 'rattristato'
cs = Counter(s)
cs_più = cs.most_common()[0]
cs_meno = cs.most_common()[-1]
print(cs)
print('Tra i più frequenti troviamo', cs_più)
print('Tra i meno frequenti troviamo', cs_meno)
print('Vi sono', len(set(cs.values())), 'frequenze diverse', set(cs.values()))

from pprint import pprint
matrimoni =  ["Amilcare-Maria Eusonia", "Oronzo Pio-Genoveffa", "Venceslao-Elvira"]
prima = matrimoni[0].split('-')
seconda = matrimoni[1].split('-')
terza = matrimoni[2].split('-')

diz = {
    prima[0] : prima[1],
    seconda[0] : seconda[1],
    terza[0] : terza[1]
}
pprint(diz)

matrimoni = ["Liutprando-Brunilde", "Clodoveo-Elvira Pancrazia Ludmilla", "Gian␣Evaristo-Ubalda"]
prima = matrimoni[0].split('-')
seconda = matrimoni[1].split('-')
terza = matrimoni[2].split('-')

diz = {
    prima[0] : prima[1],
    seconda[0] : seconda[1],
    terza[0] : terza[1]
}
pprint(diz)

ristorante, pesci = "Il Galeone", "carpe" 

registro = {
            "L'Ancora" : ['aringhe', 'carpe'],
            "Il Galeone": ['merluzzi', 'carpe', 'trote'],
            "Al Molo" : ['trote'],
            "La Cambusa": ['aringhe', 'carpe'],
}

print(pesci in registro[ristorante])

ristorante, pesci = "Il Galeone", "aringhe" 

registro = {
            "L'Ancora" : ['aringhe', 'carpe'],
            "Il Galeone": ['merluzzi', 'carpe', 'trote'],
            "Al Molo" : ['trote'],
            "La Cambusa": ['aringhe', 'carpe'],
}

print(pesci in registro[ristorante])

caramelle = 20

if caramelle > 10:
    print('Abbiamo trovato...')
    print('Tante caramelle!')
else:
    print('Purtroppo ci sono...')
    print('Poche caramelle!')

print(caramelle > 10)

caramelle = 5

if caramelle > 10:
    print('Abbiamo trovato...')
    print('Tante caramelle!')
else:
    print('Purtroppo ci sono...')
    print('Poche caramelle!')

print(caramelle > 10)

caramelle = 5

if caramelle > 10:
    print('Abbiamo trovato')

print('Cerchiamo altri dolci')


x = 3
if x > 2 and x < 4:
    print('ABBA')

if 2<x<4:
    print('ABBA')

if x > 2 :
    print('abba')

x = 2
if x > 1:
    print(x+1, x)#:

x = 3
if x > 5 or x:
    print('ACDC')

x = 7
if x==7:
    print('GLAM')

x = 7
if x < 1:
    print('BIM')
else:
    print('BUM')
print('BAM')

x = 30
if x > 8:
    print('DOH')
if x > 10:
    print('DUFF')
if x > 20:
    print('BURP')

if not True:
    print('sottosopra')
else:
    print('soprasotto')

if False:
    pass
else:
    print('ZORB')

if 0:
    print('Brandy')
else:
    print('Rum')

if False:
    print('illustrissimo')
else:
    print('esimio')
#else:
#    print('dottore')

if 2 != 2:
    'ATTENTO'
else:
    'STOLTO'

if 2 != 2:
    print('ATTENTO')
else:
    print('STOLTO')

x = [1,2,3]
if 4 in x:
    x.append(4)
else:
    x.remove(3)
print(x)

if 'False':
    print('OCCHIO ALLA STRINGA')
else:
    print('CRUDELE')

benzina = 5

if benzina < 30:
    print('Senza benza, faccio il pieno')
    benzina += 20
    print('Si riparte con', benzina, 'litri di benzina')
else:
    print('Ho abbastanza carburante')

caramelle = 0

if caramelle > 10:
    print('Abbiamo trovato...')
    print('Tante caramelle!')
elif caramelle > 0:
    print('Purtroppo ci sono...')
    print('Poche caramelle!')
else:
    print('Che sfortuna!')
    print('Non ci sono caramelle!')

print()
print('Cerchiamo altri dolci!')

caramelle = -2

if caramelle > 10:
    print('Abbiamo trovato...')
    print('Tante caramelle!')
elif caramelle > 0:
    print('Purtroppo ci sono...')
    print('Poche caramelle!')
elif caramelle == 0:
    print('Che sfortuna!')
    print('Non ci sono caramelle!')
else:
    print('Qualcosa è andato MOLTO storto! Abbiamo trovato', caramelle, 'caramelle')

print()
print('Cerchiamo altri dolci!')

y = 2
if y < 3:
    print('bingo')
elif y <= 2:
    print('bango')

y = 2
if y <= 2:
    print('bu')

z = 'q'
if not 'quando'.startswith(z):
    print('BAR')
elif not 'spqr'[2] == z:
    print('WAR')    
else:
    print('ZAR')

x = 1
if x < 5:
    print('BARCHE')
elif x > 3:
    print('ZATTERE')
else:
    print('SCIALUPPE')

x = 5
if x < 3:
    print('ORO')
elif x >= 3:
    print('ARGENTO')

if 0:
    print(0)
elif 1:
    print(1)

fragole = 5
#fragole = 2
#fragole = 10
print('fragole =', fragole)
print('A:')
if fragole > 5:
    print("Le fragole sono > 5")
elif fragole > 5:
    print("Ho detto che le fragole sono > 5!")
else:
    print("Le fragole sono <= 5")

print('B:')
if fragole > 5:
    print("Le fragole sono > 5")
if fragole > 5:
    print("Ho detto che le fragole sono > 5!")
if fragole <= 5:
    print("Le fragole sono <= 5")

x, y = 3, 5
#x, y = 5, 3
#x, y = 3, 3
print('x =', x)
print('y =', y)
print('A:')
if x > y:
    print(x)
else:
    print(y)
print('B:')
print(max(x,y))

x, y = 3, 5
#x, y = 5, 3
#x, y = 3, 3
print('x =',x)
print('y =', y)
print('A:')
if x < y:
    print(y)
else:
    print(x)
print('B:')
print(min(x,y))

x = 2
print('x = ',x)

print('A:')
if x > 3:
    print('grande')
else:
    print('piccolo')

print('B:')
if x < 3:
    print('piccolo')
else:
    print('grande')

x = 3

print('x =', x)

print('A:')
if x % 5 == 0:
    print('cippirillo')
if x % 3 == 0:
    print('cippirillo')

print('B:')
if x % 3 ==0 or x% 5 == 0:
    print('cippirillo')

#s = 'cane dalmata'
#s = 'gallo cedrone'
s = 'gatto soriano'
if s.startswith('cane'):
    print('BAU!')
elif s.startswith('gallo'):
    print('CHICCHIRICHI!')
else:
    print('???')

acuti = "áéíóú"
gravi =  "àèìòù"

parola = 'urrà'
parola = 'martello'
if parola[-1] in acuti or parola[-1] in gravi:
    print('é accentata')
else:
    print('non è accentata')

arcano = 'La Ruota'
maggiori = ['La Ruota','Il Carro', "L'Appeso"]
minori = ['Asso di Spade', 'Due di Denari', 'Regina di Coppe']

arcano = 'Asso di Spade'
arcano = 'Il Coding'

if arcano in maggiori:
    print(arcano, 'è un arcano maggiore')
if arcano in minori:
    print(arcano, 'è in minori')
else:
    print('è un mistero')

x,y = 5,9
x,y = 5, -2
print('x =', x, 'y =',y)
if x >= 0:
    if y >= 0:
        print('primo quadrante')
    else:
        print('quarto quadrante')
else:
    if y >= 0:
        print('secondo quadrante')
    else:
        print('terzo quadrante')

x,y = 5,9

print('x =',x, 'y =',y)

if x >= 0 and y >= 0:
    print('primo quadrante')
elif x >= 0 and y < 0:
    print('quarto quadrante')
elif x < 0 and y >= 0:
    print('secondo quadrante')
elif x < 0 and y < 0:
    print('terzo quadrante')

x,y = 0,0

if x == 0 and y == 0:
    print('origine')
elif x == 0:
    print('ordinata')
elif y == 0:
    print('ascissa')
elif x > 0:
    if y == 0:
        print('ascissa')
    elif y > 0:
        print('primo quadrante')
    elif y < 0:
        print('quarto quadrante')
else:
    if y == 0:
        print('ascissa')
    elif x > 0:
        print('secondo quadrante')
    else:
        print('terzo quadrante')

zaino, soldi, tessera = True, False, True
if zaino == True and (soldi == True or tessera == True):
    print('go')

zaino, soldi, tessera = True, False, True
trovato = []
if zaino:
    trovato.append('zaino')
    if soldi:
        trovato.append('soldi')
    else:
        print('Non ho i soldi!')
    if tessera:
        trovato.append('tessera')
    if soldi or tessera:
        print('Ho trovato:', ', '.join(trovato))
        print('Posso partire!')
    else:
        print('Non ho la tessere nè i soldi, non posso partire!')
else:
    print('Non ho lo zaino, non posso partire!')

cronometro = '10:23:43'
ore = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
if int(cronometro[:2]) in ore[5:10]:
    print('mattino')
elif int(cronometro[:2]) in ore[11:18]:
    print('pomeriggio')
elif int(cronometro[:2]) in ore[17:21]:
    print('sera')
elif int(cronometro[:2]) in ore[22:]:
    print('sera')

cronometro = '12:00:56'
ora = int(cronometro.split(':')[0]) % 24
if ora >= 6 and ora < 12:
    print('mattina')
elif ora >= 12 and ora < 18:
    print('pomeriggio')
elif ora >= 18 and ora < 21:
    print('sera')
else:
    print('notte')

x = 3
#x = 4
#x = 5
print('x =',x)
print('A:')
if x > 3:
    if x < 5:
        print('dentro')
    else:
        print('fuori')
else:
    print('fuori')
print('B:')
if x > 3 and x < 5:
    print('dentro')
else:
    print('fuori')

x = 2
#x = 3
#x = 4
print('x =', x)
print('A:')
if not x > 3:
    print('stelle')
else:
    print('pianeti')
print('B:')
if x > 3:
    print('pianeti')
else:
    print('stelle')

x = 10
#x = 5
#x = 0
print('x =',x)
print('A:')
if x >= 5:
    print('verde')
    if x >= 10:
        print('rosso')
print('B:')
if x >= 10:
    if x >= 5:
        print('verde')
print('rosso')


x = 7
#x = 0
#x = 15
print('x =', x)
print('A:')
if x > 5:
    if x < 10:
        print('dentro')
    else:
        print('fuori')
else:
    print('fuori')
print('B:')
if not x > 5 and not x < 10:
    print('fuori')
else:
    print('dentro')

x,y,z = 3,7,4

if x > y:
    if x > z:
        print('x è il più grande')
if y > x:
    if y > z:
        print('y è il più grande')
if z > x:
    if z > y:
        print('z è il più grande')

spesa = 200
sconto = 0

if spesa > 100:
    sconto = 0.1
else:
    sconto = 0 #non necessario
print('spesa:', spesa, '  sconto:', sconto)

spesa = 200
sconto = 0.1 if spesa > 100 else 0
print('spesa:', spesa, '  sconto:', sconto)
#variabile = valore if condizione else altro_valore

y = 3
x = 8 if y > 2 else 9
print(x)

scarpe = 15
scarpe = scarpe + 1 if scarpe < 10 else scarpe - 1
print(scarpe)

sa, sb, sc = 'ni','no','tre'
tutte = [sa,sb,sc]
x = 'CIUFCIUF' if 'tre' in tutte and 'ni' in tutte and 'no' in tutte else ':-('
print(x)
    

ginevra = True
merlino = False
morgana = True

if ginevra == True and merlino == True and morgana == True:
    print('Sono tutti veri cavalieri')
elif ginevra == True or merlino == True or morgana == True:
    print('C\'è almeno un vero cavaliere')
else:
    print('Non c\'è nessun vero cavaliere')

piano_utente = 'rialzato'
piano_ascensore = 'terra'
#piano_utente = 'terra'
#piano_ascensore = 'terra'
if piano_utente != piano_ascensore:
    print(piano_ascensore)
    print(piano_utente)
    print('DING')
else:
    print('DING')

sport = ['pallavolo', 'tennis', 'calcio', 'nuoto']

for elemento in sport:
    print('Trovato un elemento!')
    print(elemento)

print('Finito')

sport = ['pallavolo', 'tennis', 'calcio', 'nuoto']
for nome in sport:
    print('Trovato elemento!')
    print(nome)

sport = ['pallavolo', 'tennis', 'calcio', 'nuoto']
prova = 'ciao'

for prova in sport:
    print(prova)
print(prova)

for carattere in 'ciao':
    print(carattere)

for parola in ('sto', 'visitando', 'una', 'tupla'):
    print(parola)

for i in [1,2,3]:
    print(i)

for x in [7]:
    print(x)

for i in []:
    print('gurb')

for i in [1,'2',3]:
    print(type(i))

for i in 'abc':
    print(i)

for x in ((4,5,6)):
    print(x)

for x in [[1], [2,3], [4,5,6]]:
    print(x)

x = 5
for x in ['a', 'b', 'c']:
    print(x)
print(x)

for x in [1,2,3,4,5,6,7,8]:
    if x % 2 == 0:
        print(x)

la = [4,5,6]
for x in la:
    print(x)
la.reverse()
for x in la[1:]:
    print(x)

viaggio1 = ['Marrakesh','Fez','Bazaar','Kasbah']
viaggio2 = ['Koutoubia', 'El Badii', 'Chellah']

print('Inizia il primo viaggio')
for i in viaggio1:
    print('     Tu: Andiamo a', i,'!')
    print('Tappeto: Ho sentito e obbedisco!')
print('Fine del primo viaggio')

print('Inizia il secondo viaggio')
for i in viaggio2:
    print('     Tu: Andiamo a', i,'!')
    print('Tappeto: Ho sentito e obbedisco!')
print('Fine del secondo viaggio')

numeri = [3,4,1,5,12,7,9]
s = 0
for i in numeri:
    if i % 2 == 0:
        s += i
print(s)

s = 'birbantello'
for i in s:
    print(i.upper(), i)

parola = 'dirigibile'

belli = 'abcd'
brutti = 'efgh'
cattivi = 'ilm'

for i in parola:
    if i in belli:
        print(i, 'bello')
    elif i in brutti:
        print(i, 'brutto')
    elif i in cattivi:
        print(i, 'cattivo')
    else:
        print(i,'non mi interessa')

coda = ['Console','Notaio','Scheletro','Rettore','Goblin','Vampiro', 'Gioielliere']
sgraditi = {'Vampiro','Goblin','Scheletro'}
ammessi = []

print('Aprite le porte!\n')

for i in coda :
    print('Buonasera signor', i)
    if i not in sgraditi:
        print('Prego eccellenza, entri pure')
        ammessi.append(i)
    else:
        print('Ferruccio, vuoi prenderti cura del signor', i, '?')
    print('Avanti il prossimo!')
print('Sono stati ammessi i signori', ', '.join(ammessi))

recipienti = [5,1,7,4,3,9,5,2,7,3]
capienza =  15

bilancia = 0
sacchi = 0
for i in recipienti:
    print('Raccolto', i, 'kg')
    bilancia += i
    print('La bilancia segna', bilancia, 'kg')
    if bilancia >= 15:
        print('Abbiamo raggiunto la capacità di', bilancia, 'kg, avanzano', bilancia - 15, 'kg\n')
        bilancia = bilancia - capienza
        sacchi += 1
print('Abbiamo riempito', sacchi, 'sacchi\n')

for i in range(5):
    print(i)
print('\n')

for i in range(3,7):
    print(i)
print('\n')

for i in range(4,18,2):
    print(i)
print('\n')

for i in range(5,0,-1):
    print(i)
print('\n')

for i in range(5,-1,-1):
    print(i)
print('\n')

for x in range(1):
    print(x)
print('\n')

for x in range(-1):
    print(x)
print('\n')

#for 'm' in range(3):
 #   print('m')

for x in range(6,4,-1):
    print(x)
print('\n')

for x in range(1,0,-1):
    print(x)
print('\n')

for x in range(3,-3,2):
    print(x)
print('\n')

x = 3
for i in range(x):
    print(i)
print('\n')
for i in range(x,2*x):
    print(i)
print('\n')

for x in range((3)):
    print(x)
print('\n')

for i in range(4):
    print('Il doppio di', i, 'è', i*2)
print('\n')

k,b = 3,15

print('Multipli di,', k)
for i in range(k,b+1,k):
    print(i)
print('\n')
print('Non divisibili per', k)
for i in range(k+1, b):
    if i % k != 0:
        print(i)
print('\n')

a,b = 7,9
minimo = min(a,b)
massimo = max(a,b)
for i in range(minimo, massimo+1):
    print(i)
print('\n')

for i in range(1,36):
    if i % 3 == 0 and i % 5 == 0: #if % 15 == 0
        print('FIZZBUZZ')
    elif i % 3 == 0:
        print('FIZZ')
    elif i % 5 == 0:
        print('BUZZ')
    else:
        print(i)

sport = ['pallavolo', 'tennis', 'calcio', 'nuotol']

for i in range(len(sport)):
    print('posizione',i)
    print(sport[i])

cucina = ['dado', 'minestrina', 'uova', 'torta', 'sugo', 'pasta', 'ragu', 'lasagne']

for i in range(0, len(cucina)-1, 2):
    print(cucina[i], cucina[i+1])

la = ['n','e','o','n']
lb = ['s','h','o','w']

for i, j in zip(la,lb):
    print(i,j)

la = ['n','e','o','n']
lb = ['s','h','o','w']

for i in range(len(la)):
    print(la[i], lb[i])

emozioni = ['Paura', 'Rabbia','Tristezza','Gioia','Disgusto','Estasi']
grado = [-1, -1, -1, 1, -1, 1]

for i in range(len(emozioni)):
    if grado[i] == -1:
        print(emozioni[i],': negativa')
    else:
        print(emozioni[i],': positiva')


s = 'organetto'

for i in range(len(s[-5:])):
    print(s[-5+i:])

s = 'organetto'
for i in range(s.index('n'), len(s)):
    print(s[i:])

s = 'sghiribizzo'

for i in range(len(s)):
    print(s[:i+1])
    print(' '*1,s[i+1:])

s1 = "ATACATATAGGGCCAATTATTATAAGTCAC"
s2 = "CGCCACTTAAGCGCCCTGTATTAAAGTCGC"
stringa = []
for i, j in zip(s1,s2):
    if i == j:
        stringa.append('|')
    else:
        stringa.append(' ')

print(s1)
print(''.join(stringa))
print(s2)

s1 = "ATACATATAGGGCCAATTATTATAAGTCAC"
s2 = "CGCCACTTAAGCGCCCTGTATTAAAGTCGC"

lista = []
for i in range(len(s1)):
    if s1[i] == s2[i]:
        lista.append('|')
    else:
        lista.append(' ')
barre = ''.join(lista)

print(s1)
print(barre)
print(s2)

s = 'sportello'

if len(s) % 2 == 1:
    mezzo = (len(s) // 2) + 1
else:
    mezzo = (len(s) // 2)

for i in range(mezzo):
    print(s[i])
for i in range(mezzo, len(s)):
    print(s[i].upper())

versi = {'cane':'Bau!',
        'gatto':'Miao!',
        'mucca':'Muu!',
        'pecora':'Bee!'}
stanze = [('cane', 'pecora'),
        ('gatto','mucca'),
        ('mucca', 'cane')]

count = 0
for gruppo_animale in stanze:
    count += 1
    print('Nella stanza',count, 'si sentonono',versi[gruppo_animale[0]],'e', versi[gruppo_animale[1]])
print()

versi = {'cane':'Bau!',
        'gatto':'Miao!',
        'mucca':'Muu!',
        'pecora':'Bee!'}
stanze = [('cane', 'pecora'),
        ('gatto','mucca'),
        ('mucca', 'cane')]

for i in range(len(stanze)):
    stanza = stanze[i]
    print('Nella stanza', i+1, 'si sentono', versi[stanza[0]], 'e', versi[stanza[1]])

# 0 1 2 3 4 5
pokemon = ['Charizard','Gengar','Arcanine','Bulbasaur','Blaziken','Umbreon',
# 6 7 8 9 10 11
            'Lucario','Gardevoir','Eevee','Dragonite', 'Volcarona', 'Sylveon' ]
g = 3
count = 0
count1 = 0
for i in range(g):
    count1 += 1
    print('gruppo', count1,':' ,' e '.join(pokemon[count:len(pokemon)//g+count]))
    count += len(pokemon) // g
print()

# 0 1 2 3 4 5
pokemon = ['Charizard','Gengar','Arcanine','Bulbasaur','Blaziken','Umbreon',
# 6 7 8 9 10 11
            'Lucario','Gardevoir','Eevee','Dragonite', 'Volcarona', 'Sylveon' ]
g = 4
count = 0
count1 = 0
for i in range(g):
    count1 += 1
    print('gruppo', count1,':' ,' e '.join(pokemon[count:len(pokemon)//g+count]))
    count += len(pokemon) // g
print()

pokemon = ['Charizard','Gengar','Arcanine','Bulbasaur','Blaziken','Umbreon',
# 6 7 8 9 10 11
            'Lucario','Gardevoir','Eevee','Dragonite', 'Volcarona', 'Sylveon' ]
g = 4

k = len(pokemon) // g

for i in range(0, g):
    print('gruppo', i + 1, ':', ' e '.join(pokemon[i*k:(i+1)*k]))

la = ['a', 'b', 'c']

print(la*2)

lista = [1,2,3,4,5]
for i in lista:
    lista.remove(i)
    print(i)

la = ['a', 'b', 'c']

lb = la.copy()
print(lb)

for i in la:
    lb.append(i)
    print(i)

print(lb)

la = ['a', 'b', 'c']

for elemento in list(la):
    la.append(elemento)

print(la)

la = ['m', 'a', 'r', 't', 'e', 'l', 'l', 'o']

for i in range(len(la)):
    if i % 2 == 0:
        la[i] = 'z'
print(la)

sa, sb = 'gibbone', 'ORANGUTANG'
sc = []

for i in zip(sa, sb):
    sc.append(''.join(i))
sc = ''.join(sc)
if len(sa) > len(sb):
    Lan = len(sa) - len(sb)
    sc = sc + sa[-Lan:]
elif len(sa) < len(sb):
    Lan = len(sb) - len(sa)
    sc = sc + sb[-Lan:]
print(sc)

cesta = ['fragola', 'melone', 'ciliegia', 'anguria', 'mela', 'melone','anguria', 'mela']
preferita = {'ciliegia', 'mela', 'fragola'}
piatto = []

for i in cesta:
    if i in preferita:
        piatto.append(i)
        cesta.remove(i)
print(cesta)
print(piatto)

#break = chiudi il ciclo
#continue = salta questa operazione

for x in 'lavato':
    if x == 't':
        print('Break, esce dal ciclo')
        break
        print('Dopo il break')
    print(x)
print('Finito il for numero 1')

i = 1
for x in 'lavato':
    if x == 'a':
        print('continue, salta all\'elemento successivo')
        continue
        print('Dopo il continue')
    print(x)
print('Finito il for numero 2')

i = 1
for x in 'lavato':
    if x == 'a':
        print('continue, salta all\'elemento successivo')
        continue
    if x == 't':
        print('break, esce dal ciclo')
    print(x)

print('Ciclo finito')

for x in ['a', 'b', 'c']:
    print(x)
    break

for x in ['a', 'b', 'c']:
    print(x)
    break
    print('Glam')

for x in [1,2,3]:
    print(x)
    break
    break

for x in [1,2,3]:
    break
    print(x)

for x in [1,2,3]:
    print(x)

for x in [1,2,3]:
    continue
    print(x)

for x in [1,2,3]:
    print(x)
    continue

for x in [1,2,3]:
    print(x)
    continue
    print('gdf')

for x in [1,2,3]:
    break
    1/0
print('BAD KARMA')

for x in range(8):
    if x < 4:
        continue
    print('ZAM', x)

for x in range(8):
    if x >= 4:
        break
    print('ZUM', x)

for x in ['M', 'C', 'M']:
    print(x)
    for y in ['S', 'P', 'Q', 'R']:
        print(y)
        break

for x in range(6):
    if x % 2 == 0:
        continue
    print(x)

for x in ['M', 'C', 'M']:
    print(x)
    break
    for y in ['S', 'P', 'Q', 'R']:
        print(y)
print()
for x in ['M', 'C', 'M']:
    print(x)
    for y in ['S', 'P', 'Q', 'R']:
        print(y)
        continue

print()
for x in ['M', 'C', 'M']:
    print(x)
    continue
    for y in ['S', 'P', 'Q', 'R']:
        print(y)

parola = 'continuamente'

for i in parola:
    if i in 'aeiou':
        continue
    else:
        print(i)

stringa = 'cascapirillabadgnippobadzarpogno'
bad_pos = stringa.index('bad')

for i in range(len(stringa)):
    if i == bad_pos:
        break
    else:
        print(stringa[i])


stringa = 'cascapirillabadgnippobadzarpogno'
stringa = 'sobad'
for i in range(len(stringa)):
    if stringa[i:i+3] == 'bad':
        break
    else:
        print(stringa[i])

frase = 'Ad un certo punto bisogna fermarsi. Mai oltrepassare il limite.'
for i in frase.split():
    if i[-1] == '.':
        print(i[:-1])
        break
    print(i)

frase = 'Ad un certo punto bisogna fermarsi. Mai oltrepassare il limite.'
for parola in frase.split():
    if '.' in parola:
        print(parola[:-1])
        break
    print(parola)

musica = ['unz','pa','pa','tud','unz','pa','pa','tud','unz','boom','boom','tud']

count_pa = 0
for i in musica:
    if i == 'pa':
        count_pa += 1
        if count_pa == 3:
            print(i)
            print('BREAKDANCE!')
            break
    print(i)
print()
musica = ['unz','pa','pa','tud','unz','pa','pa','tud','unz','boom','boom','tud']

count_pa = 0
for i in musica[::-1]:
    if i == 'pa':
        count_pa += 1
        if count_pa == 3:
            print(i)
            print('BREAKDANCE!')
            break
    print(i)    

sequenza = "IMPERTINENZA"

triple = []
for i in range(len(sequenza)):
    if i % 3 == 0:
        triple.append(sequenza[i:i+3])
print(triple)

parola, ripetizioni = 'rospo', '14323'
nuovo = []
for i in range(len(parola)):
    nuovo.append(parola[i]*int(ripetizioni[i]))
print(''.join(nuovo))

partecipanti = ['Marta','Peppo','Elisa','Gioele','Rosa']

count = 0
for i in list(partecipanti):
    partecipanti.append(i+'-'+ str(partecipanti.index(i)+1))
    count +=1
partecipanti = partecipanti[count:]
print(partecipanti)

partecipanti = ['Marta','Peppo','Elisa','Gioele','Rosa']
for i in range(len(partecipanti)):
    partecipanti[i] = partecipanti[i] + '-' + str(i+1)
print(partecipanti)

cerca = 'à'
frase = "Questa città è piena di babbà, bignè e caffè"

lista = []
for i in frase.split():
    if cerca in i:
        if i[-1] == ',':
            i = i[:-1]
            lista.append(i)
        else:
            lista.append(i)
print(lista)

pietre = [9, 7, 6, 8, 7]
oracolo = [True, False, True, True, False]

sacca = []
for i in range(len(pietre)):
    if oracolo[i] == True:
        sacca.append(pietre[i])
print(sacca)

frase = "La strada si inerpica lungo il ciglio della montagna"

lunghezze = []
for i in frase.split():
    lunghezze.append(len(i))

print(max(lunghezze))

viaggio = "Attraversarono deserti, guadarono fiumi, si inerpicarono sui monti, e infine arrivarono al Tempio"
location = []
for i in viaggio.split():
    if i[-1] == ',':
        location.append(i[:-1])
print(location)

lista = [0, 0, 0, 0, 4, 0, 0, 0, 0]

m = len(lista) // 2

count = 0
for i in range(len(lista)):
    lista[i] = count
    if lista[i] == m:
        break
    count += 1

count = m
for i in range(len(lista[m:])):
    lista[m+i] = count
    count -= 1
    #print(lista)
print(lista)

lista = [5, 3, 8]
res = []
for i in lista:
    res.append((i,i*2))
print(res)

t = ('c', 'a', 'p', 'i', 'r', 'e')
t = ('t','a','p','p','e','t','o')
ris = []
#i = 0
#for i tra 0 e 5 ogni 2
for i in range(0, len(t)-1,2):
    ris.append((t[i], t[i+1]))
if len(t) % 2 == 1:
    ris.append((t[-1],))
print(ris)

t = ('c', 'a', 'p', 'i', 'r', 'e')
t = ('t','a','p','p','e','t','o')
ris = []

if len(t) % 2 == 0:
    for i in range(0, len(t), 2):
        ris.append((t[i], t[i+1]))
elif len(t) % 2 == 1:
    for i in range(0, len(t)-1, 2):
        ris.append((t[i], t[i+1]))
    ris.append((t[-1],))

print(ris)

for elemento in {'questo', 'è', 'un', 'insieme'}:
    print(elemento)

s = set()
s.add('pan')
s.add('de')
s.add('mo')
s.add('nio')
print(s)

for x in set(['a']) | set(['b']):
    print(x)

for x in set(['a']) & set(['b']):
    print(x)

viti = [[5,8], [7,4], [2,9], [8,2], [7,4],[2,6], [8,3], [2,6], [8,3], [8,3], [5,8]]
cacciaviti = [[8,2], [1,3], [5,8], [2,5], [1,3]]

mancanti = []
for vite in viti:
    if vite not in cacciaviti:
        mancanti.append(vite)

mancanti2 = set()
for elementi in mancanti:
    elementi = tuple(elementi)
    mancanti2.add(elementi)

print(mancanti2)

viti = [[5,8], [7,4], [2,9], [8,2], [7,4],[2,6], [8,3], [2,6], [8,3], [8,3], [5,8]]
cacciaviti = [[8,2], [1,3], [5,8], [2,5], [1,3]]

viti_set = set()
cacciaviti_set = set()

for x,y in viti:
    viti_set.add((x,y))
for x,y in cacciaviti:
    cacciaviti_set.add((x,y))

temp = list(viti_set - cacciaviti_set)
temp.sort()
richiesti = []
for x,y in temp:
    richiesti.append([x,y])

print(richiesti)

diz = {
    'bigne':5,
    'brioche':8,
    'krapfen':2
}

for chiave in diz:
    print('Trovata chiave', chiave)
    print('     con valore', diz[chiave])

for chiave, valore in diz.items():
    #print(chiave, valore)
    print('Trovata chiave', chiave)
    print('     con valore', diz[chiave])

print(diz.items())

for valore in diz.values():
    print('Trovato valore', valore)

for x in {1:'a', 2:'b', 3:'c'}:
    print(x)

for x in {'a':1, 'b':2, 'c':3}:
    print(x)

diz = {'a':1, 'b':2, 'c':3}
for x in diz:
    print(diz[x])

diz = {'a':1, 'b':2, 'c':3}
for x in diz:
    if x == 'b':
        print(diz[x])

#for k,v in {'a':1, 'b':2, 'c':3}:
    #print(k,v)

for x in {'a':1, 'b':2, 'c':3}.values():
    print(x)

for x in {'a':1, 'b':2, 'c':3}.items():
    print(x)

for x,y in {'a':1, 'b':2, 'c':3}.items():
    print(x,y)

diz = {
'p':'t',
'o':'i',
's':'n',
}
print('A:')
for x in diz.keys():
    print(x)
print('\nB:')
for y in diz:
    print(y)

diz = {
'c':'t',
'o':'e',
'r':'l',
}
print('A:')
for p,q in diz.items():
    print(q)
print('\nB:')
for x in diz.values():
    print(x)

diz = {
'g':'l',
'e':'e',
'l':'g',
}
print('A:')
for x in diz.values():
    print(x)
print('\nB:')
for z in diz.items():
    print(z[0])

diz = {
'p':'g',
'e':'i',
'r':'r',
'i':'i',
}
print('A:')
for p,q in diz.items():
    if p == q:
        print(p)
print('\nB:')
for x in diz:
    if x == diz[x]:
        print(x)

k = 'p'
#k = 'e'
#k = 'r'
#k = 'z'
diz = {
'p':'c',
'e':'h',
'r':'è',
}
print('A:')
for x in diz:
    if x == k:
        print('Trovato', diz[x])
print('\nB:')
if k in diz:
    print('Trovato', diz[k])

semi = {
    'cuori':'rosso',
    'picche':'nero',
    'quadri':'rosso',
    'fiori':'nero'}

for i in semi:
    print('Il colore di', i, 'è', semi[i])

preziosi = {
'rubini' : 'giada',
'opali' : 'topazi',
'gemme' : 'gemme',
'diamanti': 'gemme',
'rubini' : 'rubini'
}

for i in preziosi:
    if i == preziosi[i]:
        print('coppia di elementi uguali', i, 'e', preziosi[i])

for g,h in preziosi.items():
    if g == h:
        print('coppia di elementi uguali', g, 'e', h)

n = 5
diz = {}
#for i in range(n+1)[1:]:
for i in range(1,n+1):
    diz[i] = i*i

print(diz)

from pprint import pprint
fiori = ['girasole','GAROFANO', 'tulipano', 'VIOLA', 'ROSA', 'violetta']

diz = {}
for i in fiori:
    if i.isupper():
        diz[i] = True
    else:
        diz[i] = False

pprint(diz)

fiori = ['girasole','GAROFANO', 'tulipano', 'VIOLA', 'ROSA', 'violetta']
diz = {}

for el in fiori:
    diz[el] = el.isupper()

from pprint import pprint
pprint(diz)

q = 20
esposizioni = ['acquerello', 'olio', 'murale', 'tempera', 'carboncino','inchiostro']
prezzi = {'acquerello': 3000,
                'olio' : 6000,
                'murale' : 2000,
                'tempera' : 4000,
                'carboncino': 7000,
                'inchiostro': 1000
}
for i in esposizioni:
    prezzi[i]  = prezzi[i] * q
pprint(prezzi)

q = 20
esposizioni = ['acquerello', 'olio', 'murale', 'tempera', 'carboncino','inchiostro']
prezzi = {'acquerello': 3000,
'olio' : 6000,
'murale' : 2000,
'tempera' : 4000,
'carboncino': 7000,
'inchiostro': 1000
}
print('Guadagni previsti')
for i in range(len(esposizioni)):
    tecnica = esposizioni[i]
    print('  esposizioe', tecnica, ':', prezzi[tecnica]*q, '€')
print()
q = 20
esposizioni = ['acquerello', 'olio', 'murale', 'tempera', 'carboncino','inchiostro']
prezzi = {'acquerello': 3000,
'olio' : 6000,
'murale' : 2000,
'tempera' : 4000,
'carboncino': 7000,
'inchiostro': 1000
}
print('Guadagni previsti:')
for i in esposizioni:
    print('  esposizione', i, ':', prezzi[i]*q, '€')

cartoleria1 = { 'penne':10,
                'cartelle':20,
                'carta':30,
                'forbici':40}
cartoleria2 = { 'penne':80,
                'cartelle':90,
                'goniometri':130,
                'forbici':110,
                'righelli':120,}

print('materiali in comune:')
for i in cartoleria1:
    if i in cartoleria2:
        print('  ', i, ':', cartoleria1[i]+cartoleria2[i])

print()


legumi = ['ceci', 'soia']
# 0 1 2 3 4 5
magazzino = [50,90,70,10,20,50]
registro = {    'piselli' : 3,
                'soia' : 1,
                'lenticchie': 5,
                'ceci' : 4,
                'fave' : 2,
                'fagioli' : 0
}

#print('Cerco', legumi[0], 'e', legumi[1], '...')
print('Cerco', ' e '.join(legumi) + '...')
somma = 0
for i in legumi:
    print('trovati',magazzino[registro[i]], 'kg di', i)
    somma += magazzino[registro[i]]
#a = magazzino[registro[legumi[0]]]
#b = magazzino[registro[legumi[1]]]
print('Totale:', somma, 'kg' )
print()

smog = {'strada' : 40,
        'ciclabile' : 20,
        'autostrada': 90,
        'parco' : 15,
        'lago' : 5
}
preposizioni = {
        'autostrada': 'in',
        'ciclabile' : 'alla',
        'lago' : 'al',
        'parco' : 'al',
        'strada' : 'in',
}

for i in preposizioni:
    if smog[i] > 30:
        print(preposizioni[i].capitalize(), i,'l\'inquinamento è eccessivo')
    else:
        print(preposizioni[i].capitalize(), i,'l\'inquinamento è tollerabile')

sport = {   'Gianni' : 'calcio',
            'Paolo' : 'tennis',
            'Sara' : 'pallavolo',
            'Elena' : 'tennis',
            'Roberto': 'calcio',
            'Carla' : 'calcio',
}

calcio = 0
tennis = 0
pallavolo = 0

for i in sport:
    if sport[i] == 'calcio':
        calcio += 1
    elif sport[i] == 'tennis':
        tennis += 1
    elif sport[i] == 'pallavolo':
        pallavolo += 1

conteggi = {
    'calcio': calcio,
    'tennis': tennis,
    'pallavolo': pallavolo
}
print(conteggi)

sport = {'Gianni' : 'calcio',
'Paolo' : 'tennis',
'Sara' : 'pallavolo',
'Elena' : 'tennis',
'Roberto': 'calcio',
'Carla' : 'calcio',
}

conteggi = {}
for k,v in sport.items():
    if v in conteggi:
        conteggi[v] += 1
    else:
        conteggi[v] = 1

print(conteggi)

cerca = {'t','r','z'}
testo = "Il ramarro orientale è un sauro della famiglia dei Lacertidi, di colore, verde brillante"

conteggi = {}

for i in cerca:
    conteggi[i] = 0
for i in testo:
    if i in cerca:
        conteggi[i] += 1

print(conteggi)

diz = {
'a':3,
'b':8,
'c':4
}

lettere = []
for i in diz:
    lettere.append(i)

for i in lettere:
    diz['z'+i] = 10

diz = {
        'a':3,
        'b':8,
        'c':4}

for i in list(diz):
    diz['z'+i] = 10

print(diz)

arrivi = ['sedie', 'lampade', 'cavi']
catalogo = {'stufe' : 'A',
            'sedie' : 'B',
            'caraffe' : 'D',
            'lampade' : 'C',
            'cavi' : 'F',
            'giardinaggio' : 'E'}
magazzino = {}

for i in arrivi:
    if i in catalogo:
        magazzino[i] = catalogo[i]

print(magazzino)
print()

arrivi = ['sedie', 'lampade', 'cavi']
catalogo = {'stufe' : 'A',
            'sedie' : 'B',
            'caraffe' : 'D',
            'lampade' : 'C',
            'cavi' : 'F',
            'giardinaggio' : 'E'}
magazzino = {}

for i in arrivi:
    if i in catalogo:
        magazzino[catalogo[i]] = i
print(magazzino)

miniera = { 'ottone': 5,
            'rame' : 8,
            'ferro' : 1}
estratto = {}

for i in list(miniera):
    estratto[i] = [i]*miniera[i]

print(estratto)

lista = [  "vedo",
            "una",
            "luce"]
for stringa in lista:
    for carattere in stringa:
        print(carattere)
print()

for s in ['pallavolo', 'tennis', 'calcio', 'nuoto']:
    for s in range(3): # inferno da debuggare, perdi la s del ciclo for esterno
        print(s)
    print(s)

for y in range(2):
    for x in range(3):
        print(x)
    print()
    print(y)

for y in range(3):
    for x in range(2):
        print(x,y)

for x in range(2):
    for y in range(3):
        print(x,y)
    print(x,y)

for x in range(1):
    for y in range(3):
        print(x,y)

la = 'abc'
for x in la:
    for y in la:
        print(x)

for x in 'ab':
    for y in 'cd':
        print(x,y)
    for y in 'ef':
        print(x,y)

for x in 'abc':
    for y in 'abc':
        if x == y:
            print(x)

for x in 'abc':
    for y in 'abc':
        if x != y:
            print(x,y)

lista = []
for x in 'a':
    for y in 'bc':
        lista.append(x)
        lista.append(y)
print(lista)

lista = []
for x in 'abc':
    for y in 'de':
        lista.append('z')
print((lista))

c = 1
for x in range(1,4):
    s = ''
    for y in range(1,4):
        s = s + str(c)
        c += 1
    print(s)

attrici = ['Licia','Mila']
attori = ['Capitan Harlock', 'Lupin', 'Kenshiro']

for i in attrici:
    for j in attori:
        print('Entri in scena', i, '!')
        print('     entri in scena', j, '!')
        print('         ',i, 'e', j, 'si preparino... CIAK!')
        print('Grazie', j, ' - il prossimo !')
    print('Grazie', i, ' - la prossima!')
    print()

print('Fine delle audizioni!')

a,b = 5,3

for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)

a = 5
for x in range(a):
    for y in range(x,a):
        print(x,y)


parole = ['barca','molo','remo','nassa','vela','strascico']
lettere = ['a','c','s']

for parola in parole:
    for lettera in lettere:
        if lettera in parola:#parola.count(lettera) > 0:
            print(parola, 'contiene', parola.count(lettera), lettera)

poligoni = ["Il triangolo","Il quadrato","Il pentagono", "L'esagono"]
for i in range(len(poligoni)):
    for j in range(len(poligoni)):
        print(poligoni[i], 'ha', j+3, 'lati?', i+3 == j+3)

sa = 'bon'
sb = 'jour'

for i in range(len(sa)):
    for j in range(len(sb)):
        print(sa[i].upper(), sb[:j] + sb[j].upper() + sb[j+1:])

for c1 in sa:
    for i in range(len(sb)):
        print(c1.upper() + ' ' + sb[:i] + sb[i].upper() + sb[i+1:])

piano_utente = 3; piano_ascensore = 7

for i in range(piano_ascensore, piano_utente-1, -1):
    if i == piano_utente:
        print(i)
        print('DING!')
    else:
        print(i)
    
parola = 'palazzo'

for i in range(len(parola)):
    print(i, parola[i], parola[i].upper())
print()

for j in parola:
    print(parola.index(j), j, j.upper())
print()

ricetta = "oliva\t, pepe,cappero ,\n detersivo,\t \n cappero, peperone, acciuga, oliva , pepe\t,\t cappero , \noliva,pasta\n"

ricetta = ricetta.split(',')

ingr = []
for i in ricetta:
    i = i.strip()
    ingr.append(i)

servono = {}
for i in ingr:
    if i in servono:
        servono[i] += 1
    else:
        servono[i] = 1
print('Servono:')
for i,j in servono.items():
    print('     ',j,i)
print()

testo = "CiAo QuEsTo E' uN TeStO sToRto"
tradotto = []
for i in testo:
    if i.islower():
        i = i.upper()
        tradotto.append(i)
    else:
        i = i.lower()
        tradotto.append(i)
print(''.join(tradotto))

giocatore1 = ["h", "b", "f", "d", "x"]
giocatore2 = ["e", "c", "g", "a", "z"]

giocate = []
for i,j in zip(giocatore1,giocatore2):
    giocate.append(i+'_1')
    giocate.append(j+'_2')

giocate.sort(reverse=True)
print(giocate)

monte = [90,40,50,20,60, 7, 3, 4, 9, 8]
part1 = []
for i in monte[:len(monte)//2]:
    part1.append(i)

part2 = []
for i in monte[len(monte)//2:]:
    part2.append(i)

part1.sort()
part2.sort(reverse=True)
monte[:len(monte)//2] = part1
monte[len(monte)//2:] = part2
print(monte)

studenti = ['M_Alessandro', 'F_Alessia', 'F_Alice', 'M_Andrea', 'F_Anna', 'F_Arianna',
'F_Aurora', 'F_Beatrice', 'F_Bianca', 'F_Camilla', 'M_Federico', 'M_Francesco']

maschi = []
femmine = []

for i in studenti:
    if i.startswith('M'):
        maschi.append(i)
    elif i.startswith('F'):
        femmine.append(i)

print('1.a)     maschi =',maschi)
print('         femmine =',femmine)

maschi2 = []
femmine2 = []
for i in maschi:
    maschi2.append(i[2:])
for i in femmine:
    femmine2.append(i[2:])

print('1.b)     maschi =',maschi2)
print('         femmine =',femmine2,'\n')

print('2)       Stanza maschi 1:', maschi2[:3])
print('         Stanza maschi 3:', maschi2[3:],'\n')

print('3)       Stanza femmine 1:', femmine2[:3])
print('         Stanza femmine 3:', femmine2[3:3*2])
print('         Stanza femmine 3:', femmine2[3*2:],'\n')

categorie = {'a', 'b', 'c', 'd', 'e', 'f'}
competitor = [("pippo", {'a', 'c', 'e'}), ("pluto", {'c', 'd', 'e'})]

disponibili = set()
for i in categorie:
    if i not in competitor[0][1] and i not in competitor[1][1]:
        disponibili.add(i)

vendute = []
for i in (categorie):
    if i in competitor[0][1]  and i in competitor[1][1]:
        vendute.append((i,2))
    elif i in competitor[0][1]  or i in competitor[1][1]:
        vendute.append((i,1))
    else:
        vendute.append((i,0))

print('Le categorie disponibili sono:',disponibili)
print('Categorie vendute da competitor:\n\n',vendute)

parole = ['dddd', 'oooo', 'nnn', 'dddd', 'o', 'lllllll', 'oo']
parole = ''.join(parole)
freq = {}
for i in parole:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

nomi = ['hacKnights','Cult of Cobra','unsafe\nKreW']
dossier = ['hack.odt','cobra.odt','unsafe.docx']

db = {}
for i, j in zip(nomi, dossier):
    db[i] = j

ricerca = 'Cult of Cobra'

if ricerca in db:
    print(ricerca,'è documentato nel dossir \''+db[ricerca]+'\'')

i = 1
while i <= 4:
    print('Ho contato fino a', i)
    i += 1
print('Ciclo finito!')

k = 0
while k < 5:
    print(k)
    k+=1

i = 0
while False:
    print(i)
    i += 1
print('Finito !')

i = 0
while i < 3:
    print(i)
    i += 1

i = 0
while i < 3:
    print('GAM')
    i = i + 1

i = 10
while i > 0:
    if i > 5:
        print(i)
    i -= 1
print('MAW')

import random
x = 0
while x < 7:
    x = random.randint(1,10)
    print(x)
print('LUCK')

x,y = 0,0
while x + y < 4:
    x += 1
    y += 1
print(x,y)

x,y = 0,3
while x < y:
    print(x,y)
    x += 1
    y -= 1

k = 5
i = 0
while i <= k:
    if i % 2 == 1:
        print(i)
    i += 1

numeri = [8,6,5,9]

i = 0
var = 0.0
while i < len(numeri):
    var += numeri[i]
    i += 1
if len(numeri) > 0:
    print('La media è di:',var/len(numeri))
else:
    print(0.0)

i = 1
while True:
    print('Ho contato fino a', i)
    if i > 3:
        print('Break Esco dal ciclo!')
        break
        print('Dopo il break')
    i += 1
print('Ciclo finito!')
print()
i = 1
while i < 5:
    print('Ho contato fino a', i)
    i += 1
    if i % 2 == 1:
        print('continue, salta alla verifica condizione')
        continue
        print('Dopo il continue')
    print('arrivato in fondo')
print('Ciclo finito!')
print()

i = 1
while 1 < 5:
    print('Ho contato fino a', i)
    if i > 3:
        print('break! Esco dal ciclo!')
        break
        print('Dopo il break')
    i += 1
    if i % 2 == 1:
        print('continue, salta alla verifica condizione')
        continue
        print('Dopo il continue')
    print('arrivato in fondo')
print('Ciclo finito!')

print()

i = 1
while i < 4:
    print('Ho contato fino a', i)
    i += 1
    continue
print('Ciclo finito!')

i = 3
while i > 0:
    print('Ho contato fino a', i)
    if i == 2:
        print('Continue, salta alla verifica condizione')
        continue
    i -= 2#1
    print('arrivato in fondo')

print('Ciclo finito!')
print()

i = 0
while True:
    i += 1
    print(i)
    if i > 3:
        break
print('BONG')

i = 0
while True:
    i += 1
    if i < 3:
        continue
    else:
        break

print('ZANG')

print('A:')
while True:
    print('BORG')
    break
print('\nB:')
while False:
    pass
print('BORG')

print('A:')
x = 0
while x < 3:
    print(x)
    x += 1
print('\nB:')
x = 1
while x <= 3:
    print(x-1)
    x += 1
print()
print('A:')
x = 0
while x < 3:
    x += 1
print(x)

print('\'B:')
x = 0
import random
while x != 3:
    x = random.randint(1,5)
print(x)

print()

print('A:')
i = 0
while i < 3:
    print(i)
    i += 1
while i < 6:
    print(i)
    i += 1

print('\'B:')
i = 0
while i < 6:
    print(i)
    i += 1

print('A:')
i = 2
print(i)
while i > 0:
    i -= 1
    print(i)

print('\nB:')
i = 2
while i > 0:
    print(i)
    i -= 1

print('A:')
i = 2
print(i)
while i > 0:
    i -= 1
    print(i)

print('\nB:')
i = 2
while i > 0:
    print(i)
    i -= 1
print(i)


print('A:')
ping,pong = 0,3
while ping < 3 or pong > 0:
    print(ping,pong)
    ping += 1
    pong -= 1
print('\nB:')
ping,pong = 0,3
while not(ping >= 3 and pong <= 0):
    print(ping,pong)
    ping += 1
    pong -= 1
print()


print('A:')
n,i,s = 0,0,'zanna'
while i < len(s):
    if s[i] == 'n':
        n += 1
    i += 1
print(n)

print('\nB:')
n,i,s = 0,0,'zanna'
while i < len(s):
    i += 1
    if s[i-1] == 'n':
        n += 1
print(n)

x = 3
while True:
    print(x)
    if x == 0:
        break
    x -= 1

x = 3
while x >= 0:
    print(x)
    x -= 1

print()
la = [2,3,7,5,6]
k = 7
i = 0
while i <= 2:
    print(la[i])
    i += 1

print()
la = [2,3,7,5,6]
k = 7
i = 0
while i < len(la) and la[i] != k:
    print(la[i])
    i += 1
if i < len(la) and la[i] == k:
    print(la[i])

print()
x,y = 2,8
while True:
    if x < y or x == 4:
        print((x,y))
        x += 1
        y -= 1
    else:
        break
print()

k = 8
# scrivi qui
x = 0
while x <= k:
    if x % 3 == 0:
        print(x, 'CAR')
    elif x % 3 == 1:
        print(x, 'TO')
    else:
        print(x, 'NE')
    x += 1

x,y = 5,7

while x <= 10 and y <= 10:
    print(x,y)
    x+=1
    y+=1

y = 4
x = 0
while x <= y:
    print('c'*x)
    x += 1

x,k = 3,5
if x < k:
    while x <= k:
        print(x)
        x += 1
else:
    while k <= x:
        print(k)
        k += 1

x,k = 6,2
if x < k:
    while x <= k:
        print(x)
        x += 1
else:
    while x >= 2:
        print(x)
        x -= 1

x,k = 3,5
while x != k:
    print(x)
    if x < k:
        x += 1
    else:
        x -= 1
print(x)

compagnia = 'Turbolen'
aereoporto = ['Volatut','AliBucate','PiccionJet','Turbolenz', 'BoingBoing','Jettoni','Turbulenz','BoingBoing' ]

x = 0
while x < len(aereoporto):
    if aereoporto[x] == compagnia:
        print('Trovato il primo', compagnia ,'all\'indice',aereoporto.index(compagnia))
        break
    x += 1
    if x == len(aereoporto):
        print('Non ho trovato', compagnia)

compagnia = 'Turbolenz'
aereoporto = ['Volatut','AliBucate','PiccionJet','Turbolenz', 'BoingBoing','Jettoni','Turbulenz','BoingBoing' ]

x = 0
while x < len(aereoporto) and aereoporto[x] != compagnia:
    x += 1

if x == len(aereoporto):
    print('Non ho trovato', compagnia)
else:
    print('Trovato il primo', compagnia, 'all\'indice', aereoporto.index(compagnia))

pista = '★★★★hangar★★★'
x = 0
while x < len(pista):
    if pista[x].isalpha() or pista[x].isdigit():
        print(pista[x:])
        break
    x += 1

pista = '★★★★hangar★★★'
i = 0
while i < len(pista) and not (pista[i].isalpha() or pista[i].isdigit()):
    i += 1

print(pista[i:])

strada = ['Santa Fe','Denver','Dodge City', 'Silverton', 'Agua Caliente', 'Tombstone']
carson,butch = 3, 2

while carson < len(strada)-1 or butch < len(strada)-1:
    if carson == butch:
        print('Duello finale a', strada[carson] + '!')

    print('Carson raggiunge', strada[carson])
    print('Butch raggiunge', strada[butch])
    if carson == 5:
        print('\nCarson ha trovato il tesoro a ' + strada[5])
    elif butch == 5:
        print('\nButch ha trovato il tesoro a ' + strada[5])
    carson += 1
    butch += 2

strada = ['Santa Fe','Denver','Dodge City', 'Silverton', 'Agua Caliente', 'Tombstone']
carson,butch = 3, 0

print('Carson parte da', strada[carson])
print('Butch parte da', strada[butch])
#finchè carson e butch sono minori della lunghezza della strada -1
while carson < len(strada)-1 and butch < len(strada)-1:
    #carson = 
    carson = min(len(strada)-1, carson + 1)
    butch = min(len(strada)-1, butch + 2)
    print('Carson raggiunge', strada[carson])
    print('Butch raggiunge', strada[butch])
print()
if carson == len(strada)-1 and butch == len(strada)-1:
    print('Duello finale a ', strada[-1], '!')
elif carson == len(strada)-1:
    print('Carson ha trovato il tesoro a', strada[-1], '!')
else:
    print('Butch ha trovato il tesoro a', strada[-1], '!')

#variabile stringa
linguaggio = "armonia cosmica forever" # True
#divido la stringa in una lista di stringhe
linguaggio = linguaggio.split()
#n = len(linguaggio[0]) if len(linguaggio) > 0 else 0
#se c'è almeno una stringa
if len(linguaggio) > 0:
    #n prende il valore della lunghezza della prima strigna
    n = len(linguaggio[0])
else:#altrimenti n vale 0
    n = 0
#variabile vera di base
tutte_uguali = True
#variabile per controllare il while
x = 0
#finche la x non supera il numero di elementi nella lista lingueggio 
# e la variabile vera di base è vera
while x < len(linguaggio) and tutte_uguali:
    #se il valore di n è diverso dalla lunghezza di un valore della lista di linguaggio
    if n != len(linguaggio[x]):
        #la variabile vera diventa falsa arrestando il ciclo
        tutte_uguali = False
    # incremento la variabile per avvicinarmi alla conclusione del ciclo
    x += 1
# stampa se è vero o falso
print(tutte_uguali)

piantagione = ['pietre','sassi', 'C', 'banane',
                'arance', 'manghi', 'C','sabbia',
                'sassi', 'sassi','C', 'avocadi','C',
                'gramigna','C', 'kiwi', 'manghi', 'C',
                'C', 'C','rocce', 'C', 'lime', 'C', 'ciottoli',
                'C', 'arance','cocco', 'C', 'ghiaia']

cassone = []
x = 0
while x < len(piantagione) and len(cassone) < 7:
    if piantagione[x] in cassone:
        pass
    elif piantagione[x] == 'C' or piantagione[x] == 'sassi':
        pass
    elif piantagione[x] == 'pietre' or piantagione[x] == 'sabbia' or piantagione[x] == 'gramigna':
        pass
    elif piantagione[x] == 'rocce' or piantagione[x] == 'ghiaia' or piantagione[x] == 'ciottoli':
        pass
    else:
        cassone.append(piantagione[x])
    x += 1

print(cassone)

piantagione = ['pietre','sassi', 'C', 'banane',
                'arance', 'manghi', 'C','sabbia',
                'sassi', 'sassi','C', 'avocadi','C',
                'gramigna','C', 'kiwi', 'manghi', 'C',
                'C', 'C','rocce', 'C', 'lime', 'C', 'ciottoli',
                'C', 'arance','cocco', 'C', 'ghiaia']
#creo una lista
cassone = []
# scrivi qui
#creo una variabile falsa
raccogliendo = False
i = 0
#finche la x è minore del numero di elemnti e il cassone ha meno di 7 elementi
while i < len(piantagione) and len(cassone) < 7:
    #se 'elemento è uguale a C
    if piantagione[i] == 'C':
        #sblocca il raccoglitore
        raccogliendo = not raccogliendo
    else:
        #se non è uguale a C ed il raccoglitore è acceso raccogli
        if raccogliendo:
            cassone.append(piantagione[i])
    i += 1
    #mostra il raccolto
print(cassone)

stringa,car1,car2 = "accatastare la posta nella stiva", 's','t' 

stringa = stringa.split()

valore = []

x = 0
while x < len(stringa):
    if car1 in stringa[x]:
        trova = stringa[x].find(car1)
        if stringa[x][trova+1] == car2:
            valore.append('True')
        else:
            valore.append('False')
    x += 1

y = 0
ok = 0
while y < len(valore):
    if valore[y] == 'True':
        ok += 1
    y += 1

if y == ok:
    print(True)
else:
    print(False)

stringa,car1,car2 = "accatastare la posta nella stiva", 's','t' 

i = 0
ris = True
#se gli elemnti in stringa è uno
if len(stringa) == 1:
    #ris falso
    ris = False

#finche i + 1 è minore del numero di elementi in stringa e ris è vero
while i + 1 < len(stringa) and ris:
    #se il primo elemnto è uguale a car1 e il secondo è dierso da car 2
    if stringa[i] == car1 and stringa[i+1] != car2:
        #ris falso
        ris = False
    i += 1
#mostra il valore finale di ris
print(ris)

mazzo = ['3 cuori', # <---- in fondo
        '2 picche',
        '9 cuori',
        '5 quadri',
        '8 fiori',] # <---- in cima

while len(mazzo) > 0:
    carta = mazzo.pop()
    print('Pescato: ' + carta)

print('Carte finite!')
print()
mazzo = ['3 cuori','2 picche','9 cuori','5 quadri','8 fiori']

carta = ''
while len(mazzo) > 0:
    carta = mazzo.pop()
    print('pescato', carta)
    if 'cuori' in carta:
        break

if 'cuori' in carta:
    print('Ho trovato cuori')
else:
    print('Niente cuori')

print()
mazzo = ['3 cuori','2 picche','9 cuori','5 quadri','8 fiori']

si = True
carta = ''
while len(mazzo) > 0 and si:
    carta = mazzo.pop()
    print('Pescato', carta)
    if 'cuori' in carta:
        si = False

if 'cuori' in carta:
    print('Ho trovato cuori')
else:
    print('Niente cuori')

print()
mazzo = ['3 cuori','2 picche','9 cuori','5 quadri','8 fiori']

carta = ''
while len(mazzo) > 0 and 'cuori' not in carta:
    carta = mazzo.pop()
    print('Pescato', carta)

if 'cuori' in carta:
    print('Ho trovato cuori')
else:
    print('Niente cuori')

while []:
    print('z')
print('Big')

la = []
while len(la) < 3:
    la.append('x')
print(la)

la = ['x', 'y','z']
while len(la) > 0:
    print(la.pop())

la = ['x', 'y','z']
while la:
    print(la.pop(0))

la = [4,5,8,10]
while la.pop() % 2 == 0:
    print(la)

print('A:')
la = ['t','r','e','n','o']
while len(la) > 0:
    print(la.pop())
print('\nB:')
la = ['t','r','e','n','o']
la.reverse()
while len(la) > 0:
    print(la.pop(0))

print()
print('A:')
x,n,la = 2,0,[]
while x not in la:
    la.append(n)
    n += 1
print(la)
print('\nB:')
x,la = 2,[]
while len(la) < 3:
    la.append(x)
    x += 1
print(la)

lista = []
i = 0
k = 10
while sum(lista) < k:
    lista.append(i)
    i += 1
    print(lista)


lista = []
i = 0
k = 10
while True:
    if sum(lista) >= k:
        break
    else:
        lista.append(i)
        i += 1
        print(lista)

pila = ['S-Medioevo', # <---- in fondo
        'V-Australia',
        'V-Scozia',
        'G-Sospetti',
        'V-Caraibi'] # <---- in cima
copia_pila = pila.copy()
pila.reverse()
viaggi = []
x = 0

print('All\'inizio:')
print('     pila: ', copia_pila)
print('     viaggi: ', viaggi)

while x < len(pila):
    if pila[x].startswith('V'):
        viaggi.append(pila[x])
        copia_pila.pop(-1)
        print('Preso', pila[x])
        print('     pila: ', copia_pila)
        print('     viaggi: ', viaggi)
    else:
        copia_pila.pop(-1)
        print('Scartato', pila[x])
        print('     pila: ', copia_pila)
        print('     viaggi: ', viaggi)
    x += 1
print()

pila_sx = ['cassa','stivale','ferro di cavallo','secchio']
pila_dx = ['bidone','sella','latta']
sparo = 'dx'
#finchè gli elemanti di dx o sx sono maggiori di 0
while len(pila_dx) > 0 or len(pila_sx) > 0:
    #se sparo è dx
    if sparo == 'dx':
        #se gli elementi di dx sono maggiori di 0
        if len(pila_dx) > 0:
            #printa
            print('Bang! a destra:      ', pila_dx.pop())
        #sparo diventa sx
        sparo = 'sx'
    else:
        if len(pila_sx) > 0:
            print('Bang! a sinistra:    ', pila_sx.pop())
        sparo = 'dx'
    
    print('     pila_sx:', pila_sx)
    print('     pila_dx:', pila_dx)

print()
pila_sx = ['cassa','stivale','ferro di cavallo','secchio']
pila_dx = ['bidone','sella','latta']
sparo = 'dx'

while len(pila_dx) > 0 or len(pila_sx) > 0:
    if sparo == 'dx':
        if len(pila_dx) > 0:
            print('Bang! a destra', pila_dx.pop())
        sparo = 'sx'
    else:
        if len(pila_sx) > 0:
            print('Bang! a sinistra!', pila_sx.pop())
        sparo = 'dx'

    print('pila_dx:', pila_dx)
    print('pila_sx:', pila_sx)

la = [3,5,6,7]

while len(la) > 0:
    if la[-1] % 2 == 1:
        print('Dispari: attacco', la[-1]*2)
        la.append(la[-1]*2)
        #print('         la diventa',la)
    elif la[-1] % 2 == 0:
        print('   Pari: tolgo', la.pop())
        print('   Pari: tolgo', la.pop())
        #print('         la diventa',la)
    print('         la diventa',la)

print('Finito! la è', la)

panini, burgers = 9,9
while panini > 0 and burgers > 0:
    print('Servito un panino', panini -1, 'panini riamanenti,', burgers -1, 'burgers rimanenti')
    panini -= 1
    burgers -= 1
if panini > 0:
    print('Avanzano', panini, 'panini')
elif burgers > 0:
    print('Avanzano', burgers, 'burgers')
elif burgers == 0 and panini == 0:
    print('Credenza vuota!')

cerco = 'il tesoro'
caverna = ['un masso','una trappola','delle spade',
           'il tesor','una ragnatela', 'un boleto delle tombe']
trovato = False
x = 0
print('Entro')
while x < len(caverna):
    if cerco == caverna[x]:
        print('Che fortuna! Ho trovato il tesoro')
        print('Torno indietro!')
        trovato = True
        caverna.reverse()
    print('Vedo', caverna[x])
    x += 1
    if x == len(caverna) and trovato == False:
        print('Purtroppo', cerco, 'non c\'è')
        print('Torno indietro!')
        caverna.reverse()
        for y in caverna:
            print('Vedo',y)
print('Esco')

pozzo = ['███','▓▓▓','▒▒▒', '░░░'] # <-- cima del pozzo
carrello = []

x = 0
while x < len(pozzo):
    print('il pozzo è', pozzo)
    diviso = []
    for i in pozzo[-1]:
        diviso.append(i)
        carrello.append(i)
    print('Trivello lo strato', pozzo.pop(), 'e lo divido nei blocchi', diviso)
    print()

print('Il pozzo finale è    :', pozzo)
print('Il carrello finale è :', carrello)

print(iter(['a', 'b', 'c', 'd']))

itera = iter(['a', 'b', 'c', 'd'])
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))

print(range(4))

for x in range(4):
    print(x)

iteratore = iter(range(4))

print(iteratore)
print(next(iteratore))
print(list(range(4)))

sequenza = range(4)
iteratore = iter(sequenza)

nuova1 = list(iteratore)
print(nuova1)
nuova2 = list(iteratore)
print(nuova2)

sequenza = range(4)
iteratore = iter(sequenza)
print(iteratore[1])

print(range(3))
#print(range())

print(list(range(-3)))

print(list(range(3)))
print(range(3,6))

print(list(range(5,4)))
print(list(range(3,3)))

print(list(range(3)) + list(range(6)))

print(list(range(0,6,2)))

print(list(range(9,6,-1)))

la = list('prova')
print(reversed(la))

iteratore = reversed(la)
print(next(iteratore))
print(next(iteratore))
print(next(iteratore))

la = list('prova')
print(reversed(la))

iteratore = reversed(la)
lb = []
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))
print(la, '\n', lb)

la = list('sconcerto')
lb = []
iteratore = reversed(la)
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))
lb.append(next(iteratore))

print(lb[1::2])
print(la)

la = list('sconcerto')
lb = []
iteratore = reversed(la)

x = 0
while x < len(la):
    lb.append(next(iteratore))
    x += 1

print(lb[1::2])
print(la)

la = list('sconcerto')
lb = []
iteratore = reversed(la)
for i in range(len(la)):
    lb.append(next(iteratore))

print(lb[1::2])
print(la)

la = ['s', 'c', 'o', 'n', 'c', 'e', 'r', 't', 'o']
lb = []
# scrivi qui
iteratore = reversed(la)
next(iteratore)
lb.append(next(iteratore))
next(iteratore)
lb.append(next(iteratore))
next(iteratore)
lb.append(next(iteratore))
next(iteratore)
lb.append(next(iteratore))
print(lb)

la = ['s', 'c', 'o', 'n', 'c', 'e', 'r', 't', 'o']
lb = []
# scrivi qui
iteratore = reversed(la)
i = 1
while i < len(la):
    if i % 2 == 1:
        next(iteratore)
        lb.append(next(iteratore))

    i += 2
print(lb)

la = ['s', 'c', 'o', 'n', 'c', 'e', 'r', 't', 'o']
lb = []
# scrivi qui
i = 0
for x in reversed(la):
    if i % 2 == 1:
        lb.append(x)
    i += 1
print(lb)

la = list('prova')
print(list(reversed(la)))

la = list('prova')
iteratore = reversed(la)
nuova = list(iteratore)
print('la è', la)
print('nuova è', nuova)

la = list('lista')
a = sorted(la)
print(la)
print(a)

inputu =  ['Maria','Paolo','Giovanni','Alessia','Greta']
output = sorted(inputu, reverse=True)
print(inputu)
print(output)

quadri = ["La Gioconda", "La Nascita di Venere", "I Girasoli"]
anni = [1503, 1482, 1888]

print(zip(quadri, anni))
print(list(zip(quadri, anni)))
iteratore = zip(quadri, anni)
print(next(iteratore))
print(next(iteratore))
print(next(iteratore))

print(list(zip([1,2,3], ['a','b','c','d','e'])))

a = list(zip(quadri, anni))
for i in a:
    print(i[0], i[1])

n = 5
#crea una lista di tuple che come primo elemento
#parte da 0 a 5 escluso, ed il secondo elemento
# da 5 escluso a 0
print(list(zip(range(5), reversed(range(n)))))

numeri = [2,5,3,4]
raddoppiati = [ x*2 for x in numeri ]
print(raddoppiati)
print(numeri)

aumentati = [x+1 for x in numeri]
print(aumentati)
print(id(numeri), id(aumentati))

la = [x for x in 'domanda']
print(la)

animali = ['cani', 'gatti', 'scoiattoli', 'alci']
nuova = [x.upper() for x in animali]
print(animali, nuova)

animali = ['caNI', 'gaTTi', 'SCOIATtoli', 'aLLci']
nuova1 = [x.lower() for x in animali]
print(animali, nuova1)

lc = [k > 3 for k in range(7)]
print(lc)
ld = [s + s for s in ['lam','pa','da']]
print(ld)

la = ['x','z','z']
ls = [x for x in la] + [y for y in la]
print(ls)

lw = [x.split('-') for x in ['a-b', 'c-d', 'e-f']]
print(lw)

lk = ['@'.join(x) for x in [['a','b.com'],['c','d.org'],['e','f.net'] ]]
print(lk)

lj = ['z' for y in 'borgo'].count('z') == len('borgo')
print(lj)

m = [['a','b'],['c','d'],['e','f'] ]
la = [x.pop() for x in m] # sconsigliabile - perchè ?
print(' m:', m)
print('la:',la)

la =  ['gomma', 'ciunga', 'cicca']
lb = [ x*4 for x in la]
print(lb)

import math
lc = [16,25,81]
ld = [ math.sqrt(x)  for x in lc]
print(ld)

le = ['Quando', 'Fuori', 'Piove', 'Programmiamo']
lf = [ x[0] for x in le]
print(lf)

lg = ['non', 'ti', 'preoccupare', 'e', 'porta', 'pazienza']
lh = [ len(x) for x in lg]
print(lh)

ll =  [4,1,0,5,0,9,1]
lm = [ x > 3 for x in ll]
print(lm)

ln = [3,2,4,1,5,3,2,9]
lp = [ x % 2 == 0 for x in ln]
print(lp)

lq =  ['parto', 'per', 'il', 'fronte']
lr = [ x[0]+x[-1] for x in lq]
print(lr)

lo = [['a','b'],['c','d','e'], ['f','g']]
ls = [ '-'.join(x) for x in lo]
print(ls)

lt = 'lollosa'
lu = [ (x, lt.count(x)) for x in lt]
print(lu)

lv = ['bue','gatto','cane', 'mucca' ]
lz = [ x[1:-1] for x in lv]
print(lz)

lx = ['Quattrocchi', 'Forzuto', 'Puffetta', 'Tontolone']
ly = sorted([ x.upper() for x in lx])
print(ly)

lx = ['Quattrocchi', 'Forzuto', 'Puffetta', 'Tontolone']
#lx.sort()
ly = [ x.upper() for x in sorted(lx)]
print(ly)

lk = [10,25,50]
lj = ['argento','oro','platino']

lkj = [ x for x in zip(lk, lj)]
print(lkj)

lk = [10,25,50]
lj = ['argento','oro','platino']

lkj = list(zip(lk, lj))
print(lkj)

print([ x for x in [7,4,8,2,9] if x > 5])

print([ x for x in 'Il Mondo Gira' if x.isupper()])

print([x for x in range(100) if False])

print([x for x in range(3) if True])

print([x for x in range(6) if x % 2 == 0])

print([x for x in {'a','b','c'}])

print([x for x in [[5], [2,3], [4,2,3], [4]] if len(x) > 2])

print([(x,x) for x in 'xyxyxxy' if x != 'x' ])

print([x for x in ['abCdEFg'] if x.upper() == x])

la = [1,2,3,4,5]
print([x for x in la if x > la[len(la)//2]])

la = ['zebra', 'leopardo', 'giraffa', 'gnu', 'rinoceronte', 'leone']
lb = [ x for x in la if len(x) > 6]
print(lb)

la = ['barza', 'palco','porzione', 'corsa', 'maschera', 'zona']
lb = [ x.replace('z', 'Z') for x in la if 'z' in x ]
print(lb)

frase = """La data science è l'insieme di principi metodologici
basati sul metodo scientifico e di tecniche multidisciplinari
volto a interpretare ed estrarre conoscenza dai dati attraverso
la relativa fase di analisi"""

la = ' '.join([ x[0].upper() + ' ' + x[1] for x in zip(frase.split()[::2], frase.split()[1::2])])
print(la)

#print(' '.join([ x[0].upper() + ' ' + x[1] for x in zip(frase.split()[::2], frase.split()[1::2])]))

stringa = "Hattori Hanzō è un famoso ninja giapponese del periodo Sengoku"

print(('\n'.join(list(stringa.split()))).split('\n'))

la = [('condensatore', 8), ('resistenza',4), ('led',5), ('diodo',1), ('trasduttore',2), ('transistor',12) , ('sensore',3),('solenoide',10)]

print([x[0] for x in la if x[1] > 4])

indumenti = ['cappotti', 'giacconi', 'mantelli', 'ventine']
capi = [9,5,7,3]

#print([ 'Ci sono ' + str(capi[x]) + ' ' + indumenti[x]  for x in range(len(indumenti))])
print([ 'Ci sono ' + str(x[1]) + ' ' + x[0]  for x in zip(indumenti, capi)])

frase = ['Por', 'el', 'suelo', 'camina', 'mi', 'pueblo']
print([ list(range(1,len(x)+1)) for x in frase])

fauna = ["cippimerli",
         "gufolanti",
         "branchisauri",
         "cumulognembi",
         "arzigovolanti",
         "rotototteri",
         "barbagianni"]

la = [ x[0][:4] + x[1][4:] for x in zip(fauna, fauna[::-1])]
print(la)

def f():
    print('car')
f()

def fz():
    return 3
print(fz())

def fc():
    return 3
print(fc()*fc())

def fg():
    pass
print(fg())

print()
def f():
    pass
    print("ciao")
f()

def f(x):
    return x
print(f('x'))

def f():
    print('fire')
x = f()
print(x)

def f():
    return(print('fire'))
print(f())

def f(x):
    return 'x'
print(f(5))

def etc():
    print('etc...')
    #return etc()
etc()
print()

def stampola(lista):
    print('I primi due elementi sono', lista[0], 'e', lista[1])

la = [8,5,6,2]
stampola(la)

print()
def ritornola(lista):
    ret = []
    for el in lista:
        ret.append(el*2)
    return ret

la = [5,2,6,3]
risultato = ritornola(la)

print('       la:', la)
print('risultato:', risultato)

print()

def modifanta(lista):
    lista.sort()

la = [7,4,9,8]
modifanta(la)
print(la)

print()

def modirit(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]*2
    return lista

la = [8,7,5]
risultato = modirit(la)
#print(la)
print('risultato :', risultato)
print('        la: ', la)

print()

lb = [7,5,6]
modirit(lb).reverse()
print('        lb: ', lb)

print()

def modirip(lista):
    lista.sort()
    ret = lista[-1]
    lista.pop()
    return ret

la = ['b', 'c', 'a']
risultato = modirip(la)
print('risultato:', risultato)
print('       la:', la)

print()

def peccato(intero):
    intero = 666
    print(intero)

x = 5
peccato(x)

print()

def male(stringa):
    stringa = '666'

def disgrazia(lista):
    lista = [666]

def delirio(dizionario):
    dizionario = {'maligno':666}

print()

def consentito(lista):
    lista[2] = 9

fuori = [8,5,7]
consentito(fuori)
print(fuori)

def daccordo(dizionario):
    dizionario['mio campo'] = 5

def va_bene(istanza_di_classe):
    istanza_di_classe.mio_campo = 7

def dolore(lista):
    lista.sort()
    return lista

def crisi(lista):
    lista[0] = 5
    return lista

def tormento(dizionario):
    dizionario['a'] = 6
    return dizionario

def disperazione(istanza):
    istanza.mio_campo = 6
    return istanza

def my_gun():
    pass


print(list('Ciao'))

stringa_esterna = 'marinaio'

def mia_maiusc(s):
    ret = s.upper()
    return ret

risultato = mia_maiusc(stringa_esterna)
print('      risultato:', risultato)
print('stringa_esterna:', stringa_esterna)

stringa_esterna = 'marinaio'

def mia_maiusc2(s):
    s = s.upper()
    return s

risultato = mia_maiusc2(stringa_esterna)
print('      risultato:', risultato)
print('stringa_esterna:', stringa_esterna)

stringa_esterna = "marinaio"
def mia_maiusc3(s):
    stringa_esterna = s.upper()
    return stringa_esterna
risultato = mia_maiusc(stringa_esterna)
print('      risultato:', risultato)
print('stringa_esterna:', stringa_esterna)

stringa_esterna = 'marinaio'

def mia_maiusc4(s):
    ret = s.upper()
    return ret

risultato = mia_maiusc4(stringa_esterna)
stringa_esterna = risultato
print('      risultato:', risultato)
print('stringa_esterna:', stringa_esterna)

numeri_esterni = [10,20,30]

def raddoppia(lista):
    for i in lista:
        i = i*2

raddoppia(numeri_esterni)
print(numeri_esterni)

numeri_esterni = [10,20,30]

def raddoppia2(lista):
    tmp = []
    for elemento in lista:
        tmp.append(elemento*2)
    
    lista = tmp

raddoppia2(numeri_esterni)
print(numeri_esterni)

numeri_esterni = [10,20,30]
def raddoppia3(lista):
    tmp = []
    for elemento in lista:
        tmp.append(elemento * 2)
    numeri_esterni = tmp
raddoppia3(numeri_esterni)

numeri_esterni = [10,20,30]
def raddoppia5(lst):
    tmp = [] # SBAGLIATO: stiamo creando una NUOVA lista,
             # ma il testo dice di MODIFICARE
    for elemento in lst:
        tmp.append(elemento * 2) # SBAGLIATO: stiamo modificando una NUOVA lista
    return tmp # SBAGLIATO: il testo non ha chiesto di
# ritornare alcunchè
numeri_esterni = raddoppia5(numeri_esterni)
print(numeri_esterni)

numeri_esterni = [10,20,30]
salvata = numeri_esterni # preserviamo il puntatore
def raddoppia6(lista):
    tmp = []
    for elemento in lista:
        tmp.append(elemento * 2)
    return tmp
numeri_esterni = raddoppia6(numeri_esterni)
print('numeri_esterni:', numeri_esterni) # [20,40,60]
print('       salvata:', salvata) # [10,20,30]

print()
numeri_esterni = [1,2,3,4,5]

def raddoppia7(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2

raddoppia7(numeri_esterni)
print(numeri_esterni)

#print([ numeri_esterni[x]*2 for x in range(len(numeri_esterni))])

def zam(bal):
    bal = 4

x = 8
zam(x)
print(x)

def zom(y):
    y = 4

y = 8
zom(y)
print(y)

def zeb(lst):
    lst.append('d')

la = ['a','b','c']
zeb(la)
print(la)

def attenzione(la):
    la = ['?', '?']

lb = list('caspita')
attenzione(lb)
print(lb)

def umpa(string):
    string = 'lompa'
word = 'gnappa'
umpa(word)
print(word)

def sport(diz):
    diz['scarpe'] = 2
armadio = {'racchette':4,
           'palline': 7}
sport(armadio)
print(armadio)
print()
def numma(lst):
    lst + [4,5]

la = [1,2,3]
print(numma(la))
print(la)
print()

def truc(lista):
    return lista + [4,5]

lb = [1,2,3]
print(truc(lb))
print(lb)

album = [
        "Caterina Caselli - Cento giorni",
        "Delirium - Jesahel",
        "Jan Hammer - Crockett's Theme",
        "Sonata Arctica - White Pearl, Black Oceans",
        "Lucio Dalla - 4 marzo 1943.mp3",
        "The Wellermen - Wellerman",
        "Manu Chao - Por el Suelo",
        "Intillimani - El Pueblo Unido"
        ]

def funz(canzoni):
    for i in canzoni:
        print(i.replace('-',':'))

funz(album)
print()

album = [
        "Caterina Caselli - Cento giorni",
        "Delirium - Jesahel",
        "Jan Hammer - Crockett's Theme",
        "Sonata Arctica - White Pearl, Black Oceans",
        "Lucio Dalla - 4 marzo 1943.mp3",
        "The Wellermen - Wellerman",
        "Manu Chao - Por el Suelo",
        "Intillimani - El Pueblo Unido"
        ]

def funz1(canzoni):
    for i in canzoni:
        i = i.split('-')
        print(i[0].rjust(17) + ':' + '' + i[1])

print(funz1(album))

album = [
        "Caterina Caselli - Cento giorni",
        "Delirium - Jesahel",
        "Jan Hammer - Crockett's Theme",
        "Sonata Arctica - White Pearl, Black Oceans",
        "Lucio Dalla - 4 marzo 1943.mp3",
        "The Wellermen - Wellerman",
        "Manu Chao - Por el Suelo",
        "Intillimani - El Pueblo Unido"
        ]

def funz2(canzoni):
    nuova = []
    for i in canzoni:
        i = i.split(' - ')
        nuova.append(i[0])
        #nuova.append(i.split( '-  )[0])
    return nuova

print(funz2(album))
print()
albumA = [
        "Caterina Caselli - Cento giorni",
        "Delirium - Jesahel",
        "Jan Hammer - Crockett's Theme",
        "Sonata Arctica - White Pearl, Black Oceans",
        "Lucio Dalla - 4 marzo 1943.mp3",
        "The Wellermen - Wellerman",
        "Manu Chao - Por el Suelo",
        "Intillimani - El Pueblo Unido"
        ]

albumB = ["Toto Cotugno - L'Italiano vero", "Mia Martini - Minuetto", "AlBano-NEL SOLE"]

def registra(canzoniA, canzoniB):
    for i in range(len(canzoniB)):
        canzoniA[i] = canzoniB[i]
    i = 0
    while i < len(canzoniA):
        canzoniA[i] = None
        i += 1

registra(albumA, albumB)

print(albumA)

album = [
"Caterina Caselli - Cento giorni",
"Delirium - Jesahel",
"Jan Hammer - Crockett's Theme",
"Sonata Arctica - White Pearl, Black Oceans",
"Lucio Dalla - 4 marzo 1943.mp3",
"The Wellermen - Wellerman",
"Manu Chao - Por el Suelo",
"Intillimani - El Pueblo Unido"
]

def grande(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].upper()
    return lista

print(grande(album))
print()
print(album)

print()

album = [
"Caterina Caselli - Cento giorni",
"Delirium - Jesahel",
"Jan Hammer - Crockett's Theme",
"Sonata Arctica - White Pearl, Black Oceans",
"Lucio Dalla - 4 marzo 1943.mp3",
"The Wellermen - Wellerman",
"Manu Chao - Por el Suelo",
"Intillimani - El Pueblo Unido"
]

def accorcia(canzoni, numero):
    if numero > 0 and numero < len(canzoni):
        for i in range(numero):
            canzoni.pop()
    else:
        canzoni = []
    return canzoni

print(album)
print()
print(accorcia(album, 3))
print()
print(album)
print()
album = [
"Caterina Caselli - Cento giorni",
"Delirium - Jesahel",
"Jan Hammer - Crockett's Theme",
"Sonata Arctica - White Pearl, Black Oceans",
"Lucio Dalla - 4 marzo 1943.mp3",
"The Wellermen - Wellerman",
"Manu Chao - Por el Suelo",
"Intillimani - El Pueblo Unido"
]

def accorcia2(canzoni, numero):
    ret = []
    if numero >= len(canzoni):
        return ret
    for i in range(len(canzoni) - numero):
        ret.append(canzoni.pop())
    ret.reverse()
    return ret

ris1 = accorcia2(album, 3)
print('ritornato:\n', ris1,'\n')
print("l'album è:\n", album,'\n')
ris2 = accorcia2(album, 5)
print('ritornato:\n', ris2, '\n')
print("l'album è:\n", album, '\n')

print(lambda x: x*2)
print()

f = lambda x: x*2
print(f)
print()

print(f(5))
print(f(7))

#def f(x):
    #return x*2

animali = [('cane', 12), ('gatto', 14), ('pellicano', 30), ('acquila', 25), ('scoiattolo', 6)]

animali.sort(key= lambda t: t[1])
print(animali)

animali = [('cane', 12), ('gatto', 14), ('pellicano', 30), ('acquila', 25), ('scoiattolo', 6)]
print(animali)

def mia_f(t):
    return t[1]

animali.sort(key=mia_f)
print(animali)

mia_molt = lambda x,y: x*y
print(mia_molt(3,7))


def bc(f,seq):
    return (f(seq[0]), f(seq[-1]))

print(bc(lambda x: x.upper(), ['quel', 'fiume', 'è', 'in', 'piena']))
print(bc(lambda x: x[0], ['quel', 'fiume', 'è', 'in', 'piena'] ))
print()


def processa(f, lista, listb):
    orda = list(sorted(lista))
    ordb = list(sorted(listb))
    ret = []
    for i in range(len(lista)):
        ret.append(f(orda[i], ordb[i]))
    return ret

f = lambda x,y: x.upper() + y
print(processa(f, ['d','b','a','c','e','f'], ['q','s','p','t','r','n']))

def fai_torta(latte, zucchero, farina):
    #supponiamo servano 1.3kg di latte, 0.2 kg di zucchero e 1.0 per la farina
    #- prende come parametri le quantità che abbiamo in dispensa
    
    if latte > 1.3:
        print('prendo il latte')
        #return True
    else:
        print('Non ho abbastanza latte!')
        return False
    
    if zucchero > 0.2:
        print('prendo lo zucchero')
    else:
        print('Non ho abbastanza zucchero!')
        return False
    
    if farina > 1.0:
        print('prendo la farina')
    else:
        print('Non ho abbastanza farina!')
        return False
    
    print('Impasto!')
    print('Scaldo')
    print('Ho fatto la torta!')
    return True

fatta_torta = fai_torta(5,1,0.3)
if fatta_torta == True:
    print('Festeggia!')
else:
    print('No party!')


def fai_torta_eccezionale(latte, zucchero, farina):
    if latte > 1.3:
        print('Prendo il latte!')
    else:
        raise Exception('Manca er latte')
    
    if zucchero > 0.2:
        print('Prendo lo zucchero!')
    else:
        raise Exception('Non c\'è i zucchero')
    
    if farina > 1.0:
        print('Prendo a farina')
    else:
        raise Exception('Non ho abbastanza farina!')
    
    print('Impasto!')
    print('Scaldo')
    print('Ho fatto la torta!')

fai_torta_eccezionale(5,1,0.3)
print('Festeggia!')

def fai_torta_eccezionale2(latte, zucchero, farina):
    if latte > 1.3:
        print('Prendo il latte!')
    else:
        raise Exception('Manca er latte')
    
    if zucchero > 0.2:
        print('Prendo lo zucchero!')
    else:
        raise Exception('Non c\'è i zucchero')
    
    if farina > 1.0:
        print('Prendo a farina')
    else:
        print('Non ho abbastanza farina, la vado a comprare')
        raise Exception('Non ho abbastanza farina!')
    
    print('Impasto!')
    print('Scaldo')
    print('Ho fatto la torta!')

try:
    fai_torta_eccezionale2(5,1,0.3)
    print('Festeggia')
except:
    fai_torta_eccezionale2(5,1,20)
    print('Festeggia')

def fai_tortona(latte, zucchero, farina):
    if latte > 1.3:
        print('Prendo il latte')
    else:
        raise ValueError('Non ho abbastanza latte')
    
    if zucchero > 0.2:
        print('Prendo lo zucchero')
    else:
        raise ValueError('Non ho abbastanza zucchero!')
    
    if farina > 1.0:
        print('Prendo la farina')
    else:
        raise ValueError('Non ho abbastanza farina!')
    
try:
    fai_tortona(5,1,0.3)
except ValueError:
    print()
    print('Ci deve essere un problema con gli ingredienti!')
    print('Proviamo a chiedere ai vicini!')
    print('Che fortuna, ci hanno dato della farina, riproviamo!')
    print('')
    fai_tortona(5,1,4)
    print('Festeggia!')
except: #gestisce tutte le altre eccezioni
    print('Ragazzi, è successo un problema grave, non so come fare. Meglio uscire a prendere un gelato!')

print('Prima')
assert True
print('Dopo')

print('Prima')
assert False
print('Dopo')

livello = 40
print('Livello acqua', livello)
livello = 5

print('Attenzione, livello acqua basso a', livello)

assert livello >= 20
print('Fai partire tutto')

livello = 40
print('Livell acqua', livello)
livello = 5

print('Attenzione, livello acqua basso a', livello)

if livello <= 20:
    raise Exception('Livello acqua troppo basso!')

print('Fai partire tutto')

def somma(x,y):
    s = x + y
    return s

assert somma(3,2) == 5

def somma1(x,y):
    return x+y
    raise Exception('IMPLEMENTAMI')

assert somma1(2,3) == 5
assert somma1(3,1) == 4
assert somma1(-2,5) == 3


def somma2(x,y):
    return x + y

assert somma2(2,3) == 5
assert somma2(3,1) == 4
assert somma2(-2,5) == 3


def moltiplica(x,y):
    return x * y
    #raise Exception('Implementami')

assert moltiplica(2,5) == 10
assert moltiplica(0,2) == 0
assert moltiplica(3,2) == 6

def mag_tre(x,y,z):
    return max(x,y,z)

print(mag_tre(1,2,4))

def meg_tre(x,y,z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z
        
assert meg_tre(1,2,4) == 4
assert meg_tre(5,7,3) == 7
assert meg_tre(4,4,4) == 4

    
def prezzo_finale(x):
    prezzo = 24.95 
    prezzo_scontato = prezzo - (prezzo * 0.40)
    prezzo_una = prezzo_scontato + 3
    if x > 0:
        if x == 1:
            return prezzo_una
        if x > 1:
            return prezzo_una + (prezzo_scontato * (x-1) + (x-1)*0.75)
    else:
        return 0

p = prezzo_finale(10)
print(p)


def prezzo_final(x):
    if x == 0:
        return 0
    else:
        return x * 24.95*0.6 + 3 + (x-1)*0.75
    
assert prezzo_final(10) == 159.45
assert prezzo_final(0) == 0

#def prxxo_final(x):
  #  pass
 #   raise Exception('IMPLEMENTAMI')

#assert prxxo_final(10) == 159.45
#assert prxxo_final(0) == 0

def ora_arrivo(n,m):
    ore_partenza = 6
    minuti_partenza = 52
    # secondi sono dati dalle ore diviso 2 volte per 60 
    # più minuti per 60 + il tempo che ci vuole per caminare sia piano che veloce
    secondi = ore_partenza*60*60 + minuti_partenza*60 + n * (8*60+15) + m * (7*60+12)
    # minuti sono dati da secondi diviso 60
    minuti = secondi // 60
    # ore sono date da minuti diviso 60
    ore = minuti // 60
    
    ora_mostra = ore % 24
    minuti_mostra = minuti % 60

    return '%s:%s' % (ora_mostra, minuti_mostra)

    raise Exception('Scivi')

print(ora_arrivo(2,2))
print(ora_arrivo(0,0))
print(ora_arrivo(2,5))
print(ora_arrivo(8,5))
assert ora_arrivo(40,5) == '12:58'
assert ora_arrivo(100,25) == '23:37'
assert ora_arrivo(100,40) == '1:25'
assert ora_arrivo(700,305) == '19:43' # Forrest Gump
print( ora_arrivo(40,5))
print( ora_arrivo(100,25))
print( ora_arrivo(100,40))
print( ora_arrivo(700,305))

def lung1(stringa):
    return len(stringa)

x = lung1('Ciao')
print(x)

def lung2(stringa):
    count = 0
    for i in stringa:
        count += 1
    return count

x = lung2('mondo')
print(x)

def contin(parola, stringa):
    return stringa in parola

x = contin('carpenteria', 'ent')
print(x)
x = contin('carpenteria', 'zent')
print(x)

def invertilet(primo, secondo):
    if len(primo) > 3 and len(secondo) > 3:
        return primo[:-1] + secondo[-1] + ' ' + secondo[:-1] + primo[-1]
    else:
        return 'errore!'
    
x = invertilet('hiff', 'mondo')
print(x)

def nspazio(stringa, spazio):
    if spazio < len(stringa):
        return stringa[:spazio] + ' ' + stringa[spazio:]
    else:
        return 'errore!'
    
x = nspazio('largamente', 5)
print(x)
x = nspazio('ciao', 9)
print(x)
x = nspazio('ciao', 4)
print(x)

def inifin(stringa):
    if len(stringa) >= 4:
        print(stringa[:2] + stringa[-2:])
    elif len(stringa) < 4:
        print('Voglio almeno 4 caratteri')

x = inifin('ciaomondo')
x = inifin('hi')
x = inifin('ciao')

def scambia(stringa):
    print(stringa[-1] + stringa[1:-1] + stringa[0])

scambia('mondo')

def halet(parola, lettera):
    x = 0
    while x < len(parola):
        if parola[x] == lettera:
            return True
        x += 1
    return 'la lettera non c\'è'
    raise Exception('IMPLEMENTAMI')

print(halet('gatto', 'o'))
assert halet('ciao', 'o') == True
assert not halet('ciao', 'A') == True

def conta(parola, lettera):
    x = 0
    count = 0
    while x < len(parola):
        if parola[x] == lettera:
            count += 1
        x += 1
    return count

print(conta('elefante', 'e'))

def conta1(parola, lettera):
    count = 0
    for char in parola:
        if char == lettera:
            count += 1
    return count
    raise Exception('IMPLEMENTAMI')

print(conta1('elefante', 'e'))

assert conta("ciao", "z") == 0
assert conta("ciao", "c") == 1
assert conta("babbo", "b") == 3
assert conta("", "b") == 0
assert conta("ciao", "C") == 0

def contiene_minuscola(stringa):
    x = 0
    while x < len(stringa):
        if stringa[x] == stringa[x].lower():
            return True
        x += 1
    return 'Niente lettere minuscole'
    raise Exception('Scivi')

print(contiene_minuscola('ELe'))

assert contiene_minuscola("David")
assert contiene_minuscola("daviD")
assert not contiene_minuscola("DAVID") == True
assert not contiene_minuscola("") == True
assert contiene_minuscola("a")
assert not contiene_minuscola("A") == True
print()

def dialetto(stringa):
    si_no = False
    for i in range(len(stringa)):
        if stringa[i] == 'a':
            if i > 0 and stringa[i-1] == 'g':
                si_no = True
            else:
                return False
    return si_no

print(dialetto('ammagot'))
assert dialetto('paganog') == False
assert dialetto('pgaganog') == True
print(dialetto('cigao'))
print(dialetto('ciao'))
print(dialetto('zogava'))
print(dialetto('zogavga'))

def dialetto1(stringa):
    for i in range(len(stringa)):
        if stringa[i] == 'a':
            if i == 0 or stringa[i-1] != 'g':
                return False
    return True

assert dialetto1("a") == False
assert dialetto1("ab") == False
assert dialetto1("ag") == False
assert dialetto1("ag") == False
assert dialetto1("ga") == True
assert dialetto1("gga") == True
assert dialetto1("gag") == True
assert dialetto1("gaa") == False
assert dialetto1("gaga") == True
assert dialetto1("gabga") == True
assert dialetto1("gabgac") == True
assert dialetto1("gabbgac") == True
assert dialetto1("gabbgagag") == True
print()
assert dialetto("a") == False
assert dialetto("ab") == False
assert dialetto("ag") == False
assert dialetto("ag") == False
assert dialetto("ga") == True
assert dialetto("gga") == True
assert dialetto("gag") == True
assert dialetto("gaa") == False
assert dialetto("gaga") == True
assert dialetto("gabga") == True
assert dialetto("gabgac") == True
assert dialetto("gabbgac") == True
assert dialetto("gabbgagag") == True

def contavoc(stringa):
    vocali = list('aeiou')
    count = 0
    for i in stringa:
        if i.lower() in vocali:
            count += 1
    if count % 2 != 0:
        raise ValueError('Vocali dispari!')
    else:
        return count

print(contavoc('asso'))
assert contavoc("arco") == 2
assert contavoc("scaturire") == 4
try:
    contavoc("ciao") # con questa stringa ci attendiamo che sollevi l'eccezione␣
#,→ValueError
    raise Exception("Non dovrei arrivare fin qui !")
except ValueError: # se solleva l'eccezione ValueError,si sta comportando come␣
#,→previsto e non facciamo niente
    pass
try:
    contavoc("aiuola") # con questa stringa ci attendiamo che sollevi l'eccezione␣
    #,→ValueError
    raise Exception("Non dovrei arrivare fin qui !")
except ValueError: # se solleva l'eccezione ValueError,si sta comportando come␣
#,→previsto e non facciamo niente
    pass

try:
    contavoc("aiuola") # con questa stringa ci attendiamo che sollevi l'eccezione␣
#,→ValueError
    raise Exception("Non dovrei arrivare fin qui !")
except ValueError: # se solleva l'eccezione ValueError,si sta comportando come␣
#,→previsto e non facciamo niente
    pass

def palindroma(stringa):
    if stringa[::-1] == stringa:
        return True
    else:
        return False

print(palindroma('radar'))
print(palindroma('scatola'))


assert palindroma('') == True # assumiamo che la stringa vuota sia palindroma
assert palindroma('a') == True
assert palindroma('aa') == True
assert palindroma('ab') == False
assert palindroma('aba') == True
assert palindroma('bab') == True
assert palindroma('bba') == False
assert palindroma('abb') == False
assert palindroma('abba') == True
assert palindroma('baab') == True
assert palindroma('abbb') == False
assert palindroma('bbba') == False
assert palindroma('radar') == True
assert palindroma('scatola') == False

print()


def palindroma1(stringa):
    for i in range(len(stringa)//2):
        if stringa[i] != stringa[len(stringa)-i-1]:
            return False
    return True

assert palindroma1('') == True # assumiamo che la stringa vuota sia palindroma
assert palindroma1('a') == True
assert palindroma1('aa') == True
assert palindroma1('ab') == False
assert palindroma1('aba') == True

def stampaparole(stringa):
    stringa = stringa.split()
    for i in stringa:
        print(i)
    
stampaparole('la mucca sta al pascolo')

def stampa_pari(lista):
    for i in lista:
        if i % 2 == 0:
            print(i)

stampa_pari([1,2,3,4,5,6])

def cerca26(lista):
    if 26 in lista:
        return True
    else:
        return False

print(cerca26([1,26,143,431,53,6]))


def cerca431(lista):
    return 26 in lista

print(cerca431([1,26,143,431,53,6]))


def stamprisec(stringa):
    stringa = stringa.split()
    print(stringa[0], stringa[1])

stamprisec('ciao come stai?')

def trepari(lista):
    if len(lista) <= 3:
        print('non va bene')
    elif lista[0] % 2 == 0 and lista[1] % 2 == 0 and lista[2] % 2 == 0:
        print(True)
    else:
        print(False)

trepari([6,4,8,4,5])
trepari([6,3,8,4,5])
trepari([6,4])

def trepari1(lista):
    if len(lista) >= 3:
        print(lista[0] % 2 == 0 and lista[1] % 2 == 0 and lista[2] % 2 == 0)
    else:
        print('non va bene')

trepari1([6,4,8,4,5])
trepari1([6,3,8,4,5])
trepari1([6,4])

def separa_ip(stringa):
    stringa = stringa.split('.')
    for i in stringa:
        print(i)

separa_ip('192.168.0.1')

def media(lista):
    if len(lista) > 0:
        count = 0
        for i in lista:
            count += i
        return count / len(lista)
    else:
        return 0

print(media([4,4,2,3]))
print(media([]))
print(media([30,28,20,29]))

def nuoradf(lista):
    lista2 = []
    for i in lista:
        lista2.append(i*2)
    return lista2

numeri = [1,2,3,4,5]

numeri2 = nuoradf(numeri)
print(numeri)
print(numeri2)
assert nuoradf([]) == []
assert nuoradf([3]) == [6]
assert nuoradf([3,7,1]) == [6,14,2]
l = [3,7,1]
assert nuoradf(l) == [6,14,2]
assert l == [3,7,1]
print()

def radm(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]*2

numeri = [1,2,3,4,5]
print(numeri)
radm(numeri)
print(numeri)
l = []
radm(l)
assert l == []
l = [3]
radm(l)
assert l == [6]
l = [3,7,1]
radm(l)
assert l == [6,14,2]
print()

def nuoradc(lista):
    return [ x*2 for x in lista]

numeri = [1,2,3,4,5]
print(nuoradc(numeri))
print(numeri)

assert nuoradc([]) == []
assert nuoradc([3]) == [6]
assert nuoradc([3,7,1]) == [6,14,2]
l = [3,7,1]
assert nuoradc(l) == [6,14,2]
assert l == [3,7,1]

def up(lista):
    return [x.upper() for x in lista]

assert up([]) == []
assert up(['']) == ['']
assert up(['a']) == ['A']
assert up(['aA']) == ['AA']
assert up(['Ba']) == ['BA']
assert up(['Ba', 'aC']) == ['BA','AC']
assert up(['Ba dA']) == ['BA DA']
l = ['ciAo']
assert up(l) == ['CIAO']
assert l == ['ciAo']


def rimtut(lista1, lista2):
    nuova = []
    for x in lista2:
        if x not in lista1:
            nuova.append(x)
    return nuova

print(rimtut([1,2,3], [1,2,3,4,5]))

assert rimtut([],[]) == []
assert rimtut(['a'], []) == []
assert rimtut([], ['a']) == ['a']
assert rimtut(['a'], ['a']) == []
assert rimtut(['b'], ['a']) == ['a']
assert rimtut(['a', 'b'], ['a','c','b']) == ['c']
orig_l1,orig_l2 = ['a','d'], ['a','c','d','b']
assert rimtut(orig_l1, orig_l2) == ['c', 'b']
assert orig_l1 == ['a','d'] # controlla che non modifichi l'originale
assert orig_l2 == ['a','c','d','b']

print()

def rimtut2(list1, list2):
    list3 = list2[:]
    for x in list1:
        if x in list3:
            list3.remove(x)
    return list3

print(rimtut([1,2,3], [1,2,3,4,5]))

assert rimtut2([],[]) == []
assert rimtut2(['a'], []) == []
assert rimtut2([], ['a']) == ['a']
assert rimtut2(['a'], ['a']) == []
assert rimtut2(['b'], ['a']) == ['a']
assert rimtut2(['a', 'b'], ['a','c','b']) == ['c']
orig_l1,orig_l2 = ['a','d'], ['a','c','d','b']
assert rimtut2(orig_l1, orig_l2) == ['c', 'b']
assert orig_l1 == ['a','d'] # controlla che non modifichi l'originale
assert orig_l2 == ['a','c','d','b']


def solmaf(lista):
    nuova = []
    for i in lista:
        if i.isupper():
            nuova.append(i)
    return nuova

print(solmaf(['AB','Ba','Ab']))

assert solmaf(["CD"]) == [ "CD"]
assert solmaf(["ab"]) == []
assert solmaf(["dE"]) == []
assert solmaf(["De"]) == []
assert solmaf(["ab","DE"]) == ["DE"]
orig = ["ab", "CD", "Hb", "EF"]
assert solmaf(orig) == [ "CD", "EF"]
assert orig == ["ab", "CD", "Hb", "EF"]

def solmac(lista):
    return [i for i in lista if i.isupper()]

print(solmac(['AB','Ba','Ab']))
assert solmac(["CD"]) == [ "CD"]
assert solmac(["ab"]) == []
assert solmac(["dE"]) == []
assert solmac(["De"]) == []
assert solmac(["ab","DE"]) == ["DE"]
orig = ["ab", "CD", "Hb", "EF"]
assert solmac(orig) == [ "CD", "EF"]
assert orig == ["ab", "CD", "Hb", "EF"]


def somtut(lista):
    count = 0
    for i in lista:
        count += i
    return count

print(somtut([1,2,3,4,5,6]))
assert somtut([]) == 0
assert somtut([7,5]) == 12
assert somtut([9,5,8]) == 22

def somtut1(lista):
    return sum(lista)

print(somtut1([1,2,3,4,5,6]))
assert somtut1([]) == 0
assert somtut1([7,5]) == 12
assert somtut1([9,5,8]) == 22


def somparif(lista):
    count = 0
    for i in lista:
        if i % 2 == 0:
            count += i
    return count

print(somparif([1,2,3,4,5,6]))
assert somparif([]) == 0
assert somparif([9]) == 0
assert somparif([4]) == 4
assert somparif([7,2,5,8]) == 10

def somtuc(lista):
    return sum([i for i in lista if i % 2 == 0])

print(somtuc([1,2,3,4,5,6]))
assert somtuc([]) == 0
assert somtuc([9]) == 0
assert somtuc([4]) == 4
assert somtuc([7,2,5,8]) == 10

def contiene(lista, elemento):
    if elemento in lista:
        return True
    else:
        return False
    raise Exception('stupido')


print(contiene([1,2,3,4,5], 3))
print(contiene([1,2,3,4,5], 7))

assert contiene([],'a') == False
assert contiene(['a'],'a') == True
assert contiene(['a','b','c'],'b') == True
assert contiene(['a','b','c'],'z') == False

def contiene1(lst, ele):
    return ele in lst

print(contiene1([1,2,3,4,5], 3))
print(contiene1([1,2,3,4,5], 7))
assert contiene1([],'a') == False
assert contiene1(['a'],'a') == True
assert contiene1(['a','b','c'],'b') == True
assert contiene1(['a','b','c'],'z') == False

def primi(numero):
    if numero > 0:
        return list(range(numero))
        raise Exception('scrivi')
    else:
        return []

print(primi(6))

assert primi(-1) == []
assert primi(-2) == []
assert primi(0) == []
assert primi(1) == [0]
assert primi(2) == [0,1]
assert primi(3) == [0,1,2]

def primi1(numero):
    nuova = []
    if numero > 0:
        x = 0
        while x < numero:
            nuova.append(x)
            x+=1
        return nuova
    else:
        return nuova
        raise Exception('scrivi')
    
print(primi1(6))
assert primi1(-1) == []
assert primi1(-2) == []
assert primi1(0) == []
assert primi1(1) == [0]
assert primi1(2) == [0,1]
assert primi1(3) == [0,1,2]

def primi2(numero):
    lista = []
    contatore = 0
    while contatore < numero:
        lista.append(contatore)
        contatore += 1
    return lista

print(primi2(6))
assert primi2(-1) == []
assert primi2(-2) == []
assert primi2(0) == []
assert primi2(1) == [0]
assert primi2(2) == [0,1]
assert primi2(3) == [0,1,2]

def primi3(numero):
    lista = []
    for i in range(numero):
        lista.append(i)
    return lista

print(primi3(6))
assert primi3(-1) == []
assert primi3(-2) == []
assert primi3(0) == []
assert primi3(1) == [0]
assert primi3(2) == [0,1]
assert primi3(3) == [0,1,2]

def primul(lista):
    return lista[0] == lista[-1]
    raise Exception('scrivi')

print(primul([1,2,3,4]))
assert primul(['a']) == True
assert primul(['a','a']) == True
assert primul(['a','b']) == False
assert primul(['a','b','a']) == True
assert primul(['a','b','c','a']) == True
assert primul(['a','b','c','d']) == False


def duplica(lista):
    nuova = []
    for x in lista:
        nuova.append(x)
        nuova.append(x)
    return nuova
    raise Exception('scrivi')
print(duplica(['ciao', 'mondo', 'python']))

assert duplica([]) == []
assert duplica(['a']) == ['a','a']
assert duplica(['a','b']) == ['a','a','b','b']
assert duplica(['a','b','c']) == ['a','a','b','b','c','c']
assert duplica(['a','a']) == ['a','a','a','a']
assert duplica(['a','a','b','b']) == ['a','a','a','a','b','b','b','b']

def hadup(el, lista):
    count = 0
    for i in lista:
        if i == el:
            count += 1
    return count > 1

print(hadup(1, [1,2,3,4,5,1]))
assert hadup("a", []) == False
assert hadup("a", ["a"]) == False
assert hadup("a", ["a", "a"]) == True
assert hadup("a", ["a", "a", "a"]) == True
assert hadup("a", ["b", "a", "a"]) == True
assert hadup("a", ["b", "a", "a", "a"]) == True
assert hadup("b", ["b", "a", "a", "a"]) == False
assert hadup("b", ["b", "a", "b", "a"]) == True

def hadup1(el, lista):
    contatore = 0
    for x in lista:
        if x == el:
            contatore += 1
            if contatore > 1:
                return True
    return False

print(hadup1(1, [1,2,3,4,5,1]))
assert hadup1("a", []) == False
assert hadup1("a", ["a"]) == False
assert hadup1("a", ["a", "a"]) == True
assert hadup1("a", ["a", "a", "a"]) == True
assert hadup1("a", ["b", "a", "a"]) == True
assert hadup1("a", ["b", "a", "a", "a"]) == True
assert hadup1("b", ["b", "a", "a", "a"]) == False
assert hadup1("b", ["b", "a", "b", "a"]) == True

print()
def ord3(lista):
    if len(lista) >= 3:
        if lista[0] < lista[1] < lista[2]:
            return True
        else:
            return False
    else:
        return False
    
print(ord3([1,4,3]))
assert ord3([5]) == False
assert ord3([4,7]) == False
assert ord3([4,6,9]) == True
assert ord3([4,9,7]) == False
assert ord3([9,5,7]) == False
assert ord3([4,8,9,1,5]) == True # primi 3 elementi crescenti
assert ord3([9,4,8,10,13]) == False # primi 3 elementi NON crescenti


print()
def ord4(lista):
    if len(lista) >= 3:
        return lista[0] < lista[1] < lista[2]
    else:
        return False

print(ord4([1,2,3]))

print()
def ord5(lista):
    if len(lista) >= 3:
        return lista[0] <= lista[1] and lista[1] <= lista[2]
    else:
        return False
print(ord5([1,3]))
print()

def filtrab(lista):
    nuova = []
    for i in lista:
        if i == 'a' or i ==  'b':
            nuova.append(i)
    return nuova
    raise Exception('Scivi la funzione')

print(filtrab(list('cacdbacabe')))
assert filtrab([]) == []
assert filtrab(['a']) == ['a']
assert filtrab(['b']) == ['b']
assert filtrab(['a','b']) == ['a','b']
assert filtrab(['a','b','c']) == ['a','b']
assert filtrab(['a','c','b']) == ['a','b']
assert filtrab(['c','a','b']) == ['a','b']
assert filtrab(['c','a','c','d','b','a','c','a','b','e']) == ['a','b','a','a','b']
l = ['a','c','b']
assert filtrab(l) == ['a','b'] # verifica che sia ritornata una NUOVA lista
assert l == ['a','c','b'] 

print()

def collina(numero):
    return list(list(range(numero+1)[1:])+list(range(numero))[:0:-1])

print(collina(4))

assert collina(0) == []
assert collina(1) == [1]
assert collina(2) == [1,2,1]
assert collina(3) == [1,2,3,2,1]
assert collina(4) == [1,2,3,4,3,2,1]
assert collina(5) == [1,2,3,4,5,4,3,2,1]

def collina2(numero):
    lista = []
    for i in range(1,numero):
        lista.append(i)
    for i in range(numero,0,-1):
        lista.append(i)
    return lista

print(collina2(4))

assert collina2(0) == []
assert collina2(1) == [1]
assert collina2(2) == [1,2,1]
assert collina2(3) == [1,2,3,2,1]
assert collina2(4) == [1,2,3,4,3,2,1]
assert collina2(5) == [1,2,3,4,5,4,3,2,1]

print()

def vetta(lista):
    if len(lista) > 3:
        massimo = lista[0]
        for i in lista:
            if i > massimo:
                massimo = i
        return massimo
    else:
        raise ValueError('Meno di 3 elementi')
    
print(vetta([100, 400, 800, 1220, 1600, 1400, 1000, 200, 40]))

print()

def vetta2(lista):
    massimo = 0 #lista[0]
    if len(lista) >= 3:
        x = 0
        while x < len(lista):
            if lista[x] > massimo:
                massimo = lista[x]
            else:#solo se il valore più grande sta in mezzo
                return massimo
            x += 1
        return massimo
    else:
        raise ValueError('Meno di 3 elementi')

print(vetta2([100, 400, 800, 1220, 1600, 1400, 1000, 200, 40]))
assert vetta2([5,40,7]) == 40
assert vetta2([5,30,4]) == 30
assert vetta2([5,70,70, 4]) == 70
assert vetta2([5,10,80,25,2]) == 80
assert vetta2([100,400, 800, 1220, 1600, 1400, 1000, 300, 40]) == 1600

def pari(lista):
    nuova = []
    for i in range(len(lista)):
        if i % 2 == 0:
            nuova.append(lista[i])
    return nuova

print(pari([0,1,2,3,4]))

def pari2(lista):
    nuova = []
    for i in range(0, len(lista), 2):
        nuova.append(i)
    return nuova

print(pari2([0,1,2,3,4]))
assert pari([]) == []
assert pari(['a','b']) == ['a']
assert pari(['a','b','c','d']) == ['a', 'c']
assert pari(['a','b','a','c']) == ['a', 'a']
assert pari(['a','b','c','d','e','f']) == ['a', 'c','e']


def mix(lista1, lista2):
    nuova = []
    for i in range(len(lista1)):
        nuova.append(lista1[i])
        nuova.append(lista2[i])
    return nuova
    raise Exception('funzione mancante')

print(mix(['a','b','c'], ['x', 'v', 'z']))
assert mix([], []) == []
assert mix(['a'], ['x']) == ['a', 'x']
assert mix(['a'], ['a']) == ['a', 'a']
assert mix(['a', 'b'], ['x', 'y']) == ['a', 'x', 'b','y']
assert mix(['a', 'b','c'], ['x', 'y','z']) == ['a', 'x', 'b','y', 'c','z']

def nostop(stringa, stopwords):
    lista = stringa.split()
    for i in stopwords: #convertire a set è più veloce
        if i in lista:
            lista.remove(i)
    return ' '.join(lista)

print(nostop('un libro su python', ['un', 'su']))

assert nostop("un", ["un"]) == ""
assert nostop("un", []) == "un"
assert nostop("", []) == ""
assert nostop("", ["un"]) == ""
assert nostop("un libro", ["un"]) == "libro"
assert nostop("un libro su Python", ["un","su"]) == "libro Python"
assert nostop("un libro su Python per principianti", ["un","uno","il","su","per"]) == "libro Python principianti"
assert nostop("un libro\tsu Python\nper principianti", ["un","uno","il","su","per"]) == "libro Python principianti"

def nostop2(stringa, stopwords):
    insieme = set(stopwords)
    lista = stringa.split()
    ret = []
    for parola in lista:
        if parola not in insieme:
            ret.append(parola)
    return ' '.join(ret)

print(nostop2('un libro su python', ['un', 'su']))

assert nostop2("un", ["un"]) == ""
assert nostop2("un", []) == "un"
assert nostop2("", []) == ""
assert nostop2("", ["un"]) == ""
assert nostop2("un libro", ["un"]) == "libro"
assert nostop2("un libro su Python", ["un","su"]) == "libro Python"
assert nostop2("un libro su Python per principianti", ["un","uno","il","su","per"]) == "libro Python principianti"
assert nostop2("un libro\tsu Python\nper principianti", ["un","uno","il","su","per"]) == "libro Python principianti"

def trez(lst):
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = 'z'
    return lst

lst = ['f','c','s','g','a','w','a','b']
print(lst)
print(trez(lst))
print(lst)

l1 = []
trez(l1)
assert l1 == []
l2 = ['a']
trez(l2)
assert l2 == ['z']
l3 = ['a','b']
assert trez(['a','b']) # non ritorna niente!
trez(l3)
assert l3 == ['z','b']
l4 = ['a','b','c']
trez(l4)
assert l4 == ['z','b','c']
l5 = ['a','b','c','d']
trez(l5)
assert l5 == ['z','b','c','z']
l6 = ['f','c','s','g','a','w','a','b']
trez(l6)
assert l6 == ['z','c','s','z','a','w','z','b']
print()

def listoint(lista):
    lista = lista[::-1]
    numero = 0
    var = 1
    for i in range(len(lista)):
        numero += lista[i] * var
        var *= 10
    return numero

print(listoint([3,7,5]))
print(listoint([2,0]))
assert listoint([0]) == 0
assert listoint([1]) == 1
assert listoint([2]) == 2
assert listoint([92]) == 92
assert listoint([90]) == 90
assert listoint([5,7,4]) == 574

print()
#importanti
def listoint2(lista):
    numero = 0
    var = 1
    for i in reversed(lista):
        numero += i * var
        var *= 10
    return numero

print(listoint2([3,7,5]))
print(listoint2([2,0]))
assert listoint2([0]) == 0
assert listoint2([1]) == 1
assert listoint2([2]) == 2
assert listoint2([92]) == 92
assert listoint2([90]) == 90
assert listoint2([5,7,4]) == 574
print()

def intolist(numero):
    if numero == 0:
        return [0]
    else:
        ret = []
        while numero > 0:
            cifra = numero % 10 #resto di numero diviso 10
            ret.append(cifra)
            numero = numero // 10
        return list(reversed(ret))
    
print(intolist(574))
assert intolist(0) == [0]
assert intolist(1) == [1]
assert intolist(2) == [2]
assert intolist(92) == [9,2]
assert intolist(90) == [9,0]
assert intolist(574) == [5,7,4]
print()

numero = 567
print(numero)
a = numero % 10
b = numero // 10 % 10
c = numero // 100 % 10
print(c,b,a)

for i in range(50):
    print(numero % 10)
    numero = numero // 10
    if numero == 0:
        break
print()

def addone(lst):
    power = 1
    num = listoint(lst)
    return intolist(num + 1)
    
print(addone([1,2,3]))
print(addone([3,6,9,9]))

assert addone([0]) == [1]
assert addone([1]) == [2]
assert addone([2]) == [3]
assert addone([9]) == [1, 0]
assert addone([5,7]) == [5, 8]
assert addone([5,9]) == [6, 0]
assert addone([9,9]) == [1, 0, 0]


def add_one(lst):
    power = 1
    num = listoint(lst)
    return intolist(num + 1)

assert add_one([0]) == [1]
assert add_one([1]) == [2]
assert add_one([2]) == [3]
assert add_one([9]) == [1, 0]
assert add_one([5,7]) == [5, 8]
assert add_one([5,9]) == [6, 0]
assert add_one([9,9]) == [1, 0, 0]
      
def add_one_rip(lst):
    nuova = []
    riporto = 0
    uno = 1
    for i in reversed(lst):
        cifra = i + uno + riporto
        if cifra == 10:
            nuova.append(0)
            riporto = 1
            uno = 0
        else:
            nuova.append(cifra)
            riporto = 0
            uno = 0
    if riporto == 1:
        nuova.append(riporto)

    return list(reversed(nuova))

print(add_one_rip([7,8,9]))
assert add_one_rip([0]) == [1]
assert add_one_rip([1]) == [2]
assert add_one_rip([2]) == [3]
assert add_one_rip([9]) == [1, 0]
assert add_one_rip([5,7]) == [5, 8]
assert add_one_rip([5,9]) == [6, 0]
assert add_one_rip([9,9]) == [1, 0, 0]

def add_one_rip(lst):
    ret = []
    riporto = 1
    for cifra in reversed(lst):
        nuova_cifra = cifra + riporto
        if nuova_cifra == 10:
            ret.append(0)
            riporto = 1
        else:
            ret.append(nuova_cifra)
            riporto = 0
    if riporto == 1:
        ret.append(riporto)
    ret.reverse()
    return ret

print(add_one_rip([7,8,9]))
assert add_one_rip([0]) == [1]
assert add_one_rip([1]) == [2]
assert add_one_rip([2]) == [3]
assert add_one_rip([9]) == [1, 0]
assert add_one_rip([5,7]) == [5, 8]
assert add_one_rip([5,9]) == [6, 0]
assert add_one_rip([9,9]) == [1, 0, 0]

#congettura di collatz
def collatz(n):
    nuova = []
    while n != 1:
        if n % 2 == 0:
            nuova.append(n)
            n //= 2
        elif n % 2 == 1:
            nuova.append(n)
            n = n * 3 +  1
    nuova.append(n)
    return nuova, len(nuova)

print(collatz(27))

def giunto(ta, tb):
    if len(ta) > 0 and len(tb) > 0:
        if ta[-1] == tb[0]:
            return ta + tb[1:]
    return ()

print(giunto(('m','e','s'), ('s','a','g','g','e','r','o')))

assert giunto(('o','r'), ('r','o','r','e')) == ('o', 'r', 'o', 'r','e')
assert giunto(('c','u'), ('o','r','e')) == ()
assert giunto((),('e','f','g')) == ()
assert giunto(('a',),('e','f','g')) == ()
assert giunto(('a','b','c'),()) == ()
assert giunto(('a','b','c'),('d','e')) == ()

def nasty(ta, tb):
    tupla = []
    for i in range(len(ta)):
        for j in range(tb[i]):
            tupla.append(ta[i]+str(tb[i]))
    return tuple(tupla)

print(nasty(('u','r','g'), (4,2,3)))

assert nasty(('a',), (3,)) == ('a3','a3','a3')
assert nasty(('a','b'), (3,1)) == ('a3','a3','a3','b1')
assert nasty(('u','r','g'), (4,2,3)) == ('u4', 'u4', 'u4', 'u4', 'r2', 'r2', 'g3', 'g3', 'g3')
assert nasty(('g','a','s','p'), (2,4,1,3)) == ('g2', 'g2', 'a4', 'a4', 'a4', 'a4', 's1', 'p3', 'p3', 'p3')

def nasty2(ta, tb):
    i = 0
    ret = []
    for i in range(len(tb)):
        s = ta[i] + str(tb[i])
        ret.extend( (s,) + tb[i] )
        i += 1
    return tuple(ret)
print()

def sillabe(parola, trovate):
    for i in range(0, len(parola), 2):
        trovate.add(parola[i] + parola[i+1])
    #raise Exception('Implementami')

trovate = set()
sillabe('banana', trovate)
print(trovate)

trovate = set()
sillabe("ricaricare", trovate)
print(trovate)

def distingui(lista):
    nuova = set()
    nuova2 = []
    for i in lista:
        nuova.add(tuple(i))
    
    for x in nuova:
        x = list(x)
        nuova2.append(x)
    return nuova2

listona = [ ['d','d'],['a','b'],['d','d'],['c','a'],['c','a'],['d','d'],['a','b']]
print(listona)
print(distingui(listona))

def distingui2(lista):
    s = set()
    ret = []
    for sottolista in lista:
        tup = tuple(sottolista)

        if tup not in s:
            ret.append(sottolista)
            s.add(tup)
            
    return ret

listona = [ ['d','d'],['a','b'],['d','d'],['c','a'],['c','a'],['d','d'],['a','b']]
print(listona)
print(distingui2(listona))

def intersectron(lista):
    if len(lista) == 0:
        return set()
    
    ret = set(lista[0])

    #for el in lista:
        #ret.intersection_update(el)
    [ret.intersection_update(el) for el in lista]

    return ret

print(intersectron([set([1,2]), set([1,2]), set([1,3])]))
assert intersectron([]) == set()
assert intersectron([set(),set()]) == set()
assert intersectron([set(),set(),set()]) == set()
assert intersectron([{'a'},{'a'},{'a'}]) == {'a'}
assert intersectron([{'a','b'},{'b'},{'b'}]) == {'b'}
assert intersectron([{'a'},{'a','b'},{'a'}]) == {'a'}
assert intersectron([{'c'},{'c'},{'c','b'}]) == {'c'}
assert intersectron([{'a','b'},{'a','b'},{'a','b'}]) == {'a','b'}
assert intersectron([{'a','b','c'},{'a','b','c','d'},{'b','c','d'}, {'b','c'}]) == {'b','c'}
# verifica che non abbiamo modificato gli insiemi di input
s = {'a','b'}
assert intersectron([s,{'b','c'}]) == {'b'}
assert s == {'a','b'}
print()

def inter_fast(lista):
    if len(lista) == 0:
        return set()
    return set.intersection(*lista)

# INIZIO TEST - NON TOCCARE !
print(inter_fast([set([1,2]), set([1,2]), set([1,3])]))
assert inter_fast([]) == set()
assert inter_fast([set(),set()]) == set()
assert inter_fast([set(),set(),set()]) == set()
assert inter_fast([{'a'},{'a'},{'a'}]) == {'a'}
assert inter_fast([{'a','b'},{'b'},{'b'}]) == {'b'}
assert inter_fast([{'a'},{'a','b'},{'a'}]) == {'a'}
assert inter_fast([{'c'},{'c'},{'c','b'}]) == {'c'}
assert inter_fast([{'a','b'},{'a','b'},{'a','b'}]) == {'a','b'}
assert inter_fast([{'a','b','c'},{'a','b','c','d'},{'b','c','d'}, {'b','c'}]) == {'b','c'}
# verifica che non abbiamo modificato gli insiemi di input
s = {'a','b'}
assert inter_fast([s,{'b','c'}]) == {'b'}
assert s == {'a','b'}
# FINE TEST

def stampa_val(d, chiave):
    return d[chiave]

print(stampa_val({'a':5, 'b':2}, 'a'))
y = stampa_val({'a':5,'b':2}, 'b')
print(y)

def ha_chiave(d, chiave):
    if chiave in d:
        print('trovato')
    else:
        print('non trovato')
    
ha_chiave({'a':5,'b':2}, 'a')
ha_chiave({'a':5,'b':2}, 'z')

def dim(d):
    return len(d)

x = dim({'a':5,'b':2,'c':9})
print(x)

def mazzol(d):
    la = list(d)
    la.sort()
    return la

x = mazzol({'a':5,'c':2,'b':9})
print(x)

def coppie(d):
    for i in d:
        print(i, d[i])

coppie({'a':5,'b':2,'c':9})

def istogramma2(stringa):
    nuovo = {}
    for i in stringa:
        nuovo[i] = stringa.count(i)

    return nuovo

def istogramma(stringa):
    nuovo = {}
    for i in stringa:
        if i in nuovo:
            nuovo[i] += 1
        else:
            nuovo[i] = 1
    return nuovo

print(istogramma('elefante'))

assert istogramma('') == {}
assert istogramma('du') == {'d':1, 'u':1}
assert istogramma("a") == {'a':1}
assert istogramma("aa") == {'a':2}
assert istogramma("aaa") == {'a':3}
assert istogramma("ba") == {'a':1,
'b':1}
assert istogramma("aba") == {'a':2,
'b':1}
assert istogramma("abc") == {'a':1,'b':1,'c':1}
assert istogramma("acccbb") == {'a':1,'b':2,'c':3}

def listifica(d, ordine):
    nuova = []
    for i in ordine:
        nuova.append(d[i])
    return nuova

print(listifica({'a':1,'b':2,'c':3}, 'bca'))
assert listifica({}, []) == []
assert listifica({'ciao':123}, ['ciao']) == [123]
assert listifica({'a':'x','b':'y'}, ['a','b']) == ['x','y']
assert listifica({'a':'x','b':'y'}, ['b','a']) == ['y','x']
assert listifica({'a':'x','b':'y','c':'x'}, ['c','a','b']) == ['x','x','y']
assert listifica({'a':'x','b':'y','c':'x'}, ['b','c','a']) == ['y','x','x']
assert listifica({'a':5,'b':2,'c':9}, ['b','c','a']) == [2,9,5]
assert listifica({6:'x',8:'y',3:'x'}, [6,3,8]) == ['x','x','y']

def tcont(lista):
    diz = {}
    for tupla in lista:
        if tupla[0] in diz:
            diz[tupla[0]] += tupla[1]
        else:
            diz[tupla[0]] = tupla[1]

    return diz

print(tcont([('a',4), ('b',5)]))
assert tcont([]) == {}
assert tcont([('a',3)]) == {'a':3}
assert tcont([('a',3),('a',4)]) == {'a':7}
assert tcont([('a',3),('b',8), ('a',4)]) == {'a':7, 'b':8}
assert tcont([('a',5), ('c',8), ('b',7), ('a',2), ('a',1), ('c',4)]) == {'a':5+2+1, 'b':7, 'c': 8 + 4}

def inter(d1, d2):
    nuovo = set()
    for i in d1:
        if len(d2) > 0:
            if d1[i] == d2[i]:
                nuovo.add(i)
    return nuovo

a = {'chiave1': 1, 'chiave2': 2 , 'chiave3': 3}
b = {'chiave1': 1 ,'chiave2': 3 , 'chiave3': 3}
print(inter(a,b))
assert inter({'key1': 1, 'key2': 2 , 'key3': 3}, {'key1':1 ,'key2':3 , 'key3':3}) == {'key1', 'key3'}
assert inter(dict(), {'key1':1 ,'key2':3 , 'key3':3}) == set()
assert inter({'key1':1 ,'key2':3 , 'key3':3}, dict()) == set()
assert inter(dict(),dict()) == set()

def inter2(d1, d2):
    res = set()
    for i in d1:
        if i in d2:
            if d1[i] == d2[i]:
                res.add(i)
    return res

a = {'chiave1': 1, 'chiave2': 2 , 'chiave3': 3}
b = {'chiave1': 1 ,'chiave2': 3 , 'chiave3': 3}
print(inter2(a,b))
assert inter2({'key1': 1, 'key2': 2 , 'key3': 3}, {'key1':1 ,'key2':3 , 'key3':3}) == {'key1', 'key3'}
assert inter2(dict(), {'key1':1 ,'key2':3 , 'key3':3}) == set()
assert inter2({'key1':1 ,'key2':3 , 'key3':3}, dict()) == set()
assert inter2(dict(),dict()) == set()

def valori_unici(d):
    nuova = []
    for i in d.values():
        if i not in nuova:
            nuova.append(i)

    nuova.sort()
    return nuova

print(valori_unici({'a':'y','b':'x','c':'x'}))

def valori_unici2(d):
    s = set(d.values())
    ret = list(s)
    ret.sort()
    return ret

assert valori_unici({}) == []
assert valori_unici({'a':'y','b':'x','c':'x'}) == ['x','y']
assert valori_unici({'a':4,'b':6,'c':4,'d':8}) == [4,6,8]
assert valori_unici2({}) == []
assert valori_unici2({'a':'y','b':'x','c':'x'}) == ['x','y']
assert valori_unici2({'a':4,'b':6,'c':4,'d':8}) == [4,6,8]

def maiuscole(lista):
    nuovo = {}
    for parola in lista:
        nuovo[parola] = parola.upper()
    return nuovo

print(maiuscole(["ciao", "mondo", "come va?"]))
assert maiuscole([]) == {}
assert maiuscole(["ciao"]) == {"ciao":"CIAO"}
assert maiuscole(["ciao", "mondo"]) == {"ciao":"CIAO", "mondo":"MONDO"}
assert maiuscole(["ciao", "mondo", "ciao"]) == {"ciao":"CIAO", "mondo":"MONDO"}
assert maiuscole(["ciao", "mondo", "come va?"]) == {"ciao":"CIAO", "mondo":"MONDO","come va?":"COME VA?"}
print()

def filtraz(diz):
    nuovo = {}
    for chiave in diz:
        if 'z' in chiave:
            nuovo[chiave] = diz[chiave]
    return nuovo

print(filtraz({'zibibbo':'da bere',
'mc donald': 'da evitare',
'liquirizia': 'ze best',
'burger king': 'zozzerie'
}))
assert filtraz({}) == {}
assert filtraz({'az':'t'}) == {'az':'t'}
assert filtraz({'zc':'w'}) == {'zc':'w'}
assert filtraz({'b':'h'}) == {}
assert filtraz({'b':'hz'}) == {}
assert filtraz({'az':'t','b':'hz'}) == {'az':'t'}
assert filtraz({'az':'t','b':'hz','zc':'w'}) == {'az':'t', 'zc':'w'}
print()

def powers(numero):
    nuovo = {}
    for i in range(1, numero+1):
        nuovo[i] = i**2
    return nuovo

print(powers(3))
assert powers(1) == {1:1}
assert powers(2) == {   1:1,
                        2:4}

assert powers(3) == {   1:1,
                        2:4,
                        3:9}

assert powers(4) == {   1:1,
                        2:4,
                        3:9,
                        4:16}

def dilist(numero):
    nuovo = {}
    for i in range(1 , numero + 1):
        nuovo[i] = list(range(1,1+i))
    return nuovo

print(dilist(3))
assert dilist(0) == dict()
assert dilist(1) == {
1:[1]
}
assert dilist(2) == {
1:[1],
2:[1,2]
}
assert dilist(3) == {
1:[1],
2:[1,2],
3:[1,2,3]}
print()

def dilist2(n):
    ret = dict()
    for i in range(1,n+1):
        lista = []
        for j in range(1, i+1):
            lista.append(j)
        ret[i] = lista
    return ret

print(dilist2(3))
assert dilist2(0) == dict()
assert dilist2(1) == {
1:[1]
}
assert dilist2(2) == {
1:[1],
2:[1,2]
}
assert dilist2(3) == {
1:[1],
2:[1,2],
3:[1,2,3]}
print()

def prefissi(diz, lista):
    nuova = []
    for citta in lista:
        nuova.append(diz[citta])
    return nuova

print(prefissi({
            'tn':'0461',
            'bz':'0471',
            'mi':'02',
            'to':'011',
            'bo':'051'
            },['tn','to', 'mi']))

assert prefissi({'tn':'0461'}, []) == []
assert prefissi({'tn':'0461'}, ['tn']) == ['0461']
assert prefissi({'tn':'0461', 'bz':'0471'}, ['tn']) == ['0461']
assert prefissi({'tn':'0461', 'bz':'0471'}, ['bz']) == ['0471']
assert prefissi({'tn':'0461', 'bz':'0471'}, ['tn','bz']) == ['0461', '0471']
assert prefissi({'tn':'0461', 'bz':'0471'}, ['bz','tn']) == ['0471', '0461']
assert prefissi({'tn':'0461',
'bz':'0471',
'mi':'02',
'to':'011',
'bo':'051'
},
['tn','to', 'mi']) == ['0461', '011', '02']
print()

def traduci(lista, inglesismi):
    nuova = []
    for i in lista:
        if i in inglesismi:
            nuova.append(inglesismi[i])
        else:
            nuova.append(i)
    return nuova

lista = ["Oggi", "ho", "una riunione", "dove", "discuteremo", "gli obiettivi", "da","raggiungere", "per", "soddisfare", "i nostri clienti" ]
inglesismi={
"una riunione": "un meeting",
"gli obiettivi" : "i goal",
"i nostri clienti" : "il nostro target"
}
print(traduci(lista, inglesismi))
assert traduci([], {}) == []
assert traduci(['a'], {}) == ['a']
assert traduci(['a'], {'a':'x'}) == ['x']
assert traduci(['a b'], {'a b':'x'}) == ['x']
assert traduci(['a','b'], {'a':'x'}) == ['x','b']
assert traduci(['a','b'], {'a':'x','b':'y'}) == ['x','y']
assert traduci(["Oggi", "ho", "una riunione", "dove", "discuteremo",
"gli obiettivi", "da", "raggiungere", "per", "soddisfare", "i nostri clienti"],
{
"una riunione": "un meeting",
"gli obiettivi" : "i goal",
"i nostri clienti" : "il nostro target"
}) == ["Oggi", "ho", "un meeting", "dove", "discuteremo", "i goal", "da",
"raggiungere", "per", "soddisfare", "il nostro target"]
print()

def dopocar(stringa):
    if len(stringa) > 1:
        nuovo = {}
        for i in range(len(stringa)-1):
            nuovo[stringa[i]] = stringa[i+1]
        return nuovo
    
print(dopocar('au'))
assert dopocar('ab') == {'a':'b'}
assert dopocar('cera') == { 'c':'e',
                            'e':'r',
                            'r':'a'}
assert dopocar('orchestra') == {'o': 'r',
                                'c': 'h',
                                'h': 'e',
                                'e': 's',
                                's': 't',
                                't': 'r',
                                'r': 'a'}
print()
#importante
def bestmecha(diz):
    # nuova ha tanti elementi none quanti sono gli elementi di diz
    nuova = [None] * len(diz)
    #print(nuova)
    #èer ogni chiave in diz
    for chiave in diz:
        #sostituisco il nome alla posizione n con la chiave del dizionario
        nuova[diz[chiave]-1] = chiave
    return nuova


print(bestmecha( {'Patlabor' : 2, 'Evangelion' : 1} ))
assert bestmecha( {'Macross' : 1} ) == ['Macross']
assert bestmecha( {'Patlabor' : 2,
'Evangelion' : 1} ) == ['Evangelion','Patlabor']
assert bestmecha( {'Gundam' : 3,
'Evangelion': 2,
'Patlabor' : 4,
'Macross' : 1} ) == ['Macross', 'Evangelion', 'Gundam', 'Patlabor']

print()

def numnum(n):
    if n > 20:
        return n
    else:
        return n * n
    
x = numnum(3)
print(x)

y = numnum(10)
print(y)

z = numnum(33)
print(z)

print()

#importante
def nobulli(stringa):
    #divido la stringa in una lista di stringhe
    stringa_divisa = stringa.split()
    #variabile con in char da mantenere
    ok = 'waka'
    #lista nuova per metterci le parole giuste
    nuova = []
    #pr ogni parola nella lista
    for parola in stringa_divisa:
        nuova2 = [] #lista per contenere le parole formate parzialmantre
        for char in parola: # per ogni char in parola
            if char in ok: # se il char sta in ok
                nuova2.append(char) # aggiungi il carattere nalla lista parziali
        nuova.append(''.join(nuova2)) # per ogni parola parziale divisa da spazi
        # la metto in una lista togliendo gli spazi, così otterò sempre una stringa
    return ' '.join(nuova) # ora ritorno la stringa formata dalle parole divise da spazi

bullo1 = "waekai waekai waekai waekai"
res1 = nobulli(bullo1)
print(res1)

def nobulli2(stringa, ok):
    #divido la stringa in una lista di stringhe
    stringa_divisa = stringa.split()
    #variabile con in char da mantenere
    #lista nuova per metterci le parole giuste
    nuova = []
    #pr ogni parola nella lista
    for parola in stringa_divisa:
        nuova2 = [] #lista per contenere le parole formate parzialmantre
        for char in parola: # per ogni char in parola
            if char in ok: # se il char sta in ok
                nuova2.append(char) # aggiungi il carattere nalla lista parziali
        nuova.append(''.join(nuova2)) # per ogni parola parziale divisa da spazi
        # la metto in una lista togliendo gli spazi, così otterò sempre una stringa
    return ' '.join(nuova) # ora ritorno la stringa formata dalle parole divise da spazi

bullo1 = "waekai waekai waekai waekai"
res1 = nobulli2(bullo1, 'waka')
print(res1)
bullo1 = "waekai waekai waekai waekai"
bullo2 = "bwaka rwaka swaka twaka zwaka mmmwatka"
bullo3 = "eweaekea zwxarkma qwoagkpa"
res1 = nobulli(bullo1) # Deve RITORNARE il verso pulito "waka waka waka waka"
print(res1)
res2 = nobulli(bullo2) # Deve RITORNARE il verso pulito "waka waka waka waka waka␣waka"
print(res2)
res3 = nobulli(bullo3) # Deve RITORNARE il verso pulito "waka waka waka"
print(res3)
print()

def mangia(scatola):
    for i in range(len(scatola)):
        if scatola[i] % 2 == 1:
            scatola[i] = scatola[i]-1

scatola = [2, 5, 3, 8, 6, 24, 5, 3, 9]
mangia(scatola)
print(scatola)
scatola1 = [3, 3, 3, 3, 3]
scatola2 = [1, 3, 5, 7, 9]
scatola3 = [19, 3, 14, 1, 10, 9, 2, 16, 8, 7, 13, 11, 18, 17, 6, 5, 4, 12, 20, 15]
mangia(scatola1) # deve MODIFICARE scatola1
mangia(scatola2)
mangia(scatola3)
print(scatola1) # Deve stampare la lista [2, 2, 2, 2, 2]
print(scatola2) # Deve stampare la lista [0, 2, 4, 6, 8]
print(scatola3) # Deve stampare la lista [18, 2, 14, 0, 10, 8, 2, 16, 8, 6, 12, 10,␣18, 16, 6, 4, 4, 12, 20, 14]
print(mangia([2,4,5,7])) # stampa none perchè non ritorna nulla
print()
#importante
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

import random
import string
# FUNZIONE GIA' COMPLETA, NON TOCCARE !
def raggi_cosmici(flusso_dati):
    for x in range(random.randint(1,min(3,len(flusso_dati)))):
        i = random.randint(0,len(flusso_dati)-1)
#print('i',i)
        lista = list(flusso_dati[i])
        for c in range(random.randint(1,3)):
#print('lista',lista)
            lista[random.randint(0,len(lista)-1)] = random.choice('0123456789$/()')
#print('flusso_dati[i]=',flusso_dati[i])
#print('modifico',flusso_dati[i])
            flusso_dati[i] = ''.join(lista)


random.seed(7)
#random.seed(6) # scommenta
#random.seed(9) # scommenta
calendario = [
'07/11/2020',
'30/04/2020',
'02/10/2022',
'08/11/2023',
'25/01/2021',
'29/05/2023',
]
raggi_cosmici(calendario)

m = [
        ['a','b'],
        ['c', 'd'],
        ['a','è']
]

print(m[0])
print(m[1])
print(m[2])
print(m[0][0])
print(m[0][1])

print('righe')
print(len(m))
print('colonne')
print(len(m[0]))
print(m[1][1])

def esrigap(mat, i):
    return mat[i]

print(esrigap(m, 2))

def esriga_sbagliata(mat, i):
    riga = []
    riga.append(mat[i])
    return riga
m = [ ['a','b'],
['c','d'],
['a','e'] ]
riga = esriga_sbagliata(m,0)
print(riga)

def esrigaf2(mat, riga):
    nuova = []
    for i in range(len(mat)):
        if mat[i] == mat[riga]:
            for i in mat[i]:
                nuova.append(i)

    return nuova

def esrigaf(mat, riga):
    nuova = []
    for riga in mat[riga]:
        nuova.append(riga)
    return nuova

m = [
        ['a','b'],
        ['c', 'd'],
        ['a','e']
]

print(esrigaf(m,2))
assert esrigaf(m, 0) == ['a','b']
assert esrigaf(m, 1) == ['c','d']
assert esrigaf(m, 2) == ['a','e']
# controlla che non abbia cambiato la matrice originale!
r = esrigaf(m, 0)
r[0] = 'z'
assert m[0][0] == 'a'
print()

print(list(range(0,5)))

def esrigar(mat, i):
    nuova = []
    # per la lunghezza della prima lista
    for j in range(len(mat[0])):
        # prendi la lista alla posizione i e aggiumgi a nuova il primo e secondo elemento
        nuova.append(mat[i][j])
    return nuova

m = [['a','b'],
     ['c', 'd'],
     ['a','e'],
     ['f', 'p']]

print(esrigar(m,2))

print()

def esrigar2(mat, i):
    nuova = []
    for elemento in range(len(mat[0])):
        nuova.append(mat[i][elemento])
    return nuova

m = [['a','b'],
     ['c', 'd'],
     ['a','e'],
     ['f', 'p']]

print(esrigar2(m,2))
assert esrigar(m, 0) == ['a','b']
assert esrigar(m, 1) == ['c','d']
assert esrigar(m, 2) == ['a','e']
# controlla che non abbia cambiato la matrice originale!
r = esrigar(m, 0)
r[0] = 'z'
assert m[0][0] == 'a'

print()

def esrigas(mat, i):
    return mat[i][:]

m = [['a','b'],
     ['c', 'd'],
     ['a','e'],
     ['f', 'p']]

print(esrigas(m,2))
print()

assert esrigas(m, 0) == ['a','b']
assert esrigas(m, 1) == ['c','d']
assert esrigas(m, 2) == ['a','e']
# Controlla che non abbia cambiato la matrice originale !
r = esrigas(m, 0)
r[0] = 'z'
assert m[0][0] == 'a'

def esrigac(mat, i):
    return [x for x in mat[i]]

m = [['a','b'],
     ['c', 'd'],
     ['a','e'],
     ['f', 'p']]

print(esrigac(m,2))
print()

def escolf(mat, c):
    nuova = []
    for lista in mat:
        nuova.append(lista[c])
    return nuova

m = [['a','b'],
     ['c', 'd'],
     ['a','e']]

print(escolf(m,1))
assert escolf(m, 0) == ['a','c','a']
assert escolf(m, 1) == ['b','d','e']
# Controlla che la colonna ritornata non modifichi m
c = escolf(m,0)
c[0] = 'z'
assert m[0][0] == 'a'

print()

def escolc(mat, i):
    return [x[i] for x in mat]

print(escolc(m,1))

print()

def matrice_vuota(n, m):
    nuova = []
    for x in range(n):
        nuova2 = []
        for y in range(m):
            nuova2.append(0)
        nuova.append(nuova2)
    return nuova

print(matrice_vuota(3,5))

assert matrice_vuota(1,1) == [ [0] ]
assert matrice_vuota(1,2) == [ [0,0] ]
assert matrice_vuota(2,1) == [ [0],
                                [0] ]
assert matrice_vuota(2,2) == [ [0,0],
                                [0,0] ]
assert matrice_vuota(3,3) == [ [0,0,0],
                                [0,0,0],
                                [0,0,0] ]

print([0]*3)
print([[0]*3 for i in range(5)])


def matrice(righe,colonne):
    return [[5]*righe for i in range(colonne)]

print(matrice(4,7))

def deep_clone_sbagliato(mat):
    return mat[:]

m = [ ['a','b'],
      ['b','d'] ]
res = deep_clone_sbagliato(m)
print(res)
print()
res[0][0] = 'z'
print(m[0][0])
print(res)
print()

def deep_clone(mat):
    ret = []
    for riga in mat:
        ret.append(riga[:])
    return ret

m = [ ['a','b'],
['b','d'] ]
res = [ ['a','b'],
['b','d'] ]
# verifica la copia
c = deep_clone(m)
print(c)
assert c == res
# verifica che una copia in profondità (cioè, ha anche creato cloni delle righe !)
c[0][0] = 'z'
assert m[0][0] == 'a'
print()

def riempic(mat,c):
    nrighe = len(mat)
    ncolonne = len(mat[0])

    for i in range(len(mat)):
        for x in range(len(mat[0])):
            mat[i][x] = c


matri = [[1,2,3],[4,5,6],[7,8,9]]

riempic(matri, 'c')
print(matri)
m1 = [ ['a'] ]
m2 = [ ['z'] ]
riempic(m1,'z')
assert m1 == m2
m3 = [ ['a'] ]
m4 = [ ['y'] ]
riempic(m3,'y')
assert m3 == m4
m5 = [ ['a','b'] ]
m6 = [ ['z','z'] ]
riempic(m5,'z')
assert m5 == m6
m7 = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
m8 = [ ['y','y','y'],
      ['y','y','y'],
['y','y','y'] ]
riempic(m7,'y')
assert m7 == m8
# j 0 1
m9 = [ ['a','b'], # 0
['c','d'], # 1
['e','f'] ] # 2
m10 = [ ['x','x'], # 0
['x','x'], # 1
['x','x'] ] # 2
riempic(m9, 'x')
assert m9 == m10

def riempix2(mat, indcol):
    for riga in range(len(mat)):
        for colonna in range(len(mat[0])):
            if colonna == indcol:
                mat[riga][colonna] = 'x'

m = [
['a','b','c','d'],
['e','f','g','h'],
['i','l','m','n']
]
print(m)
riempix2(m,2)
print(m)
print()

def riempix(mat, j):
    for riga in mat:
        riga[j] = 'x'

m = [
['a','b','c','d'],
['e','f','g','h'],
['i','l','m','n']
]
print(m)
riempix(m,2)
print(m)

m1 = [ ['a'] ]
riempix(m1,0)
assert m1 == [ ['x'] ]
m2 = [ ['a','b'],
['c','d'],
['e','f'] ]
riempix(m2,0)
assert m2 == [ ['x','b'],
['x','d'],
['x','f'] ]
m3 = [ ['a','b'],
['c','d'],
['e','f'] ]
riempix(m3,1)
assert m3 == [ ['a','x'],
['c','x'],
['e','x'] ]

m4 = [ ['a','b','c','d'],
['e','f','g','h'],
['i','l','m','n'] ]
riempix(m4,2)
assert m4 == [ ['a','b','x','d'],
['e','f','x','h'],
['i','l','x','n'] ]

print()

def riempiz(mat, indice):
    for x in range(len(mat[0])):
        mat[indice][x] = 'z'

m = [
['a','b'],
['c','d'],
['e','f'],
['g','h']
]

print(m)
riempiz(m,2)
print(m)

m = [
['a','b'],
['c','d'],
['a','e']
]

print(m[0])
print(m[1])
print(m[2])

print(m[0][0])
print(m[0][1])
print()

print('righe')
print(len(m))

print('colonne')
print(len(m[0]))
print()

def esrigap(mat, i):
    return mat[i]

m = [
['a','b'],
['c','d'],
['a','e']
]
riga = esrigap(m, 0)
print(riga)

def esriga_sbagliata(mat, i):
    riga = []
    riga.append(mat[i])
    return riga

m = [ ['a','b'],
['c','d'],
['a','e'] ]
riga = esriga_sbagliata(m,0)
print(riga)
print()

def esrigaf(mat, i):
    nuova = []
    for x in mat[i]:
        nuova.append(x)
    return nuova

m = [ ['a','b'],
['c','d'],
['a','e'] ]
riga = esrigaf(m,0)
print(riga)
assert esrigaf(m, 0) == ['a','b']
assert esrigaf(m, 1) == ['c','d']
assert esrigaf(m, 2) == ['a','e']
# controlla che non abbia cambiato la matrice originale!
r = esrigaf(m, 0)
r[0] = 'z'
assert m[0][0] == 'a'
print()

print(range(0,5))
print(list(range(0,5)))

def esrigar(mat, i):
    nuova = []
    # per gli elementi contenuti nella lista
    for x in range(len(mat[i])):
        #prendi l'elemento nella lista i alla posizione x e aggiungilo anuova
        nuova.append(mat[i][x])
    return nuova

m = [ ['a','b'],
['c','d'],
['a','e'] ]
riga = esrigar(m,0)
print(riga)
assert esrigar(m, 0) == ['a','b']
assert esrigar(m, 1) == ['c','d']
assert esrigar(m, 2) == ['a','e']
# controlla che non abbia cambiato la matrice originale!
r = esrigar(m, 0)
r[0] = 'z'
assert m[0][0] == 'a'
print()

def esrigas(mat, i):
    return mat[i][:]

m = [
['a','b'],
['c','d'],
['a','e'],
]
print(esrigas(m,1))
assert esrigas(m, 0) == ['a','b']
assert esrigas(m, 1) == ['c','d']
assert esrigas(m, 2) == ['a','e']
# Controlla che non abbia cambiato la matrice originale !
r = esrigas(m, 0)
r[0] = 'z'
assert m[0][0] == 'a'
print()

def esrigac(mat, i):
    return [x for x in mat[i]]

m = [
['a','b'],
['c','d'],
['a','e'],
]
print(esrigac(m,1))
assert esrigac(m, 0) == ['a','b']
assert esrigac(m, 1) == ['c','d']
assert esrigac(m, 2) == ['a','e']
# Controlla che non abbia cambiato la matrice originale !
r = esrigac(m, 0)
r[0] = 'z'
assert m[0][0] == 'a'
print()

def escolf(mat, j):
    nuova = []
    for x in mat:
        nuova.append(x[j])
    return nuova

m = [
['a','b'],
['c','d'],
['a','e'],
]
print(escolf(m,1))
m = [
['a','b'],
['c','d'],
['a','e'],
]
assert escolf(m, 0) == ['a','c','a']
assert escolf(m, 1) == ['b','d','e']
# Controlla che la colonna ritornata non modifichi m
c = escolf(m,0)
c[0] = 'z'
assert m[0][0] == 'a'
print()

def escolc(mat, j):
    return [x[j] for x in mat]

m = [
['a','b'],
['c','d'],
['a','e'],
]
print(escolc(m,1))
assert escolc(m, 0) == ['a','c','a']
assert escolc(m, 1) == ['b','d','e']
# Controlla che la colonna ritornata non modifichi m
c = escolc(m,0)
c[0] = 'z'
assert m[0][0] == 'a'
print()

def matrice_vuota(n,m):
    nuova = []
    for x in range(n):
        nuova2 = []
        nuova.append(nuova2)
        for y in range(m):
            nuova2.append(0)
    return nuova

print(matrice_vuota(3,5))
assert matrice_vuota(1,1) == [ [0] ]
assert matrice_vuota(1,2) == [ [0,0] ]
assert matrice_vuota(2,1) == [ [0],
[0] ]
assert matrice_vuota(2,2) == [ [0,0],
[0,0] ]
assert matrice_vuota(3,3) == [ [0,0,0],
[0,0,0],
[0,0,0] ]
print()

print([0]*3)
print([[0]*3]*5) #sbagliatoo
print([[0]*3 for x in range(5)]) #giustoo
print([[5]*4 for x in range(7)])
print()
[print(x) for x in [[5]*4 for x in range(7)]]
print()

def deep_clone_sbagliato(mat):
    return mat[:]

m = [ ['a','b'],
['b','d'] ]
res = deep_clone_sbagliato(m)
print(res)
print()

def deep_clone(mat):
    nuova = []
    for x in mat:
        nuova.append(x)
    return nuova

m = [ ['a','b'],
['b','d'] ]
res = deep_clone(m)
print(res)

c = deep_clone(m)
assert c == res

print()
def riempic(mat, char):
    nrighe = len(mat)
    ncolonne = len(mat[0])

    for x in range(len(mat)):
        for y in range(len(mat[0])):
            mat[x][y] = char

m = [ ['a','b'],
      ['b','d'] ]
print(m)
riempic(m, 'c')
print(m)

m1 = [ ['a'] ]
m2 = [ ['z'] ]
riempic(m1,'z')
assert m1 == m2
m3 = [ ['a'] ]
m4 = [ ['y'] ]
riempic(m3,'y')
assert m3 == m4
m5 = [ ['a','b'] ]
m6 = [ ['z','z'] ]
riempic(m5,'z')
assert m5 == m6
m7 = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
m8 = [ ['y','y','y'],
['y','y','y'],
['y','y','y'] ]
riempic(m7,'y')
assert m7 == m8
# j 0 1
m9 = [ ['a','b'], # 0
['c','d'], # 1
['e','f'] ] # 2
m10 = [ ['x','x'], # 0
['x','x'], # 1
['x','x'] ] # 2
riempic(m9, 'x')
assert m9 == m10

print()

def riempix(mat, j):
    for x in mat:
        x[j] = 'x'

m = [
['a','b','c','d'],
['e','f','g','h'],
['i','l','m','n']
]
print(m)     
riempix(m,2)
print(m)
m1 = [ ['a'] ]
riempix(m1,0)
assert m1 == [ ['x'] ]
m2 = [ ['a','b'],
['c','d'],
['e','f'] ]
riempix(m2,0)
assert m2 == [ ['x','b'],
['x','d'],
['x','f'] ]
m3 = [ ['a','b'],
['c','d'],
['e','f'] ]
riempix(m3,1)
assert m3 == [ ['a','x'],
['c','x'],
['e','x'] ]
m4 = [ ['a','b','c','d'],
['e','f','g','h'],
['i','l','m','n'] ]
riempix(m4,2)
assert m4 == [ ['a','b','x','d'],
['e','f','x','h'],
['i','l','x','n'] ]

print()
def riempiz(mat, i):
    for x in range(len(mat[i])):
        mat[i][x] = 'z'
        
        
m = [
['a','b'],
['c','d'],
['e','f'],
['g','h']
]
print(m)
riempiz(m,2)
print(m)
m1 = [ ['a'] ]
riempiz(m1,0)
assert m1 == [ ['z'] ]
m2 = [ ['a','b'],
['c','d'],
['e','f'] ]
riempiz(m2,0)
assert m2 == [ ['z','z'],
['c','d'],
['e','f'] ]
m3 = [ ['a','b'],
['c','d'],
['e','f'] ]
riempiz(m3,1)
assert m3 == [ ['a','b'],
['z','z'],
['e','f'] ]
m4 = [ ['a','b'],
['c','d'],
['e','f'] ]
riempiz(m4,2)
assert m4 == [ ['a','b'],
['c','d'],  
['z','z']]
print()

def attacca_sotto2(mat1, mat2):
    righe_mat1 = len(mat1)
    righe_mat2 = len(mat2)
    colonne_mat1 = len(mat1[0])
    nuova = [[0]*(colonne_mat1) for x in range(righe_mat1+righe_mat2)]
    unite = mat1 + mat2
    for x in range(len(unite)):
        for y in range(len(unite[0])):
            nuova[x][y] = unite[x][y]
    return nuova

m2 = [ ['a','b'],
['c','d'],
['e','f'] ]

m3 = [ ['a','b'],
['c','d'],
['e','f'] ]

print(attacca_sotto2(m2,m3))
print()

def attacca_sotto(mat1,mat2):
    res = []
    for riga in mat1:
        res.append(riga[:])
    for riga in mat2:
        res.append(riga[:])
    return res

m11 = [ ['a'] ]
m12 = [ ['b'] ]
assert attacca_sotto(m11, m12) == [ ['a'],
['b'] ]
# controlla che non stiamo dando indietro un deep clone
r = attacca_sotto(m11, m12)
r[0][0] = 'z'
assert m11[0][0] == 'a'
m21 = [ ['a','b','c'],
['d','b','a'] ]
m22 = [ ['f','b', 'h'],
['g','h', 'w'] ]
assert attacca_sotto(m21, m22) == [ ['a','b','c'],
['d','b','a'],
['f','b','h'],
['g','h','w'] ]
print()

def attacca_sopra(m1,m2):
    nuova = attacca_sotto(m2,m1)
    return nuova

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b', 'h'],
['g','h', 'w'] ]

print(attacca_sopra(m1,m1))
m1 = [ ['a'] ]
m2 = [ ['b'] ]
assert attacca_sopra(m1, m2) == [ ['b'],
['a'] ]
# controlla che stiamo ritornando un deep clone
s = attacca_sopra(m1, m2)
s[0][0] = 'z'
assert m1[0][0] == 'a'
m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b', 'h'],
['g','h', 'w'] ]
assert attacca_sopra(m1, m2) == [ ['f','b','h'],
['g','h','w'],
['a','b','c'],
['d','b','a'] ]

def attacca_dx(mat1, mat2):
    nuova = []
    for i in range(len(mat1)):
        riga_da_aggiungere = mat1[i][:]
        riga_da_aggiungere.extend(mat2[i])
        nuova.append(riga_da_aggiungere)
    return nuova

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b', 'h'],
['g','h', 'w'] ]

print(attacca_dx(m1,m1))
m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
assert attacca_dx(m1, m2) == [ ['a','b','c','f','b'],
['d','b','a','g','h'] ]

print()

def insercol(mat, j, nuova_col):
    for x in range(len(mat)):
        mat[x].insert(j, nuova_col[x])

m = [
[5,4,6],
[4,7,1],
[3,2,6],]
print(m)
insercol(m, 2, [7,9,3])
print(m)
m1 = [
[5]
]
assert insercol(m1,1,[8]) == None # la funzione non ritorna nulla !
assert m1 == [ [5,8] ]
m2 = [ [5] ]
insercol(m2,0,[8])
assert m2 == [ [8,5] ]
m3 = [ [5,4,2],
[8,9,3] ]
insercol(m3,1,[7,6])
assert m3 == [ [5,7,4,2],
[8,6,9,3] ]
m4 = [ [5,4,6],
[4,7,1],
[3,2,6] ]
insercol(m4, 2, [7,9,3])
assert m4 == [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]

print()

def remcol2(mat, j):
    if j > 0 and j < len(mat[0]):
        nuova = []
        for x in mat:
            nuova.append(x[j])
            x.remove(x[j])
        return nuova
    else:
        raise ValueError

def remcol(mat, j):
    if j < 0 or j >= len(mat[0]):
        raise ValueError('j fuori dalla matrice: %s' % j)
    nuova = []
    for x in mat:
        nuova.append(x.pop(j))
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(m)
print(remcol(m,2))
print(m)

m1 = [ [5, 8] ]
assert remcol(m1,0) == [5]
assert m1 == [ [8] ]
m2 = [ [5, 8] ]
assert remcol(m2,1) == [8]
assert m2 == [ [5] ]
m3 = [ [7,2],
[9,4],
[6,1] ]
assert remcol(m3,0) == [7,9,6]
assert m3 == [ [2],
[4],
[1]]
m4 = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
assert remcol(m4,2) == [7,9,3]
assert m4 == [ [5,4,6],
[4,7,1],
[3,2,6] ]
m5 = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
assert remcol(m5,3) == [6,1,6]
assert m5 == [ [5,4,7],
[4,7,9],
[3,2,3] ]
m6 = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
try:
    remcol(m6, -3)
except ValueError:
    pass
try:
    remcol(m6, 4)
except ValueError:
    pass

def soglia2(mat, numero):
    nuova = []
    for riga in mat:
        nuova.append(riga[:])
    for x in range(len(nuova)):
        for y in range(len(nuova[0])):
            nuova[x][y] = nuova[x][y] > numero
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(soglia2(m, 1))
morig = [ [1,4,2],
[7,9,3] ]
m = [ [1,4,2],
[7,9,3] ]
s = [ [False,False,False],
[True, True, False] ]
assert soglia2(m,4) == s
assert m == morig
m = [ [5,2],
[3,7] ]
s = [
[True,False],
[False,True]
]
assert soglia2(m,4) == s

def soglia(mat, t):
    ret = []
    for riga in mat:
        nuova_riga = []
        ret.append(nuova_riga)
        for el in riga:
            nuova_riga.append(el > t)
    return ret

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(soglia(m, 1))
morig = [ [1,4,2],
[7,9,3] ]
m = [ [1,4,2],
[7,9,3] ]
s = [ [False,False,False],
[True, True, False] ]
assert soglia(m,4) == s
assert m == morig
m = [ [5,2],
[3,7] ]
s = [
[True,False],
[False,True]
]
assert soglia(m,4) == s
print()

x = 3
y = 7
print(x,y)
k = x
x = y
y = k

print(x,y)

def scambia_righe(mat, i1, i2):
    nuova = []
    for riga in mat:
        nuova.append(riga[:])
    buf = nuova[i1]
    nuova[i1] = nuova[i2]
    nuova[i2] = buf
    return nuova

m = [ ['a','d'],
['b','e'],
['c','f'] ]
riga1 = 0
riga2 = 2
print(m)
print(scambia_righe(m, riga1, riga2))
print(m)
m = [ ['a','d'],
['b','e'],
['c','f'] ]
res = scambia_righe(m, 0, 2)
assert res == [ ['c','f'],
['b','e'],
['a','d'] ]
res[0][0] = 'z'
assert m[0][0] == 'a'
m = [ ['a','d'],
['b','e'],
['c','f'] ]
res = scambia_righe(m, 0, 0)
assert res == [ ['a','d'],
['b','e'],
['c','f'] ]
res[0][0] = 'z'
assert m[0][0] == 'a'
print()

def scambia_colonne2(mat, j1, j2):
    ret = []
    for riga in mat:
        nuova_riga = riga[:] #['a', 'b', 'c']
        nuova_riga[j1] = riga[j2] #['a'] = ['c']
        nuova_riga[j2] = riga[j1] #['c'] = ['a']
        ret.append(nuova_riga) #['c', 'b', 'a']
    return ret

m = [ ['a','b','c'],
['d','e','f'] ]
res = scambia_colonne2(m, 0,2)
assert res == [ ['c','b','a'],
['f','e','d'] ]
res[0][0] = 'z'
assert m[0][0] == 'a'

def scambia_colonne(mat, j1, j2):
    nuova = []
    for riga in mat:
        nuova_riga = riga[:]
        nuova_riga[j1] = riga[j2]
        nuova_riga[j2] = riga[j1]
        nuova.append(nuova_riga)
    return nuova

m = [ ['a','b','c'],
['d','e','f'] ]
res = scambia_colonne(m, 0,2)
assert res == [ ['c','b','a'],
['f','e','d'] ]
res[0][0] = 'z'
assert m[0][0] == 'a'
print()

def diag(mat):
    if len(mat) == len(mat[0]):
        for i in range(len(mat)):
            print(mat[i][i])
        #for x,y in enumerate(range(len(mat))):
         #  print(mat[x][y])
    else:
        raise ValueError('nxn sbagliato')

m = [   ['a','b','c'],
        ['d','e','f'],
        ['c','b','z'],]
diag(m)

def diag2(mat):
    if len(mat) != len(mat[0]):
        raise ValueError("mat dovrebbe essere nxn, trovato invece %s x %s" % (len(mat), len(mat[0])))
    ret = []
    for i in range(len(mat)):
        ret.append(mat[i][i])
    return ret


def ritorna_diag(mat):
    if len(mat) == len(mat[0]):
        return [mat[x][x] for x in range(len(mat))]
    else:
        raise ValueError('nxn sbagliato')

m = [   ['a','b','c'],
        ['d','e','f'],
        ['c','b','z'],]

print(ritorna_diag(m))

m = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
assert ritorna_diag(m) == ['a','e','i']

try:
    ritorna_diag([ # 1x2 dimension, non quadrata
        ['a','b']
        ])
    raise Exception("Dovrei aver fallito !") # se diag solleva un'eccezione che
# è ValueError come ci aspettiamo
# che faccia, il codice non dovrebbe
# mai arrivare qui
except ValueError: # cattura solo ValueError, altri tipi di errori
# non sono catturati
    pass # In una clausola except devi sempre mettere del codice
# Qui mettiamo il comando pass che non fa niente
print()

def anti_diag(mat):
    if len(mat) == len(mat[0]):
        return [mat[::-1][i][i] for i in range(len(mat))][::-1]
    else:
        raise ValueError('nxn sbagliato')

m = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
print(anti_diag(m))

def anti_diag2(mat):
    n = len(mat)
    ret = []
    for i in range(n):
        ret.append(mat[i][-1-i])
        #ret.append(mat[i][n-1-i]) # versione alternativa
    return ret

m = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
print(anti_diag2(m))
m = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
assert anti_diag(m) == ['c','e','g']
print()

def is_utriang(mat):
    for x in range(1,len(mat)):
        for y in range(x):
            if mat[x][y] != 0:
                return False
    return True

assert is_utriang([ [1] ]) == True
assert is_utriang([ [3,2,5],
                    [0,6,2],
                    [0,0,4] ]) == True

assert is_utriang([ [3,2,5],
[0,6,2],
[1,0,4] ]) == False
assert is_utriang([ [3,2,5],
[0,6,2],
[1,1,4] ]) == False
assert is_utriang([ [3,2,5],
[0,6,2],
[0,1,4] ]) == False
assert is_utriang([ [3,2,5],
[1,6,2],
[1,0,4] ]) == False

def is_utriang2(mat):
    for x in range(len(mat)):
        for y in range(x):
            if mat[x][y] != 0:
                return False
    return True

assert is_utriang2([ [1] ]) == True
assert is_utriang2([ [3,2,5],
                    [0,6,2],
                    [0,0,4] ]) == True

assert is_utriang2([ [3,2,5],
[0,6,2],
[1,0,4] ]) == False
assert is_utriang2([ [3,2,5],
[0,6,2],
[1,1,4] ]) == False
assert is_utriang2([ [3,2,5],
[0,6,2],
[0,1,4] ]) == False
assert is_utriang2([ [3,2,5],
[1,6,2],
[1,0,4] ]) == False

def attacca_sx_mod(mat1, mat2):
    for x in range(len(mat1)):
        mat1[x][0:0] = mat2[x]

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
res = [ ['f','b','a','b','c'],
['g','h','d','b','a'] ]
print(m1, '\n', m2)
attacca_sx_mod(m1, m2)
print(res)
assert m1 == res

def attacca_sx_mod2(mat1, mat2):
    for x in range(len(mat1)):
        mat1[x][0:0] = mat2[x]

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
res = [ ['f','b','a','b','c'],
['g','h','d','b','a'] ]
print(m1, '\n', m2)
attacca_sx_mod2(m1, m2)
print(res)
assert m1 == res  

def is_ung(mat):
    for x in range(len(mat)):
        for y in range(x):
            if mat[y] != 0:
                return False
    return True

assert is_ung([ [3,2,5],
[0,6,2],
[1,0,4] ]) == False
assert is_ung([ [3,2,5],
[0,6,2],
[1,1,4] ]) == False
assert is_ung([ [3,2,5],
[0,6,2],
[0,1,4] ]) == False
assert is_ung([ [3,2,5],
[1,6,2],
[1,0,4] ]) == False
print()

def trasposta_1(mat):
    if len(mat) != len(mat[0]):
        raise ValueError('nxn sbagliata')
    for x in range(len(mat)):
        for y in range(x, len(mat[x])):
            el = mat[x][y]
            mat[x][y] = mat[y][x]
            mat[y][x] = el

try:
    trasposta_1([ [3,5] ])
    raise Exception("AVREI DOVUTO FALLIRE !")
except ValueError:
    pass

m1 = [ ['a'] ]
trasposta_1(m1)
assert m1 == [ ['a'] ]
m2 = [ ['a','b'],
['c','d'] ]
trasposta_1(m2)
assert m2 == [ ['a','c'],
['b','d'] ]
m3 = ([  [3,2,5],
        [1,6,2],
        [1,0,4] ])

([print(x) for x in m3])
trasposta_1(m3)
print()
[print(x) for x in m3]
print()
#importante
def trasposta_2(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    for x in range(len(mat)):
        for y in range(x, len(mat[0])):
            el = mat[x][y]
            mat[x][y] = mat[y][x]
            mat[y][x] = el
m3 = ([  [3,2,5],
        [1,6,2],
        [1,0,4] ])

([print(x) for x in m3])
trasposta_2(m3)
print()
[print(x) for x in m3]
print()

def transposta_2(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    nuova = []
    for riga in mat:
        nuova.append(riga[:])

    for x in range(len(nuova)):
        for y in range(x, len(nuova[0])):
            el = nuova[x][y]
            nuova[x][y] = nuova[y][x]
            nuova[y][x] = el
    return nuova

m3 = ([  [3,2,5],
        [1,6,2],
        [1,0,4] ])

([print(x) for x in m3])
print()
[print(x) for x in transposta_2(m3)]
print()
[print(x) for x in m3]
print()

def transporta_3(mat):
    ret = [[0]*len(mat) for x in range(len(mat[0]))]
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            ret[y][x] = mat[x][y]
    return ret

m3 = ([  [3,2,5],
        [1,6,2],
        [1,0,4] ])

m1 = [ ['a'] ]
r1 = transporta_3(m1)
assert r1 == [ ['a'] ]
r1[0][0] = 'z'
assert m1[0][0] == 'a'
m2 = [ ['a','b','c'],
['d','e','f'] ]
assert transporta_3(m2) == [ ['a','d'],
['b','e'],
['c','f'] ]


([print(x) for x in m3])
print()
[print(x) for x in transporta_3(m3)]
print()
[print(x) for x in m3]
print()

def trasposta_2(mat):
    ret = [[0]*len(mat) for x in range(len(mat[0]))]
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            ret[y][x] = mat[x][y]
    return ret

m1 = [ ['a'] ]
r1 = trasposta_2(m1)
assert r1 == [ ['a'] ]
#r1[0][0] = 'z'
assert m1[0][0] == 'a'
m2 = [ ['a','b','c'],
['d','e','f'] ]
assert trasposta_2(m2) == [ ['a','d'],
['b','e'],
['c','f'] ]
print()

def matriverba(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x].upper())
        for y in range(1,len(mat)):
            nuova.append(mat[y][x])
    return ''.join(nuova)

m = [['p','c','z','g','b', 'd'],
    ['o','a','a','i','o', 'e'],
    ['r','l','n','a','r', 'n'],
    ['t','m','n','r','s', 't'],
    ['o','a','a','a','e', 'e']];

print(matriverba(m))

def matriverba_2(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x].upper())
        for y in range(1, len(mat)):
            nuova.append(mat[y][x])
    return ''.join(nuova)

m = [['p','c','z','g','b', 'd'],
    ['o','a','a','i','o', 'e'],
    ['r','l','n','a','r', 'n'],
    ['t','m','n','r','s', 't'],
    ['o','a','a','a','e', 'e']];

print(matriverba_2(m))

def matriverba_3(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x].upper())
        for y in range(1, len(mat)):
            nuova.append(mat[y][x])
    return ''.join(nuova)

m = [['p','c','z','g','b', 'd'],
    ['o','a','a','i','o', 'e'],
    ['r','l','n','a','r', 'n'],
    ['t','m','n','r','s', 't'],
    ['o','a','a','a','e', 'e']];

print(matriverba_3(m))

def matriverba_4(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x].upper())
        for y in range(1, len(mat)):
            nuova.append(mat[y][x])
    return ''.join(nuova)

m = [['p','c','z','g','b', 'd'],
    ['o','a','a','i','o', 'e'],
    ['r','l','n','a','r', 'n'],
    ['t','m','n','r','s', 't'],
    ['o','a','a','a','e', 'e']];

print(matriverba_4(m))

def matriverba_5(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x])
        for y in range(1, len(mat)):
            nuova.append(mat[y][x])
    return nuova

m = [['p','c','z','g','b', 'd'],
    ['o','a','a','i','o', 'e'],
    ['r','l','n','a','r', 'n'],
    ['t','m','n','r','s', 't'],
    ['o','a','a','a','e', 'e']];

print(matriverba_4(m))
m1 = [['a']]
assert matriverba(m1) == 'A'
m2 = [['a','b']]
assert matriverba(m2) == 'AB'
m3 = [['c'],
['b']]
assert matriverba(m3) == 'Cb'
m4 = [['c','e'],
['b','q']]
assert matriverba(m4) == 'CbEq'
m5 = [['p','c','z','g','b', 'd'],
['o','a','a','i','o', 'e'],
['r','l','n','a','r', 'n'],
['t','m','n','r','s', 't'],
['o','a','a','a','e', 'e']];
assert matriverba(m5) == 'PortoCalmaZannaGiaraBorseDente'
print()

def cirpillino(stringa, n):
    if len(stringa) % n != 0:
        raise ValueError
    nuova = []
    for i in range(len(stringa)//n):
        nuova.append(list(stringa[i*n:(i+1)*n]))
    return nuova
    
#[print(x) for x in cirpillino('cirpillinozimpirelloulalimpo', 4)]
print()

def cirpillini2(stringa, n):
    if len(stringa) % n != 0:
        raise ValueError
    nuova = []
    for x in range(len(stringa)//n):
        nuova.append(list(stringa[x*n:(x+1)*n]))
    print(nuova)

cirpillini2('cirpillinozimpirelloulalimpo', 4)
print()

def attacca_sotto(mat1, mat2):
    nuova = []
    for riga in mat1:
        nuova.append(riga[:])
    for riga in mat2:
        nuova.append(riga[:])
    return nuova


m3 = [ ['a','b'],
['c','d'],
['e','f'] ]

m4 = [[1,2],
      [3,4],
      [5,6]]
print(attacca_sotto(m3,m4))

def attacca_sotto2(mat1, mat2):
    nuova = []
    for riga in mat1:
        nuova.append(riga[:])
    for riga in mat2:
        nuova.append(riga[:])
    return nuova

m3 = [ ['a','b'],
['c','d'],
['e','f'] ]

m4 = [[1,2],
      [3,4],
      [5,6]]
print(attacca_sotto2(m3,m4))
print()

def attacca_sopra(mat1, mat2):
    nuova = []
    for riga in mat2:
        nuova.append(riga[:])
    for riga in mat1:
        nuova.append(riga[:])
    return nuova

m3 = [ ['a','b'],
['c','d'],
['e','f'] ]

m4 = [[1,2],
      [3,4],
      [5,6]]
print(attacca_sopra(m3,m4))
print()

def attacca_sopra2(mat1,mat2):
    return attacca_sotto(mat2,mat1)

m3 = [ ['a','b'],
['c','d'],
['e','f'] ]

m4 = [[1,2],
      [3,4],
      [5,6]]
print(attacca_sopra2(m3,m4))
print()

def attacca_dx(mat1, mat2):
    nuova = []
    for x in mat1:
        nuova.append(x[:])
    for riga in range(len(nuova)):
        for y in range(len(mat2[0])):
            nuova[riga].append(mat2[riga][y])
    return nuova

m3 = [ ['a','b'],
['c','d'],
['e','f'] ]

m4 = [[1,2],
      [3,4],
      [5,6]]
print(attacca_dx(m3,m4))

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
assert attacca_dx(m1, m2) == [ ['a','b','c','f','b'],
['d','b','a','g','h'] ]

def attacca_dx2(mat1, mat2):
    nuova = []
    for x in range(len(mat1)):
        riga_agg = mat1[x][:]
        riga_agg.extend(mat2[x])
        nuova.append(riga_agg)
    return nuova

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
assert attacca_dx2(m1, m2) == [ ['a','b','c','f','b'],
['d','b','a','g','h'] ]

def attacca_dx3(mat1, mat2):
    nuova = []
    for riga in mat1:
        nuova.append(riga[:])
    for x in range(len(mat2)):
        nuova[x].extend(mat2[x])
    return nuova

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
assert attacca_dx3(m1, m2) == [ ['a','b','c','f','b'],
['d','b','a','g','h'] ]

def attacca_dx4(mat1, mat2):
    nuova = []
    for x in range(len(mat1)):
        nuova.append(mat1[x])
        nuova[x].extend(mat2[x])
    return nuova

m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
assert attacca_dx4(m1, m2) == [ ['a','b','c','f','b'],
['d','b','a','g','h'] ]
print()

def insercol(mat, j, nuova_col):
    for x in range(len(mat)):
        mat[x].insert(j, nuova_col[x])

m = [
[5,4,6],
[4,7,1],
[3,2,6],
]
print(m)  
insercol(m, 2, [7,9,3])
print(m)
print()

def remcol(mat, j):
    if j < 0 or j > len(mat):
        raise ValueError
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x].pop(j))
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(m)
print(remcol(m,2))
print(m)
print()

def soglia(mat, t):
    nuova = [x[:] for x in mat]
    for x in range(len(nuova)):
        for y in range(len(nuova[0])):
                nuova[x][y] = nuova[x][y] > t
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(m)
print(soglia(m, 1))
print(m)
print()

def soglia2(mat, t):
    nuova = []
    for x in mat:
        nuova_riga = []
        nuova.append(nuova_riga)
        for el in x:
            nuova_riga.append(el > t)
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(m)
print(soglia2(m, 1))
print(m)
print()

def scambia_righe(mat, i1, i2):
    nuova = [x[:] for x in mat]
    buf = nuova[i1]
    nuova[i1] = nuova[i2]
    nuova[i2] = buf
    return nuova

m = [ [5,4,7,6],
[4,7,9,1],
[3,2,3,6] ]
print(m)
print(scambia_righe(m, 0, 2))
print(m)
m = [ ['a','d'],
['b','e'],
['c','f'] ]
res = scambia_righe(m, 0, 2)
assert res == [ ['c','f'],
['b','e'],
['a','d'] ]
print()


def scambia_colonne(mat, j1, j3):
    nuova = [x[:] for x in mat]
    for x in nuova:
        buff = x[j1]
        x[j1] = x[j3]
        x[j3] = buff
    return nuova

m = [   [5,4,7,6],
        [4,7,9,1],
        [3,2,3,6] ]

print(m)
print(scambia_colonne(m, 0, 1))
print(m)
m = [ ['a','b','c'],
['d','e','f'] ]
res = scambia_colonne(m, 0,2)
assert res == [ ['c','b','a'],
['f','e','d'] ]
print()

def diag(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x][x])
    return nuova

m = [   [5,4,7],
        [4,7,9],
        [3,2,3] ]

print(m)
print(diag(m))
print(m)
m = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
assert diag(m) == ['a','e','i']
print()

def anti_diag(mat):
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x][-1-x])
    return nuova

m = [   [5,4,7],
        [4,7,9],
        [3,2,3] ]

print(m)
print(anti_diag(m))
print(m)
m = [ ['a','b','c'],
['d','e','f'],
['g','h','i'] ]
assert anti_diag(m) == ['c','e','g']
print()

def is_utriang(mat):
    for x in range(1, len(mat)):
        for y in range(x):
            if mat[x][y] != 0:
                return False
    return True

m = [   [5,4,7],
        [0,7,9],
        [0,0,3] ]

print(m)
print(is_utriang(m))
print(m)
assert is_utriang([ [1] ]) == True
assert is_utriang([ [3,2,5],
[0,6,2],
[0,0,4] ]) == True
assert is_utriang([ [3,2,5],
[0,6,2],
[1,0,4] ]) == False
assert is_utriang([ [3,2,5],
[0,6,2],
[1,1,4] ]) == False
assert is_utriang([ [3,2,5],
[0,6,2],
[0,1,4] ]) == False
assert is_utriang([ [3,2,5],
[1,6,2],
[1,0,4] ]) == False
print()

def attacca_sx_mod(mat1, mat2):
    for x in range(len(mat1)):
        mat1[x][0:0] = mat2[x]

m1 = [  [5,4,7],
        [0,7,9],
        [0,0,3] ]

m2 = [  [5,4,7],
        [7,7,9],
        [5,9,3] ]

print(m1, m2)
print(attacca_sx_mod(m1, m2))
print(m1)
m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
res = [ ['f','b','a','b','c'],
['g','h','d','b','a'] ]
attacca_sx_mod(m1, m2)
assert m1 == res
print()

def trasposta_1(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    for x in range(len(mat)):
        for y in range(x+1, len(mat[x])):
            buf = mat[x][y]
            mat[x][y] = mat[y][x]
            mat[y][x] = buf

m2 = [  [5,4,7],
        [7,7,9],
        [5,9,3] ]

[print(x) for x in m2]
print(trasposta_1(m2))
[print(x) for x in m2]
print()

def trasposta_2(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    
    for x in range(len(mat)):
        for y in range(x, len(mat[0])):
            buf = mat[x][y]
            mat[x][y] = mat[y][x]
            mat[y][x] = buf

m2 = [  [5,4,7],
        [7,7,9],
        [5,9,3] ]

[print(x) for x in m2]
print(trasposta_2(m2))
[print(x) for x in m2]

m = [ ['a'] ]
trasposta_1(m)
assert m == [ ['a'] ]
m = [ ['a','b'],
['c','d'] ]
trasposta_2(m)
assert m == [ ['a','c'],
['b','d'] ]
print()

def transposta_3(mat):
    nuova = [[0]*len(mat) for x in range(len(mat[0]))]
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            nuova[y][x] = mat[x][y]
    return nuova

m2 = [  [5,4,7],
        [7,7,9],
        [5,9,3],
        [5,9,3] ]

[print(x) for x in m2]
print()
#print(transposta_3(m2))
print(transposta_3(m2))
print()
[print(x) for x in m2]
print()

def tra_1(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    for x in range(len(mat)):
        for y in range(x, len(mat[0])):
            buf = mat[x][y]
            mat[x][y] = mat[y][x]
            mat[y][x] = buf

m2 = [  [5,4,7],
        [7,7,9],
        [5,9,3] ]

[print(x) for x in m2]
print(tra_1(m2))
[print(x) for x in m2]
print()
#importante
def tra_2(mat):
    nuova = [[0]*len(mat) for x in range(len(mat[0]))]
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            nuova[y][x] = mat[x][y]
    return nuova

m2 = [  [5,4,7],
        [7,7,9],
        [5,9,3],
        [8,2,5] ]

print(tra_2(m2))
print()

def matriverba(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x].upper())
        for y in range(1, len(mat)):
            nuova.append(mat[y][x])
    return ''.join(nuova)

m = [['p','c','z','g','b', 'd'],
['o','a','a','i','o', 'e'],
['r','l','n','a','r', 'n'],
['t','m','n','r','s', 't'],
['o','a','a','a','e', 'e']];
print(matriverba(m))

def trasposta_1(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    for x in range(len(mat)):
        for y in range(x, len(mat[0])):
            buf = mat[x][y]
            mat[x][y] = mat[y][x]
            mat[y][x] = buf


m = [ ['a','b'],
      ['c','d'] ]
trasposta_1(m)
print(m)
m = [ ['a'] ]
trasposta_1(m)
assert m == [ ['a'] ]
m = [ ['a','b'],
['c','d'] ]
trasposta_1(m)
assert m == [ ['a','c'],
['b','d'] ]
m = [['p','c','z','g','b', 'd'],
    ['o','a','a','i','o', 'e'],
    ['r','l','n','a','r', 'n'],
    ['t','m','n','r','s', 't'],
    ['p','c','z','g','b', 'd'],
    ['o','a','a','a','e', 'e']]
trasposta_1(m)
[print(x) for x in m]
print()

def trasposta_2(mat):
    nuova = [[0]*len(mat) for x in range(len(mat[0]))]
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            nuova[y][x] = mat[x][y]
    return nuova

m2 = [ ['a','b','c'],
['d','e','f'] ]
print(m2)
print(trasposta_2(m2))
print()


def matriverba(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x].upper())
        for y in range(1,len(mat)):
            nuova.append(mat[y][x])
    return ''.join(nuova)
#importante
m = [   ['p','c','z','g','b', 'd'],
        ['o','a','a','i','o', 'e'],
        ['r','l','n','a','r', 'n'],
        ['t','m','n','r','s', 't'],
        ['o','a','a','a','e', 'e']]
print(matriverba(m))

def matriverba2(mat):
    nuova = []
    for x in range(len(mat[0])):
        nuova.append(mat[0][x].upper())
        for riga in mat[1:]:
            nuova.append(riga[x])
    return ''.join(nuova)

m = [   ['p','c','z','g','b', 'd'],
        ['o','a','a','i','o', 'e'],
        ['r','l','n','a','r', 'n'],
        ['t','m','n','r','s', 't'],
        ['o','a','a','a','e', 'e']]
print(matriverba2(m))
print()

def cirpillino(stringa, n):
    if len(stringa) % n != 0:
        raise ValueError
    nuova = []
    for x in range(len(stringa)//n):
        nuova.append(list(stringa)[x*n:(x+1)*n])
    return nuova

[print(x) for x in cirpillino('cirpillinozimpirelloulalimpo', 4)]

assert cirpillino('z', 1) == [['z']]
assert cirpillino('abc', 1) == [['a'],
['b'],
['c']]
assert cirpillino('abcdef', 2) == [['a','b'],
['c','d'],
['e','f']]
assert cirpillino('abcdef', 3) == [['a','b','c'],
['d','e','f']]
assert cirpillino('cirpillinozimpirelloulalimpo', 4) == [['c', 'i', 'r', 'p'],
['i', 'l', 'l', 'i'],
['n', 'o', 'z', 'i'],
['m', 'p', 'i', 'r'],
['e', 'l', 'l', 'o'],
['u', 'l', 'a', 'l'],
['i', 'm', 'p', 'o']]
try:
    cirpillino('abc', 5)
    raise Exception("Avrei dovuto fallire !")
except ValueError:
    pass
print()

def bandiera(n,m):
    if m % 3 != 0:
        raise ValueError
    nuova = []
    for x in range(n):
        riga = []
        for y in range(m):
            num = y // (m // 3)
            riga.append(num)
        nuova.append(riga)
    return nuova

[print(x) for x in bandiera(5,12)]
print()

def bandiera1(n,m):
    if m % 3 != 0:
        raise ValueError
    nuova = []
    for x in range(n):
        riga = []
        for y in range(m):
            riga.append(y // (m // 3))
        nuova.append(riga)
    return nuova

[print(x) for x in bandiera1(5,12)]

assert bandiera(1,3) == [[0, 1, 2]]
assert bandiera(1,6) == [[0,0,1,1, 2,2]]
assert bandiera(4,6) == [[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2]]
assert bandiera(2,9) == [[0, 0, 0, 1, 1, 1, 2, 2, 2],
[0, 0, 0, 1, 1, 1, 2, 2, 2]]
assert bandiera(5,12) == [[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]]
try:
    bandiera(3,7)
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass

print()

def evita_diag(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    nuova = []
    for x in range(len(mat)):
        nuova.append(sum(mat[x]) - mat[x][x])
    return nuova

print(evita_diag([ [5,6,2],
                   [4,7,9],
                   [1,9,8]]))

def evita_diag2(mat):
    if len(mat) != len(mat[0]):
        raise ValueError("Matrice non quadrata: %s x %s" % (len(mat), len(mat[0])))
    ret = []
    i = 0
    for riga in mat:
        ret.append(sum(riga) - riga[i])
        i += 1
    return ret

assert evita_diag([[5]]) == [0]
m2 = [[5,7],
[9,1]]
assert evita_diag(m2) == [7,9]
assert m2 == [[5,7],
[9,1]]
assert evita_diag([ [5,6,2],
[4,7,9],
[1,9,8]]) == [8, 13, 10]
try:
    evita_diag([[2,3,5],
    [1,5,2]])
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass

def no_diag(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    
    nuova = [x[:] for x in mat]
    for x in range(len(mat)):
        nuova[x].pop(x)
            
    return nuova

m = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
[print(x) for x in m]
print(no_diag(m))
[print(x) for x in m]

m1 = [[3,4],
[8,7]]
assert no_diag(m1) == [[4],
[8]]
assert m1 == [[3,4], # verifica che non abbia cambiato l'originale
[8,7]]
m2 = [[9,4,3],
[8,5,6],
[0,2,7]]
assert no_diag(m2) == [[4,3],
[8,6],
[0,2]]
m3 = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
assert no_diag(m3) == [[5,3,4],
[7,4,1],
[9,8,5],
[6,0,4]]
try:
    no_diag([[2,3,5],
[1,5,2]])
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass


def no_diag1(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    ret = []
    i = 0
    for riga in mat:
        nuova_riga = riga[0:i] + riga[i+1:]
        ret.append(nuova_riga)
        i += 1
    return ret

m1 = [[3,4],
[8,7]]
assert no_diag1(m1) == [[4],
[8]]
assert m1 == [[3,4], # verifica che non abbia cambiato l'originale
[8,7]]
m2 = [[9,4,3],
[8,5,6],
[0,2,7]]
assert no_diag1(m2) == [[4,3],
[8,6],
[0,2]]
m3 = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
assert no_diag1(m3) == [[5,3,4],
[7,4,1],
[9,8,5],
[6,0,4]]
try:
    no_diag1([[2,3,5],
[1,5,2]])
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass

def no_diag2(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x][:x] + mat[x][x+1:])
    return nuova

m = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
[print(x) for x in m]
print(no_diag2(m))
[print(x) for x in m]

m1 = [[3,4],
[8,7]]
assert no_diag2(m1) == [[4],
[8]]
assert m1 == [[3,4], # verifica che non abbia cambiato l'originale
[8,7]]
m2 = [[9,4,3],
[8,5,6],
[0,2,7]]
assert no_diag2(m2) == [[4,3],
[8,6],
[0,2]]
m3 = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
assert no_diag2(m3) == [[5,3,4],
[7,4,1],
[9,8,5],
[6,0,4]]
try:
    no_diag2([[2,3,5],
    [1,5,2]])
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass
print()

def bandiera2(n,m):
    if m % 3 != 0:
        raise ValueError
    nuova = [[0]*m for x in range(n)]
    for x in range(len(nuova)):
        for y in range(len(nuova[0])):
            nuova[x][y] = y // (m // 3)

    return nuova

[print(x) for x in bandiera2(5,12)]

assert bandiera2(1,3) == [[0, 1, 2]]
assert bandiera2(1,6) == [[0,0,1,1, 2,2]]
assert bandiera2(4,6) == [[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2]]
assert bandiera2(2,9) == [[0, 0, 0, 1, 1, 1, 2, 2, 2],
[0, 0, 0, 1, 1, 1, 2, 2, 2]]
assert bandiera2(5,12) == [[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]]
try:
    bandiera2(3,7)
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass


def bandiera4(n,m):
    if m % 3 != 0:
        raise ValueError
    ret = []
    for x in range(n):
        riga = []
        for y in range(m):
            num = y // ( m // 3)
            riga.append(num)
        ret.append(riga)
    return ret

assert bandiera4(1,3) == [[0, 1, 2]]
assert bandiera4(1,6) == [[0,0,1,1, 2,2]]
assert bandiera4(4,6) == [[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2]]
assert bandiera4(2,9) == [[0, 0, 0, 1, 1, 1, 2, 2, 2],
[0, 0, 0, 1, 1, 1, 2, 2, 2]]
assert bandiera4(5,12) == [[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]]
try:
    bandiera4(3,7)
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass
print()

def no_anti_diag(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    nuova = [x[:] for x in mat]
    for x in range(len(mat)):
        nuova[x].pop(-1-x)
    return nuova

m = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
[print(x) for x in m]
print()
[print(x) for x in no_anti_diag(m)]
print()
[print(x) for x in m]    

assert no_anti_diag(m1) == [[3],
[7]]
assert m1 == [[3,4], # verifica che non abbia cambiato l'originale
[8,7]]
m2 = [[9,4,3],
[8,5,6],
[0,2,7]]
assert no_anti_diag(m2) == [[9,4],
[8,6],
[2,7]]
m3 = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
assert no_anti_diag(m3) == [[8,5,3],
[7,2,1],
[9,3,5],
[0,4,7]]
try:
    no_anti_diag([[2,3,5],
[1,5,2]])
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass
print()

def no_anti_diag1(mat):
    nuova = []
    for x in range(len(mat)):
        k = len(mat) -x -1
        nuova.append(mat[x][:k] + mat[x][k+1:])
    return nuova

m = [[8,5,3,4],
[7,2,4,1],
[9,8,3,5],
[6,0,4,7]]
[print(x) for x in m]
print()
[print(x) for x in no_anti_diag1(m)]
print()
[print(x) for x in m] 
print()


def repcol(mat, lista):
    count = 0
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            mat[x][y] = lista[x]

m = [
['z','a','p','p','a'],
['c','a','r','t','a'],
['p','a','l','l','a']
]
[print(x) for x in m]
print()
repcol(m, ['E', 'H', '?'])
[print(x) for x in m]
m1 = [ ['a'] ]
v1 = ['Q']
repcol(m1,v1) # non ritorna niente!
assert m1 == [['Q']]
m2 = [
['a','b'],
['c','d'],
['e','f'],
['g','h'],
]
salvata = m2[0] # salviamo puntatore alla prima riga originale
v2 = ['P','A','L','A']
repcol(m2,v2) # non ritorna niente!
assert m2 == [['P', 'P'],
['A', 'A'],
['L', 'L'],
['A', 'A']]
assert id(salvata) == id(m2[0]) # non deve creare nuove liste
m3 = [
['z','a','p','p','a'],
['c','a','r','t','a'],
['p','a','l','l','a']
]
v3 = ['E','H','?']
repcol(m3,v3) # non ritorna niente!
assert m3 == [['E', 'E', 'E', 'E','E'],
['H', 'H', 'H', 'H','H'],
['?', '?', '?', '?','?']]
print()

def matinc(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])-1):
            if mat[x][y] >= mat[x][y+1]:
                return False
    return True

m = [[1,4,6,7,9],
[0,1,2,4,8],
[2,6,8,9,10]]
print(matinc(m))
m = [[0,1,3,4],
[4,6,9,10],
[3,7,7,15]]
print(matinc(m))
m1 = [[5]]
assert matinc(m1) == True
m2 = [[7],
[4]]
assert matinc(m2) == True
m3 = [[2,3],
[3,5]]
assert matinc(m3) == True
m4 = [[9,4]]
assert matinc(m4) == False
m5 = [[5,5]]
assert matinc(m5) == False
m6 = [[1,4,6,7,9],
[0,1,2,4,8],
[2,6,8,9,10]]
assert matinc(m6) == True
m7 = [[0,1,3,4],
[4,6,9,10],
[3,7,7,15]]
assert matinc(m7) == False
m8 = [[1,4,8,7,9],
[0,1,2,4,8]]
assert matinc(m8) == False

def matinc2(mat):
    for x in range(len(mat)):
        for y in range(1, len(mat[0])):
            if mat[x][y] <= mat[x][y-1]:
                return False
    return True
print()

def flip(mat):
    nuova = [x[:] for x in mat]
    for x in range(len(nuova)):
        for y in range(len(nuova[0])):
            if nuova[x][y] == 0:
                nuova[x][y] = 1
            else:
                nuova[x][y] = 0
        nuova[x] = nuova[x][::-1]
    return nuova

assert flip([[]]) == [[]]
assert flip([[1]]) == [[0]]
assert flip([[1,0]]) == [[1,0]]
m1 = [ [1,0,0],
[1,0,1] ]
r1 = [ [1,1,0],
[0,1,0] ]
assert flip(m1) == r1
m2 = [ [1,1,0,0],
[0,1,1,0],
[0,0,1,0] ]
r2 = [ [1,1,0,0],
[1,0,0,1],
[1,0,1,1] ]
assert flip(m2) == r2
# verifica che l'm originale non sia cambiato !
assert m2 == [ [1,1,0,0],
[0,1,1,0],
[0,0,1,0] ]
print()

def flip1(mat):
    ret = []
    for riga in mat:
        nuova_riga = []
        for elem in riga:
            nuova_riga.append(1 - elem)
        nuova_riga.reverse()
        ret.append(nuova_riga)
    return ret

m = [
[1,1,0,0],
[0,1,1,0],
[0,0,1,0]
]

[print(x) for x in m]
print()
[print(x) for x in flip(m)]
print()

def muro(lista, mat):
    nuova = []
    for x in range(len(mat)):
        for j in range(lista[x]):
            nuova.append(mat[x][:])
    return nuova

lista = [3,4,1,2]
m = [['i','a','a'],
['q','r','f'],
['y','e','v'],
['e','g','h']]
[print(x) for x in m]
print()
[print(x) for x in muro(lista, m)]
print()
[print(x) for x in m]
print()

m1 = [['a']]
assert muro([2], m1) == [['a'],
['a']]
m2 = [['a','b','c','d'],
['e','q','v','r']]
r2 = muro([3,2], m2)
assert r2 == [['a','b','c','d'],
['a','b','c','d'],
['a','b','c','d'],
['e','q','v','r'],
['e','q','v','r']]
r2[0][0] = 'z'
m3 = [['i','a','a'],
['q','r','f'],
['y','e','v'],
['e','g','h']]
r3 = muro([3,4,1,2], m3)
assert r3 == [['i', 'a', 'a'],
['i', 'a', 'a'],
['i', 'a', 'a'],
['q', 'r', 'f'],
['q', 'r', 'f'],
['q', 'r', 'f'],
['q', 'r', 'f'],
['y', 'e', 'v'],
['e', 'g', 'h'],
['e', 'g', 'h']]
assert m2 == [['a','b','c','d'], # vogliamo una NUOVA matrice
['e','q','v','r']]
print()

def muro1(ripe, mat):
    res = []
    i = 0
    for i in range(len(mat)):
        riga = mat[i]
        n = ripe[i]
        for i in range(n):
            res.append(riga[:])
    return res
print()

def ordinul(mat):
    nuova = []
    for x in range(len(mat)):
        nuova.append(mat[x].pop(-1))
    nuova.sort()
    for j in range(len(mat)):
        mat[j].append(nuova[j])
    
m = [[8,5,3,2,4],
[7,2,4,1,1],
[9,8,3,3,7],
[6,0,4,2,5]]

[print(x) for x in m]
print()
ordinul(m)
[print(x) for x in m]

m1 = [[3]]
ordinul(m1)
assert m1 == [[3]]
m2 = [[9,3,7],
[8,5,4]]
ordinul(m2)
assert m2 == [[9,3,4],
[8,5,7]]
m3 = [[8,5,9],
[7,2,3],
[9,8,7]]
ordinul(m3)
assert m3 == [[8,5,3],
[7,2,7],
[9,8,9]]
m4 = [[8,5,3,2,4],
[7,2,4,1,1],
[9,8,3,3,7],
[6,0,4,2,5]]
ordinul(m4)
assert m4 == [[8, 5, 3, 2, 1],
[7, 2, 4, 1, 4],
[9, 8, 3, 3, 5],
[6, 0, 4, 2, 7]]
assert ordinul([[3]]) == None
print()

def ordinul1(mat):
    ordinata = sorted([mat[x][-1] for x in range(len(mat))])
    for j in range(len(mat)):
        mat[j][-1] = ordinata[j]

m = [[8,5,3,2,4],
[7,2,4,1,1],
[9,8,3,3,7],
[6,0,4,2,5]]

[print(x) for x in m]
print()
ordinul(m)
[print(x) for x in m]

m1 = [[3]]
ordinul1(m1)
assert m1 == [[3]]
m2 = [[9,3,7],
[8,5,4]]
ordinul1(m2)
assert m2 == [[9,3,4],
[8,5,7]]
m3 = [[8,5,9],
[7,2,3],
[9,8,7]]
ordinul1(m3)
assert m3 == [[8,5,3],
[7,2,7],
[9,8,9]]
m4 = [[8,5,3,2,4],
[7,2,4,1,1],
[9,8,3,3,7],
[6,0,4,2,5]]
ordinul1(m4)
assert m4 == [[8, 5, 3, 2, 1],
[7, 2, 4, 1, 4],
[9, 8, 3, 3, 5],
[6, 0, 4, 2, 7]]
assert ordinul1([[3]]) == None
print()

def gratt(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] == 1:
                return len(mat) - x
    return 0

m = [[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]

print(gratt(m))
assert gratt([[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]) == 4
assert gratt([ [0, 0, 0, 0],
[0, 1, 0, 0],
[0, 1, 1, 0],
[1, 1, 1, 1] ]) == 3
assert gratt([ [0, 1, 0, 0],
[0, 1, 0, 0],
[0, 1, 1, 0],
[1, 1, 1, 1] ]) == 4
assert gratt([ [0, 0, 0, 0],
[0, 0, 0, 0],
[1, 1, 1, 0],
[1, 1, 1, 1] ]) == 2

def gratt1(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] == 1:
                return len(mat) -x
    return 0
print()

def discarica(mat, q):
    nuova = []
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if q > 0:
                scarica = min(q, 7 - mat[x][y])
                q -= scarica
                nuova.append(scarica)
            else:
                return nuova
    if q > 0:
        raise ValueError('rifiuti rimasti:', q)
    else:
        return nuova

m = [
[5,4,6],
[4,7,1],
[3,2,6],
[3,6,2],
]
print(discarica(m, 22))
m1 = [ [5] ]
assert discarica(m1,0) == [] # niente da scaricare
m2 = [ [4] ]
assert discarica(m2,2) == [2]
m3 = [ [5,4] ]
assert discarica(m3,3) == [2, 1]
m3 = [ [5,7,3] ]
assert discarica(m3,3) == [2, 0, 1]
m5 = [ [2,5], # 5 2
[4,3] ] # 3 1
assert discarica(m5,11) == [5,2,3,1]
m6 = [ [5,4,6], # 2 3 1 # tonnellate da scaricare in ciascuna cella
[4,7,1], # 3 0 6
[3,2,6], # 4 3 0
[3,6,2] ] # 0 0 0
assert discarica(m6, 22) == [2,3,1,3,0,6,4,3]
try:
    discarica ([[5]], 10)
    raise Exception("Dovrei aver fallito !")
except ValueError:
    pass
print()

def discarica2(mat, q):
    rimanente = q
    ret = []
    for riga in mat:
        for j in range(len(riga)):
            da_riempire = 7 - riga[j]
            scarica = min(da_riempire, rimanente)
            rimanente -= scarica

            if rimanente > 0:
                ret.append(scarica)
            else:
                if scarica > 0:
                    ret.append(scarica)
                return ret
    if rimanente > 0:
        raise ValueError('rifiuti rimasti', rimanente)
    
m1 = [ [5] ]
assert discarica2(m1,0) == [] # niente da scaricare
m2 = [ [4] ]
assert discarica2(m2,2) == [2]
m3 = [ [5,4] ]
assert discarica2(m3,3) == [2, 1]
m3 = [ [5,7,3] ]
assert discarica2(m3,3) == [2, 0, 1]
m5 = [ [2,5], # 5 2
[4,3] ] # 3 1
assert discarica2(m5,11) == [5,2,3,1]
m6 = [ [5,4,6], # 2 3 1 # tonnellate da scaricare in ciascuna cella
[4,7,1], # 3 0 6
[3,2,6], # 4 3 0
[3,6,2] ] # 0 0 0
assert discarica2(m6, 22) == [2,3,1,3,0,6,4,3]
try:
    discarica2([[5]], 10)
    raise Exception("Dovrei aver fallito !")
except ValueError:
    pass 

def gratt3(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] == 1:
                return len(mat) -x
    return 0
print()

def lab(lista, mat):
    if len(lista) > len(mat) * len(mat[0]):
        raise ValueError
    lista.sort()
    j = 0
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if j < len(lista):
                mat[x][y] = lista[j]
                j += 1

st = ['b', 'd', 'e', 'g', 'c', 'a', 'h', 'f' ]
mat = [
[None, None, None],
[None, None, None],
[None, None, None],
[None, None, None]
]
lab(st, mat)
print(mat)
print(st)
try:
    lab(['a','b'], [[None]])
    raise Exception("TEST FALLITO: Mi aspettavo un ValueError!")
except ValueError:
    "Test passato"
try:
    lab(['a','b','c'], [[None,None]])
    raise Exception("TEST FALLITO: Mi aspettavo un ValueError!")
except ValueError:
    "Test passato"
m0 = [ [None] ]
r0 = lab([],m0)
assert m0 == [ [None] ]
assert r0 == None # si suppone la funzione non ritorni nulla
# (perciò ritorna None di default)
m1 = [ [None] ]
r1 = lab(['a'], m1)
assert m1 == [ ['a'] ]
assert r1 == None # si suppone la funzione non ritorni nulla
# (perciò ritorna None di default)
m2 = [ [None, None] ]
lab(['a'], m2) # 1 studente 2 sedie in una fila
assert m2 == [ ['a', None] ]
m3 = [ [None],
[None] ]
lab(['a'], m3) # 1 studente 2 sedie in una colonna
assert m3 == [ ['a'],
[None] ]
ss4 = ['b', 'a']
m4 = [ [None, None] ]
lab(ss4, m4) # 2 studenti 2 sedie in una fila
assert m4 == [ ['a','b'] ]
assert ss4 == ['a', 'b'] # modificato anche lista di input
# come richiesto dal testo della funzione
m5 = [ [None, None],
[None, None] ]
lab(['b', 'c', 'a'], m5) # 3 studenti 2x2 sedie
assert m5 == [ ['a','b'],
['c', None] ]
m6 = [ [None, None],
[None, None] ]
lab(['b', 'd', 'c', 'a'], m6) # 4 studenti 2x2 sedie
assert m6 == [ ['a','b'],
['c','d'] ]
m7 = [ [None, None, None],
[None, None, None] ]
lab(['b', 'd', 'e', 'c', 'a'], m7) # 5 studenti 3x2 sedie
assert m7 == [ ['a','b','c'],
['d','e',None] ]
ss8 = ['b', 'd', 'e', 'g', 'c', 'a', 'h', 'f' ]
m8 = [ [None, None, None],
[None, None, None],
[None, None, None],
[None, None, None] ]
lab(ss8, m8) # 8 studenti 3x4 sedie
assert m8 == [ ['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', None],
[None, None, None] ]
assert ss8 == ['a','b','c','d','e','f','g','h']

def  lab1(studenti, sedie):
    n = len(sedie)
    m = len(sedie[0])

    if len(studenti) > m*m:
        raise ValueError('più studenti che sedie')
    i = 0
    j = 0
    studenti.sort()
    for s in studenti:
        sedie[i][j] = s
        if j == m -1:
            j = 0
            i += 1
        else:
            j += 1
print()

def toepliz(mat):
    for x in range(1,len(mat)):
        for y in range(1,len(mat[0])):
            if mat[x][y] != mat[x-1][y-1]:
                return False
    return True

m1 = [
[1,2,3,4],
[5,1,2,3],
[9,5,1,2]
]
print(toepliz(m1))

def toepliz1(mat):
    for y in range(1, len(mat)):
        for x in range(1, len(mat[0])):
            if mat[y][x] != mat[y-1][x-1]:
                return False
    return True

m1 = [
[1,2,3,4],
[5,1,2,3],
[9,5,1,2],
]
print(toepliz1(m1))
# INIZIO TEST - NON TOCCARE !
assert toepliz([ [1] ]) == True
assert toepliz([ [3,7],
[5,3] ]) == True
assert toepliz([ [3,7],
[3,5] ]) == False
assert toepliz([ [3,7],
[3,5] ]) == False
assert toepliz([ [3,7,9],
[5,3,7] ]) == True
assert toepliz([ [3,7,9],
[5,3,8] ]) == False
assert toepliz([ [1,2,3,4],
[5,1,2,3],
[9,5,1,2] ]) == True
assert toepliz([ [1,2,3,4],
[5,9,2,3],
[9,5,1,2] ]) == False
# FINE TEST
print()

def teopliz2(mat):
    for y in range(1,len(mat)):
        for x in range(1,len(mat[0])):
            if mat[y][x] != mat[y-1][x-1]:
                return False
    return True

m =  [  [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]]

print(teopliz2(m))
print()

def mul(mat1, mat2): # righe = len(mat) colonne = len(mat[0])
    #se il numero di colonne di mat1 è diverso dal numero di righe di mat2
    #blocca tutto
    n = len(mat) #righe mat1
    m = len(mat1[0]) #colonne mat1
    q = len(mat2) # righe mat2
    p = len(mat2[0]) #colonne mat2

    if m != len(mat2):
        raise ValueError("il numero di colonne di mat1 %s deve essere uguale al numero di righe di mat2 %s !" % (m, len(mat2)))
    
    ret = [[0]*p for i in range(n)]
    for i in range(n):
        for j in range(p):
            ret[i][j] = 0
            for k in range(m):
                ret[i][j] += mat1[i][k] * mat2[k][j]
    return ret


m41 = [ [3,5],
[7,1],
[9,4],
[8,7] ]
m42 = [ [4,1,5],
[8,5,2] ]

[print(x) for x in mul(m41, m42)]

print()

def mul2(mat1, mat2):
    r1 = len(mat1)
    c1 = len(mat1[0])
    r2 = len(mat2)
    c2 = len(mat2[0])

    if c1 != r2:
        raise ValueError
    
    nuova = [[0]* c2 for x in range(r1)]
    for y in range(len(nuova)):
        for x in range(len(nuova[0])):
            nuova[y][x] = (mat1[y][0] * mat2[0][x]) + (mat1[y][1] * mat2[1][x])
    return nuova

m41 = [ [3,5],
[7,1],
[9,4],
[8,7] ]
m42 = [ [4,1,5],
[8,5,2] ]

[print(x) for x in mul2(m41, m42)]

def check_nqueen(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j]: # queen is found at i,j
                for y in range(n): # vertical scan
                    if y != i and mat[y][j]:
                        return False
                for x in range(n): # horizontal scan
                    if x != j and mat[i][x]:
                        return False
                for x in range(n):
                    y = x + j + i # top-left to bottom-right
                    if y >= 0 and y < n and y != i and x != j and mat[y][x]:
                        return False
                    y = x - j + i # bottom-left to top-right
                    if y >= 0 and y < n and y != i and x != j and mat[y][x]:
                        return False
    return True

m = ([  [True, False, False],
        [False, False, True],
        [False, False, False] ])
print(check_nqueen(m))

def queen_check(mat):
    if len(mat) != len(mat[0]):
        return ValueError
    n = len(mat)
    for y in range(n):
        for x in range(n):
            if mat[y][x]:
                for y1 in range(n): #verticale
                    if y1 != y and mat[y1][x]:
                        return False
                for x1 in range(n): #orizzontale
                    if x1 != x and  mat[y][x1]:
                        return False
                for j in range(n):
                    z = j + x + y # alto sinistra basso destra
                    if z >= 0 and z < n and z != y and j != x and mat[z][j]:
                        return False
                    z = j - x + y #alto destra basso sinistra
                    if z >= 0 and z < n and z != y and j != x and mat[z][j]:
                        return False
                    
    return True

m = ([  [False, False, False, False ],
        [False, False, False, False ],
        [False, False, True, False ],
        [False, True, False, False ],])

print(queen_check(m))
assert queen_check([ [True, False],
[False, True] ]) == False
assert queen_check([ [True] ])
assert queen_check([ [True, True],
[False, False] ]) == False
assert queen_check([ [True, False],
[False, True] ]) == False
assert queen_check([ [True, False],
[True, False] ]) == False
assert queen_check([ [True, False, False],
[False, False, True],
[False, False, False] ]) == True
assert queen_check([ [True, False, False],
[False, False, False],
[False, False, True] ]) == False
assert queen_check([ [False, True, False],
                    [False, False, False],
                    [False, False, True] ]) == True
assert queen_check([ [False, True, False],
[False, True, False],
[False, False, True] ]) == False
print()

def totale(liste):
    lista_pagati = []
    lista_nonpagati = []
    piu_pagato = []
    tot_ricevuto = 0
    tot_daricevere = 0

    for lista in liste:
        if lista[-1] == 'pagato':
            lista_pagati.append(lista)
            tot_ricevuto += lista[1]
            piu_pagato.append(lista[1])
        else:
            lista_nonpagati.append(lista)
            tot_daricevere += lista[1]

    lavoro_migliore = None
    for el in lista_pagati:
        if el[1] == max(piu_pagato):
            lavoro_migliore = el[0]
        
    print('Totale ricevuto:', tot_ricevuto)
    print('Totale da ricevere:', tot_daricevere)
    print('Il lavoro più pagato finora è:', lavoro_migliore )

lavori = [
    ["Straordinari in fonderia", 175.13, "non pagato"],
    ["Part time gelateria", 450, "non pagato"],
    ["Rendita investimenti", 500, "pagato"],
    ["Pettinatura pitoni", 1000, "pagato"],
    ["Installazione artistica", 600, "non pagato"],
    ["Noleggio scarpe eleganti", 100, "non pagato"]
]
totale(lavori)
print()

from pprint import pprint

def incarta(scaf, conf):
    if len(conf) != len(scaf):
        raise ValueError

    for y in range(len(scaf)):
        for x in range(len(scaf[0])):
            scaf[y][x] = conf[y] + scaf[y][x] + conf[y]



m = [['f','e','a','b'],
['a','c','g','f'],
['b','c','d','f']]

c =  ['/','|','!']
[print(x) for x in m]
incarta(m,c)
pprint(m)
m1 = [['a']]
riga_zero_m1 = m1[0]
res = incarta(m1, ['|'])
assert res == None
assert m1 == [['|a|']]
# controlla che la riga zeresima punti ancora esattamente alla stessa regione di memoria originale
assert id(m1[0]) == id(riga_zero_m1)
m2 = [['f','g']]
incarta(m2, ['|'])
assert m2 == [['|f|','|g|']]
m3 = [['a'],
['b'],]
incarta(m3, ['?','|'])
assert m3 == [['?a?'],
['|b|']]
m3 = [['f','e','a','b'],
['a','c','g','f'],
['b','c','d','f']]
incarta(m3, ['/','|','!'])
from pprint import pprint
#pprint(m3, width=53)
assert m3 == [['/f/', '/e/', '/a/', '/b/'],
['|a|', '|c|', '|g|', '|f|'],
['!b!', '!c!', '!d!', '!f!']]
try:
    incarta([['a']], ['/','!'])
    raise Exception('Avrei dovuto fallire prima !')
except ValueError:
    pass
print()

def cantiere(mat, mattonelle):
    if len(mattonelle) != len(mat)+1:
        raise ValueError
    nuova = [x[:] for x in mat]

    lista_matt = []
    for el in range(len(mattonelle)):
        if el == 0:
            lista = [mattonelle[el] for x in range(len(mattonelle))]
            lista[0:0] = ' '
            lista.append(' ')
            lista_matt.append(lista)
        else:
            lista = [mattonelle[el] for x in range(len(mattonelle))]
            lista[0:0] = '|'
            lista.append('|')
            lista_matt.append(lista)

    nuovissima = []
    for y in range(len(nuova)):
        nuova[y][0:0] = '|'
        nuova[y].append('|')
    
    for x,y in zip(lista_matt, nuova):
        nuovissima.append(x)
        nuovissima.append(y)
    nuovissima.append(lista_matt[-1])
    
    return nuovissima

m = [['f','e','a','b'],
['a','c','g','f'],
['b','c','d','f']]

matto = ['^','-','_','=']
[print(x) for x in cantiere(m, matto)]
print()
[print(''.join(x)) for x in cantiere(m, matto)]

m1 = [['a']]
cantiere(m1, ['^','='])

[print(x) for x in cantiere(m1,  ['^','='])]
print()
[print(''.join(x)) for x in cantiere(m1, ['^','='])]

managers_db = [
        {
            "nome":"Alessandro",
            "cognome": "Borgoloso",
            "età": 34,
            "azienda": {
            "nome": "Aringhe Candite Spa",
            "settore":"Alimentari"
}
    },
    {
        "nome":"Matilda",
"cognome": "Delle Sòle",
"età": 25,
"azienda": {
"nome": "Calzature Pitonate Srl",
"settore":"Abbigliamento"
}
},
{
"nome":"Alfred",
"cognome": "Pennyworth",
"età": 20,
"azienda": {
"nome": "Batworks",
"settore":"Abbigliamento"
}
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
"settore":"Alimentari"
}
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

def eta_media1(lista):
    somma = 0
    for x in lista:
        somma += x['età']
    return somma / len(lista)

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

def medie(lista):
    voti = []
    for x in lista:
        voti.append((x['V'] + x['VI']) /2)
    return voti

list_diz =[
{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
{'id' : 1, 'subject' : 'italian', 'V' : 73, 'VI' : 74},
{'id' : 1, 'subject' : 'german', 'V' : 75, 'VI' : 86}
]

print(medie(list_diz))

def medie1(lista):
    ret = [0.0, 0.0, 0.0]
    for y in range(len(lista)):
        ret[y] = ((lista[y]['V'] + lista[y]['VI']) / 2)
    return ret

print(medie1(list_diz))

import math

def is_list_close(lista1, lista2):
    if len(lista1) != len(lista2):
        return False
    for i in range(len(lista1)):
        if not math.isclose(lista1[i], lista2[i]):
            return False
    return True
assert is_list_close(medie([
{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
{'id' : 1, 'subject' : 'italian', 'V' : 73, 'VI' : 74},
{'id' : 1, 'subject' : 'german', 'V' : 75, 'VI' : 86}
]),
[ 76.0 , 73.5, 80.5 ])
# FINE TEST
print()

def ha_pref(diz, nome, parola):
    if nome in diz:
        return parola in diz[nome]
    else:
        return False

diz = {'aldo': ['cinema', 'musica', 'sport'],
'giovanni': ['musica'],
'giacomo': ['cinema', 'videogiochi']
}
print(ha_pref(diz, 'giacomo', 'musica'))
assert ha_pref({}, 'a', 'x') == False
assert ha_pref({'a':[]}, 'a', 'x') == False
assert ha_pref({'a':['x']}, 'a', 'x') == True
assert ha_pref({'a':['x']}, 'b', 'x') == False
assert ha_pref({'a':['x','y']}, 'a', 'y') == True
assert ha_pref({'a':['x','y'],
'b':['y','x','z']}, 'b', 'y') == True
assert ha_pref({'aldo': ['cinema', 'musica', 'sport'],
'giovanni': ['musica'],
'giacomo': ['cinema', 'videogiochi']
}, 'aldo', 'musica') == True
assert ha_pref({'aldo': ['cinema', 'musica', 'sport'],
'giovanni': ['musica'],
'giacomo': ['cinema', 'videogiochi']
}, 'giacomo', 'sport') == False
print()

sentimenti = {
                1: {
                    "espressione": "Gulp!",
                    "posizione": "i"},
                2: {
                    "espressione": "Sgaragulp !",
                    "posizione": "i"},
                3: {
                    "espressione": "Uff..",
                    "posizione": "f"}}

def onomat(frase, sentimento, sentimenti):
    #for x in range(len(sentimenti)):
    if sentimenti[sentimento]['posizione'] == 'i':
        return sentimenti[sentimento]['espressione'] + ' ' + frase
    elif sentimenti[sentimento]['posizione'] == 'f':
        return frase + ' ' + sentimenti[sentimento]['espressione']
    
print(onomat("Ma quelli sono i bassotti!", 1, sentimenti))
print(onomat("Non voglio alzarmi dall'amaca.", 3, sentimenti))
# INIZIO TEST - NON TOCCARE !!!
sentimenti = {
1: { "espressione": "Gulp!",
"posizione": "i"
},
2: { "espressione": "Sgaragulp!",
"posizione": "i"
},
3: { "espressione": "Uff..",
"posizione": "f"
},
4: { "espressione": "Yuk yuk!",
"posizione": "f"
},
5: { "espressione": "Sgrunt!",
"posizione": "i"
},
6: { "espressione": "Gasp!",
"posizione" : "i"
}
}
assert onomat("Mi chiamo Pippo.", 4, sentimenti) == "Mi chiamo Pippo. Yuk yuk!"
assert onomat("Quel topastro mi ha rovinato un'altra rapina!", 5, sentimenti) == "Sgrunt! Quel topastro mi ha rovinato un'altra rapina!"
assert onomat("Non voglio alzarmi dall'amaca.", 3, sentimenti) == "Non voglio alzarmi dall'amaca. Uff.."
# FINE TEST

def onomat2(frase, sentimenti, sentimento):
    sent = sentimento[sentimenti]
    if sent['posizione'] == 'i':
        return sent['espressione'] + ' ' + frase
    else:
        return frase + ' ' + sent['espressione']
    
assert onomat2("Mi chiamo Pippo.", 4, sentimenti) == "Mi chiamo Pippo. Yuk yuk!"
assert onomat2("Quel topastro mi ha rovinato un'altra rapina!", 5, sentimenti) == "Sgrunt! Quel topastro mi ha rovinato un'altra rapina!"
assert onomat2("Non voglio alzarmi dall'amaca.", 3, sentimenti) == "Non voglio alzarmi dall'amaca. Uff.."
# FINE TEST
print()

def sagra1(lista, dolci):
    nuova = []
    nuova.append(['Nome'] + dolci[:])
    somme = [0]*(len(dolci)+1)
    somme[0] = 'Totali' # type: ignore
    for p in pasticcerie:
        j = 1
        riga = [p['nome']]
        for dolce in dolci:
            riga.append(p[dolce])
            somme[j] += p[dolce]
            j += 1
        nuova.append(riga)
    nuova.append(somme)
    return nuova

def sagra(lista, dolci):
    nuova = [['Nome'] + dolci[:]]
    ultima = ['Totali']
    for x in lista:
        riga = []
        riga.append(x['nome'])
        for y in dolci:
            riga.append(x[y])
        nuova.append(riga)
    j = 1
    for dolce in dolci:
        tot = 0
        for x in range(1, len(nuova)):
            tot += nuova[x][j]
        ultima.append(tot) # type: ignore
        j += 1
    nuova.append(ultima)
    return nuova

pasticcerie = [{'babbà':3,
'bignè':4,
'zippole':2,
'nome':'Da Gigi'},
{'babbà':5,
'bignè':3,
'zippole':9,
'nome':'La Delizia'},
{'babbà':1,
'bignè':2,
'zippole':6,
'nome':'Gnam gnam'},
{'babbà':7,
'bignè':8,
'zippole':4,
'nome':'Il Dessert'}]

[print(x) for x in sagra(pasticcerie, ['bignè', 'babbà', 'zippole'])]
print()
from pprint import pprint
pprint(sagra(pasticcerie, ['bignè', 'babbà', 'zippole']))

dolci1 = ['cornetti']
res1 = sagra([{'nome':'La Patisserie',
'cornetti':2},
{'cornetti':5,
'nome':'La Casa Del Cioccolato'}], dolci1)
assert res1 == [['Nome', 'cornetti' ],
['La Patisserie', 2 ],
['La Casa Del Cioccolato', 5 ],
['Totali', 7 ]]
assert dolci1 == ['cornetti'] # verifica che l'input non cambi
pasticcerie2 = [{'babbà':3,
'bignè':4,
'zippole':2,
'nome':'Da Gigi'},
{'babbà':5,
'bignè':3,
'zippole':9,
'nome':'La Delizia'},
{'babbà':1,
'bignè':2,
'zippole':6,
'nome':'Gnam gnam'},
{'babbà':7,
'bignè':8,
'zippole':4,
'nome':'Il Dessert'}]
res2 = sagra(pasticcerie2, ['bignè', 'babbà', 'zippole'])
assert res2 == [['Nome', 'bignè', 'babbà', 'zippole'],
['Da Gigi', 4, 3, 2 ],
['La Delizia', 3, 5, 9 ],
['Gnam gnam', 2, 1, 6 ],
['Il Dessert', 8, 7, 4 ],
['Totali', 17, 16, 21 ]]
print()

lista = [
{'titolo':'Jerry Maguire',
'anno':1996,
'Jerry':'Dorothy',},
{'titolo':'Superman',
'Kent':'Lois',
'anno': 1978},
{'titolo':'The Lord of the Rings',
'anno': 2001,
'Aragorn':'Arwen',},
{'Ron Weasley':'Hermione',
'titolo': 'Harry Potter and the Deathly Hallows, Part 2',
'anno': 2011}
]

def scambiattori(lista):
    nuova = []
    for diz in lista:
        nuovo_diz = {}
        nuova.append(nuovo_diz)
        for chiave in diz:
            if chiave == 'titolo' or chiave == 'anno':
                nuovo_diz[chiave] = diz[chiave]
            else:
                nuovo_diz[diz[chiave]] = chiave
    return nuova
        
[print(x) for x in scambiattori(lista)]

l1 = []
assert scambiattori(l1) == []
l2 = [ {'titolo': 'Pretty Woman',
'anno': 1990,
'Edward':'Vivian'},
{'titolo': 'Titanic',
'anno': 1997,
'Jack' : 'Rose'}
]
orig_film = l2[0]
res2 = scambiattori(l2)
assert res2 == [ {'titolo': 'Pretty Woman',
'anno': 1990,
'Vivian':'Edward'},
{'titolo': 'Titanic',
'anno': 1997,
'Rose' : 'Jack'}
]
assert id(l2) != id(res2) # deve produrre NUOVA lista
assert id(orig_film) != id(res2[0]) # deve produrre NUOVO dizionario
l3 = [
{'titolo':'Jerry Maguire',
'anno':1996,
'Jerry':'Dorothy',},
{'titolo':'Superman',
'Kent':'Lois',
'anno': 1978},
{'titolo':'The Lord of the Rings',
'anno': 2001,
'Aragorn':'Arwen',},
{'Ron Weasley':'Hermione',
'titolo': 'Harry Potter and the Deathly Hallows, Part 2',
'anno': 2011}
]
assert scambiattori(l3) == [{'titolo': 'Jerry Maguire',
'anno': 1996,
'Dorothy': 'Jerry'},
{'titolo': 'Superman',
'anno': 1978,
'Lois': 'Kent'},
{'titolo': 'The Lord of the Rings',
'anno': 2001,
'Arwen': 'Aragorn'},
{'titolo': 'Harry Potter and the Deathly Hallows, Part 2',
'anno': 2011,
'Hermione': 'Ron Weasley',
}]
print()

lavori = [
{"nome": "Pettinatura pitoni", "valore": 1000, "status": "pagato"},
{"nome": "Straordinari in fonderia", "valore": 175.13, "status": "non pagato"},
{"nome": "Part time gelateria", "valore": 450, "status": "non pagato"},
{"nome": "Rendita investimenti", "valore": 500, "status": "pagato"},
{"nome": "Installazione artistica", "valore": 600, "status": "non pagato"},
{"nome": "Noleggio scarpe eleganti", "valore": 100, "status": "non pagato"}
]

def precario(lista):
    lavori_pagati = []
    miglior_lavoro = None
    guadagni_ricevuti = 0
    guadagni_da_ricevere = 0
    confronto = 0
    for lavoro in lista:
        if lavoro['status'] == 'pagato':
            lavori_pagati.append(lavoro)
            guadagni_ricevuti += lavoro['valore']
        else:
            guadagni_da_ricevere += lavoro['valore']
        if lavoro['valore'] > confronto:
            confronto = lavoro['valore']
            miglior_lavoro = lavoro['nome']
    print('1.   Totale ricevuto:', guadagni_ricevuti)
    print('     Totale da ricevere:', guadagni_da_ricevere)
    print('2.   Il lavoro più pagato finora è:', miglior_lavoro)

precario(lavori)
print()

valori = {'c':'xzwy',
'a':'yxzw',
'b':'zxwy'}

from pprint import pprint

def ricme(diz):
    nuova = []
    for x in diz:
        riga = [x]
        riga.sort()
        nuova.append(riga)
        x = diz[x]
        for y in x:
            riga.append(y)
    nuova.sort()
    return nuova
            
pprint(ricme(valori))
assert ricme({}) == []
assert ricme({'d':'q'}) == [['d','q']]
assert ricme({'d':'pq',
'e':'qp'}) == [['d','p','q'],
['e','q','p']]
assert ricme({'c':'xzwy',
'a':'yxzw',
'b':'zxwy'}) == [['a', 'y', 'x', 'z', 'w'],
['b', 'z', 'x', 'w', 'y'],
['c', 'x', 'z', 'w', 'y']]

import numpy as np
mat = np.zeros((2,3)) #2 righe per 3 colonne
print(type(mat))
mat = np.array([[5.0,8.0,1.0],
               [4.0,3.0,2.0]])
print(mat)
print(type(mat))
mat = np.ones((3,5))
print(mat)
mat = np.full((3,5), 7)
print(mat)
print(mat.shape)
num_righe, num_colonne = mat.shape
print(num_righe, num_colonne)
mat = np.array((2,3))
print(mat)
mat = np.array([[5.0,8.0,1.0],
               [4.0,3.0,2.0]])
print(mat[0,1])
mat[0,1] = 9
print(mat[0,1])
print(mat[1,2])
mat[1,2] = 7
print(mat[1,2])
#print(mat[1,1.0])

mat = np.array([[3.0, 5.0, 2.0],
                [6.0, 2.0, 9.0]])
print(mat)
mat.fill(7)
print(mat)
print()
mat = np.array([ [5,8,1],
                 [4,3,2],
                 [6,7,9],
                 [9,3,4],
                 [8,2,7] ])

print(mat[0:4, 1:3]) #estrae le righe dalla prima alla 4°
                     #estre le colonne dalla seconda alla 3°
print()
print(mat[0:1, 0:3]) #estrae la prima riga ovvero tutti gli elementi della prima riga
print(mat[:1, :]) #estrae la prima riga
print(mat[0:5, 0:1]) #estrae la prima colonna ovvere tutti gli primi elementi di ciascuna riga
print(mat[:, 0:1]) #estrae la prima colonna
print()
print(mat[0:5:2, :]) #stampa una riga si e una no e tutte lecolonne
print()

mat = np.array( [ [5, 8, 1],
[4, 3, 2],
[6, 7, 9],
[9, 3, 4],
[8, 2, 7]])
print(mat)
sotto_mat = mat[0:4, 1:3]
print(sotto_mat)

sotto_mat[0,0] = 999
print(mat)
mat [0:4, 1:3] = 7

print(mat)
print()
mat = np.array([[5, 8, 1],
                [4, 3, 2],
                [6, 7, 9],
                [9, 3, 4],
                [8, 2, 5]])

mat[0:4,1:3] = 7
print(mat)
print()

mat = np.array([[5, 8, 1],
                [4, 3, 2],
                [6, 7, 9],
                [9, 3, 4],
                [8, 2, 5]])
print(len(mat), len(mat[0]))
print(len(mat[0:4]), len(mat[0][1:3]))
mat[0:4, 1:3] = np.array([
                            [10, 50],
                            [11, 51],
                            [12, 52],
                            [13, 53]
                                    ])

print(mat)
print()

va = np.array([1,2,3])
print(va)
vb = va
vb[0] = 100
print(id(va), id(vb))
print(va, '\n', vb)
print()

va = np.array([1,2,3])
vc = va.copy()
print(id(va), id(vc))
vc[0] = 100
print(va, '\n', vc)
print()

va = np.array([5, 9, 7])
print(va)
vb = np.array([6, 8, 0])
print(vb)

vc = va + vb
print(vc)

m = np.array([[5, 9, 7],
             [6, 8, 0]])
print(3*m)
print(3+m)
print()
ma = np.array([[1, 2, 3],
               [10, 20, 30]])

mb = np.array([[1, 0, 1],
               [40, 100, 180]])

print(ma * mb)

mc = np.array([[1, 2, 3],
               [10, 20, 30]])
md = np.array([[1, 4],
               [0, 5],
               [1, 6]])

print(mc @ md)

ma = np.array([[1, 2, 0.0],
               [10, 0.0, 30]])
print(ma/4)
print(ma/0.0)
print()
m = np.array([[5, 4, 6],
              [3, 7, 1]])

print(np.sum(m))
print(np.max(m))
print(np.min(m))

c = [[1,3,4],
     [3,5,2]]
d = np.array(c)
print(d)
print(np.max(d))

print(np.max(d, axis=0))
print(np.sum(d, axis = 0))
print(np.min(d, axis= 0))
print() # tutte le righe

print(np.max(d, axis = 1))#, np.max(d, axis = 0))
print(np.sum(d, axis = 1))
print(np.min(d, axis = 1))
print() # tutte le le colonne
f = d.copy()
print(f)
print()

mat = np.array([[5,2,6],
                [1, 4, 3]])

print(mat[ mat > 2])
print(mat > 2)
print(mat[ (mat > 3) & (mat < 6)])

print(mat[(mat < 2) | (mat > 4)])
print()

v = np.array([30, 60, 20, 70, 40, 80])
a = np.where((v < 40) | (v > 60))
#[print(x) for x in a]
print(a)
print()

ma = np.array([
[ 1, 2, 3, 4],
[ 5, 6, 7, 8],
[ 9,10,11,12]
])
mb = np.array([
[ -1, -2, -3, -4],
[ -5, -6, -7, -8],
[ -9,-10,-11,-12]
])
mat = np.array([
[40,70,10,80],
[20,30,60,40],
[10,60,80,90]
])

print(np.where(mat < 50, ma, mb))

import numpy as np
print(np.arange(0.0, 1.0, 0.2))
print(np.linspace(0, 0.8, 5))

import math
print(math.nan)

print(math.nan == math.nan)

ma = np.array([[1, 2, 0.0],
               [10, 0.0, 30]])
print(ma/4)
print(ma/0.0)

x = math.nan
if x == math.nan:
    print('Sono in NaN')
else:
    print('x è altro')


x = math.nan
if math.isnan(x):
    print('x è un NaN')
else:
    print('x è altro')

y = -math.nan
if math.isnan(y):
    print('y è nan')
else:
    print('x è altro')

print([math.nan, math.nan] == [math.nan, math.nan] )
print([math.nan, math.nan] == [math.nan, 6.0])

x = 3
y = 3

if math.isnan(x) and math.isnan(y):
    print('stessa cosa')
elif x == y:
    print('stessa cosa')
else:
    print('non stessa cosa')

print(5*math.nan)
print(math.nan + math.nan)
print(math.nan / math.nan)
#print(math.nan / 0)

if math.nan:
    print('ok')
else:
    print('not ok')
print()

print(np.nan)
print(np.isnan(math.nan))

s = np.array([4.9, None, 3.2, 5.1])
print(s)

f = np.array([4.9, np.nan, 3.2, 3.2, 5.1])
print(f)

#print(math.log(-1))
print(np.log(-1))
print(np.log(np.array([3,7, -1 ,9])))

print(np.array([5])/0)
print(np.array([6,9,5,7]) / np.array([2,0,0,4]))

print(np.inf == np.inf)

x = np.inf
if x == np.inf:
    print('x è infinito')
else:
    print('x è finito')

print(np.isinf(x))

print(-np.inf == np.inf)

print(np.isinf(-np.inf))
print(np.isneginf(-np.inf))
print(np.isneginf(np.inf))

print(np.log(0))
print()

print(np.inf + np.inf)
print(-np.inf - np.inf)
print(np.inf * -np.inf)
print(np.inf - np.inf)
print(np.inf / np.inf)
print(np.inf + np.nan)
print(np.inf / np.nan)
print()

print(np.NZERO)
print(np.PZERO)
print(-0.0 == 0.0)
print(np.array([ 5.0 ]) / np.array([ 0.0 ]))
print(np.array([ 5.0 ]) / np.array([ -0.0 ]))

print(np.array([1.0]) / np.array([0.0]))
x = 5
y = 8
if np.isinf(x) or np.isinf(y) or np.isnan(x) or np.isnan(y):
    print('Numeri non uguali')
else:
    print('Uguali')

if np.isfinite(x) and np.isfinite(y):
    print('Uguali')
else:
    print('non uguali')

print(0.0 * -0.0)
print((-0.0)**3)
#print(np.log(-7) == math.log(-7))
print(np.log(-7) == np.log(-7))
print(np.isnan( 1 / np.log(1)))
print(np.sqrt(-1) * np.sqrt(-1))
print(np.sqrt(-1) == np.sqrt(-1))
print(3 ** np.inf)
print(3 ** -np.inf)
print(1/np.sqrt(-3))
print(1/np.sqrt(-0.0))
print(np.sqrt(np.inf) - np.sqrt(-np.inf))
print(np.sqrt(np.inf) + (1/np.sqrt(-0.0)))
print(np.isneginf(np.log(np.e) / np.sqrt(-0.0)))
print(np.e)
print([np.nan, np.inf] == [np.nan, np.inf])
print([np.nan, -np.inf] == [np.nan, np.inf])
print([np.nan, np.inf] == [-np.nan, np.inf])

import numpy as np

def quadrofor(nm, valore):
    nuova = [[0]*nm for x in range(nm)]
    for y in range(len(nuova)):
        for x in range(len(nuova[0])):
            if y == 0 or x == 0 or y == len(nuova)-1 or x == len(nuova)-1:
                nuova[y][x] = valore
            else:
                pass
    return nuova


[print(x) for x in quadrofor(4, 7.0)]

def quadrofor1(nm, valore):
    nuova = np.zeros((nm, nm))
    nuova[:, 0] = valore
    nuova[:, -1] = valore
    nuova[0] = valore
    nuova[-1] = valore
    return nuova

[print(x) for x in quadrofor1(4, 7.0)]
r1 = np.array( [[7.0, 7.0, 7.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 7.0, 7.0, 7.0]])
# all_close ritorna True se tutti i valori nella prima matrice sono abbastanza vicini
# (cioè entro una certa tolleranza) ai corrispondenti nella seconda
assert np.allclose(quadrofor1(4, 7.0), r1)
r2 = np.array( [ [7.0] ])
assert np.allclose(quadrofor1(1, 7.0), r2)
r3 = np.array( [ [7.0, 7.0],
[7.0, 7.0]])
assert np.allclose(quadrofor1(2, 7.0), r3)


def quadrofor2(n, k):
    mat = np.zeros((n,n))
    for i in range(n):
        mat[0, i] = k
        mat[i, 0] = k
        mat[i, n-1] = k
        mat[n-1, i] = k
    return mat

print(quadrofor2(4, 7.0))

def quadroslices(n, k):
    mat = np.zeros((n, n))
    mat[0, :] = k
    mat[:, 0] = k
    mat[:, n-1] = k
    mat[n-1, :] = k
    return mat

print(quadroslices(4, 7.0))

r1 = np.array( [[7.0, 7.0, 7.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 7.0, 7., 7.0]])
# all_close ritorna True se tutti i valori nella prima matrice sono abbastanza vicini
# (cioè entro una certa tolleranza) ai corrispondenti nella seconda
assert np.allclose(quadroslices(4, 7.0), r1)
r2 = np.array( [ [7.0] ])
assert np.allclose(quadroslices(1, 7.0), r2)
r3 = np.array( [ [7.0, 7.0],
[7.0, 7.0]])
assert np.allclose(quadroslices(2, 7.0), r3)

def quadroriemp(n, k):
    mat = np.full((n,n), k)
    mat[1:-1, 1:-1] = 0.0
    return mat

print(quadroriemp(4, 7.0))

r1 = np.array( [[7.0, 7.0, 7.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 7.0, 7., 7.0]])
# all_close ritorna True se tutti i valori nella prima matrice sono abbastanza vicini
# (cioè entro una certa tolleranza) ai corrispondenti nella seconda
assert np.allclose(quadroriemp(4, 7.0), r1)
r2 = np.array( [ [7.0] ])
assert np.allclose(quadroriemp(1, 7.0), r2)
r3 = np.array( [ [7.0, 7.0],
[7.0, 7.0]])
assert np.allclose(quadroriemp(2, 7.0), r3)
print()


m =[ [3, 2, 1, 4],
    [6, 2, 3, 5],
    [4, 3, 6, 2],
    [4, 6, 5, 4],
    [7, 2, 9, 3]]

def media_righe(mat):
    nuova = [[0]*1 for x in range(len(mat))]
    for y in range(len(mat)):
        riga = []
        for x in range(len(mat[0])):
            riga.append(mat[y][x])
        nuova[y] = [sum(riga) / len(mat[0])] # type: ignore
    return nuova


print(media_righe(m))

m1 = np.array([ [5.0] ])
r1 = np.array([ [5.0] ])
assert np.allclose(media_righe(m1), r1)
m2 = np.array([ [5.0, 3.0] ])
r2 = np.array([ [4.0] ])
assert np.allclose(media_righe(m2), r2)
m3 = np.array(
[[3,2,1,4],
[6,2,3,5],
[4,3,6,2],
[4,6,5,4],
[7,2,9,3]])
r3 = np.array([ [(3+2+1+4)/4],
[(6+2+3+5)/4],
[(4+3+6+2)/4],
[(4+6+5+4)/4],
[(7+2+9+3)/4] ])
assert np.allclose(media_righe(m3), r3)

def media_righe2(mat):
    righe, colonne = len(mat), len(mat[0])
    ret = np.zeros((righe, 1))
    for y in range(righe):
        for x in range(colonne):
            ret[y] += mat[y][x]
        ret[y] = ret[y] / colonne
    return ret

print(media_righe2(m))
print()
def media_righe3(mat):
    righe, colonne = len(mat), len(mat[0])
    nuova = np.mean(mat, axis = 1)
    nuova = nuova.reshape((righe, 1))
    return nuova

[print(x) for x in media_righe3(m)]


def media_righe4(mat):
    righe, colonne = len(mat), len(mat[0])
    media = np.mean(mat, axis = 1)
    media = media.reshape(righe, 1)
    return media

[print(x) for x in media_righe4(m)]

import numpy as np

m =[ [3, 2, 1, 4],
    [6, 2, 3, 5],
    [4, 3, 6, 2],
    [4, 6, 5, 4],
    [7, 2, 9, 3]]

def media_righe5(mat):
    mat = np.array(mat)
    righe, colonne = mat.shape
    media = np.mean(mat, axis = 1)
    media = media.reshape(righe, 1)
    return media

[print(x) for x in media_righe5(m)]
print()
m = np.array( [
[0,1,0],
[1,1,0],
[0,0,0],
[0,1,1]
])

def matrot1(mat):
    ret = np.zeros(mat.shape)
    for i in range(mat.shape[0]):
        ret[i,0] = mat[i, -1]
        for j in range(1, mat.shape[1]):
            ret[i, j] = mat[i, j-1]
    return ret

print(m)
print(matrot1(m))

def matrot(mat):
    nuova = np.zeros(mat.shape)
    for y in range(mat.shape[0]):
        nuova[y, 0] = mat[y, -1]
        for x in range(mat.shape[1]):
            nuova[y, x] = mat[y, x-1]
    return nuova

print(m)
print(matrot(m))

m1 = np.array( [ [1] ])
r1 = np.array( [ [1] ])
assert np.allclose(matrot(m1), r1)
m2 = np.array( [ [0,1] ])
r2 = np.array( [ [1,0] ])
assert np.allclose(matrot(m2), r2)
m3 = np.array([ [0,1,0] ])
r3 = np.array([ [0,0,1] ])
assert np.allclose(matrot(m3), r3)
m4 = np.array( [[0,1,0],
[1,1,0]])
r4 = np.array( [[0,0,1],
[0,1,1]])
assert np.allclose(matrot(m4), r4)
m5 = np.array([ [0,1,0],
[1,1,0],
[0,0,0],
[0,1,1]])
r5 = np.array([ [0,0,1],
[0,1,1],
[0,0,0],
[1,0,1]])
assert np.allclose(matrot(m5), r5)
print()

def matrot_pro(mat):
    m = mat.shape[0]
    n = mat.shape[1]

    ret = np.zeros((m,n))
    ret[:, 0] = mat[:, -1]
    #print(ret)
    ret[:, 1:] = mat[:, :-1]
    #print(ret)
    return ret

print(m)
print(matrot_pro(m))
m1 = np.array( [ [1] ])
r1 = np.array( [ [1] ])
assert np.allclose(matrot_pro(m1), r1)
m2 = np.array( [ [0,1] ])
r2 = np.array( [ [1,0] ])
assert np.allclose(matrot_pro(m2), r2)
m3 = np.array([ [0,1,0] ])
r3 = np.array([ [0,0,1] ])
assert np.allclose(matrot_pro(m3), r3)
m4 = np.array( [[0,1,0],
[1,1,0]])
r4 = np.array( [[0,0,1],
[0,1,1]])
assert np.allclose(matrot_pro(m4), r4)
m5 = np.array([ [0,1,0],
[1,1,0],[0,0,0],
[0,1,1]])
r5 = np.array([ [0,0,1],
[0,1,1],
[0,0,0],
[1,0,1]])
assert np.allclose(matrot_pro(m5), r5)
print()

dim = np.array( [
[2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])
def disp(mat):
    righe, colonne = mat.shape
    nuova = np.zeros((righe, colonne))

    for y in range(righe):
        for x in range(colonne):
            if mat[y][x] % 2 == 0:
                nuova[y][x] = mat[y][x] + 1
            else:
                nuova[y][x] = mat[y][x]
    return nuova

print(disp(dim))
m1 = np.array([ [2] ])
r1 = np.array([ [3] ])
assert np.allclose(disp(m1), r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])
r2 = np.array( [ [3,5,7,3],
[9,5,3,5],
[7,1,7,9]])
assert np.allclose(disp(m2), r2)


def disp_pro1(mat):
    ret = np.array(np.where(mat % 2 == 0, mat+1, mat))
    return ret

print(disp_pro1(dim))

m1 = np.array([ [2] ])
r1 = np.array([ [3] ])
assert np.allclose(disp_pro1(m1), r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])
r2 = np.array( [ [3,5,7,3],
[9,5,3,5],
[7,1,7,9]])
assert np.allclose(disp_pro1(m2), r2)

def disp_pro2(mat):
    ret = mat.copy()
    ret[ret % 2 == 0] += 1
    return ret

print(disp_pro2(dim))
m1 = np.array([ [2] ])
r1 = np.array([ [3] ])
assert np.allclose(disp_pro2(m1), r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])
r2 = np.array( [ [3,5,7,3],
[9,5,3,5],
[7,1,7,9]])
assert np.allclose(disp_pro2(m2), r2)
print()

m = np.array( [                # indice
                [ 2, 5, 6, 3], # 0 pari
                [ 8, 4, 3, 5], # 1 dispari
                [ 7, 1, 6, 9], # 2 pari
                [ 5, 2, 4, 1], # 3 dispari
                [ 6, 3, 4, 3] # 4 pari
])

def radalt1(mat):
    righe, colonne = mat.shape
    ret = mat.copy()
    for y in range(righe):
        for x in range(colonne):
            if y % 2 == 0:
                ret[y][x] *= 2
    return ret

print(radalt1(m))

def radalt(mat):
    nrighe, ncolonne = mat.shape
    ret = np.zeros((nrighe, ncolonne))
    for i in range(nrighe):
        for j in range(ncolonne):
            if i % 2 == 0:
                ret[i,j] = mat[i,j] * 2
            else:
                ret[i,j] = mat[i,j]
    return ret

print(radalt(m))
m1 = np.array([ [2] ])
r1 = np.array([ [4] ])
assert np.allclose(radalt(m1),r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [ 2, 5, 6],
[ 8, 4, 3]])
r2 = np.array( [ [ 4,10,12],
[ 8, 4, 3]])
assert np.allclose(radalt(m2), r2)
m3 = np.array( [ [ 2, 5, 6, 3],
[ 8, 4, 3, 5],
[ 7, 1, 6, 9],
[ 5, 2, 4, 1],
[ 6, 3, 4, 3] ])
r3 = np.array( [ [ 4,10,12, 6],
[ 8, 4, 3, 5],
[14, 2,12,18],
[ 5, 2, 4, 1],
[12, 6, 8, 6] ])
assert np.allclose(radalt(m3), r3)
# FINE TEST

def radalt_pro(mat):
    ret = mat.copy()
    ret[::2] *= 2
    return ret

print(radalt_pro(m))
m1 = np.array([ [2] ])
r1 = np.array([ [4] ])
assert np.allclose(radalt_pro(m1),r1)
assert m1[0][0] == 2 # controlla non si stia modificando la matrice originale
m2 = np.array( [ [ 2, 5, 6],
[ 8, 4, 3]])
r2 = np.array( [ [ 4,10,12],
[ 8, 4, 3]])
assert np.allclose(radalt_pro(m2), r2)
m3 = np.array( [ [ 2, 5, 6, 3],
[ 8, 4, 3, 5],
[ 7, 1, 6, 9],
[ 5, 2, 4, 1],
[ 6, 3, 4, 3] ])
r3 = np.array( [ [ 4,10,12, 6],
[ 8, 4, 3, 5],
[14, 2,12,18],
[ 5, 2, 4, 1],
[12, 6, 8, 6] ])
assert np.allclose(radalt_pro(m3), r3)
print()

import numpy as np

m = np.array([[7.0, 7.0, 7.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 7.0, 7.0, 7.0]]) 

def quadroslices(n, k):
    nuova = np.zeros((n,n))
    nuova[0, :] = k
    nuova[:, 0] = k
    nuova[-1, :] = k
    nuova[:, -1] = k
    return nuova

print(quadroslices(len(m), 7.0))
r1 = np.array( [[7.0, 7.0, 7.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 0.0, 0.0, 7.0],
[7.0, 7.0, 7., 7.0]])
# all_close ritorna True se tutti i valori nella prima matrice sono abbastanza vicini
# (cioè entro una certa tolleranza) ai corrispondenti nella seconda
assert np.allclose(quadroslices(4, 7.0), r1)
r2 = np.array( [ [7.0] ])
assert np.allclose(quadroslices(1, 7.0), r2)
r3 = np.array( [ [7.0, 7.0],
[7.0, 7.0]])
assert np.allclose(quadroslices(2, 7.0), r3)

def quadroriemp(n, k):
    nuova = np.full((n,n),k)
    nuova[1:-1, 1:-1] = 0.0
    return nuova

print(quadroriemp(len(m), 7.0))
print()

m = np.array(
[[3,2,1,4],
[6,2,3,5],
[4,3,6,2],
[4,6,5,4],
[7,2,9,3]])

def media_righe(mat):
    nuova = np.mean(mat, axis = 1) # creo una lista dove calcolo la media di ogni riga
    nuova = nuova.reshape((len(mat), 1))# la trasformo in una matrice da una colonna e tot righe
    return nuova

print(media_righe(m))

m = np.array( [
[0,1,0],
[1,1,0],
[0,0,0],
[0,1,1]
])

def matrot(mat):
    nuova = np.zeros((mat.shape))
    nuova[:, 0] = mat[:, -1]
    nuova[:, 1:] = mat[:, :-1]
    return nuova

print(matrot(m))

def disp2(mat):
    ret = np.array(np.where(mat % 2 == 0, mat + 1, mat))
    return ret

def disp(mat):
    ret = mat.copy()
    ret[ret % 2 == 0 ] += 1
    return ret

print(disp(np.array( [
[2,5,6,3],
[8,4,3,5],
[6,1,7,9]
])))


m = np.array( [ # indice
[ 2, 5, 6, 3], # 0 pari
[ 8, 4, 3, 5], # 1 dispari
[ 7, 1, 6, 9], # 2 pari
[ 5, 2, 4, 1], # 3 dispari
[ 6, 3, 4, 3] # 4 pari
])

def radalt(mat):
    ret = mat.copy()
    ret[::2] *= 2
    return ret

print(radalt(m))

def scacchiera(n):
    nuova = np.zeros((n,n))
    nuova[::2, ::2] = 1.0
    nuova[1::2, 1::2] = 1.0
    return nuova

print(scacchiera(4))
r1 = np.array( [ [1.0, 0.0, 1.0, 0.0],
[0.0, 1.0, 0.0, 1.0],
[1.0, 0.0, 1.0, 0.0],
[0.0, 1.0, 0.0, 1.0] ])
assert np.allclose(scacchiera(4), r1)
r2 = np.array( [ [1.0] ])
assert np.allclose(scacchiera(1), r2)
r3 = np.array( [ [1.0, 0.0],
[0.0, 1.0] ])
assert np.allclose(scacchiera(2), r3)

def scacchiera1(n):
    nuova = np.zeros((n,n))
    for y in range(0, len(nuova), 2):
        for x in range(0, len(nuova), 2):
            nuova[y][x] = 1.0
    for y in range(1, len(nuova), 2):
        for x in range(1, len(nuova), 2):
            nuova[y][x] = 1.0
    return nuova

print(scacchiera1(4))
print()

m1 = np.array( [ [1.0, 3.0, 2.0, 5.0],
[2.0, 8.0, 5.0, 9.0],
[6.0, 9.0, 7.0, 2.0],
[4.0, 7.0, 2.0, 4.0] ])
r1 = np.array( [ [1.0, 3.0, 2.0, 5.0],
[3.0, 11.0,7.0, 14.0],
[6.0, 9.0, 7.0, 2.0],
[10.0,16.0,9.0, 6.0] ])


def somma_alterna_pro(mat):
    #mat = np.array(mat)
    mat[1::2] += mat[::2]
    return mat

print(m)
print(somma_alterna_pro(m1))
somma_alterna_pro(m1)
#assert np.allclose(m1, r1) # controlla che abbiamo MODIFICATO la matrice originale
m2 = np.array( [ [5.0] ])
r2 = np.array( [ [5.0] ])
somma_alterna_pro(m1)
assert np.allclose(m2, r2)
m3 = np.array( [ [6.0, 1.0],
[3.0, 2.0] ])
r3 = np.array( [ [6.0, 1.0],
[9.0, 3.0] ])
somma_alterna_pro(m3)
assert np.allclose(m3, r3)
print()

def somma_alterna2(mat):
    for y in range(1, len(mat), 2):
        for x in range(len(mat[0])):
            mat[y][x] += mat[y-1][x]

somma_alterna2(m)
[print(x) for x in m]
print()

m = np.array([[7,9]])

def media_meta(mat):
#SOLUZIONE LENTA
    righe, colonne = mat.shape
    meta_colonne = colonne // 2
    media_sx = 0.0
    media_dx = 0.0
# scrivi qui
    for i in range(righe):
        for j in range(meta_colonne):
            media_sx += mat[i,j]
        for j in range(meta_colonne, colonne):
            media_dx += mat[i,j]
    mezzi_elementi = righe * meta_colonne
    media_sx /= mezzi_elementi
    media_dx /= mezzi_elementi
    return np.array([media_sx, media_dx])

print(media_meta(m))
m1 = np.array([ [7,9] ])
r1 = np.array([(7)/1, (9)/1 ])
assert np.allclose( media_meta(m1), r1)
m2 = np.array([ [3,4],
[6,3],
[5,2] ])
r2 = np.array([(3+6+5)/3, (4+3+2)/3 ])
assert np.allclose( media_meta(m2), r2)
m3 = np.array([ [3,2,1,4],
[6,2,3,5],
[4,3,6,2],
[4,6,5,4],
[7,2,9,3] ])
r3 = np.array([(3+2+6+2+4+3+4+6+7+2)/10, (1+4+3+5+6+2+5+4+9+3)/10 ])
assert np.allclose( media_meta(m3), r3)

def media_meta_pro(mat):
    righe, colonne = mat.shape
    meta_colonne = colonne // 2
    mezzi_elementi = righe * meta_colonne
    media = np.zeros((1,2))
    media[0,0] = np.sum(mat[:, :meta_colonne]) / mezzi_elementi
    media[0,1] = np.sum(mat[:, meta_colonne:]) / mezzi_elementi
    return media

print(media_meta_pro(m))

m1 = np.array([ [7,9] ])
r1 = np.array([(7)/1, (9)/1 ])
assert np.allclose( media_meta_pro(m1), r1)
m2 = np.array([ [3,4],
[6,3],
[5,2] ])
r2 = np.array([(3+6+5)/3, (4+3+2)/3 ])
assert np.allclose( media_meta_pro(m2), r2)
m3 = np.array([ [3,2,1,4],
[6,2,3,5],
[4,3,6,2],
[4,6,5,4],
[7,2,9,3] ])
r3 = np.array([(3+2+6+2+4+3+4+6+7+2)/10, (1+4+3+5+6+2+5+4+9+3)/10 ])
assert np.allclose( media_meta_pro(m3), r3)


def media_meta1(mat):
    righe, colonne = mat.shape
    meta_colonne = colonne // 2
    mediasx = 0
    mediadx = 0

    for y in range(righe):
        for x in range(meta_colonne):
            mediasx += mat[y,x]
        for x in range(meta_colonne, colonne):
            mediadx += mat[y,x]
    
    mezzi_elementi = righe * meta_colonne
    mediasx = mediasx / mezzi_elementi
    mediadx = mediadx / mezzi_elementi
    return np.array([mediasx, mediadx])

print(media_meta1(m))

def media_pro(mat):
    righe, colonne = mat.shape
    meta_colonne = colonne // 2
    mezzi_elementi = righe * meta_colonne
    nuova = np.zeros((1,2))
    nuova[0,0] = np.sum(mat[:, :meta_colonne]) / mezzi_elementi
    nuova[0,1] = np.sum(mat[:, :meta_colonne:]) / mezzi_elementi
    return nuova

print(media_pro(m))

def matxarr(mat, arr):
    nuova = np.zeros((mat.shape))
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            nuova[y,x] = mat[y,x] * arr[x]
    return nuova

m1 = np.array( [ [3,2,1],
[6,2,3],
[4,3,6],
[4,6,5] ] )
a1 = np.array([5, 2, 6])

print(matxarr(m1, a1))
r1 = np.array([ [3*5, 2*2, 1*6],
[6*5, 2*2, 3*6],
[4*5, 3*2, 6*6],
[4*5, 6*2, 5*6] ])
assert np.allclose(matxarr(m1,a1), r1)

def matxarr_pro(mat, arr):
    return np.array(mat) * arr
    #return np.array(arr) * mat

print(matxarr_pro(m1, a1))
print()

m = np.array([[5,4,2],
[8,5,1],
[6,7,9],
[3,6,4],
[4,3,7]])

def colgap2(mat):
    return np.array([max(mat[:,0]) - min(mat[:,0]), max(mat[:,1]) - min(mat[:,1]), max(mat[:,2]) - min(mat[:,2])])

print(colgap2(m))

def colgap(mat):
    nuova = []
    for x in range(len(mat[0])):
        colonna = []
        for y in range(len(mat)):
            colonna.append(mat[y][x])
        grande = max(colonna)
        piccolo = min(colonna)
        nuova.append(grande - piccolo)
    return np.array(nuova)
print(colgap(m))

m1 = np.array([[6]])
assert np.allclose(colgap(m1), np.array([0]))
ret = colgap(m1)
assert type(ret) == np.ndarray
m2 = np.array([[6,8]])
assert np.allclose(colgap(m2), np.array([0,0]))
m3 = np.array([[2],
[5]])
assert np.allclose(colgap(m3), np.array([3]))
m4 = np.array([[5,7],
[2,9]])
assert np.allclose(colgap(m4), np.array([3,2]))
m5 = np.array([[4,7],
[4,9]])
assert np.allclose(colgap(m5), np.array([0,2]))
m6 = np.array([[5,2],
[3,7],
[9,0]])
assert np.allclose(colgap(m6), np.array([6,7]))
m7 = np.array([[5,4,2],
[8,5,1],
[6,7,9],
[3,6,4],
[4,3,7]])
assert np.allclose(colgap(m7), np.array([5,4,8]))

def colgap3(mat):
    mx = mat[0].copy()
    mn = mat[0].copy()
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j] > mx[j]:
                mx[j] = mat[i,j]
            if mat[i,j] < mn[j]:
                mn[j] = mat[i,j]
    return mx - mn

print(colgap3(m))

def colgap_pro(mat):
    mx = np.max(mat, axis = 0)
    mn = np.min(mat, axis = 0)
    return mx - mn

print(colgap_pro(m))

def colgap__(mat):
    mx = np.max(mat, axis = 0)
    mn = np.min(mat, axis = 0)
    return mx - mn

print(colgap__(m))

# TEST
m1 = np.array([[6]])
assert np.allclose(colgap_pro(m1), np.array([0]))
ret = colgap_pro(m1)
assert type(ret) == np.ndarray
m2 = np.array([[6,8]])
assert np.allclose(colgap_pro(m2), np.array([0,0]))
m3 = np.array([[2],
[5]])
assert np.allclose(colgap_pro(m3), np.array([3]))
m4 = np.array([[5,7],
[2,9]])
assert np.allclose(colgap_pro(m4), np.array([3,2]))
m5 = np.array([[4,7],
[4,9]])
assert np.allclose(colgap_pro(m5), np.array([0,2]))
m6 = np.array([[5,2],
[3,7],
[9,0]])
assert np.allclose(colgap_pro(m6), np.array([6,7]))
m7 = np.array([[5,4,2],
[8,5,1],
[6,7,9],
[3,6,4],
[4,3,7]])
assert np.allclose(colgap_pro(m7), np.array([5,4,8]))

import numpy as np

m = np.array([[5,4,2],
[8,5,1],
[6,7,9],
[3,6,4],
[4,3,7]])

def colgap(mat):
    nuova = []
    for x in range(len(mat[0])):
        riga = []
        for y in range(len(mat)):
            riga.append(mat[y,x])
        M = max(riga)
        n = min(riga)
        nuova.append(M-n)
    return np.array(nuova)

print(colgap(m))

def colgap_pro(mat):
    mx = np.max(mat, axis = 0)
    mn = np.min(mat, axis = 0)
    return mx - mn

print(colgap_pro(m))

def colgap2(mat):
    mx = mat[0].copy() # copio la prima lista
    mn = mat[0].copy() # copio la prima lista
    for y in range(mat.shape[0]): #per ogni riga
        for x in range(mat.shape[1]): # per ogni elemento in riga
            if mat[y,x] > mx[x]: # se l'elemento è > di mx alla posizione x
                mx[x] = mat[y,x] # allora mx vale l'elemento
            if mat[y,x] < mn[x]: # se l'elemento è < di mn alla possione x
                mn[x] = mat[y,x] # allora mn vale l'elemento
    return mx - mn # ritorna una lista numpy con la differenza tra mx e mn

print(colgap2(m))

def sostmax(mat):
    #mx = np.max(mat, axis = 0)
    #mat[:] = mx
    mat[:] = np.max(mat, axis = 0)

print(sostmax(m))
m1 = np.array([[6]])
sostmax(m1)
assert np.allclose(m1, np.array([6]))
ret = sostmax(m1)
assert ret == None # non ritorna nulla!
m2 = np.array([[6,8]])
sostmax(m2)
assert np.allclose(m2, np.array([6,8]))
m3 = np.array([[2],
[5]])
sostmax(m3)
assert np.allclose(m3, np.array([[5],
[5]]))
m4 = np.array([[5,7],
[2,9]])
sostmax(m4)
assert np.allclose(m4, np.array([[5,9],
[5,9]]))
m5 = np.array([[4,7],
[4,9]])
sostmax(m5)
assert np.allclose(m5, np.array([[4,9],
[4,9]]))
m6 = np.array([[5,2],
[3,7],
[9,0]])
sostmax(m6)
assert np.allclose(m6, np.array([[9,7],
[9,7],
[9,7]]))
m7 = np.array([[5,4,2],
[8,5,1],
[6,7,9],
[3,6,4],
[4,3,7]])
sostmax(m7)
assert np.allclose(m7, np.array([[8, 7, 9],
[8, 7, 9],
[8, 7, 9],
[8, 7, 9],
[8, 7, 9]]))


def sostmax1(mat):
    nuova = []
    for x in range(len(mat[0])):
        riga = []
        for y in range(len(mat)):
            riga.append(mat[y][x])
        nuova.append(max(riga))
    
    for x in range(len(mat[0])):
        for y in range(len(mat)):
            mat[y][x] = nuova[x]

print(sostmax1(m))
print(m)

m = np.array( [ [1.0, 2.0 , 5.0 , 7.0],
[4.0, 1.0 , 8.0 , 0.0],
[2.0, 0.0 , 5.0 , 1.0],
[0.0, 2.0 , 1.0 , 1.0] ])

def quadranti_pro(mat):
    n = mat.shape[0] // 2
    nuova = np.zeros((2,2))
    nuova[0,0] = np.sum(mat[:n, :n]) / (n*n)
    nuova[0,1] = np.sum(mat[:n, n:]) / (n*n)
    nuova[1,1] = np.sum(mat[n:, n:]) / (n*n)
    nuova[1,0] = np.sum(mat[n:, :n]) / (n*n)
    return nuova

print(quadranti_pro(m))

m1 = np.array( [ [3.0, 5.0],
[4.0, 9.0] ])
r1 = np.array([ [3.0, 5.0],
[4.0, 9.0],
])
assert np.allclose(quadranti_pro(m1),r1)
m2 = np.array( [ [1.0, 2.0 , 5.0 , 7.0],
[4.0, 1.0 , 8.0 , 0.0],
[2.0, 0.0 , 5.0 , 1.0],
[0.0, 2.0 , 1.0 , 1.0] ])
r2 = np.array( [ [2.0, 5.0],
[1.0, 2.0] ] )
assert np.allclose(quadranti_pro(m2),r2)

def quadranti(mat):
    n = len(mat) // 2
    m = n*n
    nuova = []
    zeze = []
    zeun = []
    unze = []
    unun = []
    for y in range(n):
        for x in range(n):
            zeze.append(mat[y][x])
        for x in range(n):
            zeun.append(mat[y][x+n])
    for y in range(n, n+n):
        for x in range(n):
            unze.append(mat[y][x])
        for x in range(n):
            unun.append(mat[y][x+n])
    riga = [sum(zeze)/m, sum(zeun)/m]
    riga1 = [sum(unze)/m, sum(unun)/m]
    nuova.append(riga)
    nuova.append(riga1)
    return nuova

print(quadranti(m))

m1 = np.array( [ [3.0, 5.0],
[4.0, 9.0] ])
r1 = np.array([ [3.0, 5.0],
[4.0, 9.0],
])
assert np.allclose(quadranti(m1),r1)
m2 = np.array( [ [1.0, 2.0 , 5.0 , 7.0],
[4.0, 1.0 , 8.0 , 0.0],
[2.0, 0.0 , 5.0 , 1.0],
[0.0, 2.0 , 1.0 , 1.0] ])
r2 = np.array( [ [2.0, 5.0],
[1.0, 2.0] ] )
assert np.allclose(quadranti(m2),r2)
print()

def scendisali_pro(n,m):
    if m % 2 != 0:
        raise ValueError
    nuova = np.zeros((n,m))
    nuova[1::2, :m//2] = np.arange(0,m//2)
    nuova[::2, m//2:] = np.arange(m//2-1,-1,-1)
    return nuova

print(scendisali_pro(6,10))

assert np.allclose(scendisali_pro(2,2), np.array([[0., 0.],
[0., 0.]]))
assert type(scendisali_pro(2,2)) == np.ndarray
assert np.allclose(scendisali_pro(2,6), np.array([[0., 0., 0., 2., 1., 0.],
[0., 1., 2., 0., 0., 0.]]))
assert np.allclose(scendisali_pro(6,10), np.array([[0., 0., 0., 0., 0., 4., 3., 2., 1., 0.],
[0., 1., 2., 3., 4., 0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0., 4., 3., 2., 1., 0.],
[0., 1., 2., 3., 4., 0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0., 4., 3., 2., 1., 0.],
[0., 1., 2., 3., 4., 0., 0., 0., 0., 0.]]))
try:
    scendisali_pro(2,3)
    raise Exception("Avrei dovuto fallire prima!")
except ValueError:
    pass
print()

def scendisali(n,m):
    if m % 2 != 0:
        raise ValueError
    mat = np.zeros((n,m))
    for y in range(0,len(mat),2):
        for x in range(len(mat[0])//2):
            mat[y][x + len(mat[0])//2] = len(mat[0])//2 - x -1
    for y in range(1,len(mat),2):
       for x in range(len(mat[0])//2):
            mat[y][x] = x
    return mat

print(scendisali(6,10))
assert np.allclose(scendisali(2,2), np.array([[0., 0.],
[0., 0.]]))
assert type(scendisali(2,2)) == np.ndarray
assert np.allclose(scendisali(2,6), np.array([[0., 0., 0., 2., 1., 0.],
[0., 1., 2., 0., 0., 0.]]))

import numpy as np

def scendisali(n,m):
    nuova = np.zeros((n,m))
    for y in range(0,n,2):
        for x in range(m//(2)):
            nuova[y][x+m//2] = m//2 -x -1
    for y in range(1,n,2):
        for x in range(m//2):
            nuova[y][x] = x
    return nuova

print(scendisali(6,10))
assert np.allclose(scendisali(2,2), np.array([[0., 0.],
[0., 0.]]))
assert type(scendisali(2,2)) == np.ndarray
assert np.allclose(scendisali(2,6), np.array([[0., 0., 0., 2., 1., 0.],
[0., 1., 2., 0., 0., 0.]]))

def scendisali_pro(n,m):
    if m % 2 != 0:
        raise ValueError
    nuova = np.zeros((n,m))
    nuova[0::2, m//2:] = np.arange(m//2-1, -1, -1)
    nuova[1::2, :m//2] = np.arange(0,m//2)
    return nuova

print(scendisali_pro(6,10))
assert np.allclose(scendisali_pro(2,2), np.array([[0., 0.],
[0., 0.]]))
assert type(scendisali_pro(2,2)) == np.ndarray
assert np.allclose(scendisali_pro(2,6), np.array([[0., 0., 0., 2., 1., 0.],
[0., 1., 2., 0., 0., 0.]]))
try:
    scendisali_pro(2,3)
    raise Exception("Avrei dovuto fallire prima!")
except ValueError:
    pass
print()


def gradini(mat):
    if len(mat) != len(mat[0]):
        raise ValueError
    n = len(mat)
    nuova = np.zeros(n+n-1)
    for y in range(n):
        nuova[2*y] = mat[y,y]
    
    for y in range(n-1):
        nuova[2*y+1] = mat[y, y+1]

    return nuova

print(gradini(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))

def gradini2(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = []
    for y in range(n):
        nuova.append(mat[y][y])
        try:
            nuova.append(mat[y][y+1])
        except:
            pass
    return nuova

print(gradini2(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))

def gradini3(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = np.zeros(n+n-1)
    for y in range(n):
        nuova[y*2] = mat[y][y]
        try:
            nuova[y*2+1] = mat[y][y+1]
        except:
            pass
    return nuova

print(gradini3(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))

def gradini_pro(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = np.zeros(n+n-1)
    nuova[::2] = np.diag(mat)
    nuova[1::2] = np.diag(mat,1)
    return nuova

print(gradini_pro(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))

def gradini4(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    
    res = np.zeros(n+n-1)
    for i in range(n):
        res[2*i] = mat[i,i]
    
    for i in range(n-1):
        res[2*i+1] = mat[i, i+1]
    
    return res

def gradini_pro2(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    a = np.diag(mat)
    b = np.diag(mat,1)
    ret = np.zeros((1, a.shape[0] + b.shape[0]))
    ret[:, ::2] = a
    ret[:, 1::2] = b
    return ret

print(gradini_pro2(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] )))
print()

def gradini5(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = np.zeros(n+n-1)
    for y in range(n):
        nuova[y*2] = mat[y][y]
    for y in range(n-1):
        nuova[y*2+1] = mat[y][y+1]
    return nuova

print(gradini5(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] ))
)

def gradini_pro3(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    nuova = np.zeros(n+n-1)
    nuova[::2] = np.diag(mat)
    nuova[1::2] = np.diag(mat, 1)
    return nuova

print(gradini_pro3(np.array([ [6,3,5,2,5],
[3,4,2,3,4],
[6,5,4,5,1],
[4,3,2,3,9],
[2,5,1,6,7] ] ))
)
print()

def scalivert(n,m):
    nuova = np.zeros((n,m))
    for x in range(0,len(nuova[0]), 2):
        for y in range(len(nuova)):
            nuova[y][x] = y+1
    for x in range(1,len(nuova[0]), 2):
        for y in range(len(nuova)):
            nuova[y][x] = n-y
    return nuova

print(scalivert(4,4))
assert np.allclose(scalivert(1,1), np.array([ [1] ]))
assert np.allclose(scalivert(1,2), np.array([ [1,1] ]))
assert np.allclose(scalivert(2,1), np.array([ [1],
[2]]))
assert np.allclose(scalivert(2,2), np.array([ [1,2],
[2,1]]))
assert type(scalivert(2,2)) == np.ndarray
assert np.allclose(scalivert(4,5), np.array([ [1,4,1,4,1],
[2,3,2,3,2],
[3,2,3,2,3],
[4,1,4,1,4]]))

def scalivert1(n,m):
    nuova = np.zeros((n,m))
    for y in range(n):
        for x in range(m):
            if x % 2 == 0:
                nuova[y][x] = y + 1
            else:
                nuova[y][x] = n - y
    return nuova

print(scalivert1(5,5))

def scalivert_pro(n,m):
    nuova = np.zeros((n,m))
    nuova[:, ::2] = np.transpose([np.arange(1,n+1,1)])
    nuova[:, 1::2] = np.transpose([np.arange(n,0,-1)])
    return nuova

print(scalivert_pro(5,5))

def sclivert2(n,m):
    nuova = np.zeros((n,m))
    for y in range(n):
        for x in range(m):
            if x % 2 == 0:
                nuova[y][x] = y + 1
            else:
                nuova[y][x] = n - y
    return nuova

print(sclivert2(5,5))

def scalivert_pro1(n,m):
    nuova = np.zeros((n,m))
    nuova[:, ::2] = np.transpose([np.arange(1,n+1)])
    nuova[:, 1::2] = np.transpose([np.arange(n,0,-1)])
    return nuova

print(scalivert_pro1(5,5))

def sclivert_pro2(n,m):
    nuova = np.zeros((n,m))#, dtype=int)
    nuova[:, ::2] = np.tile(np.transpose([np.arange(1, n+1)]), (m+1) // 2)
    nuova[:, 1::2] = np.tile(np.transpose([np.arange(n,0,-1)]), m//2)
    return nuova

print(sclivert_pro2(5,5))

assert np.allclose(scalivert_pro(1,1), np.array([ [1] ]))
assert np.allclose(scalivert_pro(1,2), np.array([ [1,1] ]))
assert np.allclose(scalivert_pro(2,1), np.array([ [1],
[2]]))
assert np.allclose(scalivert_pro(2,2), np.array([ [1,2],
[2,1]]))
assert type(scalivert_pro(2,2)) == np.ndarray
assert np.allclose(scalivert_pro(4,5), np.array([ [1,4,1,4,1],
[2,3,2,3,2],
[3,2,3,2,3],
[4,1,4,1,4]]))
print()

def sclivert_pro3(n,m):
    nuova = np.zeros((n,m))#, dtype=int)
    nuova[::2] = np.arange(1, n+1)
    nuova[1::2] = np.arange(n,0,-1)
    return nuova

print(sclivert_pro3(5,5))
print()

def compricol(mat):
    n,m = mat.shape
    if m % 2 != 0:
        raise ValueError
    
    nuova = np.zeros((n, m//2))
    for y in range(n):
        for x in range(0, m, 2):
            nuova[y][x//2] = mat[y][x] + mat[y][x+1]
    return nuova

m = np.array([[5,4,2,6,4,2],
[7,5,1,0,6,1],
[6,7,9,2,3,7],
[5,2,4,6,1,3],
[7,2,3,4,2,5]])

print(compricol(m))
m1 = [[7,9]]
res = compricol(np.array(m1))
assert type(res) == np.ndarray
assert np.allclose(res, np.array([[16]]))
m2 = np.array([[5,8],
[7,2]])
assert np.allclose(compricol(m2), np.array([[13],
[9]]))
assert np.allclose(m2, np.array([[5,8],
[7,2]])) # non cambia la matrice originale
m3 = np.array([[5,4,2,6,4,2],
[7,5,1,0,6,1],
[6,7,9,2,3,7],
[5,2,4,6,1,3],
[7,2,3,4,2,5]])
assert np.allclose(compricol(m3), np.array([[ 9, 8, 6],
[12, 1, 7],
[13,11,10],
[ 7,10, 4],
[ 9, 7, 7]]))
try:
    compricol(np.array([[7,1,6],[5,2,4]]))
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass

def compricol1(mat):
    n,m = mat.shape
    if m % 2 != 0:
        raise ValueError
    
    nuova = np.zeros((n,m//2))
    nuova[:,:] = mat[:,::2] + mat[:, 1::2]
    return nuova

m = np.array([[5,4,2,6,4,2],
[7,5,1,0,6,1],
[6,7,9,2,3,7],
[5,2,4,6,1,3],
[7,2,3,4,2,5]])
print(compricol1(m))

def compricol2(mat):
    n,m = mat.shape
    if m % 2 != 0:
        raise ValueError
    
    nuova = mat[:, ::2].copy()
    nuova += mat[:, 1::2]
    return nuova

m = np.array([[5,4,2,6,4,2],
[7,5,1,0,6,1],
[6,7,9,2,3,7],
[5,2,4,6,1,3],
[7,2,3,4,2,5]])
print(compricol2(m))
print()

m = np.array([ [5,4,2,6,4],
[3,5,1,0,6],
[6,4,9,2,3],
[5,2,8,6,1],
[7,9,3,2,2] ])

def revtriang(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    
    nuova = mat.copy()
    for y in range(1,n):
        nuova[y,:y] = np.flip(mat[y,:y])
    return nuova
    

print(revtriang(m))
print()

def revtriang2(mat):
    n,m = mat.shape

    if n != m:
        raise ValueError
    
    nuova = mat.copy()
    for y in range(n):
        nuova[y,:y] = np.flip(mat[y,:y])
    return nuova

print(m)
print(revtriang2(m))
print()

def revtriang3(mat):
    n,m = mat.shape
    if n != m:
        raise ValueError
    
    nuova = mat.copy()

    for y in range(1,n):
        riga = []
        for x in range(y):
            riga.append(nuova[y][x])
        riga.reverse()
        for x in range(y):
            nuova[y][x] = riga[x]

    return nuova
print(m)
print(revtriang3(m))
            
m1 = np.array([[8]])
assert np.allclose(revtriang3(m1), np.array([[8]]))
m3 = np.array([[1,5],
[9,6]])
assert np.allclose(revtriang3(m3), np.array([[1,5],
[9,6]]))
m4 = np.array([[1,5,8],
[9,6,2],
[3,2,5]])
assert np.allclose(revtriang3(m4), np.array([[1,5,8],
[9,6,2],
[2,3,5]]))
assert np.allclose(m4, np.array([[1,5,8],
[9,6,2],
[3,2,5]])) # non cambia l'originale
m5 = np.array([[5,4,2,6,4],
[3,5,1,0,6],
[6,4,9,2,3],
[5,2,8,6,1],
[7,9,3,2,2]])
assert np.allclose(revtriang3(m5), np.array([[5, 4, 2, 6, 4],
[3, 5, 1, 0, 6],
[4, 6, 9, 2, 3],
[8, 2, 5, 6, 1],
[2, 3, 9, 7, 2]]))
try:
    revtriang3(np.array([[7,1,6],[5,2,4]]))
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass
print()

def camminas(mat):
    n,m = mat.shape
    return np.concatenate((mat[-1, :m//2], np.flip(mat[:,m//2]), mat[0, m//2+1:]))

m = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])

print(camminas(m))

def camminas1(mat):
    n,m = mat.shape
    nuova = np.zeros(n+m-1)
    nuova[:m//2] = mat[-1,:m//2]
    nuova[m//2:m//2+n] = mat[::-1,m//2]
    nuova[-m//2:] = mat[0,m//2:]
    return nuova

m = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])

print(camminas1(m))

m1 = np.array([[7]])
assert np.allclose(camminas(m1), np.array([7]))
m2 = np.array([[7,5,2]])
assert np.allclose(camminas(m2), np.array([7,5,2]))
m3 = np.array([[9,3,5,6,0]])
assert np.allclose(camminas(m3), np.array([9,3,5,6,0]))
m4 = np.array([[7,5,2],
[9,3,4]])
assert np.allclose(camminas(m4), np.array([9,3,5,2]))
m5 = np.array([[7,4,6],
[8,2,1],
[0,5,3]])
assert np.allclose(camminas(m5), np.array([0,5,2,4,6]))
m6 = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
assert np.allclose(camminas(m6), np.array([4,3,8,5,2,7,3,8,4,6,5,7]))
print()

def camminas2(mat):
    n,m = mat.shape
    lista = []
    for y in range(n):
        if y == 0:
            for x in range(1,m//2+1):
                lista.append(mat[y][-x])
        if y != 0 and y != n:
            for x in range(1):
                lista.append(mat[y][m//2])
        if y == n-1:
            riga = []
            for x in range(m//2):
                riga.append(mat[y][x])
            riga.reverse()
            [lista.append(x) for x in riga]
    lista.reverse()
    return np.array(lista)

m = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
print(camminas2(m))
print()

def camminaz(mat):
    n,m = mat.shape
    return np.flip(np.concatenate((mat[0,:m//2], mat[:,m//2], mat[-1, m//2+1:])))

m = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
print(camminaz(m))
m1 = np.array([[7]])
assert np.allclose(camminaz(m1), np.array([7]))
m2 = np.array([[7,5,2]])
assert np.allclose(camminaz(m2), np.array([2,5,7]))
m3 = np.array([[9,3,5,6,0]])
assert np.allclose(camminaz(m3), np.array([0,6,5,3,9]))
m4 = np.array([[7,5,2],
[9,3,4]])
assert np.allclose(camminaz(m4), np.array([4,3,5,7]))
m5 = np.array([[7,4,6],
[8,2,1],
[0,5,3]])
assert np.allclose(camminaz(m5), np.array([3,5,2,4,7]))
m6 = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
assert np.allclose(camminaz(m6), np.array([5,1,6,5,2,7,3,8,4,2,8,5]))

def camminaz1(mat):
    n,m = mat.shape
    nuova = np.zeros(n+m-1)
    nuova[:m//2] = mat[0,:m//2]
    nuova[m//2:m//2+n] = mat[:,m//2]
    nuova[m//2+n:] = mat[-1,m//2+1:]
    return np.flip(nuova)
#importanti
print(camminaz1(m))

def camminaz2(mat):
    n,m = mat.shape
    lista = []
    for y in range(n):
        if y == 0:
            for x in range(m//2+1):
                lista.append(mat[y][x])
        if y != 0 and y != n:
            for x in range(1):
                lista.append(mat[y][m//2])
        if y == n-1:
            riga = []
            for x in range(1,m//2+1):
                riga.append(mat[y][-x])
            riga.reverse()
            [lista.append(x) for x in riga]
    lista.reverse()
    return np.array(lista)

print(camminaz2(m))
print()

def camminaz3(mat):
    n,m = mat.shape
    nuova = np.zeros(n+m-1)
    nuova[:m//2] = mat[-1, -1:-m//2:-1]
    nuova[m//2:m//2+n] = mat[-1::-1, m//2]
    nuova[m//2+n:] = mat[0, m//2-1::-1]
    return nuova

print(camminaz3(m))
m1 = np.array([[7]])
assert np.allclose(camminaz3(m1), np.array([7]))
m2 = np.array([[7,5,2]])
assert np.allclose(camminaz3(m2), np.array([2,5,7]))
m3 = np.array([[9,3,5,6,0]])
assert np.allclose(camminaz3(m3), np.array([0,6,5,3,9]))
m4 = np.array([[7,5,2],
[9,3,4]])
assert np.allclose(camminaz3(m4), np.array([4,3,5,7]))
m5 = np.array([[7,4,6],
[8,2,1],
[0,5,3]])
assert np.allclose(camminaz3(m5), np.array([3,5,2,4,7]))
m6 = np.array([[5,8,2,4,6,5,7],
[7,9,5,8,3,2,2],
[6,1,8,3,6,6,1],
[1,5,3,7,9,4,7],
[1,5,3,2,9,5,4],
[4,3,8,5,6,1,5]])
assert np.allclose(camminaz3(m6), np.array([5,1,6,5,2,7,3,8,4,2,8,5]))
print()

import numpy as np

m = np.array(
    [
        # Gilberto Rocky Clelia
            [5.0,   8.0,  1.0], # Thè
            [7.0,   3.0,  2.0], # Caffè
            [9.0,   2.0,  8.0] # Ginseng
    ]
)

def macchina(mat):
    spesa_ognuno = np.sum(mat[:], axis = 0)
    spesa_x_tipo = np.sum(mat[:], axis = 1)
    #nomi = 'Gilberto Rocky Clelia'.split()
    print('Spesa di ciascuno:')
    print('         Gilberto Rocky Clelia')
    print('         ', spesa_ognuno)
    print('Spesa per tipo:')
    print('         The Caffè Ginseng')
    print('         ', spesa_x_tipo)
    print('Dei tre ha speso di più il numero:', [np.argmax(spesa_ognuno)])# np.where(spesa_ognuno == np.max(spesa_ognuno))
    print('La bevanda preferita è la numero:', [np.argmax(spesa_x_tipo)])

macchina(m)
print()

mat = np.array([[1,0,0,0,0,1,1,0],
[1,1,1,0,1,1,0,0],
[1,0,1,0,1,0,0,1],
[1,1,0,0,0,1,1,0],
[0,1,0,1,1,1,1,0],
[0,0,1,1,0,0,1,1]])
#importante
def pareggio(mat):
    return np.reshape(np.sum(mat, axis = 1) == len(mat[0]) // 2, (len(mat),1))

print(pareggio(mat))
print(type(pareggio(mat)))
print()

m1 = np.array([[0,0]])
res = pareggio(m1)
print(res) # strano qua stampa float, mentre in pareggio_pro dei boolean
assert type(res) == np.ndarray
assert np.allclose(res, np.array([ [False] ]))
m2 = np.array([[1,0]])
assert np.allclose(pareggio(m2), np.array([ [True] ]))
m3 = np.array([[0,1]])
assert np.allclose(pareggio(m3), np.array([ [True] ]))
m4 = np.array([[1,1]]) # True
assert np.allclose(pareggio(m4), np.array([ [False] ]))
m5 = np.array([[1,1],
[0,1]])
assert np.allclose(pareggio(m5), np.array([ [False],
[True] ]))
m6 = np.array([[0,1],
[1,0]])
assert np.allclose(pareggio(m6), np.array([ [True],
[True] ]))
m7 = np.array([[1,1,0,0],
[1,1,0,1],
[1,0,0,1]])
assert np.allclose(pareggio(m7), np.array([ [True],
[False],
[True] ]))
m8 = np.array([[1,0,0,0,0,1,1,0],
[1,1,1,0,1,1,0,0],
[1,0,1,0,1,0,0,1],
[1,1,0,0,0,1,1,0],
[0,1,0,1,1,1,1,0],
[0,0,1,1,0,0,1,1]])
assert np.allclose(pareggio(m8), np.array([ [False],
[False],
[ True],
[ True],
[False],
[ True] ]))
print()

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
#print(ordina_file('quartiere1.txt'))
#pprint(ordina_file('quartiere1.txt'), depth=2)
#[print(x) for x in ordina_file('quartiere1.txt')]

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
import html
def sistema_file(file):
    with open(file, encoding='utf-8') as f:
        titoli = []
        spazi = []
        valori = []
        completa = []
        for riga in f:
            riga = riga.strip()
            riga_divisa = riga.split(':')
            if riga_divisa[0].endswith('Title'):
                titoli.append(riga_divisa[1])
            elif riga_divisa[0].endswith('Level'):
                spazi.append(riga_divisa[1])
            elif riga_divisa[0].endswith('Number'):
                valori.append(riga_divisa[1])
        for y in range(len(titoli)):
            if (int(spazi[y])-1)*'\t' == '':
                print(html.unescape(titoli[y][1:]), valori[y][1:])
            else:
                print((int(spazi[y])-1)*'\t', html.unescape(titoli[y][1:]), valori[y][1:])
    #print(html.unescape('ieri sono andato &#232;'))
        #return completa
#print(0*' ' +'c')
sistema_file('immersione-in-python-toc.txt')
print()

with open('immersione-in-python-toc.txt') as f:
    linea = f.readline()
    while linea != '':
        linea = f.readline().strip()
        titolo = html.unescape(linea[len('BookmarkTitle: '):])
        linea = f.readline().rstrip()
        livello = int(linea[len('BookmarkLevel: '):])
        linea = f.readline().rstrip()
        pagina = linea[len('BookmarkPageNumber: '):]
        print(('    ' * livello) + titolo + ' ' + pagina)
        linea = f.readline()
print()

import csv
with open('esempio-1.csv', encoding='utf-8') as f:
    #creiamo un oggetto 'lettore' che pescherà righe dal file
    lettore = csv.reader(f, delimiter=',')
    for riga in lettore:
        print('Abbiamo appenaletto una riga!')
        print(riga) #stamperà la variabile 'riga', che è una lista di stringhe
        print('') #stampa una stringa vuota, per separare in verticale
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    for riga in lettore:
        print(riga)


with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    for riga in lettore:
        print('Abbiamo appena letto una riga!')
        print(riga)
        print('')
print()


with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    listona = []
    for riga in lettore:
        listona.append(riga)
    pprint(listona)
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    listona = []
    for riga in lettore:
        mini = []
        mini.append(riga[0])
        mini.append(int(riga[1]))
        listona.append(mini)
    pprint(listona)
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    listona = []
    for riga in lettore:
        listona.append([riga[0], int(riga[1])])
    pprint(listona)
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    print(list(lettore))
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    pprint([ x for x in lettore])
print()


import itertools
with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    pprint([[riga[0], int(riga[1]), riga[2]] for riga in itertools.islice(lettore, 1, None)])
print()

with open('esempio-1.csv', encoding='utf-8') as f:
    lettore = csv.DictReader(f, delimiter= ',')
    for diz in lettore:
        print(diz)
print()
with open('file-scritto.csv', 'w', newline= '') as f: 
    scrittore = csv.writer(f, delimiter=',')
    scrittore.writerow(['This', 'is', 'a header'])
    scrittore.writerow(['some', 'example', 'data'])
    scrittore.writerow(['some', 'other', 'example data'])
print()

with open('esempio-1-arricchito.csv', 'w', encoding='utf-8', newline='') as csv_da_scrivere:
    scrittore = csv.writer(csv_da_scrivere, delimiter=',')
    with open('esempio-1.csv', encoding='utf-8', newline='') as csv_da_leggere:
        lettore = csv.reader(csv_da_leggere, delimiter=',')
        for riga in lettore:
            riga.append('qualco\'altro')
            scrittore.writerow(riga)
            scrittore.writerow(riga)
            scrittore.writerow(riga)
print()
with open('esempio-1-arricchito.csv', 'r', encoding='utf-8', newline='') as f:
    lettore = csv.reader(f, delimiter=',')
    for riga in lettore:
        print(riga)
print()
#importante
with open('impianti-bifuni.csv', encoding='utf-8', newline='') as f:
    lettore = csv.reader(f, delimiter=',')
    prima_riga = f.readline().strip().split(',')
    for x in prima_riga:
        print(x + ':', prima_riga.index(x))
    print()
    for riga in lettore:
        print('Abbiamo appena letto una riga!')
        print(riga)
        print('')
print()

with open('impianti-bifuni.csv', 'r', encoding='utf-8', newline='') as f:
    prima = f.readline()
    lista_dopp = []
    #next(f)
    for riga in f:
        lista_dopp.append(riga.strip().split(',')[2])

    lista = list(dict.fromkeys(lista_dopp))
    print(lista)
print()

with open('impianti-bifuni.csv', 'r', encoding='utf-8', newline='') as f:
    lettore = csv.reader(f, delimiter=',')
    comuni = set()
    for riga in itertools.islice(lettore, 1, None):
        comuni.add(riga[2])
    print(comuni)
print()

with open('impianti-bifuni.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    comuni = set()
    for riga in lettore:
        comuni.add(riga[2])
    print(comuni)
print()

with open('impianti-bifuni.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    diz = {}
    next(lettore)
    for riga in lettore:
        if riga[-1] in diz:
            diz[riga[-1]] += 1
        else:
            diz[riga[-1]] = 1
    print(diz)
print()

with open('impianti-bifuni.csv', encoding='utf-8', newline = '') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    for riga in lettore:
        if 'si (frane)' in riga[11]:
            riga[11] = 'si + frane'
        print(riga)

with open('impianti-bifuni.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    next(lettore)
    for riga in lettore:
        if '#' in riga[11]:
            riga[11] = None
        print(riga)

import csv
with open('impianti-bifuni.csv', encoding='utf-8', newline='') as f:
    lettore = csv.reader(f, delimiter=',')
    with open('impianti-bifuni-sistemato.csv', 'w', encoding='utf-8', newline='')  as f1:
        scrittore = csv.writer(f1, delimiter=',')
        for riga in lettore:
            if '#' in riga[11]:
                riga[11] = 'Non disponibile'
            elif riga[11] == 'si (frane)':
                riga[11] = 'si + frane'
            scrittore.writerow(riga)
print()
print('scrittura completata')
print()

from pprint import pprint
def selcir(lista):
    with open('strutture-comune-trento.csv', encoding='utf-8', newline='') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        nuova = []
        for riga in lettore:
            for el in lista:
                if el in riga[16].lower():
                    nuova.append([riga[3], riga[16]])
        print('Trovati', len(nuova), 'risultati')
        return nuova

pprint(selcir(['argentario', 'gardolo']))
print()

def selcir1(filtro):
    with open('strutture-comune-trento.csv', encoding='utf-8', newline='') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        ret = []
        for riga in lettore:
            nome = riga[3]
            circoscrizione = riga[16]

            tieni = False
            for el in filtro:
                if el.lower() in circoscrizione.lower():
                    tieni = True
            if tieni:
                ret.append([nome, circoscrizione])
        print('Trovati', len(ret), 'risultati')
        return ret
    
pprint(selcir1(['argentario', 'gardolo', 'RAVINA']))
print()

def cercat(file):
    with open(file, encoding='latin-1', newline='') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        nuova = []
        for riga in lettore:
            for el in riga[3].split('-'):
                if el.strip() != '':
                    nuova.append(el.strip())
        nuova1 = list(dict.fromkeys(nuova))
        return sorted(nuova1)

risultato = cercat('punti-interesse.csv')
#print('ristorante'.split('-'))
atteso = ['Affitta Camere', 'Agriturismo', 'Alimentari', 'Appartamento Vacanze',
'Autostazione', 'Banca', 'Bancomat', 'Bar', 'Bed & Breakfast', 'Biblioteca',
'Birreria', 'Bus Navetta', 'Cambiovaluta', 'Camping', 'Centro Wellness',
'Centro commerciale', 'Corrieri', 'Discoteca', 'Editoria', 'Farmacia','Funivia',
'Gelateria', 'Grande magazzino', 'Hotel', 'Istituzioni', 'Mercatini','Mercato',
'Monumento', 'Museo', 'Noleggio Sci', 'Numeri utili', 'Parcheggio','Pasticceria',
'Piscina', 'Posta', 'Prodotti tipici', 'Pub', 'Residence', 'Rifugio','Ristorante',
'Scuola Sci', 'Sede Trentino Trasporti', 'Snow Park', 'Souvenir', 'Sport','Stadio',
'Stadio del ghiaccio', 'Stazione dei Treni', 'Taxi', 'Teatro', 'Ufficio,informazioni turistiche']
#TEST
print()
for i in range(len(atteso)):
    if risultato[i] != atteso[i]:
        print("ERRORE ALL'ELEMENTO %s:" % i)
        print(' ATTESO:', atteso[i])
        print(' TROVATO:', risultato[i])
        break
print()

def cercat1(file):
    with open(file, encoding='latin-1', newline='') as f:
        lettore = csv.reader(f, delimiter=',')
        next(lettore)
        ret = set()
        for riga in lettore:
            for el in riga[3].split('-'):
                if el.strip() != '':
                    ret.add(el.strip())
        return sorted(ret)

risultato1 = cercat1('punti-interesse.csv')

atteso = ['Affitta Camere', 'Agriturismo', 'Alimentari', 'Appartamento Vacanze',
'Autostazione', 'Banca', 'Bancomat', 'Bar', 'Bed & Breakfast', 'Biblioteca',
'Birreria', 'Bus Navetta', 'Cambiovaluta', 'Camping', 'Centro Wellness',
'Centro commerciale', 'Corrieri', 'Discoteca', 'Editoria', 'Farmacia','Funivia',
'Gelateria', 'Grande magazzino', 'Hotel', 'Istituzioni', 'Mercatini','Mercato',
'Monumento', 'Museo', 'Noleggio Sci', 'Numeri utili', 'Parcheggio','Pasticceria',
'Piscina', 'Posta', 'Prodotti tipici', 'Pub', 'Residence', 'Rifugio','Ristorante',
'Scuola Sci', 'Sede Trentino Trasporti', 'Snow Park', 'Souvenir', 'Sport','Stadio',
'Stadio del ghiaccio', 'Stazione dei Treni', 'Taxi', 'Teatro', 'Ufficio,informazioni turistiche']
#TEST
print()
for i in range(len(atteso)):
    if risultato1[i] != atteso[i]:
        print("ERRORE ALL'ELEMENTO %s:" % i)
        print(' ATTESO:', atteso[i])
        print(' TROVATO:', risultato1[i])
        break
print()
#importante
import json

with open('bike-sharing-lavis.json', encoding='utf-8') as f:
    contenuto_python = json.load(f)
    print(contenuto_python)
    print()
    for riga in contenuto_python:
        print(riga)
    print()
    print(type(contenuto_python))
    print()
    for riga in contenuto_python:
        print(type(riga))
    print()
    print(contenuto_python[0])
    print()
    print(contenuto_python[0]['address'])
    print()
    print(contenuto_python[0]['position'])
    print()
    for riga in contenuto_python[0]:
        print(riga)
print()

with open('impiegati.jsonl', encoding='utf-8') as f:
    lista_testi_json = list(f)
    print(lista_testi_json)
    print()
    i = 0
    for testo_json in lista_testi_json:
        print(type(testo_json))
        contenuto_python = json.loads(testo_json)
        print('Oggetto ', i)
        print(contenuto_python)
        i = i + 1
print()

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

rows = 4
k = 2 * rows -2
for i in range(0, rows):
    for j in range(0,k):
        print(end=" ")
    k = k-2
    for j in range(0, i+1):
        print(" * ", end=" ")
    print(" ")


import csv

#importante github

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
#importante github

#%matplotlib inline
#import matplotlib_inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,11,1.)
print(x)
y = 2*x + 10
print(y)
print(plt.plot(x, y, 'bo'))
print(plt.title('Performance Attesa Esame Fisica'))
print(plt.xlabel('Esercizi svolti'))
print(plt.ylabel('Votazione esame'))
plt.show()

x = np.arange(0, 11, 1.)
#x = np.array(list(range(11)))
y = 2*x + 10
print(y)
g = 'nutella'
plt.plot(x,y, 'r^', label=g)
plt.legend(loc = 'upper left')
#plt.plot(y, x, 'g+') 
#plt.plot( x-1, y-1, 'bH')
#plt.plot(x*3, y*2, 'b^')
print(type(np.arange(0, 11, 1.)))
#help(plt.plot)
plt.show()

x = np.arange(0,11,1.)
y = 2*x + 10

plt.plot(x, y, 'r-')
print(plt.title('Performance Attesa Esame Fisica'))
print(plt.xlabel('Esercizi svolti'))
print(plt.ylabel('Votazione esame'))
plt.annotate(
    'Risultato minimo\nper la sufficienza', xy =(4, 9*2), arrowprops={'arrowstyle':'->'}, xytext=(6, 17.2) )
plt.grid()
plt.show()

x = np.arange(0,11, 1.)
y = 2*x +10
plt.grid()
plt.plot(x,y,'r-')
plt.axis([0, 10, 0, 30])
plt.annotate('risultato minimo\nper la sufficienza',
             xy = (4, 18), arrowprops={'arrowstyle':'->'}, xytext=(6,17.2))

plt.title('Performance attesa esame Fisica')
plt.xlabel('Esercizi svolti')
plt.ylabel('Votazione esame')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
xs = np.array(list(range(1,7)))
ys = list(range(2,13,2))
plt.plot(xs, ys, 'ro')
plt.title('La mai funzione')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(xs, list('abcdef'))
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10

fig = plt.figure(figsize=(10,2))
ax = fig.add_subplot(111)#, projection = '3d')
ax.plot(x,y, 'o')
ax.set_title('Performance attesa Esame Fisica')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')
plt.tight_layout()
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(x, y, 'o')
ax.set_title('Performance attesa Esame Fisica')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Votazione esame')
plt.tight_layout()
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10
fig = plt.figure()
ax = fig.add_subplot(121)
ax.plot(x, y,'bo')
ax.set_title('Grafico a sinistra')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(122)
ax.plot(x, -y, 'bo')
ax.set_title('Grafico a destra')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')
plt.tight_layout()
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y,'r-')
ax.set_title('Grafico a sinistra')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(212)
ax.plot(x, -y, 'bo')
ax.set_title('Grafico a destra')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')
plt.tight_layout()
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10
fig = plt.figure() #creo una figura principale
ax = fig.add_subplot(321) 
ax.plot(x, y,'bo')
ax.set_title('Grafico 1')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(322)
ax.plot(x, y, 'bo')
ax.set_title('Grafico 2')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(323)
ax.plot(x, y,'bo')
ax.set_title('Grafico 3')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(324)
ax.plot(x, y, 'bo')
ax.set_title('Grafico 4')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(325)
ax.plot(x, y,'bo')
ax.set_title('Grafico 5')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(326)
ax.plot(x, y, 'bo')
ax.set_title('Grafico 6')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
xs = [1,2,3,4]
ys = [7,5,8,2]
plt.bar(xs, ys,
        0.5,
        color = 'green',
        align = 'center')
plt.show()

print(plt.subplots())
fig, ax = plt.subplots()
print(fig, ax)


mu = 0 #media
sigma = 1 #sqm
num_bins = 50 # numero di colonne per l'istogramma
#print(np.random.seed(12))
segnale = np.random.normal(mu, sigma, 500)
fig, ax = plt.subplots()
ax.plot(segnale)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
mu = 0
sigma = 1
np.random.seed(0)# sempre la stessa sequenza di numeri pseudocasuali
segnale = np.random.normal(mu, sigma, 500)
num_bins = 50
n, bins, columns = ax.hist(segnale, num_bins)
ax.set_xlabel('Segnale')
ax.set_ylabel('Numero di elementi')
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()
plt.show()

fig, ax = plt.subplots()
segnale = [1,1,1,1,1, 2,2, 3,3,3,3,3,3,3,3]
num_bins = 50
n, bins, columns = ax.hist(segnale, num_bins)
print('N:',n,'\n','Bins:', bins,'\n', 'Columns:', columns)
ax.set_xlabel('Segnale')
ax.set_ylabel('Numero di elementi')
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()
plt.show()

import math

fig, ax = plt.subplots()
segnale = [3,5,3,5]
num_bins = 50 # round(math.sqrt(len(segnale)))*10
n, bins, columns = ax.hist(segnale, num_bins)
print('N:',n,'\n','Bins:', bins,'\n', 'Columns:', columns)
ax.set_xlabel('Segnale')
ax.set_ylabel('Numero di elementi')
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()
plt.show()

fig, ax = plt.subplots()
segnale = [-3,-3,-3,7,7,7,7,7]
num_bins = 50 #range(min(segnale), max(segnale)+2)
n, bins, columns = ax.hist(segnale, num_bins)
print('N:',n,'\n','Bins:', bins[:-1],'\n', 'Columns:', columns)
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
ax.set_xlabel('Segnale')
ax.set_ylabel('Segnali intercettati')

fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

fig, ax = plt.subplots()
np.random.seed(0)
mu = 0
sigma = 1
x = np.random.normal(mu, sigma, 500)
n, bins, columns = ax.hist(x, 50, density=True)
print('N:',n,'\n','Bins:', bins[:-1],'\n', 'Columns:', columns)
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
ax.set_xlabel('Segnali')
ax.set_ylabel('Segnali intercettati')
y = norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Segnale')
ax.set_ylabel('Densità di probabilità')
ax.set_title(r'Istogramma di una Gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()
plt.show()

np.random.seed(0)
mu = 0
sigma = 1
x = np.random.normal(mu, sigma, 500)
n, bins, columns = plt.hist(x, 50, density=True)#, color='white')
print('N:',n,'\n','Bins:', bins[:-1],'\n', 'Columns:', columns)
plt.title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
plt.xlabel('Segnali')
plt.ylabel('Segnali intercettati')
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, '--')
plt.xlabel('Segnale')
plt.ylabel('Densità di probabilità')
plt.title(r'Istogramma di una Gaussiana con $\mu=0$, $\sigma=1$')
#fig.tight_layout()
plt.show()

print()

labels = ['Pippo', 'Pluto', 'Paperino']
y = np.array([3,4,1])
esplodi = [0, 0, 0.1]
fig, ax = plt.subplots()
ax.pie(y, labels=labels, explode= esplodi, autopct='%1.1f%%', startangle=90)
ax.set_title('Spar(t)izione della pizza')
fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

labels = ['tre', 'quattro', 'uno']
y = [3,4,1]
esplodi = [0, 0, 0.1]
#print(plt.subplots(ncols= 3))
fig, (ax1, ax2) = plt.subplots(ncols = 2)
ax1.pie(y, labels = labels, explode = esplodi, autopct = '%1.1f%%', startangle = 90)
ax1.set_title('Spartizione della pizza')
xticks = [1,2,3]
ax2.bar(xticks, y, align= 'center', color = ['b', 'r', 'g'], width = 0.3)
ax2.set_title('Partizione della pizza in bar')
ax2.set_xticks(xticks)
ax2.set_xticklabels(labels)
fig.tight_layout()
plt.show()
#help(plt.bar)

#cambia lo sfondo di tutti i grafici da qui in poi
plt.rcParams['axes.facecolor'] = 'azure'
plt.plot(np.array([1,2,3]), [4,5,6])
plt.show()

#rimette lo sfondo bianco a tutti i grafici futuri
plt.rcParams['axes.facecolor'] = 'white'
plt.plot(np.array([1,2,3]), [4,5,6])
plt.show()

#importante da settare quando mettiamo del testo
#matplotlib non adatta automaticamente le dimensioni
plt.xlim(0, 450)
plt.ylim(0, 600)
plt.text(250, 
         450, 
         'Ciao !', 
         fontsize = 40,
         fontweight = 'bold',
         color = 'lightgreen',
         ha = 'center', #centra orizzontalmente il testo
         va = 'center') #centra verticalmente il testo
plt.show()

fig = plt.figure(figsize=(6,6))
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

plt.xlim(0, 150) #importante da settare quando mettiamo delle immagini
plt.ylim(0, 200) #perchè matplolib non ridimensiona automaticamante
ax = fig.gca()
img = plt.imread('OIP.jpg')
ax.add_artist(AnnotationBbox(OffsetImage(img, zoom=0.5), (50, 100), frameon=False))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
#regolare intensità colore
plt.plot(np.array([150, 175]), [25, 400],
         color = 'green',
         alpha = 1.0, #colore pieno
         linewidth = 10)

plt.plot([100, 125], [25, 400],
         color = 'green',
         alpha =  0.3,  #più leggero
         linewidth = 10)

plt.plot([50, 75], [25, 400],
         color = 'green',
         alpha = 0.1, #quasi invisibile
         linewidth = 10)

plt.show()

plt.rcParams['axes.facecolor'] = 'azure'
fig = plt.figure(figsize = (7,7))

plt.xlim(0, 150)
plt.ylim(0, 200)
ax = fig.gca()
img = plt.imread('OIP.PNG')
ax.add_artist(AnnotationBbox(OffsetImage(img, zoom = 0.5), (100, 200), frameon=False))

plt.xlim(0, 450)
plt.ylim(0, 600)
plt.text(250,
         450,
         'Be fancy',
         fontsize = 30,
         fontweight = 'bold',
         color = 'lightpink',
         ha = 'center', #centra orizzontalmente il testo
         va = 'center') #centra verticalmente il testo)

plt.plot([25, 400], [100, 100], color = 'blue', linewidth = 10, alpha = 0.3)
plt.plot([25, 400], [200, 200], color = 'blue', linewidth = 10, alpha = 0.5)
plt.plot([25, 400], [300, 300], color = 'blue', linewidth = 10, alpha = 1.0)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

part1 = [[1, 10], [0, 0]]
part2 = ([4, 4], [0, 4])
part3 = {"x": [8, 8], "y": [0, 4]}
more_parts = {
        "part4":[[4, 8], [4, 4]],
        "part5":[[4, 6], [4, 6]],
        "part6":[[8, 6], [4, 6]]
        }

plt.plot(np.array(part1[0]), part1[1])
#plt.show()
plt.plot(part2[0], part2[1])
#plt.show()
plt.plot(part3['x'], part3['y'])
#plt.show()
plt.plot(more_parts['part4'][0], more_parts['part4'][1])
#plt.show()
plt.plot(more_parts['part5'][0], more_parts['part5'][1])
#plt.show()
plt.plot(more_parts['part6'][0], more_parts['part6'][1])
plt.show()

lista = np.array([
    #['giorno', 'benchmark', 'titolo'],
    [0, 18, 9],
    [2, 19, 11],
    [4, 15, 7],
    [6, 4, 9],
    [8, 8, 11],
    [10, 16, 12],
    [12, 17, 13],
    [14, 11, 9],
    [16, 9, 11],
    [18, 5, 10]]
)

plt.title('Performance titolo vs benchmark')
plt.xlabel('Giorni')
plt.ylabel('Valore $')
plt.xticks(lista[:, 0])
plt.plot(lista[:, 0], lista[:,1], color='blue')
plt.plot(lista[:, 0], lista[:, 2], color='orange')
plt.plot(lista[:, 0], [np.max(lista[:,2]) for x in lista], linestyle='--', color = 'green')
plt.plot(lista[:, 0], np.full(len(lista), min(lista[:, 2])), linestyle='--', color = 'red')

plt.show()

import matplotlib.pyplot as plt
import numpy as np
import random

x = np.array(range(0,500))
lista = np.array([random.expovariate(0.6 / 2.0) for _ in range(500)])
lista.sort()
lista2 = [random.uniform(1, 50) for _ in range(500)]
lista2.sort()
plt.plot(x, lista2)
plt.plot(x, lista)

plt.show()

import pandas as pd
import numpy as np

df = pd.read_csv('astro_pi.csv', encoding='UTF-8')
print(df)#printa il file
df.info()#informazioni generali
print(df.shape) #righe colonne
print(df.describe())#dati di riepilogo
print()
print(df['Humidity'].describe())#colonna umidity dati riepilogo
print()
print(df.Humidity.describe())#colonna humidity dati riepilogo
print()
print(df.head())#prime tot righe, default = 5
print()
print(df.tail())#ultime tot righe, default = 5
print(df.columns) #i nomi di tutte le colonne
print(df.columns[2]) #nome della colonna 3
print(df.columns[4]) #nome colonna 5
print(list(df.columns)) #lista dei nomi delle colonne, superflua
print()
print(df.corr)# correlazione tra le colonne, con valori da -1.0 a +1.0

import pandas as pd
import numpy as np

meteo = pd.read_csv('meteo.csv', encoding='UTF-8')
print('COLUMNS:')
print(meteo.columns)
print()
print('INFO:')
print(meteo.info)
print()
print('HEAD:')
print(meteo.head())
print()

import matplotlib as mpl
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [2,4,6,8]
plt.plot(np.array(x),y) #possimao direttamente passare liste
plt.title('Qualche numero')
plt.show()

x = np.arange(0., 5., 0.1)
y = x**2
print(type(x), type(y))
plt.title('La parabola')
plt.plot(x,y)
plt.show()

print(plt.get_fignums())

plt.xlim([0, 5])
plt.ylim([0, 10])
plt.title('La parabola')

plt.gca().set_aspect('equal')
plt.plot(x,y)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('astro_pi.csv', encoding='UTF-8')
df['Humidity'].plot(label = 'humidity', legend = True)
#con secondary_y = True facciamo apparire i numeri per l'asse delle y
#del sexcondo grafico sulla destra
df.Pressure.plot(secondary_y = True, label='Pressure', legend= True)
plt.plot(df['Pressure'], df['Humidity'])
plt.show()
#print(df['Pressure'])
df2 = pd.read_csv('astro_pi.csv', encoding='utf-8')
print(df2.info)
dff2 = df2.iloc[12500:13723]
print(dff2)
plt.plot(df2['Pressure'], df2['Humidity'])
plt.show()
df2.Humidity.plot(label= 'Humidity', legend=True)
df2.Pressure.plot(secondary_y=True, label='pressure', legend=True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('temp_trento.csv', encoding='utf-8')
print(df.info)
print(df.iloc[0])
print()
print(df.iloc[6])#riga 8 = 6 +2
print()
print(df.iloc[5:7])#riga 7, 8 = 5+2 e 6+2
print(df.year[2] > 6)
print(type(df.day > 6))
print()
print(type((df.day >= 6) & (df.day <= 10)))
print((df.day >= 6) & (df.day <= 10))
print(df[(df.day >= 6) & (df.day <= 10)])
[print(x) for x in [df[(df.day >= 6) & (df.day <= 10)]]]
print()

df2 = pd.read_csv('astro_pi.csv', encoding='utf-8')

print(df2[(df2.Humidity == max(df2.Humidity.values))]) #print(df2[(df2.Humidity == df2.Humidity.values.max())])
print()
print(df2.sort_values('Pressure', ascending=False).head())
print('Media pressione:', df2.Pressure.values.mean())
print('Minimo pressione:', df2.Pressure.values.min())
print('Massimo pressione:', df2.Pressure.values.max())
print('Media temperatura:', df2.Temperature.values.mean())
print(df2[df2.Longitude > 0])
print()
print(df2[df2['Date/Time'].str.contains('2022-02-01')])
print()
print(df2['Date/Time'].str[8:10])
print()
print(df2[ ['Latitude', 'Longitude', 'Temperature'] ])
print(df2.head())
df2['MagTot'] = df2['MagX']**2 + df2['MagY']**2 + df2['MagZ']**2
df2.MagTot.plot() #df2['MagTot'].plot()
plt.show()
print(df2['Date/Time'][df2.MagTot == df2.MagTot.values.max()])
print()
df2.loc[(df2.Temperature > 31.68), 'Too hot'] = True
print(df2.head())
pressione_media = df2.Pressure.values.mean()#np.mean(df2.Pressure)
df2['check_p'] = np.where(df2.Pressure >= pressione_media, 'sopra', 'sotto') #dove la temperatura è maggiore di media scrivi nella colonna check_p sopra else sotto
print(df2.head())
print()
df['Temp (Fahrenheit)'] = df['Temp-C°']* 9/5 +32
print(len(df['Temp (Fahrenheit)']))

import csv
with open ('astro_pi.csv', 'r', newline='', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    #lettore = [lettore]
    #next(lettore)
    with open ('astro_pi2.csv', 'w', newline='', encoding='utf-8') as f1:
        scrittore = csv.writer(f1, delimiter=',')
        y = 0
        f1.write(f.readline().strip() + ',Temp (Fahrenheit)' + '\n')
        for x in lettore:
            try:
                scrittore.writerow(x + [float(df['Temp (Fahrenheit)'][y])])
            except:
                pass
            y += 1
#print(df.head())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('astro_pi.csv', encoding='utf-8')
print(df.corr)
df['k'] = df['Pressure'] / df['Temperature']
df['Relazione'] = df['k'] == df.corr
print()
print(int(23.7))

df['Humidity'].transform(int)#trasforma gli elementi in int
print(df['Humidity'].transform(int))
print(df.head())
print()
def mia_f(x):
    return int(x)

df['Humidity'].transform(mia_f)
print(df.head())
print()

df['Humidity'].transform(lambda x : int(x))
print(df.head())
print(df.info())
df['Humidity_int'] = df['Humidity'].transform(lambda x : int(x))
print(df.head())
print(df.groupby(['Humidity_int'])['Humidity'].count())# quanti numeri sono uguali al primo data
print()
df['Conteggio Umidità'] = df.groupby(['Humidity_int'])['Humidity'].transform('count')
print(df)

df.Temperature.plot(label='Temperature', legend=True)
df['Humidity'].plot(label='Humidity', legend=True)
df['Pressure'].plot(secondary_y=True, label='Pressione', legend=True)
plt.show()
df['Giorno'] = df['Date/Time'].str[:10]
print(df.head())
print()
print(df.groupby(['Giorno'])['Temperature'].mean())
print()
df['Temp_media_giorno'] = df.groupby(['Giorno'])['Temperature'].transform('mean')
print(df['Giorno'], df['Temp_media_giorno'])
print()
print(df.head())
df['Temperature'].plot(label='Temperature', legend=True)
df['Temp_media_giorno'].plot(label='temp media', legend=True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('astro_pi.csv', encoding='utf-8')
df['Giorno'] = df['Date/Time'].str[0:10]
print(df.head())
for giorno in df['Giorno']:
    temp_media_giorno = df[(df.Giorno == giorno)].Temperature.values.mean()
    df.loc[(df.Giorno == giorno), 'Temp_media_giorno'] = temp_media_giorno

print(df.head())
df.Temperature.plot(label='Temperature', legend=True)
df.Temp_media_giorno.plot(label='Temepratura media', legend=True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

meteo = pd.read_csv('astro_pi.csv', encoding='utf-8')
meteo['Giorno'] = meteo['Date/Time'].str[:10]
diz_media = {}
for giorno in meteo['Giorno']:
    if giorno not in diz_media:
        diz_media[giorno] = meteo[meteo['Giorno'] == giorno]['Temperature'].mean()
for giorno in meteo['Giorno']:
    meteo.loc[(meteo.Giorno == giorno), 'temp_media_giorno'] = diz_media[giorno]

print(meteo.head())
meteo.Temperature.plot(label='Temperature', legend = True)
meteo.temp_media_giorno.plot(label = 'Temepratura media', legend = True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

meteo = pd.read_csv('astro_pi.csv', encoding='utf-8')
meteo['Giorno'] = meteo['Date/Time'].str[:10]
#.transform è necessario per evitare di avere una tabella con solo 2 righe
#print(meteo.groupby(['Giorno'])['Temperature'].mean())
meteo['Temp_media_giorno'] = meteo.groupby(['Giorno'])['Temperature'].transform('mean')
print(meteo.head())
meteo['Temperature'].plot(label = 'Temperature', legend = True)
meteo['Temp_media_giorno'].plot(label='Temp media giorno', legend=True)
plt.show()
print()

aria = pd.read_csv('aria.csv', encoding='latin-1')
aria.info()
print(aria[(aria['Stazione'] == 'Parco S. Chiara') & (aria['Inquinante'] == 'PM10')]['Valore'].mean()) #.values.mean()
filtrato = aria[(aria['Stazione'] == 'Parco S. Chiara') & (aria['Inquinante'] == 'PM10') & (aria['Data'] == '2024-01-18') ]
plt.plot(filtrato['Ora'], filtrato['Valore'])
plt.title('Inquinamanto giornaliero del 2024-01-18')
plt.xlabel('Ora')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aria = pd.read_csv('aria.csv', encoding='latin-1')
aria.info()
media = aria[(aria['Stazione']=='Parco S. Chiara') & (aria['Inquinante'] == 'PM10')]['Valore'].mean()
print(media)
valori_gio = aria[(aria['Stazione']=='Parco S. Chiara') & (aria['Inquinante'] == 'PM10') & (aria['Data']=='2024-01-18')]
print(valori_gio)
plt.plot(valori_gio['Ora'], valori_gio['Valore'])
plt.title('Media inquinante: '+ valori_gio['Data'][0])
plt.xlabel('Ora (0-24)')
plt.ylabel('Valori inquinanti (' + str(min(valori_gio['Valore'])) + '-' +  str(max(valori_gio['Valore'])) + ' ' + str(valori_gio['Unità di misura'][0]) + ')')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('astro_pi_data.csv', encoding='utf-8')
df.info()
print()
iss_coords = pd.read_csv('iss_output_coords.csv', encoding='utf-8')
iss_coords.info()
print()
geo_astropi = df.merge(iss_coords, left_on='time_stamp', right_on='timestamp', how='left', indicator=True)
geo_astropi = geo_astropi.drop('timestamp', axis = 1)

print(geo_astropi.shape)
pd.merge_ordered(df, iss_coords, fill_method='ffill', how = 'left', left_on='time_stamp', right_on='timestamp')
print(geo_astropi)

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
print('ok')
df_regioni = gpd.read_file('Localita_11_WGS84.shp')
print(df_regioni)

#estrae la popolazione per regioner da popolazione.html, e restituisce un dataframe 
#pandas (non geopandas)
#estrae la popolazione per regioner da popolazione.html, e restituisce un dataframe 
#pandas (non geopandas)
import dateutil
import pandas as pd

def estrai_dizionario(riga_html):
    colonne = riga_html.select('td')
    return dict(name = colonne[1].text,
                population = colonne[2].text.replace('.','').replace(',', '.'),
                area = colonne[3].txt.replace('.', '').replace(',', '.'))

def estrai_popolazione():
    from bs4 import BeautifulSoup
    with open('popolazione.html', encoding='UTF-8') as f:
        testo = f.read()
        listona = []    # listona di dizionari, ogni dizionario rappresenta una riga
        # usiamo parser html5lib invece di xml perchè il sito è complesso
        soup = BeautifulSoup(testo, 'html5lib')
        righe_html = soup.select('tablr.ut tr')[1:21]
        for riga_html in righe_html:
            listona.append(estrai_dizionario(riga_html))
        return pd.DataFrame(listona)
    
df_popolazione = estrai_popolazione()
print(df_popolazione)

def alberinomi(stringa):
    import csv
    with open('Alberi-Monumentali-Della-Campania.csv', 'r', encoding='utf-8', newline = '') as f:
        reader = csv.reader(f, delimiter=';')
        for x,y in enumerate(list(reader)[0]):
           print(y, x)
        #next(reader)
        for x in reader:
            if stringa.lower() in x[6].lower():
                print(x[6])

alberinomi('tiglio')

from numba import jit
import time

@jit # funziona solo con la sintassi base di python, senza moduli extra
def conto():
    for x in range(1000000000+1):
        count = x
    print('ok', x)

start = time.time()
conto()
end = time.time()
print(end-start)
'''

































 







