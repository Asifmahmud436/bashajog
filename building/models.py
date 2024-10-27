from django.db import models
from owners.models import Owner
from tenants.models import Tenant

class Building(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    owner = models.ManyToManyField(Owner)
    # tenant = models.OneToOneField(Tenant)
    # room no
    