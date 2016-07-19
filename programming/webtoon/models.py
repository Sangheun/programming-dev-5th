from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    image = models.ImageField()

    def __str__(self):
        return self.title