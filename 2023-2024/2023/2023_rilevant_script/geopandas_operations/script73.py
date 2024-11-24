# prova con la libreria geopandas

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
print('ok')
df_regioni = gpd.read_file('Localita_11_WGS84.shp')
print(df_regioni)