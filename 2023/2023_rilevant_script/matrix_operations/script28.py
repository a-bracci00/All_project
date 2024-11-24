#La funzione mul(mat1, mat2) esegue il prodotto matrice-matrice tra due matrici mat1 e mat2

def mul(mat1, mat2): # righe = len(mat) colonne = len(mat[0])
    #se il numero di colonne di mat1 è diverso dal numero di righe di mat2
    #blocca tutto
    n = len(mat1) #righe mat1
    m = len(mat1[0]) #colonne mat1
    q = len(mat2) # righe mat2
    p = len(mat2[0]) #colonne mat2

    if m != len(mat2):
        raise ValueError("il numero di colonne di mat1 %s deve essere uguale al numero di righe di mat2 %s !" % (m, len(mat2)))
    
    ret = [[0]*p for i in range(n)]
    for i in range(n):
        for j in range(p):
            ret[i][j] = 0
            for k in range(m):
                ret[i][j] += mat1[i][k] * mat2[k][j]
    return ret


m41 = [ [3,5],
[7,1],
[9,4],
[8,7] ]
m42 = [ [4,1,5],
[8,5,2] ]

[print(x) for x in mul(m41, m42)]

print()