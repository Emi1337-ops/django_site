import matplotlib.pyplot as plt
import csv
import pandas as pd

x = []
y = []

vacancies = pd.read_csv('geography_midsal_ux_vacancies.csv')


y = vacancies['mid_salary'].tolist()[::-1]
x = vacancies['area_name'].tolist()[::-1]

plt.rcParams.update({'font.size': 9})
plt.bar(x, y, color='lightblue')
#plt.xticks(range(2003, 2024, 1))
plt.xlabel('Город')
plt.ylabel('Средняя зп')
plt.title('Уровень зарплат по городам для UX-дизайнера')
plt.show()