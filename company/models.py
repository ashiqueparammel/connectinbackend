from django.db import models
from users.models import CommonSkills, CustomUser

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
    Job_title = models.CharField(max_length=250)
    job_description = models.TextField(blank=False)
    Experience = models.CharField(max_length=250)  
    job_type = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_available =models.BooleanField(default=True)
    Openings =models.IntegerField(null=True)
    
class Required_Skills(models.Model):
    Job_post=models.ForeignKey(JobPost,on_delete=models.CASCADE,related_name='required_skills')
    skills=models.ForeignKey(CommonSkills,on_delete=models.CASCADE)