# vari esercizi utilizzando matplotlib

#%matplotlib inline
#import matplotlib_inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,11,1.)
print(x)
y = 2*x + 10
print(y)
print(plt.plot(x, y, 'bo'))
print(plt.title('Performance Attesa Esame Fisica'))
print(plt.xlabel('Esercizi svolti'))
print(plt.ylabel('Votazione esame'))
plt.show()

x = np.arange(0, 11, 1.)
#x = np.array(list(range(11)))
y = 2*x + 10
print(y)
g = 'nutella'
plt.plot(x,y, 'r^', label=g)
plt.legend(loc = 'upper left')
#plt.plot(y, x, 'g+') 
#plt.plot( x-1, y-1, 'bH')
#plt.plot(x*3, y*2, 'b^')
print(type(np.arange(0, 11, 1.)))
#help(plt.plot)
plt.show()

x = np.arange(0,11,1.)
y = 2*x + 10

plt.plot(x, y, 'r-')
print(plt.title('Performance Attesa Esame Fisica'))
print(plt.xlabel('Esercizi svolti'))
print(plt.ylabel('Votazione esame'))
plt.annotate(
    'Risultato minimo\nper la sufficienza', xy =(4, 9*2), arrowprops={'arrowstyle':'->'}, xytext=(6, 17.2) )
plt.grid()
plt.show()

x = np.arange(0,11, 1.)
y = 2*x +10
plt.grid()
plt.plot(x,y,'r-')
plt.axis([0, 10, 0, 30])
plt.annotate('risultato minimo\nper la sufficienza',
             xy = (4, 18), arrowprops={'arrowstyle':'->'}, xytext=(6,17.2))

plt.title('Performance attesa esame Fisica')
plt.xlabel('Esercizi svolti')
plt.ylabel('Votazione esame')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
xs = np.array(list(range(1,7)))
ys = list(range(2,13,2))
plt.plot(xs, ys, 'ro')
plt.title('La mai funzione')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(xs, list('abcdef'))
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10

fig = plt.figure(figsize=(10,2))
ax = fig.add_subplot(111)#, projection = '3d')
ax.plot(x,y, 'o')
ax.set_title('Performance attesa Esame Fisica')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')
plt.tight_layout()
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(x, y, 'o')
ax.set_title('Performance attesa Esame Fisica')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Votazione esame')
plt.tight_layout()
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10
fig = plt.figure()
ax = fig.add_subplot(121)
ax.plot(x, y,'bo')
ax.set_title('Grafico a sinistra')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(122)
ax.plot(x, -y, 'bo')
ax.set_title('Grafico a destra')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')
plt.tight_layout()
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y,'r-')
ax.set_title('Grafico a sinistra')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(212)
ax.plot(x, -y, 'bo')
ax.set_title('Grafico a destra')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')
plt.tight_layout()
plt.show()

x = np.arange(0, 11, 1.)
y = 2*x + 10
fig = plt.figure() #creo una figura principale
ax = fig.add_subplot(321) 
ax.plot(x, y,'bo')
ax.set_title('Grafico 1')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(322)
ax.plot(x, y, 'bo')
ax.set_title('Grafico 2')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(323)
ax.plot(x, y,'bo')
ax.set_title('Grafico 3')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(324)
ax.plot(x, y, 'bo')
ax.set_title('Grafico 4')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(325)
ax.plot(x, y,'bo')
ax.set_title('Grafico 5')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')

ax = fig.add_subplot(326)
ax.plot(x, y, 'bo')
ax.set_title('Grafico 6')
ax.set_xlabel('Esercizi svolti')
ax.set_ylabel('Valutazione esame')
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
xs = [1,2,3,4]
ys = [7,5,8,2]
plt.bar(xs, ys,
        0.5,
        color = 'green',
        align = 'center')
plt.show()

print(plt.subplots())
fig, ax = plt.subplots()
print(fig, ax)


mu = 0 #media
sigma = 1 #sqm
num_bins = 50 # numero di colonne per l'istogramma
#print(np.random.seed(12))
segnale = np.random.normal(mu, sigma, 500)
fig, ax = plt.subplots()
ax.plot(segnale)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
mu = 0
sigma = 1
np.random.seed(0)# sempre la stessa sequenza di numeri pseudocasuali
segnale = np.random.normal(mu, sigma, 500)
num_bins = 50
n, bins, columns = ax.hist(segnale, num_bins)
ax.set_xlabel('Segnale')
ax.set_ylabel('Numero di elementi')
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()
plt.show()

fig, ax = plt.subplots()
segnale = [1,1,1,1,1, 2,2, 3,3,3,3,3,3,3,3]
num_bins = 50
n, bins, columns = ax.hist(segnale, num_bins)
print('N:',n,'\n','Bins:', bins,'\n', 'Columns:', columns)
ax.set_xlabel('Segnale')
ax.set_ylabel('Numero di elementi')
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()
plt.show()

import math

fig, ax = plt.subplots()
segnale = [3,5,3,5]
num_bins = 50 # round(math.sqrt(len(segnale)))*10
n, bins, columns = ax.hist(segnale, num_bins)
print('N:',n,'\n','Bins:', bins,'\n', 'Columns:', columns)
ax.set_xlabel('Segnale')
ax.set_ylabel('Numero di elementi')
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()
plt.show()

fig, ax = plt.subplots()
segnale = [-3,-3,-3,7,7,7,7,7]
num_bins = 50 #range(min(segnale), max(segnale)+2)
n, bins, columns = ax.hist(segnale, num_bins)
print('N:',n,'\n','Bins:', bins[:-1],'\n', 'Columns:', columns)
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
ax.set_xlabel('Segnale')
ax.set_ylabel('Segnali intercettati')

fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

fig, ax = plt.subplots()
np.random.seed(0)
mu = 0
sigma = 1
x = np.random.normal(mu, sigma, 500)
n, bins, columns = ax.hist(x, 50, density=True)
print('N:',n,'\n','Bins:', bins[:-1],'\n', 'Columns:', columns)
ax.set_title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
ax.set_xlabel('Segnali')
ax.set_ylabel('Segnali intercettati')
y = norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Segnale')
ax.set_ylabel('Densità di probabilità')
ax.set_title(r'Istogramma di una Gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()
plt.show()

np.random.seed(0)
mu = 0
sigma = 1
x = np.random.normal(mu, sigma, 500)
n, bins, columns = plt.hist(x, 50, density=True)#, color='white')
print('N:',n,'\n','Bins:', bins[:-1],'\n', 'Columns:', columns)
plt.title(r'Istogramma di una gaussiana con $\mu=0$, $\sigma=1$')
plt.xlabel('Segnali')
plt.ylabel('Segnali intercettati')
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, '--')
plt.xlabel('Segnale')
plt.ylabel('Densità di probabilità')
plt.title(r'Istogramma di una Gaussiana con $\mu=0$, $\sigma=1$')
#fig.tight_layout()
plt.show()

print()

labels = ['Pippo', 'Pluto', 'Paperino']
y = np.array([3,4,1])
esplodi = [0, 0, 0.1]
fig, ax = plt.subplots()
ax.pie(y, labels=labels, explode= esplodi, autopct='%1.1f%%', startangle=90)
ax.set_title('Spar(t)izione della pizza')
fig.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

labels = ['tre', 'quattro', 'uno']
y = [3,4,1]
esplodi = [0, 0, 0.1]
#print(plt.subplots(ncols= 3))
fig, (ax1, ax2) = plt.subplots(ncols = 2)
ax1.pie(y, labels = labels, explode = esplodi, autopct = '%1.1f%%', startangle = 90)
ax1.set_title('Spartizione della pizza')
xticks = [1,2,3]
ax2.bar(xticks, y, align= 'center', color = ['b', 'r', 'g'], width = 0.3)
ax2.set_title('Partizione della pizza in bar')
ax2.set_xticks(xticks)
ax2.set_xticklabels(labels)
fig.tight_layout()
plt.show()
#help(plt.bar)

#cambia lo sfondo di tutti i grafici da qui in poi
plt.rcParams['axes.facecolor'] = 'azure'
plt.plot(np.array([1,2,3]), [4,5,6])
plt.show()

#rimette lo sfondo bianco a tutti i grafici futuri
plt.rcParams['axes.facecolor'] = 'white'
plt.plot(np.array([1,2,3]), [4,5,6])
plt.show()

#importante da settare quando mettiamo del testo
#matplotlib non adatta automaticamente le dimensioni
plt.xlim(0, 450)
plt.ylim(0, 600)
plt.text(250, 
         450, 
         'Ciao !', 
         fontsize = 40,
         fontweight = 'bold',
         color = 'lightgreen',
         ha = 'center', #centra orizzontalmente il testo
         va = 'center') #centra verticalmente il testo
plt.show()

fig = plt.figure(figsize=(6,6))
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

plt.xlim(0, 150) #importante da settare quando mettiamo delle immagini
plt.ylim(0, 200) #perchè matplolib non ridimensiona automaticamante
ax = fig.gca()
img = plt.imread('OIP.jpg')
ax.add_artist(AnnotationBbox(OffsetImage(img, zoom=0.5), (50, 100), frameon=False))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
#regolare intensità colore
plt.plot(np.array([150, 175]), [25, 400],
         color = 'green',
         alpha = 1.0, #colore pieno
         linewidth = 10)

plt.plot([100, 125], [25, 400],
         color = 'green',
         alpha =  0.3,  #più leggero
         linewidth = 10)

plt.plot([50, 75], [25, 400],
         color = 'green',
         alpha = 0.1, #quasi invisibile
         linewidth = 10)

plt.show()

plt.rcParams['axes.facecolor'] = 'azure'
fig = plt.figure(figsize = (7,7))

plt.xlim(0, 150)
plt.ylim(0, 200)
ax = fig.gca()
img = plt.imread('OIP.PNG')
ax.add_artist(AnnotationBbox(OffsetImage(img, zoom = 0.5), (100, 200), frameon=False))

plt.xlim(0, 450)
plt.ylim(0, 600)
plt.text(250,
         450,
         'Be fancy',
         fontsize = 30,
         fontweight = 'bold',
         color = 'lightpink',
         ha = 'center', #centra orizzontalmente il testo
         va = 'center') #centra verticalmente il testo)

plt.plot([25, 400], [100, 100], color = 'blue', linewidth = 10, alpha = 0.3)
plt.plot([25, 400], [200, 200], color = 'blue', linewidth = 10, alpha = 0.5)
plt.plot([25, 400], [300, 300], color = 'blue', linewidth = 10, alpha = 1.0)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

part1 = [[1, 10], [0, 0]]
part2 = ([4, 4], [0, 4])
part3 = {"x": [8, 8], "y": [0, 4]}
more_parts = {
        "part4":[[4, 8], [4, 4]],
        "part5":[[4, 6], [4, 6]],
        "part6":[[8, 6], [4, 6]]
        }

plt.plot(np.array(part1[0]), part1[1])
#plt.show()
plt.plot(part2[0], part2[1])
#plt.show()
plt.plot(part3['x'], part3['y'])
#plt.show()
plt.plot(more_parts['part4'][0], more_parts['part4'][1])
#plt.show()
plt.plot(more_parts['part5'][0], more_parts['part5'][1])
#plt.show()
plt.plot(more_parts['part6'][0], more_parts['part6'][1])
plt.show()

lista = np.array([
    #['giorno', 'benchmark', 'titolo'],
    [0, 18, 9],
    [2, 19, 11],
    [4, 15, 7],
    [6, 4, 9],
    [8, 8, 11],
    [10, 16, 12],
    [12, 17, 13],
    [14, 11, 9],
    [16, 9, 11],
    [18, 5, 10]]
)

plt.title('Performance titolo vs benchmark')
plt.xlabel('Giorni')
plt.ylabel('Valore $')
plt.xticks(lista[:, 0])
plt.plot(lista[:, 0], lista[:,1], color='blue')
plt.plot(lista[:, 0], lista[:, 2], color='orange')
plt.plot(lista[:, 0], [np.max(lista[:,2]) for x in lista], linestyle='--', color = 'green')
plt.plot(lista[:, 0], np.full(len(lista), min(lista[:, 2])), linestyle='--', color = 'red')

plt.show()

import matplotlib.pyplot as plt
import numpy as np
import random

x = np.array(range(0,500))
lista = np.array([random.expovariate(0.6 / 2.0) for _ in range(500)])
lista.sort()
lista2 = [random.uniform(1, 50) for _ in range(500)]
lista2.sort()
plt.plot(x, lista2)
plt.plot(x, lista)

plt.show()