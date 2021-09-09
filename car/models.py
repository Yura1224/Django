from django.db import models

# Create your models here.
class CarModel (models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=255)
    year = models.IntegerField()
    cost = models.IntegerField()
