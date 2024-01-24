import io
import json
import re

import requests
import xmltodict


def get_valute_valute(charcode, date):
    if (date in date_dict.keys()):
        BASE_URL = ' https://api.hh.ru/vacancies'
        params = {
            'text': 'UX',
            'period': 1,
            'order_by': 'publication_time',
        }
        response = requests.get(f"{BASE_URL}01/{date}")
        tree = xmltodict.parse(response.content)
        tree = tree['ValCurs'];
        tree = tree['Valute'];
        date_dict[date] = tree
    tree = [x for x in tree if x['CharCode'] == charcode]
    valute = tree[0]['Value']
    return float(valute.replace(',', '.'))

date_dict = {}

def get_mid(salary):
    if salary == None:
        return 'Нет информации по зарплате'

    #salary = salary.fillna(0)
    sfrom = salary['from']
    sto = salary['to']
    cur = salary['currency']
    if sfrom is None:
        smid = sto
    elif sto is None:
        smid = sfrom
    else:
        smid = (sfrom + sto)/2
    return str(int(smid)) +' '+ cur

def get_hh_vacancies():
    BASE_URL = 'https://api.hh.ru/vacancies'
    params = {
        'text': 'UI',
        'period': 1,
        'order_by': 'publication_time'
    }
    #vacancies = json.load(io.StringIO(requests.get(BASE_URL, params).text))
    response = requests.get(f"{BASE_URL}", params=params)
    vacancies = response.json()

    delete_HTML = lambda x: re.sub(r"<[^<>]*>", "", x)
    crop_text = lambda x: x[:30]+'...' if len(x) > 30 else x
    time_parse = lambda x: re.sub(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\+(\d{4})", r"\3/\2/\1", x)

    id_list = []
    [id_list.append(id['id']) for id in list(vacancies.items())[0][1]]
    vac_list =[]
    for id in id_list:
        response = requests.get(f"{BASE_URL}/{id}")
        vac = response.json()
        vacancy = ([vac['name'],
                         crop_text(delete_HTML(vac['description'])),
                         (', ').join([skill['name'] for skill in vac['key_skills']]),
                         vac['employer']['name'],
                         get_mid(vac['salary']),
                         vac['area']['name'],
                         time_parse(vac['published_at']),
                         ])
        if ("UI" in vacancy[0] or "UI" in vacancy[2]):
            vac_list.append(vacancy)
    [print(vac) for vac in vac_list]

# name
# description
# key_skills
# employer
# area
# published_at
# salary


get_hh_vacancies()
# vacancies = list(get_hh_vacancies().items())
# for vacancy in vacancies[0][1]:
#    print(vacancy['id'])

