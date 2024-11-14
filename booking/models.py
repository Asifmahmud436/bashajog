from django.db import models
from building.models import Unit

class Booking(models.Model):
    unit = models.OneToOneField(Unit,on_delete=models.CASCADE)
    rent = models.IntegerField()
    is_booked = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.unit.name