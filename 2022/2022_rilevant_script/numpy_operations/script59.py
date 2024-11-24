# La funzione `macchina` calcola la spesa totale di ciascun individuo 
# e la spesa per ciascun tipo di bevanda, utilizzando la somma delle colonne e 
# delle righe di una matrice. Poi, stampa i risultati, indicando chi ha speso di 
# più tra gli individui e quale bevanda è stata la preferita, ovvero quella con la 
# spesa più alta.

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