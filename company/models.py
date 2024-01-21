from django.db import models
from users.models import CommonSkills, CustomUser



class Company(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250, unique=True)
    Industry = models.CharField(max_length=250)
    Company_Size = models.CharField(max_length=250)
    Location = models.CharField(max_length=250)
    Address = models.TextField(blank=False)
    Description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)


class JobPost(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Job_title = models.CharField(max_length=250)
    job_description = models.TextField(blank=False)
    Experience = models.PositiveIntegerField()
    job_type = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    Openings = models.IntegerField(null=True)
    ApplicationCount = models.IntegerField(default=0)


class Required_Skills(models.Model):
    Job_post = models.ForeignKey(
        JobPost, on_delete=models.CASCADE, related_name="required_skills"
    )
    skills = models.ForeignKey(CommonSkills, on_delete=models.CASCADE)
