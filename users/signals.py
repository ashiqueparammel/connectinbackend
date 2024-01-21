from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete
from .models import Follow

@receiver(post_save, sender=Follow)
def Check_Connection(sender, instance, created, **kwargs):
    if created:
        followers = instance.followers
        following = instance.following
        if Follow.objects.filter(followers=following, following=followers).exists():
            if Follow.objects.filter(followers=followers, following=following).exists():
                update_data = Follow.objects.get(followers=following, following=followers)
                update_data.Connection = True
                update_data.save()
                update_data1 = Follow.objects.get(followers=followers, following=following)
                update_data1.Connection = True
                update_data1.save()
            
            


# @receiver(pre_delete, sender=Follow)
# def check_connection_after(sender, instance, **kwargs):
#     followers = instance.followers
#     following = instance.following

#     if Follow.objects.filter(followers=following, following=followers).exists():
#         update_data = Follow.objects.get(followers=following, following=followers)
#         update_data.connection = False
#         update_data.save()
#     if Follow.objects.filter(followers=followers, following=following).exists():
#         update_data1 = Follow.objects.get(followers=followers, following=following)
#         update_data1.connection = False
#         update_data1.save()

                        