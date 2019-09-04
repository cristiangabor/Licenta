# Generated by Django 2.2.5 on 2019-09-04 14:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0015_auto_20190904_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(5.0), django.core.validators.MaxValueValidator(100.0)])),
                ('kg', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(5.0), django.core.validators.MaxValueValidator(100.0)])),
                ('height', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(5.0), django.core.validators.MaxValueValidator(100.0)])),
                ('super_power', models.CharField(choices=[('Fl', 'Flah the gratest'), ('Hl', 'Hulk all mighty'), ('Bt', 'Batman, the strategic'), ('Sp', 'Superman the call to advanture')], default='Fl', max_length=2)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]