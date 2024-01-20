from decimal import Decimal

import pandas as pd

def get_mid_salary(vacancies):
    vacancies = vacancies[[x != 0 for x in vacancies['mid_salary']]].reset_index()
    return vacancies[['mid_salary', 'area_name']].groupby(['area_name']).mean().reset_index()

def get_tables(csv):
    vacancies = pd.read_csv(csv)
    d = Decimal

    # получаем средние зп и кол-во вакансий по городам
    vac_count = len(vacancies)
    area_count = vacancies[['area_name', 'mid_salary']].groupby(['area_name']).count().reset_index()
    area_count = area_count[area_count['mid_salary'] > vac_count / 100]
    area_count['mid_salary'] = area_count['mid_salary'].apply(
        lambda x: d(100 * float(x) / vac_count).quantize(d("1.00")))
    area_count = area_count.sort_values(['mid_salary', 'area_name'], ascending=[False, True])
    area_list = area_count['area_name'].tolist()

    area_mid_salaries = get_mid_salary(vacancies)
    area_mid_salaries.loc[:, 'mid_salary'] = area_mid_salaries['mid_salary'].apply(lambda x: int(d(x).quantize(d("1"))))
    area_mid_salaries = area_mid_salaries.sort_values('mid_salary', ascending=False)
    area_mid_salaries = area_mid_salaries[area_mid_salaries['area_name'].isin(area_list)]


    #area_count = pd.Series(area_count['mid_salary'].head(10).values, index=area_count['area_name'].head(10)).to_dict()
    #area_mid_salaries = pd.Series(area_mid_salaries['mid_salary'].head(10).values, index=area_mid_salaries['area_name'].head(10)).to_dict()
    return area_mid_salaries, area_count

mid_sal, area_count = get_tables('notmal_alll_rub_vacancies.csv')
mid_sal_ux, area_count_ux = get_tables('ux_vacancies.csv')

print(2)

pd.DataFrame(mid_sal).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\geography_midsal_all_vacancies.csv', index=False)
pd.DataFrame(area_count).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\geography_areacount_all_vacancies.csv', index=False)

pd.DataFrame(mid_sal_ux).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\geography_midsal_ux_vacancies.csv', index=False)
pd.DataFrame(area_count_ux).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\geography_areacount_ux_vacancies.csv', index=False)