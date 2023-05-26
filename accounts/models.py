from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.PositiveIntegerField(null=True, blank=True) 
    nat_id = models.CharField(null=False, blank=False, default=None, max_length=10)
    
    