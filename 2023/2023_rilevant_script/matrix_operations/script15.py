# creo una bandiera crescente in base alla grandezza in input
def bandiera(n,m):
    if m % 3 != 0:
        raise ValueError
    nuova = []
    for x in range(n):
        riga = []
        for y in range(m):
            riga.append(y // (m // 3))
        nuova.append(riga)
    return nuova

[print(x) for x in bandiera(5,12)]

assert bandiera(1,3) == [[0, 1, 2]]
assert bandiera(1,6) == [[0,0,1,1, 2,2]]
assert bandiera(4,6) == [[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2],
[0, 0, 1, 1, 2, 2]]
assert bandiera(2,9) == [[0, 0, 0, 1, 1, 1, 2, 2, 2],
[0, 0, 0, 1, 1, 1, 2, 2, 2]]
assert bandiera(5,12) == [[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]]
try:
    bandiera(3,7)
    raise Exception("Avrei dovuto fallire!")
except ValueError:
    pass

print()