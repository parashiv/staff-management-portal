# Generated by Django 2.2.6 on 2019-10-28 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191028_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 28, 14, 26, 57, 203325), verbose_name='date published'),
        ),
    ]
