from django.db import models

# Create your models here.

#Demand------------------------------------------------------
class Demand_All_Vacancies(models.Model):
    published_at = models.IntegerField("Год")
    mid_salary = models.IntegerField("Средняя зп")
    year_count = models.IntegerField("Кол-во вакансий")

    def __str__(self):
        return f"{self.published_at} {self.mid_salary} {self.year_count}"

    class Meta:
        verbose_name = "Востребованность по всем Профессиям"

class Demand_UX_Vacancies(models.Model):
    published_at = models.IntegerField("Год")
    mid_salary = models.IntegerField("Средняя зп")
    year_count = models.IntegerField("Кол-во вакансий")

    def __str__(self):
        return f"{self.published_at} {self.mid_salary} {self.year_count}"

    class Meta:
        verbose_name = "Востребованность по UX"
#Demand------------------------------------------------------

#Geography---------------------------------------------------
class Geography_AreaCount_All_Vacancies(models.Model):
    area_name = models.CharField("Город", max_length=64)
    mid_salary = models.FloatField("Доля вакансий")

    def __str__(self):
        return f"{self.area_name} {self.mid_salary}"

    class Meta:
        verbose_name = "География Доля Вакансий по всем Профессиям"


class Geography_MidSalary_All_Vacancies(models.Model):
    area_name = models.CharField("Город", max_length=64)
    mid_salary = models.IntegerField("Средняя зп")

    def __str__(self):
        return f"{self.area_name} {self.mid_salary}"

    class Meta:
        verbose_name = "География Уровень Зарплат по всем Профессиям"


class Geography_AreaCount_UX_Vacancies(models.Model):
    area_name = models.CharField("Город", max_length=64)
    mid_salary = models.FloatField("Доля вакансий")

    def __str__(self):
        return f"{self.area_name} {self.mid_salary}"

    class Meta:
        verbose_name = "География Доля Вакансий по UX"


class Geography_MidSalary_UX_Vacancies(models.Model):
    area_name = models.CharField("Город", max_length=64)
    mid_salary = models.IntegerField("Средняя зп")

    def __str__(self):
        return f"{self.area_name} {self.mid_salary}"

    class Meta:
        verbose_name = "География Уровень Зарплат по UX"
#Geography---------------------------------------------------

#Skills------------------------------------------------------
class Skills_All_Vacancies(models.Model):
    published_at = models.IntegerField("Год")
    top_skills = models.CharField("Топ Навыков", max_length=600)

    def __str__(self):
        return f"{self.published_at}"

    class Meta:
        verbose_name = "Навыки для всех профессий"

class Skills_UX_Vacancies(models.Model):
    published_at = models.IntegerField("Год")
    top_skills = models.CharField("Топ Навыков", max_length=600)

    def __str__(self):
        return f"{self.published_at}"

    class Meta:
        verbose_name = "Навыки для UX"
#Skills------------------------------------------------------