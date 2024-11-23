# Le varie verisioni della funzione
# calcola la differenza tra il valore massimo e 
# minimo per ciascuna delle prime tre colonne di una matrice (mat) 
# e restituisce un array contenente queste differenze.

import numpy as np

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