# Generated by Django 3.1 on 2020-10-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverLetters', '0047_merge_20201025_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'get_latest_by': ['-created_date', 'modified_date'], 'ordering': ['-created_date', '-modified_date', '-position_title']},
        ),
        migrations.AlterField(
            model_name='job',
            name='form_creation_date',
            field=models.CharField(blank=True, default='October 25th, 2020', max_length=100),
        ),
    ]
