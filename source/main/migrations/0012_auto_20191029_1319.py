# Generated by Django 2.2.6 on 2019-10-29 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20191029_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 13, 19, 34, 581608), verbose_name='date published'),
        ),
    ]
