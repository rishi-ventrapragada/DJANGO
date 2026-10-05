# WEEK4: Basics of Django Framework & Installation of required Software's

# views.py
from django.shortcuts import render


def index(request):
    return render(request, 'myapp/index.html')
