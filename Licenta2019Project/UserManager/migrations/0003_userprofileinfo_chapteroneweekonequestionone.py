# Generated by Django 2.2.5 on 2019-09-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0002_auto_20190908_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='ChapterOneWeekOneQuestionOne',
            field=models.CharField(max_length=20, null=True),
        ),
    ]