# prova per usare la libreria numba

#from numba import jit 
import time

#@jit # funziona solo con la sintassi base di python, senza moduli extra
def conto():
    for x in range(1000000000+1):
        count = x
    print('ok', x)

start = time.time()
conto()
end = time.time()
print(end-start)