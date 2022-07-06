from django.shortcuts import render
from django.http import HttpResponse
from .models import Institution, Direction, List

# Create your views here.

def index(request):
    q = Institution.objects.all()
    dict = {'rows': [],
    'url': 'direction'}

    for i in range(len(q)):
        row = {'dir': q[i], 'num': i + 2}
        dict['rows'].append(row)

    return render(request, 'app.html', dict)

def direction(request):

    # if request.method == 'POST':
    id = int(request.POST['button'])
    rows = Direction.objects.filter(institution_id=id)

    dict = {
        'dir_list': rows,
        'isempty': rows.count() == 0
        }
    return render(request, 'inst.html', dict)
