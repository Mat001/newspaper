__author__ = 'matjaz'

from django.shortcuts import render

def home(request):
    return render(request, "home.html")
