# Generated by Django 2.2.6 on 2019-10-28 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191028_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 28, 22, 42, 17, 330629), verbose_name='date published'),
        ),
    ]
