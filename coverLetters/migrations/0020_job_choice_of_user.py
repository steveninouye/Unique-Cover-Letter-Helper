# Generated by Django 3.1 on 2020-09-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverLetters', '0019_auto_20200906_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='choice_of_user',
            field=models.ManyToManyField(to='coverLetters.UserDetail', verbose_name='UserDetail'),
        ),
    ]
