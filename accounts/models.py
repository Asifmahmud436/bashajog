from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_ROLE_FIELD = (
        ("Owner","Owner"),
        ("Tenant","Tenant"),
    )
    user_type = models.CharField(max_length=20,choices=USER_ROLE_FIELD)