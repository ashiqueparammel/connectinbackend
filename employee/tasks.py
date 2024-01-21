from celery import shared_task 
from django.core.mail import send_mail
@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"

@shared_task
def JobApplySendingMail(username,jobName,CompanyName,userEmail):
    subject ="Connect in | Job Application Status"
        
    message = f"""Hy {username}. Your Job Application has been sent successfully.
            Your selected position: {jobName} in {CompanyName} Company.
            Thank you for choosing Connect in Company. Contact us within a week."""
    from_email = "cootinternational@gmail.com"
    recipient_list = [userEmail] 
    send_mail(subject,message, from_email, recipient_list, fail_silently=True)
    
    
@shared_task
def JobBlockSendingMail(username,JobName,CompanyName,userEmail):
    subject ="Connect in | Job Application Status"
        
    message = f"""Hy {username}. We are really sorry , Your Applied {JobName} Application UnAvailabe , That Job is blocked by Connectin team 
    that job was fake  we got report from userside and we check that job {JobName} details and company{CompanyName} .and we find {JobName} job is fake .
            Thank you for choosing Connect in Company."""
    from_email = "cootinternational@gmail.com"
    recipient_list = [userEmail] 
    send_mail(subject,message, from_email, recipient_list, fail_silently=True)    