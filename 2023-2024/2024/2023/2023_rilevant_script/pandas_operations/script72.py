import pandas as pd
import numpy as np

df = pd.read_csv('astro_pi.csv', encoding='UTF-8')
print(df)#printa il file
df.info()#informazioni generali
print(df.shape) #righe colonne
print(df.describe())#dati di riepilogo
print()
print(df['Humidity'].describe())#colonna umidity dati riepilogo
print()
print(df.Humidity.describe())#colonna humidity dati riepilogo
print()
print(df.head())#prime tot righe, default = 5
print()
print(df.tail())#ultime tot righe, default = 5
print(df.columns) #i nomi di tutte le colonne
print(df.columns[2]) #nome della colonna 3
print(df.columns[4]) #nome colonna 5
print(list(df.columns)) #lista dei nomi delle colonne, superflua
print()
print(df.corr)# correlazione tra le colonne, con valori da -1.0 a +1.0

import pandas as pd
import numpy as np

meteo = pd.read_csv('meteo.csv', encoding='UTF-8')
print('COLUMNS:')
print(meteo.columns)
print()
print('INFO:')
print(meteo.info)
print()
print('HEAD:')
print(meteo.head())
print()

import matplotlib as mpl
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [2,4,6,8]
plt.plot(np.array(x),y) #possimao direttamente passare liste
plt.title('Qualche numero')
plt.show()

x = np.arange(0., 5., 0.1)
y = x**2
print(type(x), type(y))
plt.title('La parabola')
plt.plot(x,y)
plt.show()

print(plt.get_fignums())

plt.xlim([0, 5])
plt.ylim([0, 10])
plt.title('La parabola')

plt.gca().set_aspect('equal')
plt.plot(x,y)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('astro_pi.csv', encoding='UTF-8')
df['Humidity'].plot(label = 'humidity', legend = True)
#con secondary_y = True facciamo apparire i numeri per l'asse delle y
#del sexcondo grafico sulla destra
df.Pressure.plot(secondary_y = True, label='Pressure', legend= True)
plt.plot(df['Pressure'], df['Humidity'])
plt.show()
#print(df['Pressure'])
df2 = pd.read_csv('astro_pi.csv', encoding='utf-8')
print(df2.info)
dff2 = df2.iloc[12500:13723]
print(dff2)
plt.plot(df2['Pressure'], df2['Humidity'])
plt.show()
df2.Humidity.plot(label= 'Humidity', legend=True)
df2.Pressure.plot(secondary_y=True, label='pressure', legend=True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('temp_trento.csv', encoding='utf-8')
print(df.info)
print(df.iloc[0])
print()
print(df.iloc[6])#riga 8 = 6 +2
print()
print(df.iloc[5:7])#riga 7, 8 = 5+2 e 6+2
print(df.year[2] > 6)
print(type(df.day > 6))
print()
print(type((df.day >= 6) & (df.day <= 10)))
print((df.day >= 6) & (df.day <= 10))
print(df[(df.day >= 6) & (df.day <= 10)])
[print(x) for x in [df[(df.day >= 6) & (df.day <= 10)]]]
print()

df2 = pd.read_csv('astro_pi.csv', encoding='utf-8')

print(df2[(df2.Humidity == max(df2.Humidity.values))]) #print(df2[(df2.Humidity == df2.Humidity.values.max())])
print()
print(df2.sort_values('Pressure', ascending=False).head())
print('Media pressione:', df2.Pressure.values.mean())
print('Minimo pressione:', df2.Pressure.values.min())
print('Massimo pressione:', df2.Pressure.values.max())
print('Media temperatura:', df2.Temperature.values.mean())
print(df2[df2.Longitude > 0])
print()
print(df2[df2['Date/Time'].str.contains('2022-02-01')])
print()
print(df2['Date/Time'].str[8:10])
print()
print(df2[ ['Latitude', 'Longitude', 'Temperature'] ])
print(df2.head())
df2['MagTot'] = df2['MagX']**2 + df2['MagY']**2 + df2['MagZ']**2
df2.MagTot.plot() #df2['MagTot'].plot()
plt.show()
print(df2['Date/Time'][df2.MagTot == df2.MagTot.values.max()])
print()
df2.loc[(df2.Temperature > 31.68), 'Too hot'] = True
print(df2.head())
pressione_media = df2.Pressure.values.mean()#np.mean(df2.Pressure)
df2['check_p'] = np.where(df2.Pressure >= pressione_media, 'sopra', 'sotto') #dove la temperatura è maggiore di media scrivi nella colonna check_p sopra else sotto
print(df2.head())
print()
df['Temp (Fahrenheit)'] = df['Temp-C°']* 9/5 +32
print(len(df['Temp (Fahrenheit)']))

import csv
with open ('astro_pi.csv', 'r', newline='', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    #lettore = [lettore]
    #next(lettore)
    with open ('astro_pi2.csv', 'w', newline='', encoding='utf-8') as f1:
        scrittore = csv.writer(f1, delimiter=',')
        y = 0
        f1.write(f.readline().strip() + ',Temp (Fahrenheit)' + '\n')
        for x in lettore:
            try:
                scrittore.writerow(x + [float(df['Temp (Fahrenheit)'][y])])
            except:
                pass
            y += 1
#print(df.head())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('astro_pi.csv', encoding='utf-8')
print(df.corr)
df['k'] = df['Pressure'] / df['Temperature']
df['Relazione'] = df['k'] == df.corr
print()
print(int(23.7))

df['Humidity'].transform(int)#trasforma gli elementi in int
print(df['Humidity'].transform(int))
print(df.head())
print()
def mia_f(x):
    return int(x)

df['Humidity'].transform(mia_f)
print(df.head())
print()

df['Humidity'].transform(lambda x : int(x))
print(df.head())
print(df.info())
df['Humidity_int'] = df['Humidity'].transform(lambda x : int(x))
print(df.head())
print(df.groupby(['Humidity_int'])['Humidity'].count())# quanti numeri sono uguali al primo data
print()
df['Conteggio Umidità'] = df.groupby(['Humidity_int'])['Humidity'].transform('count')
print(df)

df.Temperature.plot(label='Temperature', legend=True)
df['Humidity'].plot(label='Humidity', legend=True)
df['Pressure'].plot(secondary_y=True, label='Pressione', legend=True)
plt.show()
df['Giorno'] = df['Date/Time'].str[:10]
print(df.head())
print()
print(df.groupby(['Giorno'])['Temperature'].mean())
print()
df['Temp_media_giorno'] = df.groupby(['Giorno'])['Temperature'].transform('mean')
print(df['Giorno'], df['Temp_media_giorno'])
print()
print(df.head())
df['Temperature'].plot(label='Temperature', legend=True)
df['Temp_media_giorno'].plot(label='temp media', legend=True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('astro_pi.csv', encoding='utf-8')
df['Giorno'] = df['Date/Time'].str[0:10]
print(df.head())
for giorno in df['Giorno']:
    temp_media_giorno = df[(df.Giorno == giorno)].Temperature.values.mean()
    df.loc[(df.Giorno == giorno), 'Temp_media_giorno'] = temp_media_giorno

print(df.head())
df.Temperature.plot(label='Temperature', legend=True)
df.Temp_media_giorno.plot(label='Temepratura media', legend=True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

meteo = pd.read_csv('astro_pi.csv', encoding='utf-8')
meteo['Giorno'] = meteo['Date/Time'].str[:10]
diz_media = {}
for giorno in meteo['Giorno']:
    if giorno not in diz_media:
        diz_media[giorno] = meteo[meteo['Giorno'] == giorno]['Temperature'].mean()
for giorno in meteo['Giorno']:
    meteo.loc[(meteo.Giorno == giorno), 'temp_media_giorno'] = diz_media[giorno]

print(meteo.head())
meteo.Temperature.plot(label='Temperature', legend = True)
meteo.temp_media_giorno.plot(label = 'Temepratura media', legend = True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

meteo = pd.read_csv('astro_pi.csv', encoding='utf-8')
meteo['Giorno'] = meteo['Date/Time'].str[:10]
#.transform è necessario per evitare di avere una tabella con solo 2 righe
#print(meteo.groupby(['Giorno'])['Temperature'].mean())
meteo['Temp_media_giorno'] = meteo.groupby(['Giorno'])['Temperature'].transform('mean')
print(meteo.head())
meteo['Temperature'].plot(label = 'Temperature', legend = True)
meteo['Temp_media_giorno'].plot(label='Temp media giorno', legend=True)
plt.show()
print()

aria = pd.read_csv('aria.csv', encoding='latin-1')
aria.info()
print(aria[(aria['Stazione'] == 'Parco S. Chiara') & (aria['Inquinante'] == 'PM10')]['Valore'].mean()) #.values.mean()
filtrato = aria[(aria['Stazione'] == 'Parco S. Chiara') & (aria['Inquinante'] == 'PM10') & (aria['Data'] == '2024-01-18') ]
plt.plot(filtrato['Ora'], filtrato['Valore'])
plt.title('Inquinamanto giornaliero del 2024-01-18')
plt.xlabel('Ora')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aria = pd.read_csv('aria.csv', encoding='latin-1')
aria.info()
media = aria[(aria['Stazione']=='Parco S. Chiara') & (aria['Inquinante'] == 'PM10')]['Valore'].mean()
print(media)
valori_gio = aria[(aria['Stazione']=='Parco S. Chiara') & (aria['Inquinante'] == 'PM10') & (aria['Data']=='2024-01-18')]
print(valori_gio)
plt.plot(valori_gio['Ora'], valori_gio['Valore'])
plt.title('Media inquinante: '+ valori_gio['Data'][0])
plt.xlabel('Ora (0-24)')
plt.ylabel('Valori inquinanti (' + str(min(valori_gio['Valore'])) + '-' +  str(max(valori_gio['Valore'])) + ' ' + str(valori_gio['Unità di misura'][0]) + ')')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('astro_pi_data.csv', encoding='utf-8')
df.info()
print()
iss_coords = pd.read_csv('iss_output_coords.csv', encoding='utf-8')
iss_coords.info()
print()
geo_astropi = df.merge(iss_coords, left_on='time_stamp', right_on='timestamp', how='left', indicator=True)
geo_astropi = geo_astropi.drop('timestamp', axis = 1)

print(geo_astropi.shape)
pd.merge_ordered(df, iss_coords, fill_method='ffill', how = 'left', left_on='time_stamp', right_on='timestamp')
print(geo_astropi)