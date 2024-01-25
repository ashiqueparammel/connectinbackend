from django.contrib import admin
from .models import Comments, CommonSkills, CustomUser, Follow, Like, NotInterestedPost, PublicPost, ReportPublicPost, UsersNotifications
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CommonSkills)
admin.site.register(PublicPost)
admin.site.register(Comments)
admin.site.register(NotInterestedPost)
admin.site.register(ReportPublicPost)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(UsersNotifications)