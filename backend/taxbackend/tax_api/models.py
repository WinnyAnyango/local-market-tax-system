from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, unique=True)
    
    BUSINESS_TYPES = [
        ('retail', 'Retail'),
        ('wholesale', 'Wholesale'),
        ('service', 'Service Provider'),
        ('other', 'Other'),
    ]
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPES)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_vendor = models.BooleanField(default=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.national_id})"