from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True) 
    nat_id = models.TextField(null=False, blank=False, default=0, max_length=10)
    
    
    
    