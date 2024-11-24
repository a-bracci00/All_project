'''
#import os
#cwd= os.getcwd()
#print(cwd)
with open('testo.txt','w') as f:
    pass
b= os.path.abspath('testo.txt')
print(b)
c=os.path.exists('testo.txt')
print(c)
d=os.path.isdir('testo.txt')
print(d)
e=os.path.isfile('testo.txt')
print(e)
f=os.listdir(cwd)
print(f)
def esplora(dirnome):
    for nome in os.listdir(dirnome):
        percorso= os.path.join(dirnome,nome)
        if os.path.isfile(percorso):
            print(percorso)
        else:
            esplora(percorso)
esplora(cwd)
g=os.path.join('Desktop','pyt1.py')
print(g)

try:
    fin= open('file_corrotto')
except:
    print('qualcosa non funge')


import dbm
import os
db= dbm.open('didascalie','c')

db['cleese.png'] = 'Foto di John Cleese'
a= db['cleese.png']
print(a)
db['cleese.png'] = 'Foto di john cleese che cammona in modo ridicolo'
db['giovanni.png'] = 'foto di giovanni'

for chiave in db:
    print(chiave,db[chiave])
db.close()
with dbm.open('didascalie2','c') as g:
    pass
os.remove('didascalie2.dat')
os.remove('didascalie2.dir')

import random
class Carta():
    #Rappresenta una carta
    
    def __init__(self, seme=0, valore=2):
        self.seme = seme
        self.valore = valore

    nomi_semi = ['Fiori', 'Quadri','Cuori','Picche'] 
    nomi_valori = [None,'Asso','2','3','4','5','6','7',
                '8','9','10','Fante','Regina','Re']
    
    def __str__(self):
        return '%s di %s' % (Carta.nomi_valori[self.valore],
                             Carta.nomi_semi[self.seme])

    def __lt__1(self,other):
        #controlla semi
        if self.seme < other.seme: return True
        if self.seme > other.seme: return False

        #semi uguali.. controlla i valori
        return self.valore < other.valore

    def __lt__(self,other):
        t1 = self.seme, self.valore
        t2 = other.seme, other.valore
        return t1 < t2

class Mazzo:
    #Rappresenta un mazzo
    
    def __init__(self):
        #creo una lista
        self.carte = []
        #per ogni seme
        for seme in range(4):
            #per ogni valore
            for valore in range(1,14):
                #crea una variabile che contine la carta formata
                carta = Carta(seme,valore)
                #inserisci la carta nella lista
                self.carte.append(carta)
    
    def __str__(self):
        res = []
        for carta in self.carte:
            res.append(str(carta))
        return '\n'.join(res)

    def togli_carta(self):
        return self.carte.pop()
    
    def aggiungi_carta(self, carta):
        self.carte.append(carta)

    def mescola(self):
        random.shuffle(self.carte)

    def ordina(self):
        self.carte.sort()
    
    def sposta_carte(self, mano, num):
        for i in range(num):
            mano.aggiungi_carta(self.togli_carta())
    def dai_mani(self, num_mani, num_carte):
        for i in self.carte:



class Mano(Mazzo):
    #rappresenta una mano di carte
   
    def __init__(self, label=''):
        self.carte = []
        self.label = label

def trova_classe_def(obj, nome_metodo):
    for ty in type(obj).mro():
        if nome_metodo in ty.__dict__:
            return ty

regina_di_quadri= Carta(1,12)
carta1=Carta(2,11)
print(carta1)

mazzo= Mazzo()
print(mazzo)

mano = Mano('nuova mano')
print(mano.carte)
print(mano.label)
carta = mazzo.togli_carta()
mano.aggiungi_carta(carta)
print(mano)

mano1= Mano()
print(trova_classe_def(mano, 'mescola'))

suffix_map = {}
prefix = ()

class Markov:

    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()

    def elabora_parola(self, parola, ordine=2):
        if len(self.prefix) < ordine:
            self.prefix += (parola,)
            return
        try:
            self.suffix_map[self.prefix].append(parola)
        except KeyError:
            #se non c'è una voce per questo prefisso, creane una
            self.suffix_map[self.prefix] = [parola]

        self.prefix = shift(self.prefix, parola)


class PingPongMadre():
    pass

class Ping(PingPongMadre):
    def __init__(self, pong):
        self.pong = pong

class Pong(PingPongMadre):
    def __init__(self, pings=None):
        if pings is None:
            self.pings = []
        else:
            self.pings = pings
    
    def add_ping(self, ping):
        self.pings.append(ping)

pong = Pong()
ping = Ping(pong)
pong.add_ping(ping)

if x > 0:
    y = math.log(x)
else:
    y= float('nan')

y = math.log(x) if x > 0 else float('nan')

def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale (n-1)

def __init__ (self, nome, contenuti= None):
    self.nome = nome
    if contenuti == None:
        contenuti = []
        self.contenuto_tasca = contenuti

def __init__(self, nome, contenuti=None):
    self.nome = nome
    self.contenuto_tasca = [] if contenuti == None else contenuti



class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def stampatutti(*args):
    print(args)

print(stampatutti(1,2.0,'3'))

#stampatutti(1,2.0, terzo='3')

def stampa_tutti(*args, **kwargs):
    print(args, kwargs)

print(stampa_tutti(1,2.0,terzo='3'))

d = dict(x=1, y=2)
Punto(**d)
punto = Punto()

import modulo

print(modulo)
a=modulo.sei('scemo')
print(a)

import pdb

self.mani[i].aggiungiCarta(self.mani[self.trovaVicino(i)].togliCarta())

vicino = self.trovaVicino(i)
cartaScelta = self.mani[vicino].togliCarta()
self.mani[i].aggiungiCarta(cartaScelta)


import math
# y = x / 2 * math.pi
y = x / (2 * math.pi)


print(1)
x = 2 
print(x)

inp = input('what is your name?\n')
inp = int(inp)
print(inp)

minute = 60
percentage = (minute*100)/60
print(percentage)

a = 35.0
b = 12.50
c = a*b
print(c)

hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)


nome = input('inserisci il tuo nome: ')
print('Benvenuto', nome)
ore = int(input('inserisci le ore lavorative: '))
retribuzione = int(input('inserisci la retribuzione oraria: '))
stipendio = ore*retribuzione
print('il tuo stipendio sarà di', stipendio)

width = 17
height = 12.0

a=width//2.2
b=width/2.0
c=height/3
print(width//2.2)
print(width/2.0)
print(height/3)

print(type(a))
print(type(b))
print(type(c))


a=int(input('temperatura in gradi: '))
b=(a+1.8) + 32
print('in fahrenheit sono:', b)

print(5==5)
print(5==6)
print(type(True))
print(type(False))

try:
    a=int(input('temperatura in gradi: '))
    b=(a+1.8) + 32
    print('in fahrenheit sono:', b)
except:
    print('riprova')

eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'

print(eng2sp)

eng2sp = {'one':'uno', 'two':'dos', 'three': 'tres'}
print(eng2sp)

print(eng2sp['two'])

print(len(eng2sp))

print('one' in eng2sp)
print('uno' in eng2sp)

vals = list(eng2sp.values())
print('uno' in vals)

with open('words.txt','r') as f:
    dizio = {}
    for riga in f:
        riga = riga.split()
        for parola in riga:
            dizio[parola] = 0
    print(dizio)
print('explain'in dizio)

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
print(counts.get('jan', 0))
print(counts.get('tim', 0))

#creo una variabile che contine una stringa
word = 'brontosaurus'
#creo un dizionario di none d
d = dict()
#per ogni elemento in word
for c in word:
    #prendi il dizionario alla chiave/elemento momentanea/o
    #se non c'è inseriscila con valore 1
    #altrimenti aggiungi 1 al valore
    d[c] = d.get(c,0) + 1
print(d)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

counts = {'chuck': 1,'annie': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

counts = {'chuck': 1, 'annie': 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
print(lst)
for key in lst:
    print(key, counts[key])


import string
print(string.punctuation)
#creo una variabile con file in input esterno come valore
fname = input('Enter the file name: ')
#provo l'input
try:
    fhand = open(fname)
except:
    #se non riesco print
    print('File cannot be openend:', fname)
#creo un dizionario 
counts = dict()
#per ogni riga nel file
for line in fhand:
    #prendo la linea composta da parole
    #elimino gli spazi anteriori e posteriori
    line = line.rstrip()
    #sostituisco tutti i segni di punteggiatura con gli spazi
    line = line.translate(line.maketrans('', '', string.punctuation))
    #trasformo la riga in minuscolo
    line = line.lower()
    #creo una variabile parole che contiene
    #la rida divisa tra parole
    words = line.split()
    #per ogni parola in words
    for word in words:
        #se non è nel dizionario
        if word not in counts:
            #assegna come valore 1 alla chiave
            counts[word] = 1
        else:
            #altrimenti, se già esiste aggiungi sl valore 1
            counts[word] += 1
#mostra il dizionario
print(counts)

#prima richiesta di testo da server
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

import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST,PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header lenght', pos)
print(picture[:pos].decode())

#skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#trasformare una pagina web in un fili per poi
#trattarla come tale
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())


import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()


import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('Thunderstruck', 20))

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('My Way', 15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

cur.close()

#CREATE TABLE Tracks (title TEXT, plays INTEGER)

#INSERT INTO Tracks (title, plays) VALUES ('My Way', 15)

#SELECT * FROM Tracks WHERE title = 'My Way'

#SELECT title, plays FROM Tracks ORDER BY title

#DELETE FROM Tracks WHERE title = 'My Way'

#UPDATE Tracks SET plays = 16 WHERE title = 'My Way'



from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl
#url twitter
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
#creo una variabile che contiene il file sql di none spider
conn = sqlite3.connect('spider.sqlite')
#creo un cursore
cur = conn.cursor()
#creo una tabella se non esiste già di nome twitter
#con tre colonne 
#una di testo denominata name
#e due per numeri interi una chiamata retrieved ed una friends
cur.execute('')'
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)'('')

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#creo un ciclo che si stoppa solo scrivendo quit
while True:
    #creo un input
    acct = input('Enter a Twitter account, or quit: ')
    #se acct è uguale a quit blocca il ciclo
    if (acct == 'quit'):
        break
    #se la lunghezza di acct è minore di 1
    if (len(acct) < 1):
        #prendi il puntatore e seleziona
        #colonna name dalla tabella twitter
        #dove il valore di retrieved è uguale a 0 nel primo utente 
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            #controlla se i'input è la riga di base
            acct = cur.fetchone()[0]
        except:
            #se non c'è print e riparti
            print('No unretrieved Twitter accounts found')
            continue
    #url = oauth_request.to_url
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count':'5'})
    #stampa retrieving + url
    print('Retrieving', url)
    #
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.load(data)
    #Debugging
    #print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE NAME = ?', (acct,))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()[0]
            cur.executed('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            cur.execute(')''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''(', (friend, ))
    print('New accounts=', countnew, 'revisited=', countold)
    conn.commit()

cur.close()
'''








