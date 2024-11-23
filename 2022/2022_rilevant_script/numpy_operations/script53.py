# Le versioni della funzione creano una matrice n×m con un riempimento specifico, 
# vincolando m a essere pari. Se m è dispari, solleva un'eccezione (ValueError)

import numpy as np

def scendisali_pro(n,m):
    if m % 2 != 0:
        raise ValueError
    nuova = np.zeros((n,m))
    nuova[1::2, :m//2] = np.arange(0,m//2)
    nuova[::2, m//2:] = np.arange(m//2-1,-1,-1)
    return nuova

print(scendisali_pro(6,10))

assert np.allclose(scendisali_pro(2,2), np.array([[0., 0.],
[0., 0.]]))
assert type(scendisali_pro(2,2)) == np.ndarray
assert np.allclose(scendisali_pro(2,6), np.array([[0., 0., 0., 2., 1., 0.],
[0., 1., 2., 0., 0., 0.]]))
assert np.allclose(scendisali_pro(6,10), np.array([[0., 0., 0., 0., 0., 4., 3., 2., 1., 0.],
[0., 1., 2., 3., 4., 0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0., 4., 3., 2., 1., 0.],
[0., 1., 2., 3., 4., 0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0., 4., 3., 2., 1., 0.],
[0., 1., 2., 3., 4., 0., 0., 0., 0., 0.]]))
try:
    scendisali_pro(2,3)
    raise Exception("Avrei dovuto fallire prima!")
except ValueError:
    pass
print()

def scendisali(n,m):
    if m % 2 != 0:
        raise ValueError
    mat = np.zeros((n,m))
    for y in range(0,len(mat),2):
        for x in range(len(mat[0])//2):
            mat[y][x + len(mat[0])//2] = len(mat[0])//2 - x -1
    for y in range(1,len(mat),2):
       for x in range(len(mat[0])//2):
            mat[y][x] = x
    return mat

print(scendisali(6,10))
assert np.allclose(scendisali(2,2), np.array([[0., 0.],
[0., 0.]]))
assert type(scendisali(2,2)) == np.ndarray
assert np.allclose(scendisali(2,6), np.array([[0., 0., 0., 2., 1., 0.],
[0., 1., 2., 0., 0., 0.]]))

import numpy as np

def scendisali(n,m):
    nuova = np.zeros((n,m))
    for y in range(0,n,2):
        for x in range(m//(2)):
            nuova[y][x+m//2] = m//2 -x -1
    for y in range(1,n,2):
        for x in range(m//2):
            nuova[y][x] = x
    return nuova

print(scendisali(6,10))
assert np.allclose(scendisali(2,2), np.array([[0., 0.],
[0., 0.]]))
assert type(scendisali(2,2)) == np.ndarray
assert np.allclose(scendisali(2,6), np.array([[0., 0., 0., 2., 1., 0.],
[0., 1., 2., 0., 0., 0.]]))

def scendisali_pro(n,m):
    if m % 2 != 0:
        raise ValueError
    nuova = np.zeros((n,m))
    nuova[0::2, m//2:] = np.arange(m//2-1, -1, -1)
    nuova[1::2, :m//2] = np.arange(0,m//2)
    return nuova

print(scendisali_pro(6,10))
assert np.allclose(scendisali_pro(2,2), np.array([[0., 0.],
[0., 0.]]))
assert type(scendisali_pro(2,2)) == np.ndarray
assert np.allclose(scendisali_pro(2,6), np.array([[0., 0., 0., 2., 1., 0.],
[0., 1., 2., 0., 0., 0.]]))
try:
    scendisali_pro(2,3)
    raise Exception("Avrei dovuto fallire prima!")
except ValueError:
    pass
print()
