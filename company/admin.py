from django.contrib import admin
from .models import Company, JobPost, Required_Skills

# Register your models here.
admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(Required_Skills)
