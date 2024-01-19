from django.contrib import admin
from users.models import Comments, CommonSkills, CustomUser, Follow, Like, NotInterestedPost, PublicPost, ReportPublicPost
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CommonSkills)
admin.site.register(PublicPost)
admin.site.register(Comments)
admin.site.register(NotInterestedPost)
admin.site.register(ReportPublicPost)
admin.site.register(Like)
admin.site.register(Follow)