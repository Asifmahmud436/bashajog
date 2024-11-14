from django.db import models
from owners.models import Owner
from tenants.models import Tenant

RENT_CHOICES = [
    ('Tolet','Tolet'),
    ('Filled','Filled')
]
class Unit(models.Model):
    name = models.CharField(max_length=255)
    # rent_status = models.CharField(max_length=255,choices=RENT_CHOICES,default=RENT_CHOICES)
    bedroom = models.IntegerField()
    window = models.IntegerField()

class Building(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    owner = models.ManyToManyField(Owner)
    unit = models.ManyToManyField(Unit)

    