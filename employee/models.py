from django.db import models
from company.models import JobPost
from users.models import CommonSkills, CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

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
    description = models.TextField(null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    
@receiver(post_save,sender=job_Applications)
def SendingMailToEmployee(sender,instance,created,**kwargs):
    if created:
        userEmail = instance.profile.user.email
        username = instance.profile.user.username
        jobName = instance.job_post.Job_title
        CompanyName = instance.job_post.company.company_name
        # print(userEmail, username, jobName, CompanyName, 'check this signal working or not  ==============>>>>>>>>>>>>.')
        subject ="Connect in | Job Application Status"
        
        message = f"""Hy {username}. Your Job Application has been sent successfully.
                Your selected position: {jobName} in {CompanyName} Company.
                Thank you for choosing Connect in Company. Contact us within a week."""
        from_email = "cootinternational@gmail.com"
        recipient_list = [userEmail] 
        send_mail(subject,message, from_email, recipient_list, fail_silently=True)

        