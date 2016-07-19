from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pokemon_list, name='pokemon_list'),
    url(r'^add_pokemon/', views.add_pokemon, name='add_pokemon'),
    url(r'^add_trainer/', views.add_trainer, name='add_trainer'),
]