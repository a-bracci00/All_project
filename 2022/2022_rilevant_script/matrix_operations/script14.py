# unisco 2 matrici mettendo al seconda sulla sinistra
def attacca_sx_mod(mat1, mat2):
    for x in range(len(mat1)):
        mat1[x][0:0] = mat2[x]

m1 = [  [5,4,7],
        [0,7,9],
        [0,0,3] ]

m2 = [  [5,4,7],
        [7,7,9],
        [5,9,3] ]

print(m1, m2)
print(attacca_sx_mod(m1, m2))
print(m1)
m1 = [ ['a','b','c'],
['d','b','a'] ]
m2 = [ ['f','b'],
['g','h'] ]
res = [ ['f','b','a','b','c'],
['g','h','d','b','a'] ]
attacca_sx_mod(m1, m2)
assert m1 == res
print()