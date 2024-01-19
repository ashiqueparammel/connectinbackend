from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete

class CustomUser(AbstractUser):
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    profile_image = models.ImageField(upload_to="profile", blank=True, null=True)
    profile_cover_image = models.ImageField(
        upload_to="profile_cover_image", blank=True, null=True
    )
    phone_number = PhoneNumberField(blank=True)
    is_google = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class CommonSkills(models.Model):
    skills = models.CharField(max_length=250, unique=True)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True

class PublicPost(TimestampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Post_Image = models.ImageField(upload_to="post", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    Comments = models.IntegerField(default=0)
    
    is_available = models.BooleanField(default=True)

class PublicPostCommon(TimestampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Post = models.ForeignKey(PublicPost, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

class Like(PublicPostCommon):
    pass

class Comments(PublicPostCommon):
    Post = models.ForeignKey(PublicPost, on_delete=models.CASCADE, related_name="commentss")
    content = models.TextField()

class NotInterestedPost(PublicPostCommon):
    pass

class ReportPublicPost(PublicPostCommon):
    Reason = models.TextField()

class PublicPostSaved(PublicPostCommon):
    pass


class Notifications(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)

    def __str__(self):

        return self.text
    

class Follow(models.Model):
    followers = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name ="following")
    following = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name ="followers")
    Connection = models.BooleanField(default=False)
    
    class Meta:
        unique_together=['followers','following']
    
    def __str__(self):
        return f"{self.followers.email} follows {self.following.email}"
    
    
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

                        
           
       