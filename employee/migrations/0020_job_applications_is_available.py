# Generated by Django 4.2.7 on 2024-01-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_job_applications_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_applications',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
