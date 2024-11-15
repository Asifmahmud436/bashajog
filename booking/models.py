from django.db import models
from building.models import Unit
from tenants.models import Tenant

class Booking(models.Model):
    unit = models.OneToOneField(Unit,on_delete=models.CASCADE)
    rent = models.IntegerField()
    is_booked = models.BooleanField(default=True)
    tenant = models.ForeignKey(Tenant,on_delete=models.SET_NULL,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.unit.name
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]