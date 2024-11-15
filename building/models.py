from django.db import models
from owners.models import Owner
from tenants.models import Tenant

RENT_CHOICES = [
    ('To-let','To-let'),
    ('Filled','Filled')
]

class Building(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    owner = models.ManyToManyField(Owner)
    image = models.ImageField(upload_to='building/images/building_image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
    
class Unit(models.Model):
    name = models.CharField(max_length=255)
    room = models.IntegerField()
    toilet = models.IntegerField()
    window = models.IntegerField()
    building = models.ForeignKey(Building,on_delete=models.CASCADE,related_name='unit')
    image = models.ImageField(upload_to='building/images/unit_image')
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE,blank=True,null=True,related_name='unit')
    is_occupied = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['updated']
        indexes = [
            models.Index(fields=['is_occupied','updated'])
        ]
    