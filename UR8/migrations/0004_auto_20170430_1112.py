# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UR8', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar/None/default_avatar.png', upload_to='avatar/'),
        ),
    ]