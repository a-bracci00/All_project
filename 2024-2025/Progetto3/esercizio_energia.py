path_energia = 'Energia0.5.txt'

def estrai_energia(path):
    with open(path) as f:
        for riga in f:
            riga = riga.strip()
            if 'element' in riga:
                riga = riga.split('|')
                print(riga[3].strip())

estrai_energia(path_energia)