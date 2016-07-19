from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    catched_pokemon = models.ManyToManyField(Pokemon, through='CatchInfo', blank=True, null=True)
    def __str__(self):
        return self.name

class CatchInfo(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    catched_date = models.DateField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.place


