import pandas as pd
import re
import OleFileIO_PL

with open('before.xls', 'rb') as file:
    ole = OleFileIO_PL.OleFileIO(file)
    if ole.exists('Workbook'):
        d = ole.openstream('Workbook')
        excel = pd.read_excel(d, engine='xlrd')

cyrillic_pattern = re.compile("[а-яА-ЯёЁ]")


def has_cyrillic(text):
    return bool(cyrillic_pattern.search(text.iloc[2]))


excel.drop_duplicates(subset=['ID'], inplace=True)

excel.sort_values(by=['Бренд', 'Модель'], inplace=True)

excel['has_cyrillic'] = excel.apply(has_cyrillic, axis=1)

excel.to_excel('after.xlsx', index=False)
