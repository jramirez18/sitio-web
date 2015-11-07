# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_auto_20151107_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='imagen_instrumento',
            field=models.ImageField(blank=True, null=True, upload_to='/images/', verbose_name='Imagen'),
        ),
    ]
