# Generated by Django 2.2.6 on 2019-10-29 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20191029_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 16, 8, 57, 605830), verbose_name='date published'),
        ),
    ]
