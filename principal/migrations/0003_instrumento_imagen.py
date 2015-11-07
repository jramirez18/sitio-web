# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20151106_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumento',
            name='imagen',
            field=models.ImageField(null=True, verbose_name='Profile Pic', blank=True, upload_to='images/'),
        ),
    ]
