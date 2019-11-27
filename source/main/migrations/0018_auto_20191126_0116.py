# Generated by Django 2.2.6 on 2019-11-25 19:46

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20191106_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='job_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 26, 1, 15, 45, 761166), verbose_name='job date'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 26, 1, 15, 45, 761166), verbose_name='date published'),
        ),
    ]
