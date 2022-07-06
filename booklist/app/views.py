from django.shortcuts import render
from django.http import HttpResponse
from .models import Institution, Direction, List

# Create your views here.

def index(request):
    q = Institution.objects.all()
    dict = {'rows': [],
    'url': 'direction'}

    for i in range(len(q)):
        row = {'dir': q[i], 'direction_id': q.values()[i]['id']}
        dict['rows'].append(row)

    return render(request, 'institutions.html', dict)

def direction(request):
    # if request.method == 'POST':
    id = int(request.POST['button'])
    rows = Direction.objects.filter(institution_id=id)

    dict = {
        'rows': [],
        'url': 'direction/list',
        'isempty': rows.count() == 0,
        'direction_id': id
        }

    for i in range(len(rows)):
        row = {'dir': rows[i], 'list_id': rows.values()[0]['id']}
        dict['rows'].append(row)

    return render(request, 'direction.html', dict)

def list(request):
    # if request.method == 'POST':
    id, dir_id = request.POST['button'].split()
    rows = List.objects.filter(direction_id=id)

    dict = {
        'lists': rows,
        'url': 'list',
        'isempty': rows.count() == 0,
        'caller': dir_id
        }
    return render(request, 'list.html', dict)
