# Generated by Django 2.2.5 on 2019-09-08 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0004_auto_20190908_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterOneWeekTwoQuestionOne',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterOneWeekTwoQuestionThree',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterOneWeekTwoQuestionTwo',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterThreeWeekOneQuestionOne',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterThreeWeekOneQuestionTwo',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterThreeWeekTwoQuestionOne',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterThreeWeekTwoQuestionThree',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterThreeWeekTwoQuestionTwo',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterThreoWeekOneQuestionThree',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterTwoWeekOneQuestionOne',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterTwoWeekOneQuestionThree',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterTwoWeekOneQuestionTwo',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterTwoWeekTwoQuestionOne',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterTwoWeekTwoQuestionThree',
        ),
        migrations.RemoveField(
            model_name='chapteroneweekone',
            name='ChapterTwoWeekTwoQuestionTwo',
        ),
        migrations.AlterField(
            model_name='chapteroneweekone',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progress_ChOneWeekOne', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ChapterTwoWeekTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChapterTwoWeekTwoQuestionOne', models.CharField(max_length=20, null=True)),
                ('ChapterTwoWeekTwoQuestionTwo', models.CharField(max_length=20, null=True)),
                ('ChapterTwoWeekTwoQuestionThree', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progress_ChTwoWeekTwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChapterTwoWeekOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChapterTwoWeekOneQuestionOne', models.CharField(max_length=20, null=True)),
                ('ChapterTwoWeekOneQuestionTwo', models.CharField(max_length=20, null=True)),
                ('ChapterTwoWeekOneQuestionThree', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progress_ChTwoWeekOne', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChapterThreeWeekTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChapterThreeWeekTwoQuestionOne', models.CharField(max_length=20, null=True)),
                ('ChapterThreeWeekTwoQuestionTwo', models.CharField(max_length=20, null=True)),
                ('ChapterThreeWeekTwoQuestionThree', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progress_ChThreWeekTwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChapterThreeWeekOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChapterThreeWeekOneQuestionOne', models.CharField(max_length=20, null=True)),
                ('ChapterThreeWeekOneQuestionTwo', models.CharField(max_length=20, null=True)),
                ('ChapterThreoWeekOneQuestionThree', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progress_ChThreeWeekOne', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChapterOneWeekTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChapterOneWeekTwoQuestionOne', models.CharField(max_length=20, null=True)),
                ('ChapterOneWeekTwoQuestionTwo', models.CharField(max_length=20, null=True)),
                ('ChapterOneWeekTwoQuestionThree', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progress_ChOneWeekTwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
