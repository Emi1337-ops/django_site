import re
import pandas as pd

def make(csv):
    skills = {}
    vacancies = pd.read_csv(csv)

    for year in vacancies.keys():
        skills[year] = ['@'.join(vacancies[year])]
    return skills


a = make('skills_all_vacancies.csv')
b = make('skills_ux_vacancies.csv')
print(2)
pd.DataFrame(a).to_csv(r'/project_site/project_apps/csvs/skills_all_vacancies.csv', index=False)
pd.DataFrame(b).to_csv(r'/project_site/project_apps/csvs/skills_ux_vacancies.csv', index=False)