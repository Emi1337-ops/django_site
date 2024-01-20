from decimal import Decimal
import re
import pandas as pd

def get_mid_salary(vacancies):
    vacancies = vacancies[[x != 0 for x in vacancies['mid_salary']]].reset_index()
    return vacancies[['mid_salary', 'published_at']].groupby(['published_at']).mean().reset_index()

def get_tables(csv):
    #получаем таблицу из csv и добавляем заголовок
    vacancies = pd.read_csv(csv)

    #получаем средние зарплаты по годам
    time_parse = lambda x: re.sub(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\+(\d{4})", r"\1", x)
    vacancies.loc[:, 'published_at'] = vacancies['published_at'].apply(time_parse)
    d = Decimal
    mid_sal = get_mid_salary(vacancies)
    year_count = vacancies[['published_at', 'mid_salary']].groupby(['published_at']).count().reset_index()
    mid_sal.loc[:, 'mid_salary'] = mid_sal['mid_salary'].apply(lambda x: d(x).quantize(d("1")))
    mid_sal.insert(loc=2, column='year_count', value=year_count[['mid_salary']])
    return mid_sal


all_vacancies = get_tables('notmal_alll_rub_vacancies.csv')
vacancies = get_tables('ux_vacancies.csv')
print(2)
pd.DataFrame(all_vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\demand_all_vacancies.csv', index=False)
pd.DataFrame(vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\demand_ux_vacancies.csv', index=False)
