from django.db import models
from company.models import JobPost
from users.models import CustomUser

# Create your models here.

class EmployeeProfile(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Job_titile = models.CharField(max_length=250)
    cv_file =models.FileField(upload_to='cv_files/')
    
class SavedPost(models.Model):
    profile_id = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE) 
    job_post_id = models.ForeignKey(JobPost,on_delete=models.CASCADE)
    is_available =models.BooleanField(default=True)
    
class Education(models.Model):
    qualification = models.CharField(max_length=250)  
    Studied_year = models.CharField(max_length=250)  
    Institute_name = models.CharField(max_length=250)  
    description = models.CharField(max_length=250)  
    profile_id = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE) 
    is_available =models.BooleanField(default=True)
    

class PersonalSkills(models.Model):
    skills = models.CharField(max_length=250)
    profile_id = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE) 
    is_available =models.BooleanField(default=True)
    
      
        
    
class job_Applications(models.Model):
    profile_id = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE) 
    job_post_id = models.ForeignKey(JobPost,on_delete=models.CASCADE)
    education_id = models.ForeignKey(Education,on_delete=models.CASCADE)
    skills = models.ForeignKey(PersonalSkills,on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    
    
    
        
    