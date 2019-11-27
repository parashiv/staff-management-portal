# Generated by Django 2.2.6 on 2019-11-06 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20191106_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post_content',
            new_name='job_details',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='post_title',
            new_name='job_title',
        ),
        migrations.AddField(
            model_name='posts',
            name='job_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 13, 3, 3, 395608), verbose_name='job date'),
        ),
        migrations.AddField(
            model_name='posts',
            name='job_location',
            field=models.CharField(default='HostelXYZ', max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 13, 3, 3, 395608), verbose_name='date published'),
        ),
    ]