from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hum', views.hum, name='hum'),
    path('build', views.build, name='build'),
]
