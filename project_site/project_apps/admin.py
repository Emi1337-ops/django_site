from django.contrib import admin
import project_apps.models as models

# Register your models here.
admin.site.register(models.Demand_All_Vacancies)
admin.site.register(models.Demand_UX_Vacancies)

admin.site.register(models.Geography_AreaCount_All_Vacancies)
admin.site.register(models.Geography_MidSalary_All_Vacancies)
admin.site.register(models.Geography_AreaCount_UX_Vacancies)
admin.site.register(models.Geography_MidSalary_UX_Vacancies)

admin.site.register(models.Skills_All_Vacancies)
admin.site.register(models.Skills_UX_Vacancies)