from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Blog Home Page!")

def about(request):
    return HttpResponse("This is the About Page of the Blog.")

def post_detail(request, post_id):
    return HttpResponse(f"This is the detail view for post with ID: {post_id}")

def user_profile(request, username):
    return HttpResponse(f"This is the profile page for user: {username}")   

def article_year(request, year):
    return HttpResponse(f"This is the article archive for the year: {year}")

# def article_detail(request, year, month):
#     return HttpResponse(f"<h1>This is the article detail for {year}-{month}</h1>")

#keyword arguements
def article_detail(request,**kwargs):
    
    return HttpResponse(f"<h1>This is the article detail for {kwargs['year']}_{kwargs['month']}_{kwargs['day']}</h1>")