# Generated by Django 3.1 on 2020-09-16 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coverLetters', '0044_auto_20200916_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='choice_of_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coverLetters.userdetail'),
        ),
    ]
