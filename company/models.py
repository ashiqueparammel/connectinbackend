from django.db import models
from users.models import CustomUser

class Company(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250,unique=True)
    Industry = models.CharField(max_length=250)
    Company_Size = models.CharField(max_length=250)
    Location = models.CharField(max_length=250)
    Address = models.TextField(blank=False)
    is_available =models.BooleanField(default=True)
    

class JobPost(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    Job_titile = models.CharField(max_length=250)
    job_discription = models.TextField(blank=False)
    Experiance = models.CharField(max_length=250)  
    job_type = models.CharField(max_length=250)
    requerd_skills = models.TextField(blank=False)
    salary = models.CharField(max_length=250)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_available =models.BooleanField(default=True)
    
      