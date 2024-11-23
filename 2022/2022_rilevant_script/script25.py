#La funzione discarica(mat, q) distribuisce una quantità q tra gli elementi della matrice mat,
# incrementando i valori fino a 7. Restituisce la lista dei valori scaricati e 
# solleva un'eccezione se q non è esaurito.

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