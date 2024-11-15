from django.db import models
from accounts.models import CustomUser

class Owner(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='owner')
    phone_no = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='owners/images/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username