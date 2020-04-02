from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html', {'projects': projects})
