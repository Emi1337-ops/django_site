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
    return render(request, 'demand.html')

def geography_page(request):
    return render(request, 'geography.html')

def skills_page(request):
    return render(request, 'skills.html')

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