# Generated by Django 2.2.6 on 2019-11-06 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20191029_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 12, 41, 26, 984164), verbose_name='date published'),
        ),
    ]