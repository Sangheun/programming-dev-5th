from django.conf import settings

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='포켓몬 트레이너')

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=100, verbose_name='포켓몬 종류')

    def __str__(self):
        return self.name


class Place(models.Model):
    place = models.CharField(max_length=100, verbose_name='포켓몬 잡은 장소')

    def __str__(self):
        return self.place

class Show(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='포켓몬 트레이너')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='잡은 포켓몬')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='포켓몬 잡은 장소')
