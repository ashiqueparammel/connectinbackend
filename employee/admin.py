from django.contrib import admin

from .models import Education, EmployeeProfile, PersonalSkills, SavedPost, job_Applications

# Register your models here.
admin.site.register(EmployeeProfile)
admin.site.register(SavedPost)
admin.site.register(Education)
admin.site.register(PersonalSkills)
admin.site.register(job_Applications)
