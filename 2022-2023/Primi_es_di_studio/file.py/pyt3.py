'''
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


import urllib.request
import urllib.parse
import urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()

import urllib.request
import urllib.parse
import urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()

import socket
URL = input('Inserisci Url: ')
try:
    URL_split = URL.split('/')
    URL_ = URL_split[2]
except:
    print('stupido2')
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((URL_, 80))
except:
    print('stupido')
    exit()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
    for i in data.decode():
        count += 1
mysock.close()
print('Caratteri totali:', count)


import xml.etree.ElementTree as ET

data = #('')'
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>#('')'
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


import xml.etree.ElementTree as ET

input = #('')'
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>#('')'

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

a = {
    "name": "Chuck",
    "phone": {
        'type': 'intl',
        'number': '+1 734 303 4456'
    },
    'email': {
        'hide': 'yes'
    }
}
print(a)


import json

data = #('')'
[
    { 
      "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    },
    { 
      "id" : "009",
      "x" : "7",
      "name" : "Brent"
    }
]#('')'

info = json.loads(data)
print(info)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])


import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
# if you have a Google Places API key, enter it here
#api_key = 'AIzaSy___IDByT70'
# 'https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-cuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().encode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or ['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['result'][0]['geometry']['location']['lat']
    lng = js['result'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['result'][0]['formatted_address']
    print(location)

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)


import urllib.request
import urllib.parse
import urllib.error
import twurl
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter twitter Account:')
    if len(acct) < 1:
        break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])


import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    if address == 'stop':
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)


stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff, 1))
print(dir(stuff))


usf = input('Enter the US Floor Number: ')
wf = int(usf) - 1
print('Non-US Floor Number is', wf)


class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x+1
        print('So far', self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)


class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)


an = PartyAnimal()
print('Type', type(an))
print('Dir', dir(an))
print('Type', type(an.x))
print('Type', type(an.party))


class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am costructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

# creo una classe


class PartyAnimal:
    # una variabile iniziale con 0
    x = 0
    # una seconda variabile iniziale con stringa vuota
    name = ''

    def __init__(self, nam):
        # la stringa vuota prende il valore nam
        # che verrà inserita poi
        self.name = nam
        # mostra a schermo il nome + parola
        print(self.name, 'constructed')

    def party(self):
        # prendo il valore di x e gli aggiungo 1
        self.x = self.x + 1
        # mostra il nome + parola + numero di partecipanti
        print(self.name, 'party count', self.x)


s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()


import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()

import sqlite3
# creo/apro il file.sqlite3
conn = sqlite3.connect('archivio.sqlite3')
# creo un cursore
cur = conn.cursor()
# creo una tabella con due colonne
# una di testo chiamata from_friend
# una per interi chiamata to_friend
cur.execute('DROP TABLE IF EXISTS Pals')
cur.execute('CREATE TABLE Pals (from_friend TEXT, to_friend TEXT)')
cur.execute(
    'INSERT INTO Pals (from_friend, to_friend) VALUES("drchuck", "lhawthorn")')
cur.execute(
    'CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)')
cur.execute(
    'CREATE TABLE Follows (from_id INTEGER, to_id INTEGER, UNIQUE (from_id, to_id))')
conn.close()

import urllib.request
import urllib.parse
import urllib.error
import twurl
import sqlite3
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friens/list.json'

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute(
    'CREATE TABLE IF NOT EXISTS People (id INTEGER KEY, name TEXT UNIQUE, retrieved INTEGER)')

cur.execute(
    'CREATE TABLE IF NOT EXISTS Follows (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))')

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'):
        break
    if len(acct) < 1:
        cur.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1')
        try:
            (id, acct) = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (acct, ))

        try:
            id = cur.fetchone()[0]
        except:
            cur.execute(
                'INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)', (acct, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid

        url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
        print('Retrieving account', acct)
        try:
            connection = urllib.request.urlopen(url, context=ctx)
        except Exception as err:
            print('Failed to Retrieve', err)
            break

        data = connection.read().decode()
        headers = dict(connection.getheaders)

        print('Remaining', headers['x-rate-limit-remaining'])

        try:
            js = json.loads(data)
        except:
            print('Unable to parese json')
            print(data)
            break

        # Debugging
        #print(json.dumps(js, indent=4))

        if 'users' not in js:
            print('Incorrect JSON received')
            print(json.dumps(js, indent=4))
            continue

        cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))

        countnew = 0
        countold = 0
        for u in js['users']:
            friend = u['screen_name']
            print(friend)
            cur.execute(
                'SELECT id FROM People WHERE name = ? LIMIT 1', (friend, ))

            try:
                friend_id = cur.fetchone()[0]
                countold = countold + 1
            except:
                cur.execute(
                    'INSERS OR IGNORE INTO People (name, retrieved) VALUES (?,0)', (friend, ))
                conn.commit()
                if cur.rowcount != 1:
                    print('Error inserting account:', friend)
                    continue
                friend_id = cur.lastrowid
                countnew = countnew + 1
            cur.execute(
                'INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?, ?)', (id, friend_id))
        print('New accounts=', countnew, 'revisited=', countold)
        print('Remaining', headers['x-rate-limit-remaining'])
        conn.commit()
    cur.close()

cur.execute(
    'CREATE TABLE IF NOT EXISTS People (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)')
cur.execute(
    'CREATE TABLE IF NOT EXISTS Follows (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id)')
#inserisci il valore se non c'e
#se c'è non vogliamo doppioni quindi ignora la richiest<a di inserimento
cur.execute(
    'INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0', (friend, ))
cur.execute('INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?,?), (id, friend_id)')


friend = u['screen_name']
cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (friend, ))
try:
    friend_id = cur.fetchone()[0]
    countold = countold + 1
except:
    cur.execute('INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0', (friend, ))
    conn.commit()
    if cur.rowrow != 1:
        print('Error inserting account:', friend)
        continue
    friend_id = cur.lastrowid()
    countnew = countnew + 1

cur.execute(
    'SELECT * FORM Follows JOIN People ON Follows.from_id = People.id WHERE People.id = 1')

import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM People')
count = 0
print('People:')
for row in cur:
    if count < 5:
        print(row)
    count = count + 1
print(count, 'rows.')

cur.execute('SELECT * FROM Follows')
count = 0
print('Follows:')
for row in cur:
    if count < 5:
        print(row)
    count = count + 1
print(count, 'rows.')

cur.execute(
    'SELECT * FROM Follows JOIN People ON Follows.to_id = People.id WHERE Follows.from_id = 2')

count = 0
print('Connections for id = 2:')
for row in cur:
    if count < 5:
        print(row)
    count = count + 1
print(count, 'rows.')

cur.close()
'''
