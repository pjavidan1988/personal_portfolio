from django.shortcuts import render
from .models import Project


def Home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
