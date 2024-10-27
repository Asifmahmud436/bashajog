from django.db import models
from accounts.models import CustomUser

class Tenant(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    phone_no = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='tenants/images/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username