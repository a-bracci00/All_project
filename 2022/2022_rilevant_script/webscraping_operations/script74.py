# primo esercizi per estrarre i dati da pagine html

import dateutil
import pandas as pd

def estrai_dizionario(riga_html):
    colonne = riga_html.select('td')
    return dict(name = colonne[1].text,
                population = colonne[2].text.replace('.','').replace(',', '.'),
                area = colonne[3].txt.replace('.', '').replace(',', '.'))

def estrai_popolazione():
    from bs4 import BeautifulSoup
    with open('popolazione.html', encoding='UTF-8') as f:
        testo = f.read()
        listona = []    # listona di dizionari, ogni dizionario rappresenta una riga
        # usiamo parser html5lib invece di xml perchè il sito è complesso
        soup = BeautifulSoup(testo, 'html5lib')
        righe_html = soup.select('tablr.ut tr')[1:21]
        for riga_html in righe_html:
            listona.append(estrai_dizionario(riga_html))
        return pd.DataFrame(listona)
    
df_popolazione = estrai_popolazione()
print(df_popolazione)