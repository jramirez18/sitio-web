# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20151107_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='imagen_instrumento',
            field=models.ImageField(blank=True, verbose_name='Imagen', upload_to='/home/jramirez/sitio/principal/static/images/', null=True),
        ),
    ]
