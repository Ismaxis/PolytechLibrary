from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('direction', views.direction, name='direction'),
    path('direction/list', views.list, name='list'),
]
