# Generated by Django 4.2.9 on 2024-01-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_apps', '0002_alter_demand_all_vacancies_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand_all_vacancies',
            name='year_count',
            field=models.IntegerField(verbose_name='Кол-во вакансий'),
        ),
        migrations.AlterField(
            model_name='demand_ux_vacancies',
            name='year_count',
            field=models.IntegerField(verbose_name='Кол-во вакансий'),
        ),
        migrations.AlterField(
            model_name='skills_all_vacancies',
            name='published_at',
            field=models.IntegerField(verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='skills_all_vacancies',
            name='top_skills',
            field=models.CharField(max_length=600, verbose_name='Топ Навыков'),
        ),
        migrations.AlterField(
            model_name='skills_ux_vacancies',
            name='published_at',
            field=models.IntegerField(verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='skills_ux_vacancies',
            name='top_skills',
            field=models.CharField(max_length=600, verbose_name='Топ Навыков'),
        ),
    ]