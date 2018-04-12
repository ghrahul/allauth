from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20)
    capital = models.CharField(max_length=20)
    president = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    
