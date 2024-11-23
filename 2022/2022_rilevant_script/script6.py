# creo matrice di una stringa
def cirpillino(stringa, n):
    if len(stringa) % n != 0:
        raise ValueError
    nuova = []
    for i in range(len(stringa)//n):
        nuova.append(list(stringa[i*n:(i+1)*n]))
    return nuova
    
[print(x) for x in cirpillino('cirpillinozimpirelloulalimpo', 4)]
print()