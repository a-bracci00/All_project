# Questo è un commento.
'''
Questo
è
un
commento.
'''

# Calcoliamo la circonferenza e l'area di un cerchio dato il raggio

from math import pi
raggio = int(input(
    "Inserisci il raggio per calcolare la circonferenza e l'area in centimetri: "))

# Usiamo la virgola ',' al posto del più '+'
# Non dovremo convertire gli int in str
# la differenza è che usando il più creeremo una stringa formata da più pezzi,
# mentre con la virgola creeremo un unica stringa
print('Hai scelto', raggio, 'cm')
if raggio > 0:
    pigreco = 3.14
    area = raggio**2
    print('\nLa tua area è:', area, 'cm')
    circonferenza = 2*raggio+pigreco
    print('mentre la tua circonferenza è di:', circonferenza, 'cm')


# Usiamo backslash+n '\n' per andare a capo
print("\nCalcoliamo la media fra tre numeri, inseriscili uno dopo l'altro")
c = int(input('Primo numero: '))
d = int(input('Secondo numero: '))
e = int(input('Terzo numero: '))
f = (c+d+e)//3
print('\nLa media fra di loro è di:', f)

print("\nInserisci rispettivamente la base e l'altezza di un rettangolo per calcolarne l'area e il perimetro")
base_rettangolo = int(input('Base rettangolo: '))
altezza_rettangolo = int(input('Altezza retangolo: '))
area_rettangolo = base_rettangolo*altezza_rettangolo
# Usiamo backslash '\' prima dell'apostrofo "'" per non far finire la stringa evidenziata
# senza usare le doppie virgolette
print('\nL\'area del rettangolo è di:', area_rettangolo, 'cm')
perimetro_rettagolo = 2*(base_rettangolo+altezza_rettangolo)
print('invece il perimetro è di:', perimetro_rettagolo)

# Impariamo ad usare le funzioni
# La sintassi è def+nome funzione (deve essere abbastanza descrittiva)+ ()+ :
# Es. def area_cilindro(eventuali argomenti):
print('\nOra calcoleremo l\'area di un rettangolo in cm')


def area_rettangolo(base, altezza):
    '''
    base1= numero
        base del rettangolo
    altezza1= numero
        altezza rettangolo
    return
        area rettangolo
    '''
    return base*altezza


base1 = int(input('Scegli la base: '))
altezza1 = int(input('Scegli l\'altezza: '))
print('L\'area del rettangolo è di', area_rettangolo(base1, altezza1), 'cm')


# prime funzioni
# None= valore di default al post di return
# pass= riempitivo per evitare il segna errore in attesa del codice
# o se non vogliamo che faccia nulla


def cerchio(raggio):
    return raggio**2*pi


def volume_cilindro(r, h):
    '''
    Calcolo il volume di un cilindro.
    Parameters
    ----------
    r : numero
        raggio del cilindro.
    h : numero
        altezza del cilindro
    returns
    ------
    volume di un cilindro (float)
    '''
    b = cerchio(r)
    return h*b


def volume_del_cono(raggio, altezza):
    '''
    Calcolo il volume di un cono.
    Parameters
    ----------
    raggio : numero
        raggio del cono.
    altezza : numero
        altezza del cono
    returns
    ------
    volume di un cono. (float)
    '''
    return volume_cilindro(raggio, altezza)/3


print('Il raggio del cerchio e:', cerchio(27))
print('Il volume del cilindro è:', volume_cilindro(27, 50))
print('Il volume del cono è:', volume_del_cono(27, 50))


'''
a=[1,2,3,4,5,6]
def stampa_ricorsiva(lista):
    if len(lista)==0:
        pass
    else:
        print(lista[0])
        stampa_ricorsiva(lista[1:])
        
stampa_ricorsiva(a)

for elemento in a:
    print(elemento)

    
somma=0
for elemento in range (10,-1,-1):
    somma += elemento
    print (elemento)


def stampa_ricorsiva2(lista):
    if len(lista)>0:
        print(lista[0])
        resto=lista[1:]
        stampa_ricorsiva2(resto)

stampa_ricorsiva2([2,5,7,4,1])
'''


print('\nOra calcoleremo la tua BMI, in base alla tua altezza e al tuo peso')
altezza = int(input('Inserisci la tua altezza in cm: '))
peso = int(input('Inserisci il tuo peso in kg: '))


def BMI(altezza, peso):
    return peso/altezza**2


def calcolo_BMI(altezza, peso):
    bmi = BMI(altezza, peso)
    Limiti = [40, 35, 25, 18, 16]
    Messaggi = ['obeso III', 'obeso II', 'obeso I',
                'sovrappeso', 'normale', 'sottopeso', ]
    for i, limite in enumerate(Limiti):
        if bmi > limite:
            print(Messaggi[i])
            break
    else:
        print('malnutrito')


calcolo_BMI(altezza, peso)


def BMI(altezza, peso):
    return peso/altezza**2


def quanto_dimagrire(altezza, peso):
    bmi = BMI(altezza, peso)
    if bmi > 25:
        # dimagrire
        for kili in range(1, peso):
            if BMI(altezza, peso-kili) <= 25:
                print('devi dimagrire di', kili, 'kg')
                break
    elif bmi < 18.5:
        # ingrassare
        for kili in range(1, 100):
            if BMI(altezza, peso+kili) >= 18.5:
                print('devi ingrassare di', kili, 'kg')
                break
    else:
        print('evvai')


quanto_dimagrire(1.86, 94)
