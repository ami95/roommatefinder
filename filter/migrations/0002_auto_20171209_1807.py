# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-09 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepics/cat.jpeg', upload_to='profilepics'),
        ),
    ]
