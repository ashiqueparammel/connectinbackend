from celery import shared_task, chain
from django.core.mail import send_mail
from asgiref.sync import sync_to_async
@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"

@shared_task()
def JobApplySendingMail(username,jobName,CompanyName,userEmail):
    subject = "Connect in | Job Application Confirmation"

    message = f"""Hello {username},

    Thank you for applying for the position of {jobName} at {CompanyName} Company through Connect in.

    We have received your application, and it is currently being reviewed by our hiring team. Please note that only shortlisted candidates will be contacted for further steps.

    Position: {jobName}
    Company: {CompanyName}

    We appreciate your interest in joining our team. If you have any questions or updates regarding your application, feel free to reach out to us.

    Best of luck with your job application!

    Best regards,
    Connect in Team
    """

    from_email = "cootinternational@gmail.com"
    recipient_list = [userEmail]

    send_mail(subject,message, from_email, recipient_list, fail_silently=True)
    
@shared_task()
def JobApplyAccepted(username,jobName,CompanyName,userEmail):
    subject = "Connect in | Congratulations! Your Job Application has been Accepted"

    message = f"""Hello {username},

    Congratulations! We are delighted to inform you that your application for the position of {jobName} at {CompanyName} Company has been accepted.

    Details:
    - Position: {jobName}
    - Company: {CompanyName}

    We are excited to welcome you to our team. Please review the attached contract and other relevant documents. If you have any questions or need further information, feel free to reach out to us.

    Thank you for choosing Connect in Company as your workplace. We look forward to working together.

    Best regards,
    Connect in Team
    """

    from_email = "cootinternational@gmail.com"
    recipient_list = [userEmail]

    send_mail(subject,message, from_email, recipient_list, fail_silently=True)    
    
@shared_task()
def JobApplyRejected(username,jobName,CompanyName,userEmail):   
    subject = "Connect in | Update on Your Job Application"

    message = f"""Hello {username},

    We appreciate your interest in the position of {jobName} at {CompanyName} Company through Connect in.

    After careful consideration, we regret to inform you that your application has not been successful at this time. We received many qualified applicants, and the decision was a challenging one.

    Position: {jobName}
    Company: {CompanyName}

    We genuinely appreciate the effort and time you invested in the application process. We encourage you to explore other opportunities on Connect in, and we wish you the best in your job search.

    If you have any feedback or questions about your application, feel free to reach out to us.

    Thank you for considering Connect in Company as a potential employer.

    Best regards,
    Connect in Team
    """

    from_email = "cootinternational@gmail.com"
    recipient_list = [userEmail]

    send_mail(subject,message, from_email, recipient_list, fail_silently=True)    
    
    
    
@shared_task
def JobBlockSendingMail(username,JobName,CompanyName,userEmail):
    for i in range(len(username)):
        
        subject ="Connect in | Job Application Status"
            
        message = f"""Hy {username[i]}. We are really sorry , Your Applied {JobName} Application UnAvailabe , That Job is blocked by Connectin team 
        that job was fake  we got report from userside and we check that job {JobName} details and company{CompanyName} .and we find {JobName} job is fake .
                Thank you for choosing Connect in Company."""
        from_email = "cootinternational@gmail.com"
        recipient_list = [userEmail[i]] 
        send_mail(subject,message, from_email, recipient_list, fail_silently=True)    