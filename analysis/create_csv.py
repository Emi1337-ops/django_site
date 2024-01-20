import re
from decimal import Decimal
import requests
import xmltodict
import openpyxl as op
import pandas as pd

date_dict = {}
def get_valute_valute(charcode, date):
    if not(date in date_dict.keys()):
        BASE_URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
        response = requests.get(f"{BASE_URL}01/{date}")
        tree = xmltodict.parse(response.content)
        tree = tree['ValCurs'];
        tree = tree['Valute'];
        date_dict[date] = tree
    vac = [x for x in date_dict[date] if x['CharCode'] == charcode]
    if len(vac) > 0:
        valute = vac[0]['VunitRate']
    else:
        valute = '1'
    return float(valute.replace(',', '.'))


def is_vac_get_name(vacancy):
    vacancy_names = ['design', 'UX' ,'UI','дизайн', 'иллюстратор']
    if vacancy[1] == 0:
        return (True in [(x in vacancy[0]) for x in vacancy_names])
    return (True in [(x in vacancy[1]) for x in vacancy_names])

def is_normal_salary(vacancy):
    if (vacancy > 10000000):
        return False
    return True

def get_mid(x, y):
    if (0 in [x, y]):
        return x + y
    return (x + y)/2

def get_mid_salary(vacancy):
    value = get_mid(float(vacancy[2]), float(vacancy[3]))
    date = vacancy[6]
    currency = vacancy[4]
    if not(currency in [0, 'RUR']):
        time_parse = lambda x: re.sub(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\+(\d{4})", r"\2/\1", x)
        value *= get_valute_valute(currency, time_parse(date))
    return value



# big_vacancies = pd.read_csv('alll_notrub_vacancies.csv')
# big_vacancies = big_vacancies.fillna(0)
# mid_salaries = [get_mid_salary(x) for x in big_vacancies.values]
# big_vacancies.insert(loc=3, column='mid_salary', value=mid_salaries)
#pd.DataFrame(big_vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\alll_rub_vacancies.csv', index=False)

# big_vacancies = pd.read_csv('alll_rub_vacancies.csv')
# big_vacancies = big_vacancies[[is_normal_salary(vacancy) for vacancy in big_vacancies['mid_salary']]].reset_index()
# big_vacancies = big_vacancies.drop(columns=['index'])
# pd.DataFrame(big_vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\notmal_alll_rub_vacancies.csv', index=False)

big_vacancies = pd.read_csv('notmal_alll_rub_vacancies.csv')
vacancies = big_vacancies[[is_vac_get_name(name) for name in big_vacancies.values]].reset_index()
vacancies = vacancies.drop(columns=['index'])
pd.DataFrame(vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\ux_vacancies.csv', index=False)
