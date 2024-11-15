from django.db import models
from owners.models import Owner
from tenants.models import Tenant
from django.core.validators import MinValueValidator

class Building(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    owner = models.ManyToManyField(Owner)
    image = models.ImageField(upload_to='building/images/building_image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.address[:30]}'
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
    
class Unit(models.Model):
    name = models.CharField(max_length=255)
    room = models.IntegerField(validators=[MinValueValidator(1)])
    toilet = models.IntegerField(validators=[MinValueValidator(1)])
    window = models.IntegerField(validators=[MinValueValidator(0)])
    building = models.ForeignKey(Building,on_delete=models.CASCADE,related_name='units')
    image = models.ImageField(upload_to='building/images/unit_image')
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE,blank=True,null=True,related_name='units')
    is_occupied = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}-{self.building.name}'
    
    class Meta:
        ordering = ['updated']
        indexes = [
            models.Index(fields=['is_occupied','updated'])
        ]
    