# Generated by Django 2.2.5 on 2019-09-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0026_auto_20190904_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='super_power',
            field=models.CharField(choices=[('Disciple', 'Disciple - Your power consists in your desire for continuous learning.'), ('Parent', 'Parent - Your power consists in your love and guidence.'), ('Trainer', 'Trainer - Your power consists in your experience and willingness to share.')], default='Disciple', max_length=2),
        ),
    ]