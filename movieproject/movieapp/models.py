from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=230)
    desc=models.TextField()
    year=models.IntegerField()


def __str__(self):
    return self.name
