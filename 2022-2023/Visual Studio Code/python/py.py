'''
# cancellare elementi da una lista conoscendone l'indice
t=[1,2,3]
x= t.pop(1)
print(t)

# se omettiamo l'indice verrà eliminato l'ultimo elemento
t=[1,2,3]
x=t.pop()

# usiamo del per eliminare un elemento senza immagazzinarlo
t=[1,2,3]
del t[1]

# eliminare elementi conoscendone l'elemento ma non l'indice
t=['a','b','c']
t.remove('b')
# il suo valore di ritorno è None

# cancellare più elementi con del + slicing

t=['a','b','c','d','e','f']
del t[1:5]
# eliminerà da 'b' a 'e'

# convertire una stringa in una lista di caratteri
# convertire una stringa in singole lettere
s='spam'
t= list(s)

# spezzare una stringa di parole in singole parole
s= 'profonda nostalgia dei fiordi'
t=s.split()

# in split() possiamo selezionare il delitatore (' ' '-' '_' etc..) che vogliamo usare
s='spam-spam-spam'
delimita='-'
t=s.split(delimita)


# prendere una lista di stringhe e concatenarne gli elementi con il metodo join
t=['profonda','nostalgia','dei','fiordi']
delimita =' ' 
s=delimita.join(t)

# in questo caso li concatenerà separandoli con uno spazio ' ' = spazio 
# se vogliamo concatenarle senza spazi useremo una stringa vuota''= stringa vuota

a='banana'
b='banana'
# per controllare se due variabili si riferiscono allo stesso oggetto
# usiamo is
a is b = True

# ma se creiamo due liste apparentemente uguali saranno diversi
a = [1,2,3]
b = [1,2,3]
a is b = False
# sono equivalenti ma non identiche

# alias o riferimento
# creare due riferimenti allo stesso oggetto
a =[1,2,3]
b=a
b is a=True

# se l'oggetto è mutabile, i cambiamenti si riflettono anche sull'altro
b[0]=42
# a[0] verrà cambiata

# liste come argomenti
del decapita(t):
    del t[0]

lettere=['a','b','c']
decapita(lettere)

# append modifica una lista
t1=[1,2]
t2 = t1.append(3)
print(t1) = [1,2,3]
print(t2)= None

# + ne crea una nuova
t3=t1+[4]
print(t1)=[1,2,3] #vecchia lista immutata
print(t3)=[1,2,3,4] #nuova lista


def somma_nidificata(t):
    nuova=[]
    for el in t:
        for c in el:
            nuova.append(c)
    return sum(nuova)
            
t=[[1,2],[3],[4,5,6]]
print(somma_nidificata(t))


102

# funzione istogramma con parametro
def istogramma(s):
    # d= dizionario vuoto
    d=dict()
    # per ogni elemento in s
    for c in s:
        # se l'elemento non è in d 
        if c not in d:
            # l'elemento in quella posizione ha valore 1
            d[c] =1
        else:
            # altrimenti incrementa il valore di 1
            d[c] +=1
    # ritorna il dizionario con gli elementi 
    return d

s='brontosauro'
h=istogramma(s)

# .get(chiave:valore)
print(h.get('r',0))

def istogramma(s):
    d=dict()
    for i in s:
        d[i]=+1
    return d
s='brontosauro'
print(istogramma(s))

h=istogramma('parrot)

def stampa_isto(h)
    for c in h:
        print(c,h[c])
stampa_isto(h)

for chiave in sorted(h):
    print(chiave, h[chiave])

def inverso_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
# raise soleva un'eccezione
# LookupError() è il tipo di eccezione che vogliamo che compaia
    raise LookupError()

def inverti_diz(d):
    # inverso = dizionario vuoto
    inverso=dict()
    # per ogni chiave in d
    for chiave in d:
        # il valore è == alla chiave di d
        valore = d[chiave]
        # se il valore non sta nel dizionario inverso
        if valore not in inverso:
            # il valore di inverso è == a chiave
            inverso[valore] = [chiave]
        else:
            # altrimenti aggiungi la chiave come valore in inverso
            inverso[valore].append(chiave)
    return inverso

# flag
verbose=True
def esempio1():
    if verbose:
        print('esempio1 in esecuzione')


conta=0
# non può cambiare il valore di una variabile 
# già assegnata a livello globale
def esempio3():
    # conta non ha valore
    conta=conta+1

def esempio4():
    # con global, prendiamo il valore di conta
    # all'esterno della funzione per poi cambiarlo
    global conta
    conta +=1

noto ={0:0, 1:1}
def esempio5():
    noto[2]=1

# se vogliamo aggiungere, rimuovere e sostituire elementi di
# una lista o dizionario globali, possiamo farlo tranqillamente
# ma se vogliamo riassegnarne il valore obbiamo uare globar + nome variabile


# apro il file dandogli un nome
with open('words.txt') as f:
    # creo una funzione con argomanro il file
    def leggi_inserisci(f):
        # creo un dizionari vuoto
        d={}
        # per ogni elemento nel file
        for i in f:
            # prendo l'elemento e ne tolgo l'accapo '\n'
            a=i[:-1]
            # ora metto l'elemento come chiave nel dizionario
            d[a]=a
        # ritorno il dizionario
        return d
    # immagazino il risultato di leggi_inserisci in di
    di=leggi_inserisci(f)
    # cre una funzione con argomenti parola e il precedente dizionario
    def controlla(parola,d):
        # se la parola che cerco sta nel dizionario
            if parola in d:
                # ritorna true
                return True
            else:
                # altrimenti ritorna false
                return False
    # immagazzino il risultato in una variabile
    vero_falso=controlla('goof',di)

t=('a','b','c','d','e')
print(t)

# per creare una tupla con oggetto singolo
# ci va la virgola dopo il valore
t1='a',
print(type(t1))

# senza virgola è una stringa
t2=('a')
print(type(t2))

# tuple vuote
t3=tuple()
t3=()


t4=tuple('lupini')
print(t4)
# il risultato sarà una tupla formata dalla parola scomposta

# la maggior parte degli operatori di lista funzionano anche con le tuple
print(t[0]) #valore all'indice 0
print(t[1:3]) #valori dal secondo al terzo

# le tuple non possono essere modificate
# t[0] = 'a'

# ma possiamo modificarla con un altra tupla
t=('a',) + t[1:]
# questo creerà una nuova tupla facendo in modo che t si riferisca ad essa
print(t)

# operatori di confronto
(0,1,2) < (0,3,4)
# python confronterà il primo con il primo di ciascuna tupla
# se sono uguali passerà al secondo e via dicendo
# si fermerà con il confroto di due elementi diversi


# inverti dizionario
def inverti_diz(d):
    # creo il dizionario per metterci i valori inversi
    inverso = dict()
    # per ogni elemento nella lista
    for chiave in d:
        # il valore è divente elemento alla posizione dell'elemento
        valore = d[chiave]
        # se il valore non è nel dizionario
        if valore not in inverso:
            # metti l'elemento come chiave
            inverso[valore] = [chiave]
        else:
            # altrimenti aggiungi la chiave al valore
            inverso[valore].append(chiave)
    # ritorna il dizionario inverso
    return inverso

from tabnanny import verbose


verbose = True


def esempio1():
    if verbose:
        print('esempio1 in esecuzione')


stata_chiamata = False


def esempio2():
    # sbagliato
    stata_chiamata = True


def esempio2():
    # non creare una nuova variabile locale
    # ma modifica quella globale
    global stata_chiamata
    stata_chiamata = True


conta = 0


def esempio3():
    # sbagliato
    # non possiamo usare una variabile senza inizializzarla
    conta = conta+1


def esempio3():
    global conta
    conta += 1


noto = {0: 0, 1: 1}


def esempio4():
    # possiamo modificare il valore mutabile
    # ma non riassegnarne il valore
    noto[2] = 1


def esempio5():
    global noto
    # con global possiamo riassegnarne il valore
    noto = dict()


from pprint import pprint


pprint('sei uno scemo')
print('sei uno scemo')


def scansiona_parole(file):
    with open(file) as f:
        dizio = {}
        for i in f:
            i = i[:-1]
            dizio[i] = i
        return dizio


def trova_parola(parola):
    if parola in fun_scan:
        return True
    else:
        return False


fun_scan = scansiona_parole('words.txt')
print(trova_parola('zymogen'))

# Raccolta
# numero variabile di argomenti
# mettendo * davanti agli argomenti
def stampatutti(*args):
    print(args)

stampatutti(1,2.0,'3)

# spacchettamento
# se abbiamo una sequenza di valori
# e vogliamo passarla ad una funzione
# possiamo riusare *

# divmod ritorna la divisione ed il resto di 2 numeri
t=(7,3)
divmod(t)
# errore divmod expected 2 arguments, got 1

divmod(*t)
# (2.1)

# molte funzioni possono usare le tuple i argonmanti diversi
# ad esempio max e min

max(1,2,3)
# 3
min(1,2,3)
# 1

# ma con sum non funziona

sum(1,2,3)
# error sum expected at most 3 arguments, got 3

# args = varia argomenti
def sommatutto(*args):
    return sum(args)

print(sommatutto(1, 2, 3))

# ZIP
# zip unisce due file alternandoli (appunto, tipo zip)
s = 'abc'
t = [0,1,2]
zip(s,t)
# il risultato è un oggetto zip capace di iterare attraverso le coppie

for coppia in zip(s,t):
    print(coppia)
# ('a',0) ('b',1) ('c',3)

list(zip(s,t))
# [('a',0), ('b',1), ('c',3)]

# se le sequenze non sono della stessa lunghezza
# la lunghezza finale sarà uguale alla minore

list(zip('Anna','Edo'))
# [('A','E'),('n','d'),('n','o')]

t=('a',0) ('b',1) ('c',2)
for lettera, numero in t:
    print(numero, lettera)

# 0 a
# 1 b
# 2 c

def corrispondenza(t1,t2):
    for x,y in zip(t1,t2)
        if x==y:
            return True
    return False

# per scansionare in seguenza gli elementi e i loro indici
for indice, elemento in enumerate('abc'):
    print(indice, elemento)
# 0 a
# 1 b
# 2 c

# Dizionari e Tuple
# metodo items restituisce una sequenza di tuple chiave-valore

d={'a':0, 'b':1, 'c':2}
t = d.items()
# dict_items([('c',2), ('a',0), ('b',1)])

for chiave, valore in d.items():
    print(chiave,valore)

# c 2
# a 0
# b 1
# come di consueto non sono in ordine

t=[('c',2), ('a',0), ('b',1)]
d = dict(t)
# {'a':0, 'c':2,'b':1}

# la combinazione di dict e zip produce un modo conciso
# di creare un dizionario

d = dict(zip('abc', range(3)))
# {'a':0, 'c':2,'b':1}

# anche .update() prende una lista di tuple e le aggiunge
# come coppie chiave-valore ad un dizionario esistente

# elenco[cognome, nome] = numero
# for cognome, nome in elenco:
    # print(nome, cognome, elenco[cognome,nome])

from structshape import structshape
t=[1,2,3]
structshape(t)
# list of 3 int

t2=[[1,2],[3,4],[5,6]]
structshape(t2)
# list of 3 list of 2 int

t3=[1,2,3,4.0,'5','6',[7],[8],9]
# list of 3 tuple of (int, str)

d=dict(lt)
structshape(d)
# dict of 3 int->str

def piu_frequente(stringa):
    pass
piu_frequente('elefante')



# creo una funzione che mi ordina le stringhe


def ordina(s):
    "ordina una stringa e la ritorna"
    # creo una lista di nome t
    t = list(s)
    # ordino la lista in modo alfabetico
    t.sort()
    # separo le parole nella lista tramite spazio
    t = ''.join(t)
    # ritorno la lista
    return t

# creo una funzione che mi crei gli anagrammi partendo da un file txt


def calcola_anagrammi(filename):
    # creo un dizionario di nome d
    d = {}
    # per ogni linea(elemento) nel file txt
    for linea in open(filename):
        # prendi la parola eliminandone gli spazi anteriori e posteriori
        # per poi far diventare ogni carattere in minusolo
        parola = linea.strip().lower()
        # richiamo la funzione ordina parola
        t = ordina(parola)
        # se la stringa corrente in t non è nel dizionario d
        # inserisco in quella posizione essa stessa come valore
        if t not in d:
            d[t] = [parola]
            # altrimenti la aggiungo come chiave
        else:
            d[t].append(parola)
        # ritorno il dizionario
    return d

# creo una funzione che mi stampi gli anagrammi precedentemente trovati
# estrapolandoli dal dizionario d


def stampa_anagrammi(d):
    # per orgni valore(elemento) nei valori di d
    for v in d.values():
        # se la lunghezza di v è maggiore di uno
        if len(v) > 1:
            # stampa il nuemro di lettere più il valore
            print(len(v), v)

# creo una funzione che stampi gli anagrammi ordinandoli


def stampa_anagrammi_in_ordine(d):
    # creo una lista di nome t
    t = []
    # per ogni valore(elemento) nei nalori di d
    for v in d.values():
        # se la linghezza del valore è maggiore di 1
        if len(v) > 1:
            # aggiungo il numero delle lettere di v e v
            t.append((len(v), v))
    # riordino t alfabeticamente ma al contrario
    t.sort(reverse=True)
    # scansioni tutta la lista t, per ogni elemento in t
    for x in t:
        # stampa l'elemento
        print(x)


# creo il main
if __name__ == "__main__":
    # la variabile d conterrà il dizionario interno d
    d = calcola_anagrammi('words.txt')
    # chiamo la funzione con input d
    stampa_anagrammi_in_ordine(d)
'''
