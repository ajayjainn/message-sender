# Generated by Django 3.1.4 on 2021-01-15 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendersy', '0008_auto_20210115_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(auto_now_add=True, verbose_name=datetime.time(11, 19, 25, 415721)),
        ),
    ]