import OleFileIO_PL
import pandas as pd
import numpy
import os
import time
import purchase_price_for_catalog as pp
import logic_for_price_v2 as test_test

start = time.time()

list_dir = os.listdir('export_from_storm')

for iii in list_dir:

    pp_dict = pp.price_dict[iii.replace('.xls', '')]
    print(iii.replace('.xls', ''))
    path = f'export_from_storm/{iii}'  # нужен цикл, который будет проходить по каждому файлу!
    with open(path, 'rb') as file:
        ole = OleFileIO_PL.OleFileIO(file)
        if ole.exists('Workbook'):
            d = ole.openstream('Workbook')
            x = pd.read_excel(d, engine='xlrd')

    rival_list = ['Rozetka', 'Telemart', 'Brain', 'CompX', 'Can.ua', 'ELMIR.UA', 'MTA.ua', 'Stylus']

    x.drop(x.loc[x["Тип цены"] == "Строгач"].index, inplace=True)

    x['url'] = x['Вход'].replace(r"/.*", "", regex=True).astype(float).fillna(numpy.nan)
    x['Поставщик'] = x['Поставщик'].replace(r"/.*", "", regex=True)
    x.drop(x.loc[x["Поставщик"].isin(['Фот', 'ФОТ60', 'ФотУц', 'Магаз'])].index, inplace=True)
    x['min'] = x.loc[:, rival_list].astype(float).min(axis=1).fillna(numpy.nan)
    x['ggg'] = x.loc[:, rival_list].astype(float).idxmin(axis=1, skipna=True)
    x['min_%'] = round(x['min'] / x['url'] - 1, 3) * 100
    x[['new', 'rule', 'min_riv']] = x.apply(test_test.logic_power, axis=1, pp_dict=pp_dict, columns=rival_list, result_type='expand')
    x['my'] = round(x['new'] / x['url'] - 1, 3) * 100

    def fast(row):
        if row['my'] <= row['min_%']:
            return 1
        else:
            return 0

    x['good'] = x.apply(fast, axis=1)

    x.to_excel(f'extended_files/{iii.replace(".xls", "")}.xlsx', index=False)
    x = x.loc[:, ['ID', 'new']].assign(currency='uah')
    x.to_excel(f'import_to_storm/{iii.replace(".xls", "")}_to_storm.xlsx', index=False)

print(round(time.time() - start, 2), ' sec')
