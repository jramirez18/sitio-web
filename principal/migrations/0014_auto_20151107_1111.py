# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_auto_20151107_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='imagen_instrumento',
            field=models.ImageField(verbose_name='Imagen', blank=True, null=True, upload_to='home/jramirez/sitio/principal/static/images/'),
        ),
    ]
