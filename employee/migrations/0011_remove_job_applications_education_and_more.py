# Generated by Django 4.2.7 on 2024-01-01 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_job_applications_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_applications',
            name='education',
        ),
        migrations.RemoveField(
            model_name='job_applications',
            name='skills',
        ),
    ]
