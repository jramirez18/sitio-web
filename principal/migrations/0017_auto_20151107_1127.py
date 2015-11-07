# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_auto_20151107_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='imagen_instrumento',
            field=models.ImageField(upload_to='home/jramirez/sitio/principal/static/images/', verbose_name='Imagen', blank=True, null=True),
        ),
    ]
