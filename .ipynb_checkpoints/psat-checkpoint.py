import pandas as pd
import numpy as np

values_grande = []
values_iguacu = []
values_parana = []
values_paranapanema = []
values_paranaiba = []
values_tocantins = []
values_saofrancisco = []
values_uruguai = []

# lendo os arquivos

diaini=1
diafim=12

for dias in range(diaini, diafim+1, 1):

    filename = 'psat_' + str(dias).zfill(2) + '122022.txt'

    df = pd.read_table(filename, delim_whitespace=True, header=None)

    # colocando em um df

    df.columns=['NAME','LAT','LON','PREC']

    # separando em bacias

    sub_bacias_grande = ['PSATAGV' , 'PSATCMG', 'PSATCES', 'PSATELC', 'PSATFUN', 'PSATFUR', 'PSATMRB', 'PSATPRG', 'PSATPAS','PSATPTB', 'PSATPTC']

    sub_bacias_iguacu = ['PSATFZA', 'PSATJSG', 'PSATSCX', 'PSATSCL', 'PSATUVT']

    sub_bacias_parana = ['PSATBSM', 'PSATFLE', 'PSATITP', 'PSATIVM', 'PSATPTQ','PSATISOT', 'PSATJUP', 'PSATSDG', 'PSATFZBT', 'PSATPPRA'] 

    #sub_bacias_parana = ['PSATBSM', 'PSATFLE', 'PSATITP', 'PSATIVM', 'PSATPTQ', 'PSATESP', 'PSATSRC', 'PSATFRCL', 'PSATISOT', 'PSATJUP', 'PSATSDG', 'PSATFZBT', 'PSATPPRA']

    sub_bacias_paranaiba = ['PSATESP', 'PSATSRC', 'PSATFRCL','PSATCBI', 'PSATCBIV', 'PSATEMB', 'PSATIMBR', 'PSATNPTE', 'PSATARV', 'PSATSFC', 'PSATSSM']

    #sub_bacias_paranaiba = ['PSATCBI', 'PSATCBIV', 'PSATEMB', 'PSATIMBR', 'PSATNPTE', 'PSATARV', 'PSATSFC', 'PSATSSM']

    sub_bacias_paranapanema = ['PSATCNI', 'PSATCPV', 'PSATCHT', 'PSATJUR', 'PSATMAU', 'PSATROS']

    sub_bacias_saofrancisco = ['PSATQMD', 'PSATRBX', 'PSATSFR', 'PSATSRM', 'PSATTMR', 'PSATBOQ']

    sub_bacias_tocantins = ['PSATSME', 'PSATBTE', 'PSATARAG', 'PSATLAJ', 'PSATPTRL', 'PSATLJET', 'PSATUCR']

    #sub_bacias_uruguai = ['PSATBGR', 'PSATCNV', 'PSATFCH', 'PSATITA', 'PSATMCD', 'PSATMOJ', 'PSATQQX', 'PSATPSJ', 'PSATSTPL']

    sub_bacias_uruguai = ['PSATBGR', 'PSATCNV', 'PSATFCH', 'PSATITA', 'PSATMCD', 'PSATMOJ', 'PSATQQX', 'PSATPSJ']

    df.set_index('NAME', inplace=True)

    grande = np.round(df.loc[sub_bacias_grande]['PREC'].mean(), 0)
    iguacu = np.round(df.loc[sub_bacias_iguacu]['PREC'].mean(), 0)
    parana = np.round(df.loc[sub_bacias_parana]['PREC'].mean(), 0)
    paranaiba = np.round(df.loc[sub_bacias_paranaiba]['PREC'].mean(), 0)
    paranapanema = np.round(df.loc[sub_bacias_paranapanema]['PREC'].mean(), 0)
    saofrancisco = np.round(df.loc[sub_bacias_saofrancisco]['PREC'].mean(), 0)
    tocantins = np.round(df.loc[sub_bacias_tocantins]['PREC'].mean(), 0)
    uruguai = np.round(df.loc[sub_bacias_uruguai]['PREC'].mean(), 0)

    values_grande.append(grande)
    values_iguacu.append(iguacu)
    values_parana.append(parana)
    values_paranapanema.append(paranapanema)
    values_paranaiba.append(paranaiba)
    values_tocantins.append(tocantins)
    values_saofrancisco.append(saofrancisco)
    values_uruguai.append(uruguai)

chuva_grande = np.sum(values_grande)
chuva_iguacu = np.sum(values_iguacu)
chuva_parana = np.sum(values_parana)
chuva_paranapanema = np.sum(values_paranapanema)
chuva_paranaiba = np.sum(values_paranaiba)
chuva_tocantins = np.sum(values_tocantins)
chuva_saofrancisco = np.sum(values_saofrancisco)
chuva_uruguai = np.sum(values_uruguai)

print (f"Acumulada até às 09h do dia {diafim}/12")
print (f"Grande: {chuva_grande}mm")
print (f"Paranaiba: {chuva_paranaiba}mm")
print (f"Tocantins: {chuva_tocantins}mm")
print (f"São Francisco: {chuva_saofrancisco}mm")
print (f"Paranapanema: {chuva_paranapanema}mm")
print (f"Paraná: {chuva_parana}mm")
print (f"Iguaçu: {chuva_iguacu}mm")
print (f"Uruguai: {chuva_uruguai}mm")


