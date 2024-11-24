# La funzione aggiunge delle "cornici" di mattonelle attorno e tra le righe della matrice mat, 
# restituendo una nuova matrice con le modifiche. 
# Se la dimensione di mattonelle non è corretta rispetto a mat, solleva un'eccezione

def cantiere(mat, mattonelle):
    if len(mattonelle) != len(mat)+1:
        raise ValueError
    nuova = [x[:] for x in mat]

    lista_matt = []
    for el in range(len(mattonelle)):
        if el == 0:
            lista = [mattonelle[el] for x in range(len(mattonelle))]
            lista[0:0] = ' '
            lista.append(' ')
            lista_matt.append(lista)
        else:
            lista = [mattonelle[el] for x in range(len(mattonelle))]
            lista[0:0] = '|'
            lista.append('|')
            lista_matt.append(lista)

    nuovissima = []
    for y in range(len(nuova)):
        nuova[y][0:0] = '|'
        nuova[y].append('|')
    
    for x,y in zip(lista_matt, nuova):
        nuovissima.append(x)
        nuovissima.append(y)
    nuovissima.append(lista_matt[-1])
    
    return nuovissima

m = [['f','e','a','b'],
['a','c','g','f'],
['b','c','d','f']]

matto = ['^','-','_','=']
[print(x) for x in cantiere(m, matto)]
print()
[print(''.join(x)) for x in cantiere(m, matto)]

m1 = [['a']]
cantiere(m1, ['^','='])
