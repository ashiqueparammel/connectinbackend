from django.http import HttpResponse
from employee.models import job_Applications
from employee.tasks import JobBlockSendingMail, test_func
from .models import Company, JobPost
from users.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Company)
def CompanyUpdate(sender, instance, created, **kwargs):
    if not created:
        companyname = instance.company_name
        update_user = CustomUser.objects.get(id=instance.user.id)
        update_user.username = companyname
        update_user.save()


@receiver(post_save, sender=Company)
def companyBlock(sender, instance, created, **kwargs):
    if not created and not instance.is_available:
        JobPost.objects.filter(company=instance).update(is_available=False)
    if not created and instance.is_available:
        JobPost.objects.filter(company=instance).update(is_available=True)
        


@receiver(post_save, sender=JobPost)
def  JobPostBlock(sender, instance, created, **kwargs):
    if not created and not instance.is_available:
        job_Applications.objects.filter(job_post=instance).update(is_available=False)
        Mail_Send_Users = job_Applications.objects.filter(job_post=instance.id)
        
        usernames = []
        emails = []
        for users in Mail_Send_Users:
            usernames.append(users.profile.user.username)
            emails.append(users.profile.user.email)
            
        # JobBlockSendingMail(usernames,instance.Job_title,instance.company.company_name,emails)
               
    if not created and instance.is_available:
        job_Applications.objects.filter(job_post=instance).update(is_available=True)
        
       
    
    # print(type(Mail_Send_Users),'====================<<<<<<<<<<<<<<<<<<<<<<<<<')
    # JobBlockSendingMail(users.profile.user.username,instance.Job_title,instance.company.company_name,users.profile.user.email)
    # print(JobName,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # print(Mail_Send_Users, "=======================================")
    # print(userEmail, username, jobName, CompanyName, 'check this signal working or not  ==============>>>>>>>>>>>>.')
        

