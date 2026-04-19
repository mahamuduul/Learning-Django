import email

from django.shortcuts import render
from datetime import datetime

# Create your views here.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name":"Mahamudul Hasan",
        "age": 25,
        "skills": ["Python", "Django", "JavaScript"],
        "user": User("Mahamudul Hasan", 25),
        "blog":{
            "title": "My First Blog Post",
            "content": "This is the content of my first blog post.",
            "published_date": datetime(2024, 6, 1),
        },
        "empty_value": None,
    }
    return render(request, 'blog/home.html', context)