# Le versioni della funzione costruiscono una matrice n×m dove le colonne pari 
# sono riempite con numeri crescenti dall'alto verso il basso (da 1 a n), 
# mentre le colonne dispari sono riempite con numeri decrescenti dall'alto verso il basso 
# (da n a 1).

import numpy as np

def scalivert(n,m):
    nuova = np.zeros((n,m))
    for x in range(0,len(nuova[0]), 2):
        for y in range(len(nuova)):
            nuova[y][x] = y+1
    for x in range(1,len(nuova[0]), 2):
        for y in range(len(nuova)):
            nuova[y][x] = n-y
    return nuova

print(scalivert(4,4))
assert np.allclose(scalivert(1,1), np.array([ [1] ]))
assert np.allclose(scalivert(1,2), np.array([ [1,1] ]))
assert np.allclose(scalivert(2,1), np.array([ [1],
[2]]))
assert np.allclose(scalivert(2,2), np.array([ [1,2],
[2,1]]))
assert type(scalivert(2,2)) == np.ndarray
assert np.allclose(scalivert(4,5), np.array([ [1,4,1,4,1],
[2,3,2,3,2],
[3,2,3,2,3],
[4,1,4,1,4]]))

def scalivert1(n,m):
    nuova = np.zeros((n,m))
    for y in range(n):
        for x in range(m):
            if x % 2 == 0:
                nuova[y][x] = y + 1
            else:
                nuova[y][x] = n - y
    return nuova

print(scalivert1(5,5))

def scalivert_pro(n,m):
    nuova = np.zeros((n,m))
    nuova[:, ::2] = np.transpose([np.arange(1,n+1,1)])
    nuova[:, 1::2] = np.transpose([np.arange(n,0,-1)])
    return nuova

print(scalivert_pro(5,5))

def sclivert2(n,m):
    nuova = np.zeros((n,m))
    for y in range(n):
        for x in range(m):
            if x % 2 == 0:
                nuova[y][x] = y + 1
            else:
                nuova[y][x] = n - y
    return nuova

print(sclivert2(5,5))

def scalivert_pro1(n,m):
    nuova = np.zeros((n,m))
    nuova[:, ::2] = np.transpose([np.arange(1,n+1)])
    nuova[:, 1::2] = np.transpose([np.arange(n,0,-1)])
    return nuova

print(scalivert_pro1(5,5))

def sclivert_pro2(n,m):
    nuova = np.zeros((n,m))#, dtype=int)
    nuova[:, ::2] = np.tile(np.transpose([np.arange(1, n+1)]), (m+1) // 2)
    nuova[:, 1::2] = np.tile(np.transpose([np.arange(n,0,-1)]), m//2)
    return nuova

print(sclivert_pro2(5,5))

assert np.allclose(scalivert_pro(1,1), np.array([ [1] ]))
assert np.allclose(scalivert_pro(1,2), np.array([ [1,1] ]))
assert np.allclose(scalivert_pro(2,1), np.array([ [1],
[2]]))
assert np.allclose(scalivert_pro(2,2), np.array([ [1,2],
[2,1]]))
assert type(scalivert_pro(2,2)) == np.ndarray
assert np.allclose(scalivert_pro(4,5), np.array([ [1,4,1,4,1],
[2,3,2,3,2],
[3,2,3,2,3],
[4,1,4,1,4]]))
print()

def sclivert_pro3(n,m):
    nuova = np.zeros((n,m))#, dtype=int)
    nuova[::2] = np.arange(1, n+1)
    nuova[1::2] = np.arange(n,0,-1)
    return nuova

print(sclivert_pro3(5,5))
print()