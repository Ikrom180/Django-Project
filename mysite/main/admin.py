from django.contrib import admin
from django.contrib.auth.templatetags.auth import register
from .models import ToDoList, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(ToDoList)