import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Institution, Direction, List

# Create your views here.

def index(request):
    dict = {
        "urls": 'hum'
    }
    return render(request, 'app.html', dict)

def hum(request):
    q = Institution.objects.all()
    dict = {
        'dir_list': q,
        }
    return render(request, 'inst.html', dict)


# def index(request):
#     q = Institution.objects.all()
#     dict = {'dir_list': q}
#     return render(request, 'app.html', dict)
