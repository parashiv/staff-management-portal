# Generated by Django 2.2.6 on 2019-11-26 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20191126_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='job_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 26, 21, 58, 18, 792018), verbose_name='job date'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 26, 21, 58, 18, 792018), verbose_name='date published'),
        ),
    ]
