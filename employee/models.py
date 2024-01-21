from django.db import models
from company.models import JobPost
from users.models import CommonSkills, CustomUser

# Create your models here.

class EmployeeProfile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    header = models.CharField(max_length=250 ,blank=True,null=True)
    description = models.CharField(max_length=250 ,blank=True,null=True)
    Location = models.CharField(max_length=250 ,blank=True,null=True)
    cv_file =models.FileField(upload_to='cv_files/',blank=True,null=True)
    
class SavedPost(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=True) 
    job_post = models.ForeignKey(JobPost,on_delete=models.CASCADE)
    is_available =models.BooleanField(default=True)
    
class Education(models.Model):
    qualification = models.CharField(max_length=250)  
    Studied_year = models.CharField(max_length=250)  
    Institute_name = models.CharField(max_length=250)  
    description = models.CharField(max_length=250)  
    profile = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,related_name='personal_Education') 
    is_available =models.BooleanField(default=True)
    

class PersonalSkills(models.Model):
    skills=models.ForeignKey(CommonSkills,on_delete=models.CASCADE) 
    profile = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,related_name='personal_skills') 
  

class job_Applications(models.Model):
    profile = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE) 
    job_post = models.ForeignKey(JobPost,on_delete=models.CASCADE)
    Experience = models.PositiveSmallIntegerField(null=True)
    currentSalary = models.IntegerField(null=True)
    ExpectedSalary = models.IntegerField(null=True)
    description = models.TextField(null=True ,blank=True)
    posted_date = models.DateTimeField(auto_now_add=True) 
    Read = models.BooleanField(default=False)
    ApplicationStatus = models.CharField(default='Pending')
    Updated = models.BooleanField(default=False)
    is_available =models.BooleanField(default=True)
    

class ReportJobPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    Reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)        