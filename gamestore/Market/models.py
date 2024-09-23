from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.URLField(max_length=1000)
    metascore = models.IntegerField()
    age = models.IntegerField()
    about_game = models.TextField()
    platform = models.CharField(max_length=200)

    def __str__(self):
        return self.name
