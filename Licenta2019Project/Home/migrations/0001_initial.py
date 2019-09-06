# Generated by Django 2.2.5 on 2019-09-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
    ]