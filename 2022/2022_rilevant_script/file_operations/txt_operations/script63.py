# Qualche operazione semplice su dei file txt

import html
def sistema_file(file):
    with open(file, encoding='utf-8') as f:
        titoli = []
        spazi = []
        valori = []
        #completa = []
        for riga in f:
            riga = riga.strip()
            riga_divisa = riga.split(':')
            if riga_divisa[0].endswith('Title'):
                titoli.append(riga_divisa[1])
            elif riga_divisa[0].endswith('Level'):
                spazi.append(riga_divisa[1])
            elif riga_divisa[0].endswith('Number'):
                valori.append(riga_divisa[1])
        for y in range(len(titoli)):
            if (int(spazi[y])-1)*'\t' == '':
                print(html.unescape(titoli[y][1:]), valori[y][1:])
            else:
                print((int(spazi[y])-1)*'\t', html.unescape(titoli[y][1:]), valori[y][1:])
    #print(html.unescape('ieri sono andato &#232;'))
        #return completa
#print(0*' ' +'c')
sistema_file('immersione-in-python-toc.txt')
print()

with open('immersione-in-python-toc.txt') as f:
    linea = f.readline()
    while linea != '':
        linea = f.readline().strip()
        titolo = html.unescape(linea[len('BookmarkTitle: '):])
        linea = f.readline().rstrip()
        livello = int(linea[len('BookmarkLevel: '):])
        linea = f.readline().rstrip()
        pagina = linea[len('BookmarkPageNumber: '):]
        print(('    ' * livello) + titolo + ' ' + pagina)
        linea = f.readline()
print()