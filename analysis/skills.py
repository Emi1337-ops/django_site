import pandas as pd


def add_to_dict(skills, skills_dict):
    if skills == 0 or skills == '0':
        return
    for skill in skills.split('\n'):
        if not(skill in skills_dict.keys()):
            skills_dict[skill] = 1
        else:
            skills_dict[skill] += 1

def get_tables(csv):
    skills_dict = {}
    vacancies = pd.read_csv(csv)

    for vacancy in vacancies.values:
        add_to_dict(vacancy[1], skills_dict)
    return skills_dict

all_vacancies = sorted(get_tables('notmal_alll_rub_vacancies.csv').items(), key=lambda x:-x[1])[:20]

ux_vacancies = sorted(get_tables('ux_vacancies.csv').items(), key=lambda x:-x[1])[:20]
print(2)
pd.DataFrame(all_vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\geography_midsal_all_vacancies.csv', index=True)
pd.DataFrame(ux_vacancies).to_csv(r'c:\Users\dima0\PycharmProjects\project_site\analysis\geography_areacount_all_vacancies.csv', index=True)

