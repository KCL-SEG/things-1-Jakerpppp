from django.db import models

# Create your models here.
#models.Model is the parent class
class Thing(models.Model):
    name = models.CharField()
    description = models.TextField()
    quantity = models.IntegerField()

