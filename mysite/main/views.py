from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

# def index(response, id):
#     return HttpResponse("<h1>%d<h1>" % id)

def index(response, id): #We make it dynamically
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

# def list(response):
#     return render(response, "main/list.html", {"name": "List"})















