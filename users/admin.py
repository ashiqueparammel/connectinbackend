from django.contrib import admin
from users.models import CommonSkills, CustomUser
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CommonSkills)