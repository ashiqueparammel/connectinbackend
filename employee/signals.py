from django.dispatch import receiver
from django.db.models.signals import post_save
from company.models import JobPost
from .models import job_Applications
from .tasks import JobApplyAccepted, JobApplyRejected, JobApplySendingMail


@receiver(post_save,sender=job_Applications)
def SendingMailToEmployee(sender,instance,created,**kwargs):
    if created:
        username = instance.profile.user.username
        userEmail = instance.profile.user.email
        jobName = instance.job_post.Job_title
        CompanyName = instance.job_post.company.company_name
        JobId = instance.job_post.id
        JobApplySendingMail(username,jobName,CompanyName,userEmail)
        UpdateApplicationCount = JobPost.objects.get(id=JobId)
        UpdateApplicationCount.ApplicationCount+=1
        UpdateApplicationCount.save()
    else:
        username = instance.profile.user.username
        userEmail = instance.profile.user.email
        jobName = instance.job_post.Job_title
        CompanyName = instance.job_post.company.company_name
        
        if instance.ApplicationStatus == 'Accept' :
            JobApplyAccepted(username,jobName,CompanyName,userEmail)
        elif instance.ApplicationStatus == 'Reject' : 
            JobApplyRejected(username,jobName,CompanyName,userEmail)   

               