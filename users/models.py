from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class CustomUser(AbstractUser):
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    profile_image = models.ImageField(upload_to='profile',blank=True,null=True)
    profile_cover_image = models.ImageField(upload_to='profile_cover_image',blank=True,null=True)
    phone_number = PhoneNumberField(blank=True)
    is_google = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

class CommonSkills(models.Model):
    skills = models.CharField(max_length=250)  