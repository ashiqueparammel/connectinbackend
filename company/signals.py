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