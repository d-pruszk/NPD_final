import pandas as pd
import numpy as np

def contains_spaces(address):
    return "    " in address
# def contains_5(address):
#     return " 5" in address
# def load_population(path_population):
#     """Function for loading population statistics, preferred source: https://stat.gov.pl/obszary-tematyczne/ludnosc/ludnosc/powierzchnia-i-ludnosc-w-przekroju-terytorialnym-w-2024-roku,7,21.html"""
#     population_df = pd.read_excel(path_population, sheet_name='Tabl. 21',header = 2)
#     population_df = population_df.iloc[:, [0, 1, 5]]
#     population_df = population_df.dropna()
#     population_df = population_df[~population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'].map(contains_4)]
#     population_df = population_df[~population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'].map(contains_5)]
#     return(population_df)
def load_fire(path_fire):
    """Function for loading fire statistics, preferred source: https://dane.gov.pl/pl/dataset/4695?page=2&per_page=20&q=&sort=-data_date&model=resources, file: 3. Pozary wg kodu obiektu w rozbiciu na wojewodztwo, powiat, gmine_64722"""
    fire_df = pd.read_csv(path_fire)
    fire_df = fire_df.iloc[:, [0, 3, 4]]
    fire_df = fire_df.dropna()
    fire_df = fire_df.pivot_table(index=['TERYT'], aggfunc='sum')
    return(fire_df)

def load_population(path_population):
    """Function for loading population statistics, preferred source: https://stat.gov.pl/obszary-tematyczne/ludnosc/ludnosc/ludnosc-stan-i-struktura-ludnosci-oraz-ruch-naturalny-w-przekroju-terytorialnym-w-2024-r-stan-w-dniu-30-06,6,37.html, file: tabela11.xls"""
    excel_file = pd.ExcelFile(path_population)
    sheets = excel_file.sheet_names
    df_total = pd.read_excel(path_population, sheet_name=sheets[0], header=5)
    for sheet in sheets[1:]:  # loop through sheets inside an Excel file
        # print(sheet)
        # df = excel_file.parse(sheet_name=sheet)
        population_df = pd.read_excel(path_population, sheet_name=sheet, header=5)
        # print(population_df)
        # df_total = df_total.append(population_df)
        df_total = pd.concat([df_total, population_df],axis=0,ignore_index=True)
    # df_total.to_excel('combined_file.xlsx')
    df_total = df_total.iloc[:, :5]
    df_total = df_total.dropna()
    # df_total = df_total[df_total['Wyszczególnienie\nSpecification'].map(contains_spaces)]
    # population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'] = population_df['Identyfikator\nterytorialny\nTerritorial\nidentifier'].astype(str).str[:-2].str[1:].astype(np.int64)
    df_total['Identyfikator terytorialny\nCode'] = df_total['Identyfikator terytorialny\nCode'].astype(np.int64)
    # df_total['Identyfikator terytorialny\nCode'] = df_total['Identyfikator terytorialny\nCode'].astype(np.int64)
    # print(df_total)
    df_total = df_total[df_total['Identyfikator terytorialny\nCode'].astype(str).str[-1:] != '0']
    df_total['Identyfikator terytorialny\nCode'] = df_total['Identyfikator terytorialny\nCode'].astype(str).str[0:-1].astype(np.int64)
    df_total = df_total.rename(columns={'Identyfikator terytorialny\nCode': 'TERYT'})
    return(df_total)

# def load_alcohol(path_alcohol):
#     """Function for loading alcohol concessions statistics, preferred source: , file: """
#     alcohol_df = pd.read_csv(path_alcohol)
#     alcohol_df = alcohol_df.iloc[:,2:4]
#     return(alcohol_df)
#
# def load_kody(path):
#     """Function for loading alcohol concessions statistics, preferred source: https://www.gov.pl/attachment/2f386d04-ec98-46f6-adde-3c9832c09a9a"""
#     df = pd.read_excel(path)
#     df = df.iloc[:,[2,4]]
#     return(df)
def load_alcohol(path_alcohol,path_kody):
    """Function for loading alcohol concessions statistics, preferred source: https://dane.gov.pl/pl/dataset/1191,informacja-o-przedsiebiorcach-posiadajacych-zezwolenia-na-handel-hurtowy-napojami-alkoholowymi-1/resource/64402/table?page=1&per_page=20&q=&sort=, additional file required for decoding zip codes into TERIT codes, preferred source: https://baza-kodow-pocztowych.poczta-polska.pl/"""
    alcohol_df = pd.read_csv(path_alcohol)
    alcohol_df = alcohol_df.iloc[:,2:4]
    kody_df = pd.read_excel(path_kody)
    kody_df = kody_df.iloc[:, [2, 4]]
    alcohol_df = pd.merge(alcohol_df, kody_df, how='left', on='Kod pocztowy')
    alcohol_df = alcohol_df.iloc[:, [0, 2]]
    alcohol_df = alcohol_df.pivot_table(index='Gmina', aggfunc='count')
    alcohol_df = alcohol_df.rename(columns={'Kod pocztowy': 'Liczba koncesji'})
    return(alcohol_df)



