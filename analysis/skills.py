import re
import pandas as pd

time_parse = lambda x: re.sub(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\+(\d{4})", r"\1", x)

def add_to_dict(skills, year, skills_dict):
    if skills == 0 or skills == '0':
        return
    if not(year in skills_dict.keys()):
        skills_dict[year] = {}
    for skill in skills.split('\n'):
        if not(skill in skills_dict[year].keys()):
            skills_dict[year][skill] = 1
        else:
            skills_dict[year][skill] += 1

def get_tables(csv):

    skills_dict = {}
    vacancies = pd.read_csv(csv)

    for vacancy in vacancies.values:
        add_to_dict(vacancy[1], time_parse(vacancy[7]), skills_dict)
    return skills_dict


all_vacancies = get_tables('all_rub_vacancies.csv')
for year in all_vacancies.items():
    all_vacancies[year[0]] = [x[0] for x in sorted(year[1].items(), key=lambda x:-x[1])[:20]]

# ux_vacancies = get_tables('ux_vacancies.csv')
# for year in ux_vacancies.items():
#     ux_vacancies[year[0]] = [x[0] for x in sorted(year[1].items(), key=lambda x:-x[1])[:20]]

pd.DataFrame(all_vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\skills_all_vacancies.csv', index=True)
# pd.DataFrame(ux_vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\geography_areacount_all_vacancies.csv', index=True)

