import csv
import os

import pandas as pd
from django.shortcuts import render
import project_apps.models as models
import project_apps.csvs as csvs
from django.templatetags.static import static


# Create your views here.
def main_page(request):
    return render(request, 'main.html')

def demand_page(request):
    vacancies = models.Demand_All_Vacancies.objects.all()
    all = '<table class="demand_all_vacancies">'
    all += '<caption>Востребованность профессий по годам</caption>'
    all += '<thead><tr>'
    all+= '<th>Год</th>'
    all += '<th>Средняя зп RUB</th>'
    all += '<th>Количество вакансий</th>'
    all += '</tr></thead>'
    all += '<tbody>'
    for vacancy in reversed(vacancies):
        all += f"<tr><td>{vacancy.published_at}</td> <td>{vacancy.mid_salary}</td> <td>{vacancy.year_count}</td></tr>"
    all+= '</tbody></table>'

    vacancies = models.Demand_UX_Vacancies.objects.all()
    ux = '<table class="demand_all_vacancies">'
    ux += '<caption>Востребованность UX-дизайнера по годам</caption>'
    ux += '<thead><tr>'
    ux += '<th>Год</th>'
    ux += '<th>Средняя зп RUB</th>'
    ux += '<th>Количество вакансий</th>'
    ux += '</tr></thead>'
    ux += '<tbody>'
    for vacancy in reversed(vacancies):
        ux += f"<tr><td>{vacancy.published_at}</td> <td>{vacancy.mid_salary}</td> <td>{vacancy.year_count}</td></tr>"
    ux += '</tbody></table>'
    return render(request, 'demand.html', context={"demand_all_vacancies": all, "demand_ux_vacancies": ux})

# <table class="rtable">
#   <thead>
#     <tr>
#       <th>Browser</th>
#       <th>Sessions</th>
#       <th>Percentage</td>
#       <th>New Users</th>
#       <th>Avg. Duration</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <td>Chrome</td>
#       <td>9,562</td>
#       <td>68.81%</td>
#       <td>7,895</td>
#       <td>01:07</td>
#     </tr>
#     <tr>
#       <td>Firefox</td>
#       <td>2,403</td>
#       <td>17.29%</td>
#       <td>2,046</td>
#       <td>00:59</td>
#     </tr>
#     <tr>
#       <td>Safari</td>
#       <td>1,089</td>
#       <td>2.63%</td>
#       <td>904</td>
#       <td>00:59</td>
#     </tr>
#     <tr>
#       <td>Internet Explorer</td>
#       <td>366</td>
#       <td>2.63%</td>
#       <td>333</td>
#       <td>01:01</td>
#     </tr>
#     <tr>
#       <td>Safari (in-app)</td>
#       <td>162</td>
#       <td>1.17%</td>
#       <td>112</td>
#       <td>00:58</td>
#     </tr>
#     <tr>
#       <td>Opera</td>
#       <td>103</td>
#       <td>0.74%</td>
#       <td>87</td>
#       <td>01:22</td>
#     </tr>
#     <tr>
#       <td>Edge</td>
#       <td>98</td>
#       <td>0.71%</td>
#       <td>69</td>
#       <td>01:18</td>
#     </tr>
#     <tr>
#       <td>Other</td>
#       <td>275</td>
#       <td>6.02%</td>
#       <td>90</td>
#       <td>N/A</td>
#     </tr>
#   </tbody>
# </table>
def geography_page(request):
    #all---------------------------
    vacancies = models.Geography_AreaCount_All_Vacancies.objects.all()
    area = '<table class="geography_areacount_all_vacancies">'
    area += '<caption>Доля вакансий по городам</caption>'
    area += '<thead><tr>'
    area += '<th>Город</th>'
    area += '<th>Доля вакансий %</th>'
    area += '</tr></thead>'
    area += '<tbody>'
    for vacancy in vacancies:
        area += f"<tr><td>{vacancy.area_name}</td> <td>{vacancy.mid_salary}</td></tr>"
    area += '</tbody></table>'

    vacancies = models.Geography_MidSalary_All_Vacancies.objects.all()
    mids = '<table class="geography_midsal_all_vacancies">'
    mids += '<caption>Уровень зарплат по городам</caption>'
    mids += '<thead><tr>'
    mids += '<th>Город</th>'
    mids += '<th>Средняя зп RUB</th>'
    mids += '</tr></thead>'
    mids += '<tbody>'
    for vacancy in vacancies:
        mids += f"<tr><td>{vacancy.area_name}</td> <td>{vacancy.mid_salary}</td></tr>"
    mids += '</tbody></table>'
    # all---------------------------
    vacancies = models.Geography_AreaCount_UX_Vacancies.objects.all()
    area_ux = '<table class="geography_areacount_all_vacancies">'
    area_ux += '<caption>Доля вакансий по городам для UX-дизайнера</caption>'
    area_ux += '<thead><tr>'
    area_ux += '<th>Город</th>'
    area_ux += '<th>Доля вакансий %</th>'
    area_ux += '</tr></thead>'
    area_ux += '<tbody>'
    for vacancy in vacancies:
        area_ux += f"<tr><td>{vacancy.area_name}</td> <td>{vacancy.mid_salary}</td></tr>"
    area_ux += '</tbody></table>'

    vacancies = models.Geography_MidSalary_UX_Vacancies.objects.all()
    mids_ux = '<table class="geography_midsal_all_vacancies">'
    mids_ux += '<caption>Уровень зарплат по городам для UX-дизайнера</caption>'
    mids_ux += '<thead><tr>'
    mids_ux += '<th>Город</th>'
    mids_ux += '<th>Средняя зп RUB</th>'
    mids_ux += '</tr></thead>'
    mids_ux += '<tbody>'
    for vacancy in vacancies:
        mids_ux += f"<tr><td>{vacancy.area_name}</td> <td>{vacancy.mid_salary}</td></tr>"
    mids_ux += '</tbody></table>'
    return render(request, 'geography.html',
                  context={"geography_areacount_all_vacancies": area, "geography_midsal_all_vacancies": mids,
                           "geography_areacount_ux_vacancies": area_ux, "geography_midsal_ux_vacancies": mids_ux})

def skills_page(request):
    vacancies = models.Skills_All_Vacancies.objects.all()
    dicts = {}
    for vacancy in vacancies:
        dicts[vacancy.published_at] = vacancy.top_skills.split('@')

    alls = '<table class="skills">'
    alls += '<caption>Топ-20 навыков по годам</caption>'
    alls += ('<thead><tr>')
    for year in dicts.keys():
        alls += (f'<th class="skills_th">{year}</th>')
    alls += ('</tr></thead>')
    alls += '<tbody class="skills_body">'
    for step in range(20):
        alls += (f"<tr>")
        for year in range(2015, 2024):
            alls += f"<td class='skills_td'>{dicts[year][step]}</td>"
        alls += (f"</tr>")
    alls += '</tbody></table>'


    vacancies = models.Skills_UX_Vacancies.objects.all()
    dicts = {}
    for vacancy in vacancies:
        dicts[vacancy.published_at] = vacancy.top_skills.split('@')

    ux = '<table class="skills">'
    ux += '<caption>Топ-20 навыков по годам для UX-дизайнера</caption>'
    ux += ('<thead><tr>')
    for year in dicts.keys():
        ux += (f'<th class="skills_th">{year}</th>')
    ux += ('</tr></thead>')
    ux += '<tbody class="skills_body">'
    for step in range(20):
        ux += (f"<tr>")
        for year in range(2015, 2024):
               ux += f"<td class='skills_td'>{dicts[year][step]}</td>"
        ux  += (f"</tr>")
    ux += '</tbody></table>'
    return render(request, 'skills.html', context={"skills_all_vacancies": alls, "skills_ux_vacancies": ux})

def vacancies_page(request):
    return render(request, 'vacancies.html')


# demand_All_Vacancies = []
#
# Vacancies = pd.read_csv("project_apps/csvs/demand_all_vacancies.csv")
# for vacancy in Vacancies.values:
#     demand_All_Vacancies.append(models.Demand_All_Vacancies(published_at=vacancy[0], mid_salary=vacancy[1], year_count=vacancy[2]))
#
# demand = models.Demand_All_Vacancies.objects.bulk_create(demand_All_Vacancies)
#
# for person in demand:
#     continue

# demand_UX_Vacancies = []
#
# Vacancies = pd.read_csv("project_apps/csvs/demand_ux_vacancies.csv")
# for vacancy in Vacancies.values:
#     demand_UX_Vacancies.append(models.Demand_UX_Vacancies(published_at=vacancy[0], mid_salary=vacancy[1], year_count=vacancy[2]))
#
# demand = models.Demand_UX_Vacancies.objects.bulk_create(demand_UX_Vacancies)
#
# for person in demand:
#     continue

#GEOGRAPHY------------------------------------------------------------------------------------------------------------------------

# geography_areacount_all_Vacancies = []
#
# Vacancies = pd.read_csv("project_apps/csvs/geography_areacount_all_vacancies.csv")
# for vacancy in Vacancies.values:
#     geography_areacount_all_Vacancies.append(models.Geography_AreaCount_All_Vacancies(area_name=vacancy[0], mid_salary=vacancy[1]))
# demand = models.Geography_AreaCount_All_Vacancies.objects.bulk_create(geography_areacount_all_Vacancies)
# for person in demand:
#     continue

# geography_areacount_UX_Vacancies = []
#
# Vacancies = pd.read_csv("project_apps/csvs/geography_areacount_ux_vacancies.csv")
# for vacancy in Vacancies.values:
#     geography_areacount_UX_Vacancies.append(models.Geography_AreaCount_UX_Vacancies(area_name=vacancy[0], mid_salary=vacancy[1]))
# demand = models.Geography_AreaCount_UX_Vacancies.objects.bulk_create(geography_areacount_UX_Vacancies)
# for person in demand:
#     continue


# geography_midsal_all_Vacancies = []
#
# Vacancies = pd.read_csv("project_apps/csvs/geography_midsal_all_vacancies.csv")
# for vacancy in Vacancies.values:
#     geography_midsal_all_Vacancies.append(models.Geography_MidSalary_All_Vacancies(area_name=vacancy[0], mid_salary=vacancy[1]))
# demand = models.Geography_MidSalary_All_Vacancies.objects.bulk_create(geography_midsal_all_Vacancies)
# for person in demand:
#     continue


# geography_midsal_ux_Vacancies = []
#
# Vacancies = pd.read_csv("project_apps/csvs/geography_midsal_ux_vacancies.csv")
# for vacancy in Vacancies.values:
#     geography_midsal_ux_Vacancies.append(models.Geography_MidSalary_UX_Vacancies(area_name=vacancy[0], mid_salary=vacancy[1]))
# demand = models.Geography_MidSalary_UX_Vacancies.objects.bulk_create(geography_midsal_ux_Vacancies)
# for person in demand:
#     continue

#GEOGRAPHY------------------------------------------------------------------------------------------------------------------------

# skills_all_Vacancies = []
#
# Vacancies = pd.read_csv("project_apps/csvs/skills_all_vacancies.csv")
# for year in Vacancies.keys():
#     skills_all_Vacancies.append(models.Skills_All_Vacancies(published_at=year, top_skills=Vacancies[year][0]))
# demand = models.Skills_All_Vacancies.objects.bulk_create(skills_all_Vacancies)
# for person in demand:
#     continue


# skills_ux_Vacancies = []
#
# Vacancies = pd.read_csv("project_apps/csvs/skills_ux_vacancies.csv")
# for year in Vacancies.keys():
#     skills_ux_Vacancies.append(models.Skills_UX_Vacancies(published_at=year, top_skills=Vacancies[year][0]))
# demand = models.Skills_UX_Vacancies.objects.bulk_create(skills_ux_Vacancies)
# for person in demand:
#     continue