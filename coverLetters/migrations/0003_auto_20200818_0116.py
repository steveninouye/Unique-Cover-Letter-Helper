# Generated by Django 3.0.3 on 2020-08-18 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coverLetters', '0002_job_recruiter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='extra_line_one',
            new_name='bullet_point_one',
        ),
    ]
