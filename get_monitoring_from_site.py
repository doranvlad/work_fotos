import requests
import re
import json


with open('auth.json', 'r', encoding='utf-8') as file1:
    auth = json.load(file1)

url = 'http://storm2/login.php'
path = 'export_from_storm/'

s = requests.Session()
log = s.post(url, data=auth)

if 'Прайс' in log.text:
    print('Авторизация прошла успешно!')
else:
    print('Ошибка авторизации')


with open('category_id.json', 'r', encoding='utf-8') as file2:
    category = json.load(file2)


for i in category:
    url2 = f'http://storm2/inc/price_monitor.php?pms_id={category[i]}&excel=Excel#a{category[i]}'

    response = s.get(url2)

    print(response.url)

    match = re.search(r"(/print/stat/.*?\.xls)", response.text)
    print(f'http://storm2'+ match.group(1))

    url3 = s.get(f'http://storm2/'+ match.group(1))
    filename = f"{i}.xls"

    with open(path+filename, "wb") as f:
        f.write(url3.content)

    print("Файл успешно сохранен!")
