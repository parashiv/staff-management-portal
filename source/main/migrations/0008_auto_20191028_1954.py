# Generated by Django 2.2.6 on 2019-10-28 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191028_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 28, 19, 54, 18, 653214), verbose_name='date published'),
        ),
    ]