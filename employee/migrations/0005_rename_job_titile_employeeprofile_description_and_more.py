# Generated by Django 4.2.7 on 2023-12-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employeeprofile_job_titile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='Job_titile',
            new_name='description',
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='header',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]