from django.shortcuts import render

from .models import Projects

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def database_practice(request):
    projects = Projects.objects.all()
    return render(request, 'database_practice.html', {'projects': projects})