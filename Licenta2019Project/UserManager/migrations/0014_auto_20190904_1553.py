# Generated by Django 2.2.5 on 2019-09-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0013_auto_20190904_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='kg',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='super_power',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
