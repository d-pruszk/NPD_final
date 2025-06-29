from NPD_final.Analysis.data_loading import *
import pandas as pd
import numpy as np
from NPD_final.Analysis.Compute_stats import *

pd.set_option('display.max_columns', 20)
pd.set_option('display.width',1000)

path_fire = '3.csv' # chcemy plik 3 z pożarami w podziale na gminę
# path_population = 'powierzchnia_i_ludnosc_w_przekroju_terytorialnym_w_2024_roku_tablice.xlsx' # https://stat.gov.pl/obszary-tematyczne/ludnosc/ludnosc/powierzchnia-i-ludnosc-w-przekroju-terytorialnym-w-2024-roku,7,21.html
path_population = 'tabela11.xls'
path_alcohol = 'raport_zezwoleń_alkoholowych_czynych_na_dzień_4_lutego_2025_r..csv' # Patrzymy na gminy (Municipality)
# path_SIMC = 'SIMC_Statystyczny_2025-06-29.csv' #https://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/uzytkownicy_indywidualni/pobieranie/pliki_pelne.aspx?contrast=default
path_kody = 'Oficjalny_Spis_Pocztowych_Numerw_Adresowych_2024.xlsx'

population_df = load_population(path_population)
fire_df = load_fire(path_fire)
alcohol_df = load_alcohol(path_alcohol,path_kody)
# kody_df = load_kody(path_kody)

# print(population_df.iloc[0:10,0:])
# print(fire_df.iloc[0:10,0:])

# Map the custom function to the Address column to create a new column containing the result of the function
# df = df[df["Address"].map(contains_new_york)]
# print(population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'])
# print(population_df.iloc[:,[0,1,5]])

#
# print(population_df[~population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'].map(contains_4)])
# print(population_df[~population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'].map(contains_5)])

# population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'] = population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'].astype(str).str[:-2].str[1:].astype(np.int64)
# population_df = population_df.iloc[:,1:5]
# population_df = population_df.dropna()
print(population_df)
print(fire_df)
print(alcohol_df)
# print(kody_df)


# alcohol_df = pd.merge(alcohol_df,kody_df,how='left',on='Kod pocztowy')

# alcohol_df = alcohol_df.iloc[:,[0,2]]


# population_df = population_df.rename(columns={'Identyfikator terytorialny\nCode': 'TERYT'})
# population_df = pd.merge(population_df,fire_df,how='left',on='TERYT')
# print(population_df)

# fire_df = fire_df.pivot_table(index=['TERYT'], aggfunc='sum')
# print(fire_df)


# alcohol_df = alcohol_df.pivot_table(index='Gmina',aggfunc = 'count')
# print(alcohol_df)

stats_population = calculate_basic_stats(population_df, 'Ogółem \nTotal')
stats_fire = calculate_basic_stats(fire_df, 'OGÓŁEM Liczba zdarzeń')
stats_alcohol = calculate_basic_stats(alcohol_df, 'Liczba koncesji')

print
print(stats_population)
print(stats_fire)
print(stats_alcohol)

merged_df = pd.merge(population_df,fire_df,how='left',on=['TERYT'])
merged_df = pd.merge(merged_df,alcohol_df,how='left',on=['Gmina'])
# print(merged_df)