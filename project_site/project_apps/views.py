from django.shortcuts import render

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