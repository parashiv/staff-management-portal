# Generated by Django 2.2.7 on 2019-11-27 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20191126_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='job_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 27, 7, 17, 14, 515455), verbose_name='job date'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 27, 7, 17, 14, 515502), verbose_name='date published'),
        ),
    ]
