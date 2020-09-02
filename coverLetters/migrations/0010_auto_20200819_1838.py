# Generated by Django 3.0.3 on 2020-08-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverLetters', '0009_userdetail_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='city_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='github',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='middle_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='portfolio_website',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='preferred_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='state_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='street_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='zip_code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]