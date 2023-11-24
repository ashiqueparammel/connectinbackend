from django.db import models

from users.models import CustomUser

class Company(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250,unique=True)
    Industry = models.CharField(max_length=250)
    Company_Size = models.CharField(max_length=250)
    Location = models.CharField(max_length=250)
    Address = models.TextField(blank=False)
    