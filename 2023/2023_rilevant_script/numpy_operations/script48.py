#Le verioni della funzione calcolano la media degli elementi nella metà sinistra delle colonne e 
# la media di tutti gli elementi delle righe, 
# restituendo questi due valori in una matrice a una riga e due colonne.

import numpy as np

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