# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20170606_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
