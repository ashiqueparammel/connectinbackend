from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete
from .models import Follow, UsersNotifications
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
channel_layer = get_channel_layer()

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
                
        notification_text = f'Started following you'
        
        if UsersNotifications.objects.filter(user=following,NotifyUser=followers,text=notification_text,NotificationsType='following' ).exists():
            pass
        else:   
            UsersNotifications.objects.create(user=following,NotifyUser=followers,text=notification_text,NotificationsType='following' )  
        
            




# @receiver(post_save,sender=Follow)
# def send_user_created_notification(sender,instance,created,*args,**kwargs):

#     if created:
       

              
#         # async_to_sync(channel_layer.group_send)(
#         #     "admin_group",
#         #     {
#         #         'type': 'create_notification',
#         #         'message': notification_text
#         #     }
#         # )




                        