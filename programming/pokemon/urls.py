from django.conf.urls import url
from . import views

app_name = 'pokemon'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pokemon/', views.pokemon, name='pokemon'),
    url(r'^person/', views.person, name='person'),
    url(r'^place/', views.place, name='place'),
    url(r'^catch/', views.catch, name='catch'),
    url(r'^show/', views.show, name='show'),
]