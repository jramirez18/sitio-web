# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20151106_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='imagen_instrumento',
            field=models.ImageField(blank=True, upload_to='/sitio/principal/static/images/', verbose_name='Imagen', null=True),
        ),
    ]
