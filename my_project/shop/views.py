from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Shop Home Page!")

def products(request):
    return HttpResponse("This is the Products Page of the Shop.")
   