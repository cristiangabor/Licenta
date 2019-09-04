# Generated by Django 2.2.5 on 2019-09-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0004_auto_20190903_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='kg',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='super_power',
            field=models.CharField(choices=[('Fl', 'Flah the gratest'), ('Hl', 'Hulk all mighty'), ('Bt', 'Batman, the strategic'), ('Sp', 'Superman the call to advanture')], default='Fl', max_length=2),
        ),
    ]
