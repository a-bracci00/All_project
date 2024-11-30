'''
if True:
    print('questo')
    print('sarà')
    print('stampato')
else:
    print('quest\'altro')
    print('non lo sarà')

if 'ciao':
    print('scemo')
else:
    print('stupido')

if False:
    print('scemo')
else:
    print('bravo')

if 0:
    print('ottimo')
else:
    print('eccellente')

if None:
    print('noneee')
else:
    print('io si')

if []:
    print('non lo sarà')
else:
    print('forse si')

ciao = 'ciao '
mondo = 'mondo'
ciao_mondo = ciao + mondo
print(ciao_mondo)

cinque = 5
print(ciao + str(cinque))

ciaoo = 'ciao %s' % 7
print(ciaoo)

gatto = 'miao'

ciaooo = 'che %s finalmente imparo %s' % (gatto, 'python')
print(ciaooo)

print('trento'.capitalize())
print('trento'.upper())
print('trento'.count('t'))

x = ['ciao', 'soft', 'python']
x1 = [gatto, 123, {'a': 'b'}]

x2, x3, x4 = x[0], x[1], x[2]


print(x, x1, x2, x3, x4)

x[1] = 'tfos'
x[2] = 'nohtyp'

print(len(x))

print(x, x1, x2, x3, x4)

print(x[len(x)-1])

print(x[-1])

x5 = []
x5.append('ciao')
x5.append('soft')
print(x5)

x6 = [8, 2, 4]
x6.sort(reverse=True)
x7 = sorted(x6)
print(x6)

#x8 = ['CIAO', 25, 'SOFT', 12, 'PYTHON', 22]
# x8.sort()
# print(x8)

help(sorted)
x9 = ['soft', 'ciao', 'python']
x10 = sorted(x9, reverse=True)
print(x9, x10)
x9.sort()
x11 = list(reversed(['soft', 'ciao', 'python']))
print(x9, x11)

d = {'chiave 1': 'valore 1', 'chiave 2': 'valore 2'}
print(d)

print(d['chiave 1'])

print(d['chiave 2'])

d['chiave 3'] = 123

print(d)

d['chiave 4'] = ('io', 'sono', 'una', 'tupla')

print(d)

d['dizionario 2'] = {'chiave 1': 'scemo', 'chiave 2': 'sei',
                     'chiave 3': 'scemo', 'chiave 4': 'rimani'}

print(d)

d[123] = 'valore 3'

print(d)

d[('io', 'sono', 'una', 'tupla')] = 'valore 4'

print(d)

d['a', 'b'] = 'valore 5'

print(d)

#d[{'chiave'}] = 'valore 6'

la = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o']

lb = ['z']
lb.extend(la[:3])
lb.extend(la[-3:])
print(lb)


parole = ['vedo', 'una', 'zebra', 'laggiù']
la = []
la.extend(parole[0][:3])
la.extend(parole[1][:3])
la.extend(parole[2][:3])
la.extend(parole[3][:3])
print(la)
'''
