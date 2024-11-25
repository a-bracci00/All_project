import math

path_connettività = 'connettività.txt'
path_spostamento_nodi = 'spostamento_nodi.txt'

def connettivita(path):
    trave_nodi = {}
    with open(path) as f:
        for riga in f:
            riga_senza_spazi = riga.strip()
            elementi_riga = riga_senza_spazi.split()
            trave_nodi[int(elementi_riga[0])] = int(elementi_riga[6]), int(elementi_riga[7])
    #print('ok')
    return trave_nodi

diz_travi_nodi = connettivita(path_connettività)

def spostamento(path):
    #apro il file
    #imposto un count
    count = 0
    #creo una lista che conterrà le coordinate di ogni nodo
    inizio_nodi = []
    #creo una lista che conterrà le coordinate dell'inizio dei numeri
    inizio_numeri = []
    #creo una lista che conterrà le coordinate della fine dei numeri
    fine_numeri = []
    with open(path) as f:
        #imposto un count
        #per ogni riga in f
        for riga in f:
            #aggiungi uno al count
            count += 1
            #prendo la riga e ne elimino gli spazi
            riga = riga.strip()
            #se inizia per NODE
            if riga.startswith('NODE'):
                #aggiungi la coordinata in inizio nodi
                inizio_nodi.append(count)
            #se inizia per TIME
            if riga.startswith('TIME'):
                #aggiungi la coordinata a inizio numeri
                inizio_numeri.append(count+1)
            #se inizia per Maximum
            if riga.startswith('Maximum'):
                #aggiungi la coordinata a fine numeri
                fine_numeri.append(count-3)
    #ritorna le tre liste
    #print('ok1')
    return(inizio_nodi, inizio_numeri, fine_numeri)

def prendi_numeri_in_base_alla_trave(diz, spostamento, path):
    lista_numeri_nodi = []
    
    for trave in diz:
        nodo = trave-1
        with open(path) as f:
            lista_numeri_A = (f.readlines()[spostamento[1][nodo]:spostamento[2][nodo]])
            lista_numeri_nodi.append(lista_numeri_A)

    return lista_numeri_nodi

spostamento = spostamento(path_spostamento_nodi)
liste_nodi = prendi_numeri_in_base_alla_trave(diz_travi_nodi, spostamento, path_spostamento_nodi)

def pulisci(liste):
    liste_pulite = []
    for lista in liste:
        righe_in_liste = []
        for riga in lista:
            riga = riga.strip()
            riga = riga.split()
            righe_in_liste.append(riga)
        righe_in_liste.pop()    
        liste_pulite.append(righe_in_liste)

    return liste_pulite

valori_spostamento = pulisci(liste_nodi)

def calcolo(valori, diz):
    #liste_risultati = []
    for trave in diz:
        nodo1 = diz[trave][0]-1
        nodo2 = diz[trave][1]-1
        #print(nodo1, nodo2)
        lista1 = valori[nodo1]
        lista2 = valori[nodo2]
        #print(lista1, lista2)
        lista_risultati = []
        for x,y in zip(lista1, lista2):
            #print(x,y)
            calcolo = math.sqrt((float(x[1]) - float(y[1]))**2 + (float(x[3]) - float(y[3]))**2 + (float(x[2]) - float(y[2]))**2)
            #print(calcolo)
            lista_risultati.append(calcolo)
        #liste_risultati.append(max(lista_risultati))
        print((max(lista_risultati)))
    #return(liste_risultati)
    #print(liste_risultati)
    #for i in liste_risultati: 
        #print(i)

#liste = calcolo(valori_spostamento, diz_travi_nodi)
calcolo(valori_spostamento, diz_travi_nodi)

    
