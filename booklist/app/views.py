import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Institution, Direction, List

# Create your views here.

def index(request):
    q = Institution.objects.all()
    print(q)
    urls = ['hum', 'build'];
    dict = {'rows': []}

    for i in range(len(urls)):
        row = {'url': urls[i], 'dir': q[i]}
        dict['rows'].append(row)

    return render(request, 'app.html', dict)

def hum(request):
    q = Direction.objects.filter(institution_id=2)
    dict = {
        'dir_list': q,
        }
    return render(request, 'inst.html', dict)

def build(request):
    q = Direction.objects.filter(institution_id=3)
    dict = {
        'dir_list': q,
        }
    return render(request, 'inst.html', dict)


# def index(request):
#     q = Institution.objects.all()
#     dict = {'dir_list': q}
#     return render(request, 'app.html', dict)
