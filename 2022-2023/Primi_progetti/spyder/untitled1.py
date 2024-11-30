# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:35:29 2022

@author: UTENTE
"""
#%%
#leggo il file json e ne estraggo il dizionario/struttura
import json

with open ('api.github.com.json', encoding='utf-8') as F:
    dizionario= json.load(F)
#costruisco un dizionario e lo salvo in un file json
with open ('api.github.com.2.json', mode='w', encoding='utf-8') as F:
    json.dump(dizionario,F, indent=(4))

#%%
#leggo una pagina
import requests
pagina= requests.get('https://python.org')
status= pagina.status_code
contenuto= pagina.text

#%%
import requests
pagina_json=requests.get('https://api.github.com')
risultato= pagina_json.json()
#%%
#leggo un'immagine
import requests
logo= requests.get('https://www.python.org/static/img/python-logo@2x.png')
dati= logo.content
with open('logo.png', mode='wb') as F:
    F.write(dati)
#%%
with open('dati.txt', mode='w', encoding='utf-8') as F:
    print('10,37,       81    ,    22,-5,\n', file=F)
    print('    42,\n', file=F)
    print('89,', file=F)
with open('dati.txt', encoding='utf-8') as F:
    testo=F.read()
    #rimuovo le virgole
    testo= testo.replace(',',' ')
    #uso split per separare i numeri
    frammenti=testo.split()
    #converto i frammenti di testo in numeri
    numeri=[int(valore) for valore in frammenti]
#%%
#lettura di matrici

with open('matrice.txt.txt',encoding ='utf8') as F:
    matrice=[]
    for riga in F:
        #la splitto e converto in numeri
        frammenti= riga.split('|')
        numeri= [int(pezzo) for pezzo in frammenti]
        #aggiungiamola alla matrice
        matrice.appent(numeri)
        #avremo una lista di liste
        #con mantrice= matrice+numeri avremo una lista singola
#%%
# ista comprehension
with open('matrice.txt.txt',encoding='utf8') as F:
    #ripeto per ogni riga
    matrice2=[
        [int(el) for el in riga.split('|')] for riga in F
        ]
#%%
#lista funzionale
with open('matrice.txt.txt',encoding='utf8') as F:
    def converti_riga(riga):
        return list(map(int,riga.split('|')))
    matrice3=list(map(converti_riga,F))
#%%
